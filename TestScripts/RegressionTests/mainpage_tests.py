""" This module contains the all test cases."""
import logging
import unittest
import pytest
import allure
import sys
import string
import random
import FrameworkUtilities.logger_utility as log_utils
from PageObjects.MainPage.main_page import Mainpage
from FrameworkUtilities.execution_status_utility import ExecutionStatus
from FrameworkUtilities.data_reader_utility import DataReader
from FrameworkUtilities.config_utility import ConfigUtility


@allure.story('[Conversation] - Automate  the  Signin  screen across all three apps')
@allure.feature('Web App SigninPage Tests')
@pytest.mark.usefixtures("get_driver")
class MainTest(unittest.TestCase):
    """
    This class contains the executable test cases.
    """

    data_reader = DataReader()
    config = ConfigUtility()
    log = log_utils.custom_logger(logging.INFO)

    def setUp(self):
        self.mainpage = Mainpage(self.driver)
        self.exe_status = ExecutionStatus(self.driver)
        self.prop = self.config.load_properties_file()

    # def tearDown(self):
    #     self.login_page.logout_from_app()

    def string_generator(self, string_size=8, chars=string.ascii_uppercase + string.digits):
        """
        This function is used to generate random string
        :return: it returns random string
        """
        return ''.join(random.choice(chars) for _ in range(string_size))

    @pytest.fixture(autouse=True)
    def class_level_setup(self, request):
        """
        This method is used for one time setup of test execution process.
        :return: it returns nothing
        """

        if self.data_reader.get_data(request.function.__name__, "Runmode") != "Y":
            pytest.skip("Excluded from current execution run.")

    @allure.testcase("Validate  startscan btn Test")
    def test_validate_start_scan_buttons(self):
        """
        This test is used to verify the start scan button availability. (positive scenario)
        :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step("Validate  startscan btn Test successful"):
            result = self.mainpage.verify_start_scan_button()
            self.exe_status.mark_final(test_step="Validate  startscan btnSuccessful", result=result)

    @allure.testcase("Validate  stopscan btn Test")
    def test_validate_stop_scan_buttons(self):
        """
        This test is is used to verify the stop scan button availability. (positive scenario)
        :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step("Validate  stopscan btn Successful"):
            result = self.mainpage.verify_stop_scan_button()
            self.exe_status.mark_final(test_step="Validate  stopscan btn Successful", result=result)

    def test_validate_vertical_scroll_find_element(self):
        """
        This method is used to verify  scrolling the page vertically (positive scenario)
        :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step("Validate vertical scroll and find element  Successful"):
            result = self.mainpage.verify_medical_screen_elements()
            self.exe_status.mark_final(test_step="Validate vertical scroll and find find element Successful", result=result)

    def test_validate_connecting_medical_device_to_app(self):
        """
        This method is used to verify  connecting of medical device with app (positive scenario)
        :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step("Validate connecting  medical device with app  Successful"):
            result = self.mainpage.verify_medicaldevice_pairing()
            self.exe_status.mark_final(test_step="connecting  medical device with app", result=result)

    def test_validate_retrieve_all_buttons(self):
        """
       This method is used to verify  pressing on all retrieve buttons (positive scenario)
        :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step("Validate pressing on all retrive buttons is Successful"):
            result = self.mainpage.verify_retrieve_all_buttons()
            self.exe_status.mark_final(test_step="pressing on all retrieve buttons", result=result)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
