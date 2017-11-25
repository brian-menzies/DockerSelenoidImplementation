# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from Helpers.BaseTest import GetAWSConfig
#
#
#
# class PythonOrgSearch(unittest.TestCase):
#
#     def test_search_in_python_org(self):
#         capabilities = {
#             "browserName": "chrome",
#             "version": "62.0"
#         }
#
#         aws_machine_url = GetAWSConfig("HUB_MACHINE_IP")
#         print('http://' + aws_machine_url + ":4444/wd/hub")
#         # full_machine_url =
#
#
#         # self.driver = webdriver.Remote(
#         #     command_executor='http://ec2-18-216-154-51.us-east-2.compute.amazonaws.com:4444/wd/hub',
#         #     desired_capabilities=capabilities)
#         #
#         # driver = self.driver
#         # driver.get("https://github.com")
#         # assert "GitHub" in driver.title
#         # elem = driver.find_element_by_name("q")
#         # elem.send_keys("dzitkowskik")
#         # elem.send_keys(Keys.RETURN)
#         # assert "No results found." not in driver.page_source


# import xml.etree.ElementTree as etree
# from xml.etree.ElementTree import *
# from xml.etree.ElementTree import ElementTree
# tree=ElementTree()
# tree.parse('STRUCTURAL.xml')
# root = tree.getroot()
# col=tree.find('selectionsets/selectionset')
# #find the value needed
# val=tree.findtext('selectionsets/selectionset/findspec/conditions/condition/value/data')
# setname=col.attrib['name']
# listnames=val + " 6"
# inplist=["D","E","F","G","H"]
# entry=3
# catcher=[]
# ss=root.find('selectionsets')
# outxml=ss
# for i in range(len(inplist)):
#     str(val)
#     col.set('name',(setname +" "+ inplist[i]))
#     col.find('findspec/conditions/condition/value/data').text=str(inplist[i]+val[1:3])
#     #print (etree.tostring(col)) #everything working well til this point
#     timper=col.find('selectionset')
#     root[0].append(col)
#     # new=etree.SubElement(outxml,timper)
# #you need to create a tree with element tree before creating the xml file
#
# itree=etree.ElementTree(outxml)
# itree.write('Selection Sets.xml')
# print (etree.tostring(outxml))
#
# # print (Test_file.selectionset())




#
#
#
#
#
#
# from xml.etree import ElementTree as ET
# import io
# import os
#
# # Setup the test input
# inbuf = io.StringIO(''.join(['LIBRARY:\n', '1,1,1,1,the\n', '1,2,1,1,world\n',
#                              '2,1,1,2,we\n', '2,5,2,1,have\n', '7,3,1,1,food\n']))
#
# tags = ['BOOK', 'CHAPTER', 'SENT', 'WORD']
# with inbuf as into, io.StringIO() as xmlfile:
#     root_name = into.readline()
#     root = ET.ElementTree(ET.Element(root_name.rstrip(':\n')))
#     re = root.getroot()
#     for line in into:
#         values = line.split(',')
#         parent = re
#         for i, v in enumerate(values[:4]):
#             parent =  ET.SubElement(parent, tags[i], {'ID': v})
#             if i == 3:
#                 parent.text = values[4].rstrip(':\n')
#     root.write(xmlfile, encoding='unicode', xml_declaration=True)
#     xmlfile.seek(0, os.SEEK_SET)
#     for line in xmlfile:
#         print(line)
#
# with open(xmlfile, 'w') as f:
#     f.write('filename.xml')
#     f.close()
#
#
# # xmlfile.write('filename.xml')
# #
# # print(xmlfile)
# # result = ET.fromstring(xmlfile)
# # tree = ET.ElementTree(result)
# # tree.write("filename.xml")

#
# def indent(elem, level=0):
#     i = "\n" + level*"  "
#     if len(elem):
#         if not elem.text or not elem.text.strip():
#             elem.text = i + "  "
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = i
#         for elem in elem:
#             indent(elem, level+1)
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = i
#     else:
#         if level and (not elem.tail or not elem.tail.strip()):
#             elem.tail = i
#
#
#
# a = [['txt','stxt','pi','min','max'],['txt1','stxt1','pi1','min1','max1']]
# b = [[0.45,1.23],[0.75,1.53]]
# from xml.etree import ElementTree as ET
# root =  ET.Element("xml")
# for l1 in zip(a,b):
#         sroot_root = ET.Element("Class ",name = l1[0][0])
#         doc = ET.SubElement(sroot_root, "subclass" , name = l1[0][1])
#         ET.SubElement(doc, l1[0][4], min = str(l1[1][0]),max = str(l1[1][1]))
#         root.append(sroot_root)
#
#
# tree = ET.ElementTree(root)
# indent(root)
# tree.write("test.xml")





from xml.etree import ElementTree as ET
xml = ET.Element('xml')
tag = ET.SubElement(xml, 'tag')
tag.text = 'this is line 1.' + '\n' + 'this is line 2.'
tree = ET.ElementTree(xml)
tree.write('test.xml')