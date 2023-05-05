# GVE DevNet Voice Gateway Licensing
This repository contains code that will assign Smart Licensing to routers. The code accomplishes this by reading information about the routers from a spreadsheet and then connects to the routers using the Python library Netmiko to issue the commands to enable smart licensing on the routers.

![/IMAGES/workflow.png](/IMAGES/workflow.png)

## Contacts
* Danielle Stacy

## Solution Components
* Python 3.11
* Netmiko
* Pandas
* Cisco IOS

## Prerequisites
**Router Credentials**: In order to connect to the routers, the script requires an Excel file called `routers.xlsx` that has columns for the ip address, username, password, and desired http client source-interface for each router. Prior to running the script, make sure that this Excel file is filled out with the information of each router you would like to provide smart licensing.

![/IMAGES/routers_spreadsheet.png](/IMAGES/routers_spreadsheet.png)

**Smart Licensing ID Token**: The script will take an id token generated from Cisco Smart Software Manager. Generate the token following the steps [here](https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/ios-xml/ios/smart-licensing/qsg/b_Smart_Licensing_QuickStart/b_Smart_Licensing_QuickStart_chapter_01.html.xml#id_73526). Once the token is generated, copy it where it will be used in the Installation/Configuration steps later.

## Installation/Configuration
1. Clone this GitHub repository with the command `git clone [add GitHub link here]`.
2. Set up a Python virtual environment. Make sure Python 3 is installed in your environment first, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
3. Add the token you generated in the **Prerequisites** section to the environment variable `TOKEN` in the .env file. Additionally, if you have an IP address that you will be mapping to tools.cisco.com, enter that as the `HOST_IP_ADDRESS` variable.
```python
TOKEN = "enter token here"
HOST_IP_ADDRESS = "enter the static ip address to map to tools.cisco.com here"
```
4. Install the requirements with `pip3 install -r requirements.txt`.

## Usage
To run the program, use the command:
```
$ python3 apply_license.py
```

After the code finishes running, it creates a file called `log.txt` that contains the output of the configuration commands ran on each router as well as the output of the `show license status` and `show license all` commands.

![/IMAGES/smart_license_output.png](/IMAGES/smart_license_output.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.