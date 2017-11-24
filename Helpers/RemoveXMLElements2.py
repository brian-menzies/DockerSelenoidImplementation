from xml.etree.ElementTree import ElementTree
import os

import xml.etree.ElementTree as et

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, 'XML_Files/')

path = XMLFILES_FOLDER + 'AWS_Instances.xml'

print(path)

file = 'AWS_Instances.xml'
tree = et.parse(path)
root = tree.getroot()
print(root)

elements_to_remove = tree.findall('AWS_Instances')

def iterator(parents, nested=False):
    for child in reversed(parents):
        if nested:
            if len(child) >= 1:
                iterator(child)
        if True:  # Add your entire condition here
            parents.remove(child)

iterator(elements_to_remove, nested=True)
tree.write('AWS_Updates_Instances.xml')
print("Created New XML File [AWS_Intances2] that contains "
      "base data and can be added to when Starting Tests "
      "and Launching New Machines / Instances")