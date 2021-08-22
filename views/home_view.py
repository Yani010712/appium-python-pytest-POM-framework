from appium.webdriver.common.mobileby import MobileBy

from views.base_view import BaseView
from views.details_view import DetailsView


class HomeView(BaseView):
    GEM_SHIP_ITEM = (MobileBy.XPATH, '//android.widget.TextView[@index=2]')

    def nav_to_details_page(self):
        self.wait_for(self.GEM_SHIP_ITEM).click()
        # return an instance of the page object representing that new view, a new instance of DetailsView from the nav to details page function
        return DetailsView(self.driver)
        
