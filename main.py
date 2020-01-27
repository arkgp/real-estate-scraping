from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

class ListingScraper:

    def __init__(self, url):
        self.url = url
    
    def run(self):
        if self.url.find("sothebysrealty") != -1:
            self.run_sothebys()
        elif self.url.find("centris") != -1:
            self.run_centris()
        elif self.url.find("duproprio") != -1:
            self.run_duproprio()

    def run_sothebys(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.url)
        title = self.browser.find_element_by_tag_name("h1").text[:3]
        os.mkdir(title)
        self.browser.save_screenshot(title + "/main.png")
        self.browser.find_element_by_css_selector("html body#top.page-detail.desktop div.listing_images_wrap ul.user_options li.mod_media div span").click()
        initial_count = int(self.browser.find_element_by_class_name("gal_count").text[4:])
        photo_count = int(self.browser.find_element_by_class_name("gal_count").text[4:])
        self.browser.find_element_by_class_name("fullscreen").click()
        while photo_count:
            time.sleep(0.5)
            self.browser.save_screenshot(title + "/picture" + str(initial_count - photo_count + 1) + ".png")
            actions = ActionChains(self.browser)
            actions.send_keys(Keys.RIGHT)
            actions.perform()
            photo_count -= 1
        self.browser.close()

    def run_centris(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.url)
        time.sleep(5)
        title = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div[1]/div/div/article/div[2]/div/div[3]/h2").text[:39]
        os.mkdir(title)
        self.browser.save_screenshot(title + "/main.png")
        self.browser.find_element_by_css_selector("li.gallery > a:nth-child(1) > span:nth-child(1)").click()
        initial_count = int(self.browser.find_element_by_css_selector(".footer > div:nth-child(1) > strong:nth-child(1)").text[2:])
        photo_count = int(self.browser.find_element_by_css_selector(".footer > div:nth-child(1) > strong:nth-child(1)").text[2:])
        while photo_count:
            time.sleep(0.8)
            self.browser.save_screenshot(title + "/picture" + str(initial_count - photo_count + 1) + ".png")
            actions = ActionChains(self.browser)
            actions.send_keys(Keys.RIGHT)
            actions.perform()
            photo_count -= 1
        self.browser.close()

    def run_duproprio(self):
        pass

if __name__ == "__main__":
    scraper = ListingScraper("https://sothebysrealty.ca/en/property/quebec/montreal-real-estate/ahuntsic-cartierville/19438/")
    scraper.run()