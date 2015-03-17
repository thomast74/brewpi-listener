brewpi-listener
===============

Description
-----------

The BrewPi Listener is retrieving status updates that are sent from all BrewPi Sparks in your local network.
This setup makes it is easy to integrate you BrewPi Sparks with minimum effort. Just setup wifi on your BrewPi Spark and shortly after you will see the new BrewPi Spark in your BrewPi WebApp.

The BrewPi Listener bridges the gap between the BrewPi WebApp who does not know anything about your BrewPi Sparks and the BrewPi Sparks that do not know anything about your BrewPi WebApp.

The BrewPi Listener is retrieving Status Updates via UDP from the BrewPi Sparks and hands them over to the WebApp API Service Layer. The API Service Layer can then contact the BrewPi Spark directly and ask for device list etc and makes itself known to the BrewPi Spark for logging sensor and actuator data.

Setup
-----

Follow the instructions to setup BrewPi Listener to start retrieving status updates from the BrewPi Sparks.

1. create folder /opt/brewpi if not already exists
    > sudo mkdir /opt/brewpi

2. Create folder /opt/brewpi/brewpi-listener
    > sudo mkdir /opt/brewpi/brewpi-listener

3. Change directory to this folder
    > cd /opt/brewpi/brewpi-listener

4. If you have not installed git yet, it is time to do so
    > sudo apt-get install git-core

5. Clone the git repository
    > sudo git clone https://github.com/thomast74/brewpi-listener.git

6. Run install script
    > sudo chmod +x ./install.sh
    > sudo ./install.sh

Check log file for errors /var/log/brewpi/BrewPiListener.err.log

The application is installed as a daemon and will automatically start after booting up.
