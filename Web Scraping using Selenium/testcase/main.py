import unittest
from selenium import webdriver
import page

# setUp and tearDown functions are executed for each test function
# setUp is called at the beginning of execution and tearDown at the end
# unitest will automatically call functions that start with "test"
class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome('D:\Program Files (x86)\chromedriver.exe')
        self.driver.get('http://python.org')

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

        mainPage.search_text_element = 'pycon'
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
