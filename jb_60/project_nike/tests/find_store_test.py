from jb_60.project_nike.pages.find_store_page import StorePage


class TestFindStore():

    def test_find_first_store(self,setup_nike):
        page = setup_nike

        stores_in_madrid = StorePage.count_store_in_location(page,'Madrid')
        assert stores_in_madrid > 0
