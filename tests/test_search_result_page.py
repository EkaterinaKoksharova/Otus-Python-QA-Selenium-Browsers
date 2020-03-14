""" Тесты для страницы результата поиска"""


from pages.search_result_page import SearchResultPage


class TestSearchResultPage:
    """ Тесты для страницы результата поиска"""

    def test_search_result_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице результата поиска"""

        browser.get(SearchResultPage.search_result_page_url)

        browser.find_element(*SearchResultPage.search_input)

        browser.find_element(*SearchResultPage.category_list)
        browser.find_element(*SearchResultPage.category_desktops)
        browser.find_element(*SearchResultPage.category_laptops_and_notebooks)
        browser.find_element(*SearchResultPage.category_components)
        browser.find_element(*SearchResultPage.category_tablets)
        browser.find_element(*SearchResultPage.category_software)
        browser.find_element(*SearchResultPage.category_phones_and_pdas)
        browser.find_element(*SearchResultPage.category_cameras)
        browser.find_element(*SearchResultPage.category_mp3_players)

        browser.find_element(*SearchResultPage.subcategories_checkbox)
        browser.find_element(*SearchResultPage.search_in_product_descriptions_checkbox)
        browser.find_element(*SearchResultPage.search_button)