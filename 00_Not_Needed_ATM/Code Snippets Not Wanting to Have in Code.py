
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
















# code that reads the file line by line
def read_the_file(file_to_read):
    f = open('library.xml','r')
    line = f.readline()
    print("1. Line is : ", line)
    if '<AWSINSTANCEINFO>' in line:
        next_line = f.readline()
        print("2. Next line is : ", next_line)
        write_f = open('myfile', 'w')
        while '/AWSINSTANCEINFO' not in next_line:
            write_f.write(next_line)
            next_line = f.readline()
            print("3. Next line is : ", next_line)
        write_f.close()
        return write_f.name
    else:
        return f.name

# code that processes the xml file
def process_the_xml_file(file_to_process):
    print("5. File to process is : ", file_to_process)
    file = open(file_to_process, 'r')
    lines=file.readlines()
    print(lines)
    file.close()


# calling the code to read the file and process the xml
path_to_file='test.xml'
write_f=read_the_file(path_to_file)
print("4. Write f is : ", write_f)
process_the_xml_file(write_f)






for key in dictionary:
    # for key in attributes:
        # Have to Start at 1 as I don't have a Dictionary Entry 0 as Code Doesn't Create It As Written Currently
    # print("Key is: ", key)
    # print(dictionary[key][0])
    # print(dictionary[key][1])
    # print(dictionary[key][2])
    # print("Dictionary Entry 1 is: ", dictionary[1][0])
    # print("Dictionary Entry 2 is: ", dictionary[2][1])
    # print("Dictionary Entry 3 is: ", dictionary[3][2])
    # Print the results to the Console for the Tester / Developer to See
    # print("{0}: {1}".format(key, INSTANCE[key]))






xml_content = ROOT(
    INSTANCE(
        NAME(dictionary[key][0].split(": ")[0], dictionary[key][0].split(": ")[1]),
        TYPE(dictionary[key][1].split(": ")[1]),
        STATE(dictionary[key][2].split(": ")[1]),
        PRIVATEIP(dictionary[key][3].split(": ")[1]),
        PUBLICIP(dictionary[key][4].split(": ")[1]),
        LAUNCHTIME(dictionary[key][5].split(": ")[1]),
        TIMECHECKED(dictionary[key][6].split(": ")[1]),
        TIMECREATED(dictionary[key][7].split(": ")[1])
    )
)





# indent(root)

    # INSTANCEINFO = ElementMaker.INSTANCEINFO
    # INSTANCE = ElementMaker.INSTANCE
    # NAME = ElementMaker.NAME
    # TYPE = ElementMaker.TYPE
    # STATE = ElementMaker.STATE
    # PRIVATEIP = ElementMaker.PRIVATEIP
    # PUBLICIP = ElementMaker.PUBLICIP
    # LAUNCHTIME = ElementMaker.LAUNCHTIME
    # TIMECHECKED = ElementMaker.TIMECHECKED
    # TIMECREATED = ElementMaker.TIMECREATED
    #
    # instance_info = ElementMaker.SubElement(ROOT, INSTANCEINFO())
    # output_to_xml_file(instance_info, 1)
    #
    # instance_content = ElementMaker.SubElement(instance_info, INSTANCE())
    # output_to_xml_file(instance_content, 1)
    #
    # name_content = ElementMaker.SubElement(instance_info, NAME(dictionary[key][0].split(": ")[1]))
    # output_to_xml_file(name_content, 1)
    #
    # type_content = ElementMaker.SubElement(instance_info, TYPE(dictionary[key][1].split(": ")[1]))
    # output_to_xml_file(type_content, 1)
    #
    # state_content = ElementMaker.SubElement(instance_info, STATE(dictionary[key][2].split(": ")[1]))
    # output_to_xml_file(state_content, 1)
    #
    # private_ip_content = ElementMaker.SubElement(instance_info, PRIVATEIP(dictionary[key][3].split(": ")[1]))
    # output_to_xml_file(private_ip_content, 1)
    #
    # public_ip_content = ElementMaker.SubElement(instance_info, PUBLICIP(dictionary[key][4].split(": ")[1]))
    # output_to_xml_file(public_ip_content, 1)
    #
    # launch_time_content = ElementMaker.SubElement(instance_info, LAUNCHTIME(dictionary[key][5].split(": ")[1]))
    # output_to_xml_file(launch_time_content)
    #
    # time_checked_content = ElementMaker.SubElement(instance_info, TIMECHECKED(dictionary[key][6].split(": ")[1]))
    # output_to_xml_file(time_checked_content)
    #
    # time_created_content = ElementMaker.SubElement(instance_info, TIMECREATED(dictionary[key][7].split(": ")[1]))
    # output_to_xml_file(time_created_content)



    # xml_file = open(xml_path, 'wb')
    # xml_file.write(xml_content)
    # xml_file.close()
    # print(xml_content)
    # print(lxml.etree.tostring(instance_info, pretty_print=True))
    # string_xml = str(lxml.etree.tostring(instance_info, pretty_print=True))
    # tree = ET.XML(xml_content)
    # root = Element('INSTANCE_INFO_IN_XML_FILE')
    # tree = ElementTree(root)
    # with open(xml_path, "wb") as f:
    #     f.write(ET.tostring(tree))

    # tree.write(open(xml_path, 'w'), encoding='unicode', xml_declaration=True)

    # with open(xml_path, 'w') as f:
    #     f.write(string_xml)
    #     f.close()

    # with open(xml_path, 'wb') as myfile:
    #     myfile.write(xml_content)
    #







# for index in range(0, len(xml_list)):
#     tree = xml_list[index]
#     indent(root)




#
# def output_to_xml_file(part_to_output, indent_level):
#     print(lxml.etree.tostring(part_to_output, pretty_print=True))
#     string_xml = str(lxml.etree.tostring(part_to_output, pretty_print=True))
#     with open(xml_path, 'a') as file:
#         file.write(string_xml)
#         indent(part_to_output, indent_level)
#         file.close()





# def current_time():
#     # Format and Handle the Current Time Values to
#     # Match Those Given by Call to Service
#     date = datetime.date.today()
#     time = datetime.datetime.now()
#
#     time_sections = ['hour', 'minute', 'second']
#     number_sections = range(0, len(time_sections))
#
#     for section in number_sections:
#         if section == 0:
#             if time.hour <= 9:
#                 hours = "0" + str(time.hour)
#             else:
#                 hours = time.hour
#         elif section == 1:
#             if time.minute <= 9:
#                 minutes = "0" + str(time.minute)
#             else:
#                 minutes = time.minute
#         elif section == 2:
#             if time.second <= 9:
#                 seconds = "0" + str(time.second)
#             else:
#                 seconds = time.second
#
#     return str(date.year) + "-" + str(date.month) + "-" + str(date.day) \
#            + " " + str(hours) + ":" + str(minutes) + ":" + str(seconds)





# xmlfile = ET.parse('file.xml')
a = xmlfile.getroot()

f = ET.Element('f')
g = ET.SubElement(f,'g')

f.tail = "\n    "
f.text = "\n        "
g.tail = "\n    "

a.insert(1, f)