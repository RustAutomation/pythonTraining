from FirstSeleniumScript import SearchPage
from selenium.webdriver.common.by import By


class GSeacrhPage:
    GOOGLE_SEARCH_FIELD = (By.XPATH, "//input[@title='Поиск']")
    GOOGLE_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    GOOGLE_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")


class SearchHelper(SearchPage):

    def enter_word(self, word):
        search_field = self.find_element(GSeacrhPage.GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(GSeacrhPage.GOOGLE_SEARCH_BUTTON, time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(GSeacrhPage.GOOGLE_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu
