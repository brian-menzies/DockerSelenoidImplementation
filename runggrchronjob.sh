#!/bin/bash
while true
do
 sleep 10
 curl --silent '' > /etc/grid-router/quota/orasitester.xml
 docker kill -s HUP ggrbalancer
done
