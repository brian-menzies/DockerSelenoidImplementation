import sqlite3
import xml.etree.cElementTree as ElementTree

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

# Setup XML File Structure
user_filename = 'quotafile/orasitester.xml'
root = ElementTree.Element('qa:browsers', attrib={"xmlns:qa": "urn:config.gridrouter.qatools.ru"})
region_name = {'name': "us-east-1"}


# Initialize Lists to be Fed into By Data Retrieval Call
chrome_versions = []
firefox_versions = []
edge_versions = []
safari_versions = []
opera_versions = []
ie_versions = []


# Start Querying Database
db = sqlite3.connect('hubips.db')
cursor = db.cursor()

# Instantiate a List of Lists to Continue to Be Updated During DB Data Retrieval Calls Below
lists = [chrome_versions, firefox_versions, ie_versions, safari_versions, opera_versions]
query_parameters = ['chromeversions', 'firefoxversions', 'edgeversions', 'safariversions', 'operaversions', 'ieversions']
i=0

for parameter in range(0, len(query_parameters)):
    execute_command = "SELECT " + query_parameters[parameter] + \
                      " FROM ips WHERE " + query_parameters[parameter] + \
                      " IS NOT NULL"
    cursor.execute(execute_command)
    all_rows = cursor.fetchall()

    # Iterate Through All Rows, Appending Version List of Corresponding Browser
    for row in all_rows:
        split_versions = str(row[0]).split(',')
        number_versions = len(split_versions)
        for version in range(0, number_versions):
            # Begin Set up For Writing orasitester.xml File
            if not split_versions[version].lower() == 'none':
                lists[i].append(split_versions[version])
    i +=1


latest_browser_list = []
latest_versions_list = []

if not len(chrome_versions) == 0:
    chrome_versions = list(set(chrome_versions))
    latest_chrome = max(chrome_versions)
    latest_browser_list.append(chrome_versions)
    latest_versions_list.append(latest_chrome)

if not len(firefox_versions) == 0:
    firefox_versions = list(set(firefox_versions))
    latest_firefox = max(firefox_versions)
    latest_browser_list.append(firefox_versions)
    latest_versions_list.append(latest_firefox)


if not len(edge_versions) == 0:
    edge_versions = list(set(edge_versions))
    latest_edge = max(edge_versions)
    latest_browser_list.append(edge_versions)
    latest_versions_list.append(latest_edge)


if not len(safari_versions) == 0:
    safari_versions = list(set(safari_versions))
    latest_safari = max(safari_versions)
    latest_browser_list.append(safari_versions)
    latest_versions_list.append(latest_safari)


if not len(opera_versions) == 0:
    opera_versions = list(set(opera_versions))
    latest_opera = max(opera_versions)
    latest_browser_list.append(opera_versions)
    latest_versions_list.append(latest_opera)


if not len(ie_versions) == 0:
    ie_versions = list(set(ie_versions))
    latest_ie = max(ie_versions)
    latest_browser_list.append(ie_versions)
    latest_versions_list.append(latest_ie)


# Instantiate More Lists that Will Be Used During XML Creation To Limit Amount of Code Needed
name_attributes = ['chrome', 'firefox', 'edge', 'safari', 'opera', 'internet explorer']

# Get all IPS and Finish Creating the XML File and Create It
for attribute in range(0, len(name_attributes)):
    # Create XML Browser Node
    i = 0
    try:
        version_atttr = {'defaultVersion': (latest_versions_list[attribute]), 'name': (name_attributes[attribute])}
        # version_atttr = {'name': (name_attributes[attribute]), 'defaultVersion': (latest_browser_list[attribute])}
        xml_name = ElementTree.SubElement(root, 'browser', attrib=version_atttr)

        for browser_version in range(0, len(latest_browser_list[attribute])):
            execute_command = "SELECT ipaddr" \
                          " FROM ips WHERE " + query_parameters[attribute] + \
                          " LIKE '%" + str(latest_browser_list[attribute][browser_version]).strip() + "%'"
            cursor.execute(execute_command)
            all_rows = cursor.fetchall()
            version_xml = ElementTree.SubElement(xml_name, 'version', attrib={"number": (str(latest_browser_list[attribute][browser_version]).strip() + ".0")})
            region_xml = ElementTree.SubElement(version_xml, 'region', attrib=region_name)
            for row in all_rows:
                host_xml = ElementTree.SubElement(region_xml, 'host', attrib={'name': row[0], 'port': '4445', 'count': '1'})

    except:
        pass

    i += 1

tree = ElementTree.ElementTree(root)
indent(root)

tree.write(user_filename)
