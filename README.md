oinkbrew-listener
=================

Description
-----------

The Oink Brew Listener is retrieving status updates that are sent from all BrewPi Sparks with Oink Brew Firmware in your local network.
This setup makes it is easy to integrate your BrewPi Sparks with minimum effort. 
Load Oink Brew Firmware onto BrewPi Spark.
Setup wifi on your BrewPi Spark and shortly after you will see the new BrewPi Spark in your Oink Brew WebApp or Oink Brew Mobile.

The Oink Brew Listener bridges the gap between the Oink Brew WebApp who does not know anything about your BrewPi Sparks and the BrewPi Sparks that do not know anything about your Oink Brew WebApp.

The Oink Brew Listener is retrieving Status Updates via UDP from the Oink Brew Firmware and hands them over to the WebApp API Service Layer. The API Service Layer can then contact the BrewPi Spark directly and ask for device list etc and makes itself known to the BrewPi Spark for logging sensor and actuator data.

Setup
-----

Follow the instructions to setup Oink Brew Listener to start retrieving status updates from the BrewPi Sparks with Oink Brew Firmware

1. create folder /opt/oinkbrew if not already exists
    > sudo mkdir /opt/oinkbrew

2. Create folder /opt/oinkbrew/oinkbrew_listener
    > sudo mkdir /opt/oinkbrew/oinkbrew_listener

3. Change directory to this folder
    > cd /opt/oinkbrew/oinkbrew_listener

4. If you have not installed git yet, it is time to do so
    > sudo apt-get install git-core

5. Clone the git repository
    > sudo git clone https://github.com/thomast74/oinkbrew-listener.git

6. Run install script
    > sudo chmod +x ./install.sh
    > sudo ./install.sh

Check log file for errors /var/log/oinkbrew/oinkbrew_listener.err.log

The application is installed as a daemon and will automatically start after booting up.
