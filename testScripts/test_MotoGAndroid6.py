import time
from appium import webdriver
import pandas as pd
from proxysetup.pattern_mathing import beacon_check
# import requests
import signal
import subprocess
import unittest
import time
import HtmlTestRunner
import os
import allure
import pytest
import unittest
from utilities.helpers import testcasehelpers
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from ddt import ddt, data, file_data, unpack,idata
from allure.constants import AttachmentType
import glob

tc = testcasehelpers()

@pytest.mark.usefixtures("MotoGsetup")
@ddt
class TestCase2(unittest.TestCase):

    # @data(*tc.get_data())
    # @unpack
    # def test_sdk700_motog(self, ad_format, tags, platform, click_prepend, creative_name, email_id, feature_list, job_id, placementtype, pricing_model, size, test_matrix):
    #     get_time = time.localtime(time.time())
    #     time_now = "{0}_{1}_{2}_{3}_{4}_{5}".format(get_time.tm_mday,get_time.tm_mon,
    #                                                 get_time.tm_year,get_time.tm_hour,get_time.tm_min,get_time.tm_sec)
    #     file_name = "test_sdk700_motog_{0}.log".format(time_now)
    #     project_path= os.getcwd()
    #     print(project_path)
    #     p = subprocess.Popen("mitmdump --insecure -p 8080 -s  '{0}/proxysetup/mitm_script.py' >"
    #                                " '{0}/proxysetup/logs/{1}'".format(project_path, file_name), shell=True, preexec_fn=os.setsid )
    #     # testcasehelpers.add_styling_render_check(self, tags)
    #     # data = tags
    #     # base_url = 'http://rc-studio.inmobi.com/automation/studiokeg/api/host?'
    #     # appid = placementid
    #     # end_url = 'overwrite=true&addtrueview=false&env=studio.inmobi.com'
    #     # rc_url = base_url + 'appid=%s' % appid + '&' + 'c=pso' + '&' + end_url
    #     # API_ENDPOINT = rc_url
    #     # r = requests.post(url=API_ENDPOINT, data=data)
    #     # allure.attach('scripts', tags, type=AttachmentType.TEXT)
    #     testcasehelpers.host_tags_to_keg(self, 101, tags)
    #     tc.sdk700(self, 101,  placementtype, size)
    #     time.sleep(10)
    #     list_of_files = glob.glob('/Users/rmqa/Desktop/git/automation/proxysetup/logs/*')  # * means all if need specific format then *.csv
    #     latest_file = max(list_of_files, key=os.path.getctime)
    #     print latest_file
    #     filepath = project_path +'/proxysetup/logs/'+ latest_file
    #     # matched_list = beacon_check('{0}/proxysetup/logs/{1}'.format(filepath, file_name))
    #     matched_list = beacon_check(latest_file)
    #     if len(matched_list) == 0:
    #         print("No match found")
    #         allure.attach('ClickURL-NotTracked', 'match not found', type=AttachmentType.TEXT)
    #     else:
    #         print("Match found")
    #         for match in matched_list:
    #             print(match+ '\n')
    #             allure.attach('ClickURL-Tracked', match, type=AttachmentType.TEXT)
    #     os.killpg(os.getpgid(p.pid), signal.SIGTERM)


    @data(*tc.get_data())
    @unpack
    def test_sdk610_motog(self, ad_format, tags, platform, click_prepend, creative_name, email_id, feature_list, job_id, placementtype, pricing_model, size, test_matrix):
        testcasehelpers.host_tags_to_keg(self, 101, tags)
        testcasehelpers.sdk700(self, 101, placementtype, size)
        allure.attach('Job_Id', job_id, type=AttachmentType.TEXT)
        # testcasehelpers.callApiUpdate(self)
    #

    # @data(*tc.get_data())
    # @unpack
    # def test_sdk610_motog_closebutton(self, ad_format, tags, platform, click_prepend, creative_name, email_id, feature_list, job_id, placementtype, pricing_model, size, test_matrix):
    #     testcasehelpers.host_tags_to_keg(self, 101, tags)
    #     testcasehelpers.sdkclosebuttontest(self, 101, placementtype, size)


if __name__ == '__main__':
    unittest.main()
