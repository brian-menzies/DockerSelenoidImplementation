import lxml.builder
import os
import xml.etree.cElementTree as ElementTree
from Helpers.FilePath import get_full_path

"""
A process for parsing a Text (.txt) File and Creating an XML File that Portrays the Same Information,
But in a Much Prettier and More Concise and Easily-Readable Style
"""


# Formatting Functions Used Constantly Throughout The
# Code Talking to the EC2 Instances Seen Below
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = get_full_path()


XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, 'Plug_and_Play_Files/')
xml_path = XMLFILES_FOLDER + 'Instance_Info.xml'

TXTFILES_FOLDER = os.path.join(PROJECT_ROOT, 'Plug_and_Play_Files/')
txt_path = TXTFILES_FOLDER + 'SampleTextFile.txt'


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i



def process_the_xml_file(file_to_process):
    print("5. File to process is : ", file_to_process)
    file = open(file_to_process, 'r')
    lines = file.readlines()
    print(lines)
    file.close()

# Set up the New XML Standard and Non-Changing
# Elements to Be Used While Looping Through the Results
ElementMaker = lxml.builder.ElementMaker()
ROOT = ElementMaker.root

dictionary = {}
with open(txt_path) as f:
    instance_number = 0
    line_number = 1
    for line in f:
        if "Name" in line:
            print("Found [Name] on Line [%s]. Starting a New Dictionary Index from Instance Number [%s] and Appending "
                  "All Values to This New Dictionary Index Number Until Finding Another Instance of the Text [Name]"
                  % (line_number, instance_number))
            instance_number += 1
            # (instance_id, name, val) = (instance_number, line.split(": ")[0], line.split(": ")[1].replace("\n", ""))
            (instance_id, val) = (instance_number, line.replace("\n", ""))
            dictionary[instance_id] = [val]
            print("Current Dictionary is: ", dictionary)
            print("")
            print("")

        else:
            current_instance_number = instance_number
            new_val = (line.replace("\n", ""))
            dictionary[current_instance_number].append(new_val)

        print(line_number)
        print("Current Dictionary is: ", dictionary)
        line_number += 1
        print("")
        print("")


print("------")

attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time', 'Time Checked', 'Time Created']
print("Found the Following EC2 Instances:")
print("------")
instance_id = 1


xml_list = []

# Elements that Don't Need to Be in the Loop as they Won't Be Changing

root = ElementTree.Element("AWSINSTANCEINFO")

for key in dictionary:

    instance = ElementTree.SubElement(root, "INSTANCE")
    instance_name = ElementTree.SubElement(instance, "NAME").text = dictionary[key][0].split(": ")[1]
    instance_type = ElementTree.SubElement(instance, "TYPE").text = dictionary[key][1].split(": ")[1]
    instance_state = ElementTree.SubElement(instance, "STATE").text = dictionary[key][2].split(": ")[1]
    instance_private_ip = ElementTree.SubElement(instance, "PRIVATEIP").text = dictionary[key][3].split(": ")[1]
    instance_public_ip = ElementTree.SubElement(instance, "PUBLICIP").text = dictionary[key][4].split(": ")[1]
    instance_launch_time = ElementTree.SubElement(instance, "LAUNCHTIME").text = dictionary[key][5].split(": ")[1]
    instance_time_checked = ElementTree.SubElement(instance, "TIMECHECKED").text = dictionary[key][6].split(": ")[1]
    instance_time_created = ElementTree.SubElement(instance, "TIMECREATED").text = dictionary[key][7].split(": ")[1]


    instance_id += 1


tree = ElementTree.ElementTree(root)
indent(root)
tree.write("AWS_Config.xml")