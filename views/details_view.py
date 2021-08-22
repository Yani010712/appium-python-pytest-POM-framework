from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException

from views.base_view import BaseView

class DetailsView(BaseView):
    GEM_IMAGE = (MobileBy.XPATH, '//android.widget.ImageView[@resource-id="com.ncl.nclcruiseinfo:id/cruiseDetailImageView"]')
    FACTS_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="Ship Facts"]')
    CREW_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="Crew"]')
    CREW_VALUE = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.ncl.nclcruiseinfo:id/valueLabel"]')
    CRUICE_SPEED = (MobileBy.XPATH, '//android.widget.TextView[@text="Cruise Speed"]')
    SPEED_VALUE = (MobileBy.XPATH, '//android.widget.TextView[@text="24 knots"]')
    DRAFT_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="Draft"]')
    DRAFT_VALUE = (MobileBy.XPATH, '//android.widget.TextView[@text="28.2 feet"]')
    ENGINES_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="Engines"]')
    DIESEL_ELECTRIC_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="Diesel Electric"]')
    GROSS_REGISTER_TONNAGE_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="Gross Register Tonnage"]')
    GROSS_REGISTER_TONNAGE_VALUE = (MobileBy.XPATH, '//android.widget.TextView[@text="93,530"]')
    INAUGURAL_DATE_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="Inaugural Date"]')
    INAUGURAL_DATE_VALUE = (MobileBy.XPATH, '//android.widget.TextView[@text="2007"]')
    MAX_BEAN_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="Max Beam"]')
    MAX_BEAN_VALUE = (MobileBy.XPATH, '//android.widget.TextView[@text="125 feet"]')

    def display_first_element_text(self, locator):
            return self.wait_for(locator).text

    def display_element_text(self, locator):
            return self.find(locator).text
    
    def display_element_image(self, locator):
        return self.wait_for(locator).is_displayed()
        
    def nav_back(self):
        from views.home_view import HomeView
        self.driver.back()
        return HomeView(self.driver)











        
    # def display_element(self, identifier):
    #     try:
    #         return self.wait_for(identifier).text
    #     except TimeoutException:
    #         return None

    # def displays_crew(self):
    #     try:
    #         return self.wait_for(self.CREW_LABEL).text
    #     except TimeoutException:
    #         return None


  