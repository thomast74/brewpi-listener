brewpi-listener
===============

Description
-----------

The BrewPi Listener is retrieving status updates that are sent from all BrewPi Sparks in your local network.
This setup makes it is easy to integrate you BrewPi Sparks with minimum effort. Just setup wifi on your BrewPi Spark and shortly after you will see the new BrewPi Spark in your BrewPi WebApp.

The BrewPi Listener bridges the gap between the BrewPi WebApp who does not know anything about your BrewPi Sparks and the BrewPi Sparks that do not know anything about your BrewPi WebApp.

The BrewPi Listner is retrieving Status Updates via UDP from the BrewPi Sparks and hands them over to the WebApp API Service Layer. The API Service Layer can then contact the BrewPi Spark directly and ask for device list etc and makes itself known to the BrewPi Spark for logging sensor and actuator data.

Setup
-----

Follow the instructions to setup BrewPi Listener to start retrieving status updates from the BrewPi Sparks.
