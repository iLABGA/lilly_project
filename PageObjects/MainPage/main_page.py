"""This module is used for login page objects."""

import logging
from SupportLibraries.base_helpers import BaseHelpers
from FrameworkUtilities.logger_utility import custom_logger
from FrameworkUtilities.config_utility import ConfigUtility
import time

class Mainpage(BaseHelpers):
    """This class defines the method and element identifications for Main page."""

    config = ConfigUtility()
    log = custom_logger(logging.INFO)

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver
    #     self.mp = MainPage
    #     self.prop = self.config.load_properties_file()
    #
    # welcome_page_login_link = "//android.widget.TextView[contains(@text, 'Login')]"
    # email = "//android.widget.TextView[contains(@text,'Email')]//following::android.widget.EditText[1]"
    # password = "//android.widget.TextView[contains(@text,'Password')]//following::android.widget.EditText[1]"
    # login_button = "//android.widget.TextView[contains(@text, 'Log in')]"
    # logout_button = "//android.widget.TextView[contains(@text, 'Logout')]"
    # logout_scroll_view_class = "android.widget.ScrollView"
    # logout_text_class = "android.widget.TextView"
    # logout_text = "Logout"
    #
    number_firstpage = "//android.widget.TextView[@text='NUM 1']"
    number_secondpage = "//android.widget.TextView[@text='NUM 2']"
    start_scan_button = "//android.widget.Button[@text='START SCAN']"
    stop_scan_button = "//android.widget.Button[@text='STOP SCAN']"
    init_with_mac = "//android.widget.Button[@text='INIT WITH MAC']"
    disconnect_button = "//android.widget.Button[@text='DISCONNECT']"
    connect_button = "//android.widget.Button[@text='CONNECT']"
    connected = "//android.widget.TextView[@text='Connected']"
    disconnected = "//android.widget.TextView[@text='Disconnected']"
    start_observing_button = "//android.widget.Button[@text='START OBSERVING']"
    stop_observing_button = "//android.widget.Button[@text='STOP OBSERVING']"
    test_cache = "//android.widget.Button[@text='TEST CACHE']"
    clear_cache = "//android.widget.Button[@text='CLEAR CACHE']"
    scanning = "//android.widget.TextView[@text='Scanning']"
    bond_status1 = "//android.widget.TextView[@text='Bond Status: Not bonded']"
    bond_status2 = "//android.widget.TextView[@text='Bond Status: Bonded']"
    connection_status1 = "//android.widget.TextView=[@text='Connection Status: RxBleConnectionState{CONNECTING}']"
    connection_status2 = "//android.widget.TextView=[@text='Connection Status: RxBleConnectionState{DISCONNECTED}']"
    scroll_grey_screen = "//android.widget.ScrollView=[@text='']"
    pairing_request_ok = "//android.widget.Button=[@text='OK']"
    show_device_info = "//android.widget.Button=[@text='SHOW DEVICE INFO']"
    # retrieve buttons
    retrieve_new = "//android.widget.Button[@text='RETRIEVE NEW']"
    retrieve_all = "//android.widget.Button[@text='RETRIEVE ALL']"
    retrieve_oldest = "//android.widget.Button[@text='RETRIEVE OLDEST']"
    retrieve_newest = "//android.widget.Button[@text='RETRIEVE NEWEST']"
    retrieve_sequence_num = "//android.widget.Button[@text='RETRIEVE SEQ. #']"
    retrieve_from_sequence_num = "//android.widget.Button[@text='RETRIEVE FROM SEQ. #']"
    # state buttons
    save_state = "//android.widget.Button=[@text='SAVE STATE']"
    restore_state = "//android.widget.Button=[@text='RESTORE STATE']"
    # GET buttons
    get_features = "//android.widget.Button=[@text='GET FEATURES']"
    get_current_time = "//android.widget.Button=[@text='GET CURRENT TIME']"
    get_battery_level = "//android.widget.Button=[@text='GET BATTERY LEVEL']"
    get_local_timeinfo = "//android.widget.Button=[@text='GET LOCAL TIME INFO']"
    get_refresh_timeinfo = "//android.widget.Button=[@text='GET REF TIME INFO']"
    get_model_number = "//android.widget.Button=[@text='GET MODEL #']"
    get_manufacture_name = "//android.widget.Button=[@text='GET MAN. NAME']"
    get_serial_number = "//android.widget.Button=[@text='GET SERIAL #']"
    get_hw_rev = "//android.widget.Button=[@text='GET HW REV']"
    get_fw_rev = "//android.widget.Button=[@text='GET FW REV']"
    get_sw_rev = "//android.widget.Button=[@text='GET SW REV']"
    get_sys_id = "//android.widget.Button=[@text='GET SYS ID']"
    get_pnp_id = "//android.widget.Button=[@text='GET PNP ID']"
    get_Fw_Rev_class = "android.widget.Button"
    get_Fw_Rev_Text = "GET FW REV"
    scroll_view_class = "android.widget.ScrollView"
    stpo_scan = "STOP SCAN"
    # medical device info
    medical_device_info_1 = "//android.widget.TextView[@text='Contour7830H6086398 (54:6C:0E:CB:D5:E1)']"  # Contour
    medical_device_info_2 = "//android.widget.TextView[@text='meter+06647277 (10:CE:A9:3B:D7:57)']"  # Accu-Chek Guide


    def verify_start_scan_button(self):
        """
        This method is used to verify the start scan button availabilty.
        :return: this method returns boolean value for element present start scan button
        """
        self.mouse_click_action_on_element_present(self.number_secondpage)
        result = self.is_element_present(self.start_scan_button, max_time_out=30)

        if not result:
            self.log.error("Unable to find start scan button")

        return result

    def verify_stop_scan_button(self):
        """
        This method is used to verify the stop scan button availabilty.
        :return: this method returns boolean value for element present stop scan button
        """

        result = self.is_element_present(self.stop_scan_button)

        if not result:
            self.log.error("Unable to find stop scan button.")

        return result
    def verify_medical_screen_elements(self):
        """
        This method is used to verify  scrolling the page vertically.
        :return: this method returns boolean value for element present and scrolling successful
        """
        self.vertical_scroll(self.scroll_view_class, self.get_Fw_Rev_class, self.get_Fw_Rev_Text)
        self.vertical_scroll(self.scroll_view_class, self.get_Fw_Rev_class, self.stpo_scan)
        self.wait_for_sync()
        result = self.is_element_present(self.stop_scan_button)

        if not result:
            self.log.error("Unable to scroll  application.")

        return result

    def verify_medicaldevice_pairing(self):
        """
        This method is used to verify  connecting of medical device with app (positive scenario)
        :return: return test status
        """
        self.mouse_click_action_on_element_present(self.number_firstpage)
        self.mouse_click_action_on_element_present(self.start_scan_button)
        self.mouse_click_action_on_element_present(self.stop_scan_button)
        self.mouse_click_action_on_element_present(self.medical_device_info_2)
        self.mouse_click_action_on_element_present(self.connect_button)
        self.wait_for_sync()
        self.wait_for_sync()
        self.wait_for_sync()
        result = self.is_element_present(self.retrieve_all)

        if not result:
            self.log.error("Unable to connect medical device.")

        return result

    def verify_retrieve_all_buttons(self):
        """
        This method is used to verify  pressing on all retrieve buttons (positive scenario)
        :return: return test status
        """
        self.wait_for_sync()
        self.wait_for_sync()
        self.mouse_click_action_on_element_present(self.retrieve_all)
        self.device_back_button_click()
        self.wait_for_sync()
        self.mouse_click_action_on_element_present(self.retrieve_oldest)
        self.device_back_button_click()
        self.wait_for_sync()
        self.mouse_click_action_on_element_present(self.retrieve_newest)
        self.device_back_button_click()
        self.wait_for_sync()
        self.mouse_click_action_on_element_present(self.retrieve_new)
        self.wait_for_sync()
        self.device_back_button_click()
        self.wait_for_sync()
        self.mouse_click_action_on_element_present(self.retrieve_sequence_num)
        self.wait_for_sync()
        self.device_back_button_click()
        self.wait_for_sync()
        self.mouse_click_action_on_element_present(self.retrieve_from_sequence_num)
        self.wait_for_sync()
        self.device_back_button_click()
        result = self.is_element_present(self.retrieve_from_sequence_num)

        if not result:
            self.log.error("Unable to press all the retrieve buttons.")

        return result

