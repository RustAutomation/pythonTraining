from GSearchPage import SearchHelper

def test_google_search(browser):
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word("Hello")
    google_main_page.click_on_the_search_button()
    elements = google_main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements