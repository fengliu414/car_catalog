from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import CarBrand, CarItem, User, Base

engine = create_engine('sqlite:///cars_database.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Website author", email="fengliu414@gmail.com",
             picture='https://s-media-cache-ak0.pinimg.com/736x/01/59/40/01594057534c60f94af3165f26d85629.jpg')
session.add(User1)
session.commit()


# Car Brand
CarBrand1 = CarBrand(name="BMW")
session.add(CarBrand1)
session.commit()


CarItem1 = CarItem(user_id=1, name="BMW 2 Series", description="Available in Coupe, Convertible",
                   price="$33,150 Starting MSRP", car_brand=CarBrand1,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="BMW 3 Series", description="Available in Sedan, Sports Wagon, GranTurismo",
                   price="$33,450 Starting MSRP", car_brand=CarBrand1,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="BMW 4 Series", description="Available in Gran Coupe, Coupe, Convertible",
                   price="$41,950 Starting MSRP", car_brand=CarBrand1,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="BMW 5 Series", description="Available in Sedan, Gran Turismo",
                   price="$51,200 Starting MSRP", car_brand=CarBrand1,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()

CarItem5 = CarItem(user_id=1, name="BMW 6 Series", description="Available in Gran Coupe, Convertible, ALPINA Gran Coupe",
                   price="$81,400 Starting MSRP", car_brand=CarBrand1,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem5)
session.commit()

CarItem6 = CarItem(user_id=1, name="BMW 7 Series", description="Available in Sedan",
                   price="$83,100 Starting MSRP", car_brand=CarBrand1,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem6)
session.commit()


# Car Brand
CarBrand2 = CarBrand(name="Mercedez-Benz")
session.add(CarBrand2)
session.commit()


CarItem1 = CarItem(user_id=1, name="Benz CLA Class", description="Available in Sedan",
                   price="$33,150 Starting MSRP", car_brand=CarBrand2,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="Benz C Class", description="Available in Sedan",
                   price="$33,450 Starting MSRP", car_brand=CarBrand2,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="Benz E Class", description="Available in Sedan",
                   price="$41,950 Starting MSRP", car_brand=CarBrand2,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="Benz S Class", description="Available in Sedan",
                   price="$51,200 Starting MSRP", car_brand=CarBrand2,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()


# Car Brand
CarBrand3 = CarBrand(name="Nissan")
session.add(CarBrand3)
session.commit()


CarItem1 = CarItem(user_id=1, name="VERSA", description="A nice car",
                   price="$11,990 Starting MSRP", car_brand=CarBrand3,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="SENTRA", description="A nice car",
                   price="$16,990 Starting MSRP", car_brand=CarBrand3,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="ALTIMA", description="A nice car",
                   price="$22,500 Starting MSRP", car_brand=CarBrand3,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="MAXIMA", description="A nice car",
                   price="$32,610 Starting MSRP", car_brand=CarBrand3,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()


# Car Brand
CarBrand4 = CarBrand(name="Audi")
session.add(CarBrand4)
session.commit()


CarItem1 = CarItem(user_id=1, name="A3", description="A nice car",
                   price="$29,027 Starting MSRP", car_brand=CarBrand4,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="A4", description="A nice car",
                   price="$33,418 Starting MSRP", car_brand=CarBrand4,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="A5", description="A nice car",
                   price="$39,629 Starting MSRP", car_brand=CarBrand4,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="A6", description="A nice car",
                   price="$45,563 Starting MSRP", car_brand=CarBrand4,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()

CarItem5 = CarItem(user_id=1, name="A7", description="A nice car",
                   price="$65,728 Starting MSRP", car_brand=CarBrand4,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem5)
session.commit()

CarItem6 = CarItem(user_id=1, name="A8", description="A nice car",
                   price="$78,568 Starting MSRP", car_brand=CarBrand4,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem6)
session.commit()


# Car Brand
CarBrand5 = CarBrand(name="Bentley")
session.add(CarBrand5)
session.commit()


CarItem1 = CarItem(user_id=1, name="Bentayga", description="A nice car",
                   price="$222,590 Starting MSRP", car_brand=CarBrand5,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="Continental", description="A nice car",
                   price="$201,225 Starting MSRP", car_brand=CarBrand5,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="Flying Spur", description="A nice car",
                   price="$203,725 Starting MSRP", car_brand=CarBrand5,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="Mulsanne", description="A nice car",
                   price="$306,425 Starting MSRP", car_brand=CarBrand5,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()


# Car Brand
CarBrand6 = CarBrand(name="Ferrari")
session.add(CarBrand6)
session.commit()


CarItem1 = CarItem(user_id=1, name="488 GTB", description="A nice car",
                   price="$249,150 Starting MSRP", car_brand=CarBrand6,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="488 Spider", description="A nice car",
                   price="$276,450 Starting MSRP", car_brand=CarBrand6,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="California", description="A nice car",
                   price="$206,473 Starting MSRP", car_brand=CarBrand6,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()


# Car Brand
CarBrand7 = CarBrand(name="Honda")
session.add(CarBrand7)
session.commit()


CarItem1 = CarItem(user_id=1, name="Accord", description="A nice car",
                   price="$19,947 Starting MSRP", car_brand=CarBrand7,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="Civic", description="A nice car",
                   price="$18,674 Starting MSRP", car_brand=CarBrand7,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="CR-V", description="A nice car",
                   price="$23,842 Starting MSRP", car_brand=CarBrand7,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="Fit", description="A nice car",
                   price="$16,469 Starting MSRP", car_brand=CarBrand7,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()

CarItem5 = CarItem(user_id=1, name="Odyssey", description="A nice car",
                   price="$28,527 Starting MSRP", car_brand=CarBrand7,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem5)
session.commit()

CarItem6 = CarItem(user_id=1, name="Pilot", description="A nice car",
                   price="$31,525 Starting MSRP", car_brand=CarBrand7,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem6)
session.commit()


# Car Brand
CarBrand8 = CarBrand(name="Ford")
session.add(CarBrand8)
session.commit()


CarItem1 = CarItem(user_id=1, name="Edge", description="A nice car",
                   price="$26,043 Starting MSRP", car_brand=CarBrand8,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="Escape", description="A nice car",
                   price="$19,327 Starting MSRP", car_brand=CarBrand8,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="Expedition", description="A nice car",
                   price="$40,040 Starting MSRP", car_brand=CarBrand8,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="Explorer", description="A nice car",
                   price="$29,046 Starting MSRP", car_brand=CarBrand8,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()

CarItem5 = CarItem(user_id=1, name="Fiesta", description="A nice car",
                   price="$13,256 Starting MSRP", car_brand=CarBrand8,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem5)
session.commit()

CarItem6 = CarItem(user_id=1, name="Focus", description="A nice car",
                   price="$14,237 Starting MSRP", car_brand=CarBrand8,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem6)
session.commit()

CarItem7 = CarItem(user_id=1, name="Fusion", description="A nice car",
                   price="$20,550 Starting MSRP", car_brand=CarBrand8,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem7)
session.commit()

CarItem8 = CarItem(user_id=1, name="Mustang", description="A nice car",
                   price="$23,364 Starting MSRP", car_brand=CarBrand8,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem8)
session.commit()


# Car Brand
CarBrand9 = CarBrand(name="Infinity")
session.add(CarBrand9)
session.commit()


CarItem1 = CarItem(user_id=1, name="Q50", description="A nice car",
                   price="$30,110 Starting MSRP", car_brand=CarBrand9,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="Q60", description="A nice car",
                   price="$35,253 Starting MSRP", car_brand=CarBrand9,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="Q70", description="A nice car",
                   price="$46,008 Starting MSRP", car_brand=CarBrand9,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="QX30", description="A nice car",
                   price="$26,355 Starting MSRP", car_brand=CarBrand9,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()

CarItem5 = CarItem(user_id=1, name="QX50", description="A nice car",
                   price="$31,312 Starting MSRP", car_brand=CarBrand9,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem5)
session.commit()

CarItem6 = CarItem(user_id=1, name="QX60", description="A nice car",
                   price="$37,830 Starting MSRP", car_brand=CarBrand9,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem6)
session.commit()

CarItem7 = CarItem(user_id=1, name="QX70", description="A nice car",
                   price="$41,728 Starting MSRP", car_brand=CarBrand9,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem7)
session.commit()

CarItem8 = CarItem(user_id=1, name="QX80", description="A nice car",
                   price="$56,711 Starting MSRP", car_brand=CarBrand9,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem8)
session.commit()


# Car Brand
CarBrand10 = CarBrand(name="Jaguar")
session.add(CarBrand10)
session.commit()


CarItem1 = CarItem(user_id=1, name="F-PACE", description="A nice car",
                   price="$42,398 Starting MSRP", car_brand=CarBrand10,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="F-TYPE", description="A nice car",
                   price="$56,938 Starting MSRP", car_brand=CarBrand10,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="XE", description="A nice car",
                   price="$31,706 Starting MSRP", car_brand=CarBrand10,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="XF", description="A nice car",
                   price="$45,608 Starting MSRP", car_brand=CarBrand10,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()

CarItem5 = CarItem(user_id=1, name="XJ", description="A nice car",
                   price="$72,834 Starting MSRP", car_brand=CarBrand10,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem5)
session.commit()


# Car Brand
CarBrand11 = CarBrand(name="Lamborghini")
session.add(CarBrand11)
session.commit()


CarItem1 = CarItem(user_id=1, name="Huracan", description="A nice car",
                   price="$199,800 Starting MSRP", car_brand=CarBrand11,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()


# Car Brand
CarBrand12 = CarBrand(name="Lexus")
session.add(CarBrand12)
session.commit()


CarItem1 = CarItem(user_id=1, name="CT", description="A nice car",
                   price="$31,314 Starting MSRP", car_brand=CarBrand12,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="ES", description="A nice car",
                   price="$38,272 Starting MSRP", car_brand=CarBrand12,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="GS", description="A nice car",
                   price="$45,742 Starting MSRP", car_brand=CarBrand12,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="GX", description="A nice car",
                   price="$50,298 Starting MSRP", car_brand=CarBrand12,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()

CarItem5 = CarItem(user_id=1, name="IS", description="A nice car",
                   price="$37,063 Starting MSRP", car_brand=CarBrand12,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem5)
session.commit()

CarItem6 = CarItem(user_id=1, name="LS", description="A nice car",
                   price="$72,810 Starting MSRP", car_brand=CarBrand12,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem6)
session.commit()

CarItem7 = CarItem(user_id=1, name="LX", description="A nice car",
                   price="$85,959 Starting MSRP", car_brand=CarBrand12,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem7)
session.commit()


# Car Brand
CarBrand13 = CarBrand(name="Porsche")
session.add(CarBrand13)
session.commit()


CarItem1 = CarItem(user_id=1, name="718 Boxster", description="A nice car",
                   price="$55,183 Starting MSRP", car_brand=CarBrand13,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="911", description="A nice car",
                   price="$88,712 Starting MSRP", car_brand=CarBrand13,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="Cayenne", description="A nice car",
                   price="$58,034 Starting MSRP", car_brand=CarBrand13,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()

CarItem4 = CarItem(user_id=1, name="Mecan", description="A nice car",
                   price="$47,307 Starting MSRP", car_brand=CarBrand13,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem4)
session.commit()

CarItem5 = CarItem(user_id=1, name="Panamera", description="A nice car",
                   price="$85,135 Starting MSRP", car_brand=CarBrand13,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem5)
session.commit()


# Car Brand
CarBrand14 = CarBrand(name="Rolls-Royce")
session.add(CarBrand14)
session.commit()


CarItem1 = CarItem(user_id=1, name="Dawn", description="A nice car",
                   price="$343,875 Starting MSRP", car_brand=CarBrand14,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem1)
session.commit()

CarItem2 = CarItem(user_id=1, name="Ghost", description="A nice car",
                   price="$298,350 Starting MSRP", car_brand=CarBrand14,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem2)
session.commit()

CarItem3 = CarItem(user_id=1, name="Wraith", description="A nice car",
                   price="$317,700 Starting MSRP", car_brand=CarBrand14,
                   picture="https://media.ed.edmunds-media.com/mercedes-benz/cla-class/2016/oem/2016_mercedes-benz_cla-class_sedan_cla250_fq_oem_3_1280.jpg")
session.add(CarItem3)
session.commit()


print "added car items!"
