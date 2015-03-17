#!/bin/bash

# Copyright 2015 BrewPi
# This file is part of BrewPi.

# BrewPi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# BrewPi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with BrewPi Listener.
# If not, see <http://www.gnu.org/licenses/gpl.html>.
#
# @author Thomas Trageser



#
# create required folder of not already exists
#
if [ ! -d "/etc/brewpi" ]
then
    mkdir /etc/brewpi
fi

if [ ! -d "/var/log/brewpi" ]
then
    mkdir /var/log/brewpi
fi

#
# install software requirements
#
apt-get install python-daemon -q

#
# copy files into correct folder
#
cp BrewPiListener.cfg /etc/brewpi/BrewPiListener.cfg
cp brewpi-listener /etc/init.d/brewpi-listener

#
# configure to run for log levels
#
chmod +x /etc/init.d/brewpi-listener
update-rc.d brewpi-listener defaults

#
# start daemon
#
service brewpi-listener start
