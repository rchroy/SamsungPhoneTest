from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging


class galaxy_z_fold2_5g(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cookie_button = "//button[@class ='cookie-bar__close cookie-bar__main-close']"
    galaxy_z_fold2_5g_phone_name = "//a[@class='product-card-v2__name-link' and @data-modelname='SM-F916B']"
    galaxy_z_fold2_5g_phone_price = "//div[@class='pf-finder-v2__content']/div[1]/div[1]//div[@class='product-card-v2__price-full']"
    galaxy_z_fold2_5g_buy_button = "//div//a[@data-modelname = 'SM-F916B' and @class ='cta cta--contained cta--black js-buy-now']"
    galaxy_z_fold2_5g_device_details = "//div[@class='hubble-product__options s-option-device s-diff-radio']//span[@class= 's-rdo-text']"
    galaxy_z_fold2_5g_colour_details = "//div[@class='hubble-pd-radio s-type-color js-radio-wrap is-checked']"
    galaxy_z_fold2_5g_memory_details = "//div[@class='hubble-product__options s-option-storage s-diff-radio']//span[@class= 's-rdo-text']"
    galaxy_z_fold2_5g_connectivity_details = "//div[@class='hubble-product__options s-option-connect s-diff-radio']//span[@class= 's-rdo-text']"
    galaxy_z_fold2_5g_final = "//div[@class='hubble-product__summary-product']"
    galaxy_z_fold2_5g_price = "//div[@class='hubble-product__total-wrap']//div[@class ='hubble-product__total-text']"



    def closeCookieButton(self):
        self.elementClick(self._cookie_button)

    def getPhoneNameText(self):
        self.getText(self.galaxy_z_fold2_5g_phone_name)

    def getPhonePriceText(self):
        self.getText(self.galaxy_z_fold2_5g_phone_price)

    def clickBuyButton(self):
        self.elementClick(self.galaxy_z_fold2_5g_buy_button)

    def getDeviceDetails(self):
        self.getText(self.galaxy_z_fold2_5g_device_details)

    def getColorDetails(self):
        self.getText(self.galaxy_z_fold2_5g_colour_details)

    def getMemoryDetails(self):
        self.getText(self.galaxy_z_fold2_5g_memory_details)

    def getConnectivityDetails(self):
        self.getText(self.galaxy_z_fold2_5g_connectivity_details)

    def getFinalDetails(self):
        self.getText(self.galaxy_z_fold2_5g_final)

    def getFinalPriceDetails(self):
        self.getText(self.galaxy_z_fold2_5g_price)



    def galaxy_z_fold2_5g_browsing(self):
        self.closeCookieButton()
        self.getPhoneNameText()
        self.getPhonePriceText()
        self.clickBuyButton()
        self.getDeviceDetails()
        self.getColorDetails()
        self.getMemoryDetails()
        self.getConnectivityDetails()
        self.getFinalDetails()
        self.getFinalPriceDetails()
