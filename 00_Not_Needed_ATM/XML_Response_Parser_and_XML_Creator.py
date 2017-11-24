import xml.etree.ElementTree as ET
from Helpers.FilePath import get_full_path
import requests
import os
from collections import defaultdict

from Helpers.GetConfig import GetConfig



def parse_and_format_xml(request_url):
    XML = requests.get(request_url, stream=True)
    # tree = ET.parse(XML.raw)
    root = ET.fromstring(XML.content)

    #
    # tree = ET.parse(response_message.raw)
    # root = tree.getroot()

    print("Root of Response message is: ", root)
    newroot = ET.Element("root")
    newroot.insert(0, root)
    print(ET.tostring(newroot, pretty_print=True))



username = GetConfig("GHUSER")
password = GetConfig("GHPASS")

# Removes the XML File containing the Sensitive Information at the Tear Down Mehod
try:
    os.remove(get_full_path("XML_Files/data.xml"))
    print("DATA XML File Removed!")
except:
    pass


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response1 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters, stream=True)
request_url = "http://api.open-notify.org/iss-pass.json"

# Print the content of the response (the data the server returned)
print(response1.content)


# Format the Data
formatted_response = parse_and_format_xml(request_url)


# Write it to An XML File of Your Designation
with open('data.xml', 'w') as f:
    f.write(formatted_response)


# This gets the same data as the command above
response2 = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74", stream=True)
print(response2.content)

with open('data.xml', 'w') as f:
    f.write(response2.text)