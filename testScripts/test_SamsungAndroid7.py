import requests
import allure
import pytest
import unittest
import random
from selenium.webdriver.common.by import By
from utilities.helpers import testcasehelpers
from selenium.common.exceptions import NoSuchElementException
from ddt import ddt, data, file_data, unpack, idata
from allure.constants import AttachmentType



tc = testcasehelpers()


@pytest.mark.usefixtures("Samsungsetup")
@ddt
class TestCase1(unittest.TestCase):

    @data(*tc.get_data())
    @unpack
    def test_sdk700_samsung(self, ad_format, tags, platform, click_prepend, creative_name, email_id, feature_list, job_id, placementtype, pricing_model, size, test_matrix):
        testcasehelpers.host_tags_to_keg(self, 102, tags)
        tc.sdk700(self, 102, placementtype, size)
        allure.attach('Job_Id', job_id, type=AttachmentType.TEXT)
        # testcasehelpers.callApiUpdate(self)


    # @data(*tc.get_data())
    # @unpack
    # def test_sdk610_samsung(self, ad_format, tags, platform, click_prepend, creative_name, email_id, feature_list, job_id, placementtype, pricing_model, size, test_matrix):
    #     testcasehelpers.host_tags_to_keg(self, 102, tags)
    #     tc.sdk610(self,  102, placementtype, size)
    #     allure.attach('Job_Id', job_id, type=AttachmentType.TEXT)

    #
    # @data(*tc.get_data())
    # @unpack
    # def test_sdk700_samsung_closebutton(self, ad_format, tags, platform, click_prepend, creative_name, email_id, feature_list, job_id, placementtype, pricing_model, size, test_matrix):
    #     testcasehelpers.host_tags_to_keg(self, 101, tags)
    #     tc.sdkclosebuttontest(self, 101, placementtype, size)


if __name__ == '__main__':
    unittest.main()
