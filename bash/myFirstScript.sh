#!/bin/bash

echo "this is my first script! Hello World!"

echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session Length: $SECONDS
echo Home Dir: $HOME

a=$(ip a | grep 'noprefixroute ens192' | awk '{print $2}')
echo My IP is $a
