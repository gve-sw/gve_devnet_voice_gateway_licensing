#!/usr/bin/env python3
"""
Copyright (c) 2022 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
import pandas as pd
from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")
HOST_IP_ADDRESS = os.getenv("HOST_IP_ADDRESS")

# Open spreadsheets to get router information and save to router_dict
router_df = pd.read_excel("routers.xlsx")
num_rows = len(router_df)
router_dict = {}
for row in range(num_rows):
    ip = router_df.loc[row, "ip"]
    username = router_df.loc[row, "username"]
    password = router_df.loc[row, "password"]
    interface = router_df.loc[row, "interface"]
    router_dict[ip] = {
        "username": username,
        "password": password,
        "interface": interface
    }

# Iterate through router_dict to connect to each router and issue the commands with Netmiko
for ip in router_dict:
    cisco_router = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": router_dict[ip]["username"],
        "password": router_dict[ip]["password"]
    }

    # configuration commands that will be ran on each router
    config_commands = [
        'license smart transport callhome',
        'ip http client source-interface ' + interface,
        'ip host tools.cisco.com ' + HOST_IP_ADDRESS,
        'call-home',
        'http resolve-hostname ipv4-first',
        'profile "CiscoTAC-1"',
        'active',
        'destination address http https://tools.cisco.com/its/service/oddce/services/DDCEService',
        'end',
        'license smart register idtoken ' + TOKEN + ' force',
        'write'
    ]

    # show commands that will be ran on each router
    show_commands = [
        'show license status',
        'show license all'
    ]

    # connect to router with Netmiko and run the above commands
    with ConnectHandler(**cisco_router) as router_connect:
        config_output = router_connect.send_config_set(config_commands)

        for cmd in show_commands:
            show_output = router_connect.send_command(cmd)

    # open the file log.txt and write the output from the commands to the file
    with open("log.txt", "a") as log_file:
        log_file.write(ip + " Configuration Commands:\n\n" + config_output)
        log_file.write("\n\n Show Command Output:\n\n" + show_output)
        log_file.write("-" * 50 + "\n\n")