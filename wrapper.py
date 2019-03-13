from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
from utilities import *
import time
from selenium.webdriver.common.keys import Keys
# import tkinter as tk
import os
from selenium.common.exceptions import NoSuchElementException
import sys

class Brwser():
    jenkins_url = ''
    def __init__(self, choptions):
        chrome_options = Options()
        for option in choptions:
            chrome_options.add_argument(option)

        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def send_click(self,xpth, position, wait,description):
        tmp = self.driver.find_elements_by_xpath(xpth)
        try:
            x = tmp[0]
        except IndexError as exception:
            print("Failed: unable to send click (Element not found)")
            print(exception)
            print(description)
            message = "Action: "+str(description)+" Postion:  "+str(xpth).replace("'","").replace('"','')+":    Failed: unable to send click (Element not found)"
            self.report(message)
            self.clos()
            sys.exit(1)
        if position:
            print(description)
            tmp[position].click()
            if wait:
                self.go_sleep(wait)
            else:
                self.go_sleep(10)
        else:
            print(description)
            for el in tmp:
                if el.is_displayed():
                    el.click()
                    if wait:
                        self.go_sleep(wait)
                    else:
                        self.go_sleep(10)
                    return ''


    def go_to(self,url):
        self.driver.get(url)

    def open_tab(self,url):
        self.driver.execute_script('''window.open("'''+url+'''","_blank");''')

    def text_position(self,text,xpath,position):
        tmp = self.driver.find_elements_by_xpath(xpath)
        tmp[position].clear()
        tmp[position].send_keys(text)

    def send_text(self, text, xpth):
        try:
            tmp = self.driver.find_element_by_xpath(xpth).send_keys(text)
            print("sending text: " + text)
        except NoSuchElementException as exception:
            print("Element not found and test failed")
            print(exception)
            message = text + " " + str(exception).replace('"','').replace("'", "")
            self.report(message)
            self.clos()
            sys.exit(1)

    def go_sleep(self, dur):
        time.sleep(dur)

    def switch_tab(self, pos):
        self.driver.switch_to_window(self.driver.window_handles[pos])

    def paste(self, xpat, text):
        #c = self.driver.execute_script('return window.getSelection().toString();')
        self.send_text(text, xpat)


    def text(self, xpth):
        value =  self.driver.find_element_by_xpath(xpth).text
        return value


    def loop_until_found(self,xpth):
        x = 0
        while x < 61:
            elements = self.driver.find_elements_by_xpath(xpth)
            for element in elements:
                if element.is_displayed():
                    print("is displayed")
                    print("---__---")
                    self.send_click(xpth, '', '','')
                    return ''

            time.sleep(1)
            x = x +1
        self.report("Element is not visible or not clickable ")
        self.clos()
        sys.exit(1)

    def longer_loop(self,xpth):
        x = 0
        while x < 11:
            elements = self.driver.find_elements_by_xpath(xpth)
            for element in elements:
                if element.is_displayed():
                    print("is displayed")
                    print("---__---")
                    self.send_click(xpth, '', '','')
                    return ''

            time.sleep(60)
            x = x + 1
        self.report("Failed: Services took longer than ten minutes to respond.")
        self.clos()
        sys.exit(1)


    def scroll_into_element(self,xpath):
        try:
            x = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", x)
        except NoSuchElementException as exception:
            print("Element not found and test failed")
            print(exception)
            message = "Unable to scroll into element" + " " + str(exception).replace('"','').replace("'", "")
            self.report(message)
            self.clos()
            sys.exit(1)
    def run_command(self,command):
        os.system(command)
        self.go_sleep(3)
    def does_file_exist(self,filename):
        if os.path.isfile(filename):
            os.system('rm '+ filename)

    def clos(self):
        self.driver.quit()

    def ref(self):
        self.driver.refresh()

    def report(self,message):
        os.system("curl -k  -X POST -H 'Content-type: application/json' --data '{\"text\":\""+message+"\"}' https://hooks.slack.com/services/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")

    def get_jenkins_url(self):
        print("getting Jenins url")
        tmp = self.driver.current_url
        tmp = tmp.replace('/manage','')
        self.jenkins_url = tmp
        print("got Jenkins URL")

    def go_to_credentials_url(self):
        cred_url=self.jenkins_url + '/credentials/store/system/domain/_/newCredentials'
        self.go_to(cred_url)

    def go_to_config_url(self):
        config_url=self.jenkins_url + '/job/propel-demo-org/configure'
        self.go_to(config_url)

    def go_to_jenkins_configure_url(self):
        jenkins_configure_url=self.jenkins_url + '/configure'
        self.go_to(jenkins_configure_url)

    def clear_txt(self,xpath):
        self.driver.find_element_by_xpath(xpath).clear()
    def user_creds(self):
        creds_url = self.jenkins_url + '/user/502787729/configure'
        self.go_to(creds_url)
        self.go_sleep(3)
        buttons = self.driver.find_elements_by_xpath("//*[contains(text(), 'Show API Token...')]")
        buttons[0].click()
        api = self.driver.find_element_by_id('apiToken')
        api = api.get_attribute('value')
        return api

    def check_releasability_report_url(self):
        releasability_url = self.jenkins_url + '/3rj50x5b/ci/job/propel-demo-org/job/cid-landing-page-7/job/master/1/'
        self.go_to(releasability_url)

    def check_page_for_phrase(self, text, xpath):
        x = self.driver.find_elements_by_xpath(xpath)
        count = 0
        while count < 75 and not x:
            x = self.driver.find_elements_by_xpath(xpath)
            count = count+1
            self.go_sleep(60)
            print(count)

        if x:
            return False
        return True

    def current_url(self,xpath):
        return self.driver.current_url

    def check_exists_by_xpath(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException as exception:
            print("***********element does not exist**************")
            print(xpath)
            return False
        print("element exist!")
        return True
# This function is to compare two values
    def comp_val(self, val1, val2):
        if val1 == val2:
            print("Values match")
            return True

        print("***Card value doesn't match with the table***")
        return False
