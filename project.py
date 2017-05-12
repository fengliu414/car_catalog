from flask import Flask, render_template, request, redirect
from flask import make_response, jsonify, url_for, flash
from flask import session as login_session
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from database_setup import Base, CarBrand, CarItem, User
import random
import string
import httplib2
import json
import requests


app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Car Exhibition"

# Connect to Database and create database session
engine = create_engine('sqlite:///cars_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?' \
          'grant_type=fb_exchange_token&client_id' \
          '=%s&client_secret=%s&fb_exchange_token=%s' \
          % (app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # strip expire tag from access token
    itm = result.split(":")[1]
    itm1 = itm.split(",")[0]
    token = itm1.split('"')[1]

    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    # let's strip out the information before the equals sign in our token
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # Get user picture
    url = 'https://graph.facebook.com/v2.4/me/picture?%s&redirect=0' \
          '&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' "style = "width: 300px; height: 300px;border-radius: 150px;' \
              '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token='
    '%s' % (facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "You have been logged out"


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='',
                                             redirect_uri='postmessage')
        # oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('User is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h2>Welcome '
    output += login_session['username']
    output += '!</h2></br>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 200px; height: 200px;border-radius: 100px;'
    output += '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    return output


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON APIs to view Car Brand Information
@app.route('/car_brand/<int:car_brand_id>/car_item/JSON')
def itemsOfCarBrandJSON(car_brand_id):
    car_items = session.query(CarItem).filter_by(
        car_brand_id=car_brand_id).all()
    return jsonify(CarItems=[i.serialize for i in car_items])


@app.route('/car_brand/<int:car_brand_id>/car_item/<int:car_item_id>/JSON')
def carItemJSON(car_brand_id, car_item_id):
    car_item = session.query(CarItem).filter_by(id=car_item_id).one()
    return jsonify(CarItem=car_item.serialize)


@app.route('/car_brand/JSON')
def carBrandJSON():
    car_brands = session.query(CarBrand).all()
    return jsonify(CarBrands=[r.serialize for r in car_brands])


# Show all car brands
@app.route('/')
@app.route('/car_brand/')
def showBrands():
    car_brands = session.query(CarBrand).order_by(asc(CarBrand.name))
    car_items = session.query(CarItem).order_by(
                desc(CarItem.time_created)).limit(10).all()
    return render_template('car_brands.html', num=10, car_brand="",
                           car_brands=car_brands, car_items=car_items)


# # Show a car model
@app.route('/car_brand/<int:car_brand_id>/')
@app.route('/car_brand/<int:car_brand_id>/car_item/')
def showItem(car_brand_id):
    car_brand = session.query(CarBrand).filter_by(id=car_brand_id).one()
    car_brands = session.query(CarBrand).order_by(asc(CarBrand.name))
    car_items = session.query(CarItem).filter_by(
        car_brand_id=car_brand_id).all()
    num = len(car_items)
    return render_template('car_items.html', num=num, car_items=car_items,
                           car_brand=car_brand, car_brands=car_brands)


# show the specific item user selected
@app.route('/car_brand/<int:car_brand_id>/car_item/<int:car_item_id>/show',
           methods=['GET'])
def showCarItem(car_brand_id, car_item_id):
    ItemToShow = session.query(CarItem).filter_by(id=car_item_id).one()
    car_brand = session.query(CarBrand).filter_by(id=car_brand_id).one()
    if 'username' not in login_session:
        flash("You need to login to check details!")
        return redirect(url_for('showItem', car_brand_id=car_brand_id))
    else:
        return render_template('show_car_item.html', item=ItemToShow,
                               brand=car_brand)


# Create a new car item
@app.route('/car_brand/<int:car_brand_id>/car_item/new/',
           methods=['GET', 'POST'])
def newCarItem(car_brand_id):
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    else:
        car_brand = session.query(CarBrand).filter_by(id=car_brand_id).one()
        if request.method == 'POST':
            if "add_new" in request.form:
                if request.form['name']:
                    newItem = CarItem(name=request.form['name'],
                                      description=request.form['description'],
                                      price=request.form['price'],
                                      car_brand_id=car_brand_id,
                                      picture=request.form['image'],
                                      user_id=login_session['user_id'])
                    session.add(newItem)
                    session.commit()
                    flash('New Car %s Model Successfully Created'
                          % (newItem.name))
                else:
                    flash("You must at least specify the car model's name")
                    return redirect(url_for('newCarItem',
                                            car_brand_id=car_brand_id))
            return redirect(url_for('showItem', car_brand_id=car_brand_id))
        else:
            return render_template('new_car_item.html', car_brand=car_brand)


# Edit a car item
@app.route('/car_brand/<int:car_brand_id>/car_item/<int:car_item_id>/edit',
           methods=['GET', 'POST'])
def editCarItem(car_brand_id, car_item_id):

    editedItem = session.query(CarItem).filter_by(id=car_item_id).one()
    creator = getUserInfo(editedItem.user_id)
    if 'username' not in login_session or \
       creator.id != login_session['user_id']:
        flash("You are not authorized to modify the content!")
        return redirect(url_for('showCarItem', car_brand_id=car_brand_id,
                                car_item_id=car_item_id))
    else:
        if request.method == 'POST':
            if "save_edit" in request.form:
                if request.form['name']:
                    editedItem.name = request.form['name']
                if request.form['description']:
                    editedItem.description = request.form['description']
                if request.form['price']:
                    editedItem.price = request.form['price']
                if request.form['image']:
                    editedItem.picture = request.form['image']

                session.add(editedItem)
                session.commit()
                flash('Car Model Successfully Edited!')
            return redirect(url_for('showCarItem', car_brand_id=car_brand_id,
                                    car_item_id=car_item_id))
        else:
            return render_template('edit_car_item.html',
                                   car_brand_id=car_brand_id,
                                   car_item_id=car_item_id,
                                   item=editedItem)


# Delete a car item
@app.route('/car_brand/<int:car_brand_id>/car_item/<int:car_item_id>/delete',
           methods=['GET', 'POST'])
def deleteCarItem(car_brand_id, car_item_id):
    itemToDelete = session.query(CarItem).filter_by(id=car_item_id).one()
    creator = getUserInfo(itemToDelete.user_id)
    if 'username' not in login_session \
       or creator.id != login_session['user_id']:
        flash("You are not authorized to delete the content!")
        return redirect(url_for('showCarItem', car_brand_id=car_brand_id,
                                car_item_id=car_item_id))
    else:
        if request.method == 'POST':
            if "delete_item" in request.form:
                session.delete(itemToDelete)
                session.commit()
                flash('Car Model Successfully Deleted')
            else:
                return redirect(url_for('showCarItem',
                                        car_brand_id=car_brand_id,
                                        car_item_id=car_item_id))
            return redirect(url_for('showItem', car_brand_id=car_brand_id))
        else:
            return render_template('delete_car_item.html', item=itemToDelete)


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            # del login_session['credentials']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showBrands'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showBrands'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
