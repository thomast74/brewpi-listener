#!/bin/bash

# Copyright 2015 Oink Brew
# This file is part of Oink Brew.

# Oink Brew is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Oink Brew is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Oink Brew Listener.
# If not, see <http://www.gnu.org/licenses/gpl.html>.
#
# @author Thomas Trageser



#
# create required folder of not already exists
#
if [ ! -d "/etc/oinkbrew" ]
then
    mkdir /etc/oinkbrew
fi

if [ ! -d "/var/log/oinkbrew" ]
then
    mkdir /var/log/oinkbrew
    chmod a+w /var/log/oinkbrew
fi

#
# install software requirements
#
apt-get install python-daemon python-requests -y

#
# copy files into correct folder
#
cp oinkbrew_listener.cfg /etc/oinkbrew/oinkbrew_listener.cfg
cp oinkbrew_listener /etc/init.d/oinkbrew_listener

#
# configure to run for log levels
#
chmod +x /etc/init.d/oinkbrew_listener
update-rc.d oinkbrew_listener defaults
update-rc.d oinkbrew_listener enable

#
# start daemon
#
/etc/init.d/oinkbrew_listener start
