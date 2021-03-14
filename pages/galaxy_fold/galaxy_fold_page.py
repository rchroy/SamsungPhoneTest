from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging


class galaxy_fold(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cookie_button = "//button[@class ='cookie-bar__close cookie-bar__main-close']"
    galaxyfold_phone_name = "//a[@class='product-card-v2__name-link' and @data-modelname='SM-F900F']"
    galaxyfold_phone_price = "//div[@class='pf-finder-v2__content']/div[1]/div[3]//div[@class='product-card-v2__price-full']"
    galaxyfold_buy_button = "//div//a[@data-modelname='SM-F900F' and @class ='cta cta--contained cta--black js-buy-now']"
    galaxyfold_device_details = "//div[@id='pd-header-gallery']//h2[@class='pd-info__title']"
    galaxyfold_device_storage_memory_details = "//div[class='pd-select-option option-device off-scroll off-change bundle-group']//span[@class='pd-option-selector__text']"
    galaxyfold_colour_details = "//div[@id='option-color']//li[1]//span[@class='pd-option-selector__text']"
    galaxyfold_storage_details = "//div[@id='option-device-memory']//strong[@class='pd-option-selector__main-text']"
    galaxyfold_ram_details = "//div[@id='option-storage-memory']//strong[@class='pd-option-selector__main-text']"
    galaxyfold_final = "//div[@class='summary']"
    galaxyfold_price = "//div[@id='option-device']//span[@class='pd-option-selector__sub-text']"



    def closeCookieButton(self):
        self.elementClick(self._cookie_button)

    def getPhoneNameText(self):
        self.getText(self.galaxyfold_phone_name)

    def getPhonePriceText(self):
        self.getText(self.galaxyfold_phone_price)

    def clickBuyButton(self):
        self.elementClick(self.galaxyfold_buy_button)

    def getDeviceDetails(self):
        self.getText(self.galaxyfold_device_details)

    def getDeviceStorageMemoryDetails(self):
        self.getText(self.galaxyfold_device_storage_memory_details)

    def getColorDetails(self):
        self.getText(self.galaxyfold_colour_details)

    def getStorageDetails(self):
        self.getText(self.galaxyfold_storage_details)

    def getRamDetails(self):
        self.getText(self.galaxyfold_ram_details)

    def getFinalDetails(self):
        self.getText(self.galaxyfold_final)

    def getFinalPriceDetails(self):
        self.getText(self.galaxyfold_price)



    def galaxy_fold_browsing(self):
        self.closeCookieButton()
        self.getPhoneNameText()
        self.getPhonePriceText()
        self.clickBuyButton()
        self.getDeviceDetails()
        self.getColorDetails()
        self.getStorageDetails()
        self.getRamDetails()
        self.getFinalDetails()
        self.getFinalPriceDetails()
