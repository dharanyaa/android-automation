from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from allure.constants import AttachmentType
import allure
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import uuid
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from proxysetup.pattern_mathing import beacon_check
import subprocess
import time
import os
import signal
import cv2
import requests
import glob


RC_URL ="http://rc-studio.inmobi.com/automation/studiokeg/showad.asm?c=inmobi"

class testcasehelpers():

    @staticmethod
    def check_element_clickable_click(self, secs, selector, elementName):

        try:
            element = WebDriverWait(self.driver, secs).until(ec.element_to_be_clickable((selector, elementName)))
            print element
            element.click()
        except NoSuchElementException:
            return False
        return True


    @staticmethod
    def get_data():
        # pwd = os.path.dirname(__file__)
        try:
            pwd = os.getcwd()
            # dest_fname = os.path.join(pwd, relative_fname)
            print pwd
            # df = pd.read_excel(os.path.join(os.getcwd(), 'testdata/data.xlsx'), sheet_name='Sheet1')
            list_of_files = glob.glob('/Users/rmqa/Desktop/data/*')  # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            print 'latest file:*********' + latest_file
            df = pd.read_excel(latest_file, sheet_name='Sheet1')
            # df = pd.read_csv('/Users/rmqa/Desktop/git/automation/testdata/data.csv')
            print df
            rows = []
            for row in df.iterrows():
                index, data = row
                rows.append(data.tolist())
            print rows
            return rows
        except:
            list_of_files = glob.glob('/Users/rmqa/Desktop/data/*')
            if(list_of_files==None):
                print "the data is empty"


    @staticmethod
    def take_screenshot_attachreport(self, name, scenario):

        try:
            random = str(uuid.uuid4())
            allure.attach(name+scenario+"_"+random, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except Exception as e:
            raise e


    @staticmethod
    def getCapabilityInfo(self):

        try:
            allure.attach('platform version', self.driver.desired_capabilities.get("platformVersion"), type=AttachmentType.TEXT)
            allure.attach('platformName', self.driver.desired_capabilities.get("platformName"), type=AttachmentType.TEXT)
            allure.attach('ManufacturerName', self.driver.desired_capabilities.get('deviceManufacturer'), type=AttachmentType.TEXT)
            print self.driver.desired_capabilities
        except Exception as e:
            raise e


    @staticmethod
    def checkAutoredirect(self, placementtype):

        try:
            allure.attach('BeforeCheck_Activity', self.driver.current_activity, type= AttachmentType.TEXT)

            if(placementtype == 'fullscreen'):
                if('com.inmobi.rendering.InMobiAdActivity' == self.driver.current_activity):
                    allure.attach('Interstitial_CurrentActivity', self.driver.current_activity, type=AttachmentType.TEXT)
            else:
                if ('com.inmobi.app.kitchensink.network.NetworkAdsActivity'  == self.driver.current_activity):
                    allure.attach('Banner_CurrentActivity', self.driver.current_activity, type=AttachmentType.TEXT)
            time.sleep(10)
            if ('com.inmobi.rendering.InMobiAdActivity' == self.driver.current_activity) or (
                    'com.inmobi.app.kitchensink.network.NetworkAdsActivity' == self.driver.current_activity):
                testcasehelpers.check_element_clickable_click(self, 20, By.CLASS_NAME, "android.webkit.WebView")
                allure.attach('Ad_click_CurrentActivity', self.driver.current_activity, type=AttachmentType.TEXT)
            elif ('org.chromium.chrome.browser.ChromeTabbedActivity' == self.driver.current_activity):
                allure.attach('Ad_not_clicked_Activity', self.driver.current_activity, type=AttachmentType.TEXT)
            else:
                allure.attach('Normal_Interstitial_Clicking_on_the_ad', self.driver.current_activity,
                              type=AttachmentType.TEXT)
                testcasehelpers.check_element_clickable_click(self, 10, By.XPATH,
                                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View")
        except Exception as e:
            raise e


    @staticmethod
    def sdkclose(self):
        try:
            allure.attach('Before_Close_button_check', self.driver.current_activity, type=AttachmentType.TEXT)
            if (self.driver.findElement(By.xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View[1]'))!= 0):
                testcasehelpers.check_element_clickable_click(self, 5, By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View[1]')
                allure.attach('After_Close_button_check', self.driver.current_activity, type=AttachmentType.TEXT)
                if (self.driver.current_activity == 'com.inmobi.app.kitchensink.network.NetworkAdsActivity'):
                    allure.attach('Close_button_check', 'Sdk close button success!', type=AttachmentType.TEXT)
            else:
                allure.attach('SDK_Close_button_not_found', self.driver.current_activity, type=AttachmentType.TEXT)
        except Exception as e:
            raise e


    @staticmethod
    def sdkclosebuttontest(self, placementid, url, placementtype, size):
        package_name = 'com.inmobi.app.kitchensink10520170508'
        try:
            self.driver.start_activity(package_name,
                                       'com.inmobi.app.kitchensink.MainActivity')
            testcasehelpers.check_element_clickable_click(self, 2, By.CLASS_NAME, 'android.widget.LinearLayout')
            self.driver.find_element_by_id('{}:id/inputPlacementId'.format(package_name)).clear();
            self.driver.find_element_by_id('{}:id/inputPlacementId'.format(package_name)).send_keys(placementid);
            self.driver.back()
            self.driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Done\"))").click()
            testcasehelpers.check_element_clickable_click(self, 2, By.ID,
                                                          '{}:id/btnMonetization'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 2, By.ID,
                                                          '{}:id/btnAdNetwork'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 2, By.ID,
                                                          '{}:id/btnSettings'.format(package_name))
            if (self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).text != RC_URL):
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).clear();
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).send_keys('')
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).send_keys(RC_URL)
            self.driver.back()
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("{}:id/spinnerPlacementType")'.format(package_name)).click()
            self.driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector()).scrollIntoView(text(\"{0}\"))".format(placementtype)).click()
            if (placementtype == 'inline'):
                testcasehelpers.check_element_clickable_click(self, 4, By.ID,
                                                              '{}:id/spinnerInlinePlacementSize'.format(package_name))
                self.driver.find_element_by_android_uiautomator(
                    "new UiScrollable(new UiSelector()).scrollIntoView(text(\"{}\"))".format(size)).click()
            self.driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Done\"))").click()
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                          '{}:id/btnReload'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                          '{}:id/btnBack'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                          '{}:id/btnAdNetwork'.format(package_name))
            print 'clicking on the button'
            if (placementtype == 'fullscreen'):
                time.sleep(10)
                self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().resourceId("{}:id/btnShowIntAd")'.format(package_name)).click()
            testcasehelpers.take_screenshot_attachreport(self, 'Adloads', 'renders')
            time.sleep(2)
            testcasehelpers.take_screenshot_attachreport(self, 'AdInterval-1', 'renders')
            time.sleep(2)
            testcasehelpers.take_screenshot_attachreport(self, 'AdInterval-2', 'renders')
            time.sleep(2)
            if (placementtype == 'fullscreen'):
                testcasehelpers.sdkclose(self)
            else:
                allure.attach('Banner_Noclose', 'banner ad, no close button', type=AttachmentType.TEXT)
        except NoSuchElementException as e:
            raise e
            return False



    @staticmethod
    def sdk700(self, placementid, placementtype, size):

        # print placementtype, url, placementid, size

        package_name = 'com.inmobi.app.kitchensink10520170508'
        try:
            self.driver.start_activity(package_name,
                                           'com.inmobi.app.kitchensink.MainActivity')
            testcasehelpers.check_element_clickable_click(self, 2, By.CLASS_NAME, 'android.widget.LinearLayout')
            self.driver.find_element_by_id('{}:id/inputPlacementId'.format(package_name)).clear();
            self.driver.find_element_by_id('{}:id/inputPlacementId'.format(package_name)).send_keys(placementid);
            self.driver.back()
            self.driver.find_element_by_android_uiautomator(
                    "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Done\"))").click()
            testcasehelpers.check_element_clickable_click(self, 2, By.ID,
                                                              '{}:id/btnMonetization'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 2, By.ID,
                                                              '{}:id/btnAdNetwork'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 2, By.ID,
                                                              '{}:id/btnSettings'.format(package_name))
            if (self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).text != RC_URL):
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).clear();
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).send_keys('')
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).send_keys(RC_URL)
            self.driver.back()
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("{}:id/spinnerPlacementType")'.format(package_name)).click()
            self.driver.find_element_by_android_uiautomator(
                    "new UiScrollable(new UiSelector()).scrollIntoView(text(\"{0}\"))".format(placementtype)).click()
            if(placementtype == 'inline'):
                testcasehelpers.check_element_clickable_click(self, 4, By.ID,'{}:id/spinnerInlinePlacementSize'.format(package_name))
                self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"{}\"))".format(size)).click()
            self.driver.find_element_by_android_uiautomator(
                    "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Done\"))").click()
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                              '{}:id/btnReload'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                              '{}:id/btnBack'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                              '{}:id/btnAdNetwork'.format(package_name))
            print 'clicking on the button'
            if(placementtype == 'fullscreen'):
                time.sleep(10)
                self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().resourceId("{}:id/btnShowIntAd")'.format(package_name)).click()
            testcasehelpers.take_screenshot_attachreport(self, 'Adloads', 'renders')
            time.sleep(2)
            testcasehelpers.take_screenshot_attachreport(self, 'AdInterval-1', 'renders')
            time.sleep(2)
            testcasehelpers.take_screenshot_attachreport(self, 'AdInterval-2', 'renders')
            time.sleep(2)
            time.sleep(10)
            render = testcasehelpers.validate_render(self)
            print render
            self.assertTrue(render)
            print self.assertTrue(render)
            try:
                # assert self.assertTrue(render)
                allure.attach('render_fail_try', 'Ad not rendered', type=AttachmentType.TEXT)
            except AssertionError:
                allure.attach('render_fails', 'Ad not rendered' , type=AttachmentType.TEXT)
                raise
            if(render):
                testcasehelpers.checkAutoredirect(self, placementtype)
                time.sleep(10)
                testcasehelpers.take_screenshot_attachreport(self, 'exitlink', 'Onexit')
            allure.attach('Exitlink_Activity', self.driver.current_activity, type=AttachmentType.TEXT)
            testcasehelpers.getCapabilityInfo(self)
            return True
        except NoSuchElementException as e:
            raise e
            return False



    @staticmethod
    def sdk610(self, placementid, placementtype, size):
        package_name ='com.inmobi.app.kitchensink10420170208'
        try:
            self.driver.start_activity(package_name,
                                           'com.inmobi.app.kitchensink.MainActivity')
            testcasehelpers.check_element_clickable_click(self, 2, By.CLASS_NAME, 'android.widget.LinearLayout')
            self.driver.find_element_by_id('{}:id/inputPlacementId'.format(package_name)).clear();

            self.driver.find_element_by_id('{}:id/inputPlacementId'.format(package_name)).send_keys(placementid);
            self.driver.back()
            self.driver.find_element_by_android_uiautomator(
                    "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Done\"))").click()
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                              '{}:id/btnMonetization'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 2, By.ID,
                                                              '{}:id/btnAdNetwork'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 3, By.ID,
                                                              '{}:id/btnSettings'.format(package_name))
            if (self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).text != RC_URL):
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).clear()
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).send_keys('')
                self.driver.find_element_by_id('{}:id/editAdServer'.format(package_name)).send_keys(RC_URL)
            self.driver.back()
            self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("{}:id/spinnerPlacementType")'.format(package_name)).click()
            # self.driver.find_element_by_android_uiautomator(
            #         "new UiScrollable(new UiSelector()).scrollIntoView(text(\"inline\"))").click()
            # testcasehelpers.check_element_clickable_click(self, 3, By.ID,
            #                                                   '{}:id/spinnerInlinePlacementSize'.format(package_name))
            # self.driver.find_element_by_android_uiautomator(
            #     'new UiSelector().resourceId("{}:id/spinnerPlacementType")'.format(package_name)).click()
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\""+placementtype+"\"))").click()
            if (placementtype == 'inline'):
                testcasehelpers.check_element_clickable_click(self, 5, By.ID, '{}:id/spinnerInlinePlacementSize'.format(package_name))
                self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"{}\"))".format(size)).click()
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"Done\"))").click()
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                              '{}:id/btnReload'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                              '{}:id/btnBack'.format(package_name))
            testcasehelpers.check_element_clickable_click(self, 5, By.ID,
                                                              '{}:id/btnAdNetwork'.format(package_name))
            print 'clicking on the button'
            if (placementtype == 'fullscreen'):
                time.sleep(10)
                self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("{}:id/btnShowIntAd")'.format(package_name)).click()
            testcasehelpers.take_screenshot_attachreport(self, 'Adloads', 'render')
            time.sleep(2)
            testcasehelpers.take_screenshot_attachreport(self, 'AdInterval-1', 'render')
            time.sleep(2)
            testcasehelpers.take_screenshot_attachreport(self, 'AdInterval-2', 'render')
            time.sleep(2)
            render = testcasehelpers.validate_render(self)
            assert True in render
            self.assertTrue(render)
            print render
            if (render):
                testcasehelpers.checkAutoredirect(self, placementtype)
                time.sleep(10)
                testcasehelpers.take_screenshot_attachreport(self, 'ExitlinkPage', 'Onexit')
            allure.attach('ExitLink_Activity', self.driver.current_activity, type=AttachmentType.TEXT)
            testcasehelpers.getCapabilityInfo(self)
            return True
        except NoSuchElementException as e:
            raise e
            return False


    @staticmethod
    def validate_render(self):
        count = 0
        random = str(uuid.uuid4())
        file_name = 'creative_'+random+'.png'
        try:
            screenshots_dir = "/reports/screenshots/"
            filepath = os.getcwd()+screenshots_dir+file_name
            print filepath
            self.driver.get_screenshot_as_file(os.getcwd()+screenshots_dir+file_name)
            time.sleep(10)
            image_object = cv2.imread(filepath)
            image_object = image_object[:, :, ::-1]
            for i in range(0, int(image_object.shape[0] * 1 / 5)):
                for j in range(0, image_object.shape[1]):
                    if image_object[i][j][0] >= 118 and image_object[i][j][0] <= 123:
                        if image_object[i][j][1] >= 240 and image_object[i][j][1] <= 245:
                            if image_object[i][j][2] >= 0 and image_object[i][j][2] <= 5:
                                count = count + 1
            if count >= 16000:
                allure.attach('Unable_to_detect_creative', 'No creative', type=AttachmentType.TEXT)
                # self.log.self.log.info('Unable to detect creative')
                return False
            else:
                allure.attach('Detected_creative', 'Creative found', type=AttachmentType.TEXT)
                # self.log.self.log.info('Creative detected')
                return True
        except Exception, e:
            allure.attach('Unable_to_validate_render', 'cannot validate render', type=AttachmentType.TEXT)
            # self.log.error("unable to validate render: Exception" + e.message)


    @staticmethod
    def host_tags_to_keg(self, placementid, tags):
        try:
            styling = '<style> body {background-color: rgb(119,245,2) !important;} </style>'
            if (tags is not None):
                data = styling + str(tags)
                allure.attach('tags_is_not_null', data, type=AttachmentType.TEXT)
                base_url = 'http://rc-studio.inmobi.com/automation/studiokeg/api/host?'
                appid = placementid

                end_url = 'overwrite=true&addtrueview=false&env=studio.inmobi.com'

                rc_url = base_url + 'appid=%s' % appid + '&' + 'c=inmobi' + '&' + end_url

                print "RC_URL"
                print rc_url

                API_ENDPOINT = rc_url
                r = requests.post(url=API_ENDPOINT, data=data)
                allure.attach('scripts', data, type=AttachmentType.TEXT)
                return True
            else:
                allure.attach('tags_is_null', 'None', type=AttachmentType.TEXT)
                return False
        except Exception as err:
            allure.attach('Problem_reading_hosting_tags', 'Problem in reading and hosting the tags', type=AttachmentType.TEXT)


