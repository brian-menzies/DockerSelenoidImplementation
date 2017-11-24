
r = requests.get('url',  auth=(username, password))
# tree = ET.parse(r.text)
# root = tree.getroot()

with open('data.xml', 'w') as f:
    f.write(r.text)


# Delete Entire XML File Contents
fName = 'data.xml'
with open(fName, "w"):
    pass


# Referencing Path to XML and trying to make sure Python Code File Sees it Correctly
path = '/00_Not_Needed_ATM/AWS_Instances.xml'
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    tree = ElementTree.parse(fullname)



# Trying to Create XML of Available AWS Instances
root = ET.Element("root")
instance = ET.SubElement(root, "instance")

for instance in running_instances:

for attribute in attributes:
    ET.SubElement(instance, attributes[attribute]
    tree = ET.ElementTree(root)


tree.write("filename.xml", pretty_print=True)




# Print the results to the Console for the Tester to See While Testing
attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
print("Found the Following EC2 Instances")
print("------")
for instance_id, INSTANCE in ec2info.items():
    for
key in attributes:
# Print the results to the Console for the Tester / Developer to See
print("{0}: {1}".format(key, INSTANCE[key]))

# XML Insertions that Need to Loop with This Function


print("------")

# Add the Instances to an XML File to be able to be used by Modules within
# the Helper Classes / Tests Themselves When Run During Setup
ElementMaker = lxml.builder.ElementMaker()
ROOT = ElementMaker.root




# To Test and See how it'll work in the EC2_Info_Retriever File
import boto.ec2
from dateutil.parser import *
import subprocess
import datetime


instance_id = subprocess.check_output(['curl', '-s', 'http://169.254.169.254/latest/meta-data/instance-id'])

conn = boto.ec2.connect_to_region('ap-southeast-2',aws_access_key_id='Your_Key', aws_secret_access_key='Your_Secret')

reservations = conn.get_all_reservations(instance_ids=[instance_id])

for r in reservations:
    for instance in r.instances:
        lt_datetime = parse(instance.launch_time)
        lt_delta = datetime.datetime.now(lt_datetime.tzinfo) - lt_datetime
        uptime = str(lt_delta)
        print(uptime)







# From EC2_INFO_RETRIEVER.PY, at time of copying was Line 38
'Launch Time': INSTANCE.launch_time,




import datetime
def format_time(self):
    # Retrieves the Month, Day, and Year Information to Be Formatted Shortly
    date = datetime.date.today()
    print(date)

    time = datetime.datetime.now()
    milliseconds = str(time.microsecond)
    print("Current Milliseconds are: ", milliseconds)

    milliseconds_beginning = milliseconds[:2] if len(milliseconds) > 2 else milliseconds
    print("Beginning of Milliseconds is: ", milliseconds_beginning)

    milliseconds_ending = milliseconds[2:4] if len(milliseconds) > 2 else milliseconds
    print("Ending of Milliseconds is: ", milliseconds_ending)

    full_time = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(time.hour) + "-" + str(
        time.minute) + "-" + str(time.second) + "+" + milliseconds_beginning + ":" + milliseconds_ending
    print("Date and Time Data are: ", full_time)
    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "-" + str(datetime.datetime.now().time())
    # date = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "-" + str(datetime.datetime.now().time())
    # print("Date and Time Data are: ", date)