import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class PythonOrgSearch(unittest.TestCase):

    def test_search_in_python_org(self):
        capabilities = {
            "browserName": "chrome",
            "version": "62.0"
        }

        self.driver = webdriver.Remote(
            command_executor='http://ec2-18-216-154-51.us-east-2.compute.amazonaws.com:4444/wd/hub',
            desired_capabilities=capabilities)

        driver = self.driver
        driver.get("https://github.com")
        assert "GitHub" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("dzitkowskik")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()