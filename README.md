# Car Catalog

A website that shows various car brands as well as their popular car model
<br />
<br />
<br />

## How to configure the linux server and run on localhost
<br />
1. Follow the <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/00413454014/modules/357367901175460/lessons/4597278561/concepts/47133485700923">instructions</a> to setup the VM environment using vagrant<br />
2. Download this repository and store it in vagrant folder<br />
3. In the terminal, change directory to "catalog_app" project root directory<br />
4. Setup the database <pre>python database_setup.py </pre>
5. Fill some pre-selected data into the database <pre>python lotsofcars.py</pre>
6. Run the localhost: <pre>python project.py</pre>
7. Check the website at: <a href="http://localhost:5000">http://localhost:5000</a><br />
<br />

#### Notice:
The car brands are fixed and can't be modified. However, user can add/modify/delete car models under a specific brand after successfully login.

