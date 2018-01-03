#!/bin/bash
while true
do
 sleep 10
 curl --silent 'http://54.145.92.108:1337/orasitester.xml' > /etc/grid-router/quota/orasitester.xml
 docker kill -s HUP ggrbalancer
done
