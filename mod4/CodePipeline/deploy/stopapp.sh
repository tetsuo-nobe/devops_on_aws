#!/bin/sh

systemctl stop SimpleSpringBoot
sudo rm /var/SimpleSpringBoot/SimpleSpringBoot-0.1.0.jar
sudo rm /etc/systemd/system/SimpleSpringBoot.service
