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



import datetime
def current_time(self):
    date = datetime.date.today()
    time = datetime.datetime.now()
    if time.second <= 9:
        seconds = "0" + str(time.second)
    else:
        seconds = time.second
    return str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)