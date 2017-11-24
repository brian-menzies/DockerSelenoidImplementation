from xml.etree.ElementTree import ElementTree
import os

class Accounts:
    def __init__(self):
        pass

accounts = Accounts()

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, 'XML_Files/')

path = XMLFILES_FOLDER + 'AWS_Instances.xml'

print(path)

tree = ElementTree
parsed_file = ElementTree.parse(accounts, source=path)
print("Parsing Existing AWS_Instances XML File")

root = tree.getroot(accounts)
print("Root is :", root)
print("Automatically  Got Root of Parsed File")


aws_instances = parsed_file.findall('instance')

for child in root:
    if child.name != "instance":
        continue
    if True:# TODO: do your check here!
        root.remove(child)

print(aws_instances)
for instance in aws_instances:
    instance.remove(instance)
    print("Removed All Machine Info / Instance Elements from XML Document")

tree.write(accounts, 'AWS_Updated_Instances.xml')
print("Created New XML File [AWS_Intances2] that contains base data and can be added to when Starting Tests and Launching New Machines / Instances")

# os.remove("AWS_Instances2.xml")
# print("Removed [AWS_Instances2] XML File from Project")