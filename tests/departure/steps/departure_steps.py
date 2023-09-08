import time
from behave import then, when, given
from BDDCommon.CommonFuncs import webcommon
import logging as logger
from selenium.webdriver.common.action_chains import ActionChains

@then("Click on edit icon")
def click_on_edit_icon(context):
  
  button = webcommon.find_element(context, 'class name', "board-departure")
  webcommon.set_load(context, 50)
  button.click()
  pass

@then("the modal departure should be appear")
def on_modal_appear(context):

  webcommon.set_load(context, 30)
  modalDepartureCheck = webcommon.find_elements(context, 'xpath', '/html/body/div/div/div/div/div[3]/div')
  if (len(modalDepartureCheck) > 0) :
    modalDeparture = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div/div[3]/div')
    assert modalDeparture.is_displayed(), 'Modal not displayed'
  else :
    raise Exception('Modal not showing')

@then("Input Soekarno Hatta on departure input field")
def on_input_field(context):
    
    input_element = webcommon.find_element(context, 'class name', 'Form_formControl__j2pFZ')
    input_element.send_keys("Soekarno Hatta")
    time.sleep(2)
    pass

@then("Click Soekarno Hatta departure")
def click_on_departure(context):
    css_selector = ".th-list:first-child"

    try:
        element_to_click = webcommon.find_element(context, 'css selector', css_selector)
        element_to_click.click()
    except Exception as e:
        print(f"Failed click elemen {e}")

@then("Input Ngurah on arrival input field")
def on_input_field(context):
    input_element = webcommon.find_element(context, 'class name', 'Form_formControl__j2pFZ')
    input_element.clear()
    input_element.send_keys("Ngurah")
    time.sleep(2)
    pass

@then("Click Ngurah arrival")
def click_on_departure(context):
    css_selector = ".th-list:first-child"

    try:
        element_to_click = webcommon.find_element(context, 'css selector', css_selector)
        element_to_click.click()
    except Exception as e:
        print(f"Failed click elemen {e}")

@then("Click the pencil icon in the upper right corner next to passenger to add passengers")
def click_on_pencil_icon(context):

  button = webcommon.find_element(context, 'class name', "board-passenger")
  button.click()
  pass

@then("Choose the cabin class")
def choose_cabin_class_and_passengers(context):
    css_selector = "div.badge-jejakin:nth-child(2)"

    element_to_click = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div')
    webcommon.set_load(context, 50)
    element_to_click.click()

@then("Choose the number of passengers")
def choose_cabin_class_and_passengers(context):
    css_selector = "div.badge-jejakin:nth-child(5)"

    element_to_click = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[2]/div')
    time.sleep(2)
    element_to_click.click()

@then("Click save button passenger")
def click_save_button(context):
  
  button = webcommon.find_element(context, 'class name', "Button_btn___hqnz")
  webcommon.set_load(context, 10)
  ActionChains(context.driver).move_to_element(button).click(button).perform()
  pass

@then("Click the pencil icon in the upper right corner next to travel purpose to add travel purpose")
def click_on_pencil_icon(context):

  button = webcommon.find_element(context, 'class name', "board-purpose")
  button.click()
  time.sleep(2)
  pass

@then("Choose the travel purpose")
def choose_travel_purpose(context):
    css_selector = "div.btp-list:nth-child(2)"

    element_to_click = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]')
    time.sleep(2)
    element_to_click.click()

@then("Click the Take Action button")
def click_action_button(context):
 
  buttons = webcommon.find_element(context, 'class name', "Button_btn___hqnz")
  webcommon.set_load(context, 30)
  time.sleep(4)
  buttons.click()
  pass

@then("Choose one of the programs to participate in")
def choose_programs(context):
    css_selector = "div.Payment_contribute__Siat2:nth-child(3)"

    element_to_click = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div[3]')
    element_to_click.click()

@then("Click the pencil button")
def click_edit_icon(context):
  
  button = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div')
  ActionChains(context.driver).move_to_element(button).click(button).perform()
  pass

@then("Input amount to contribute")
def on_input_field(context):
    
    input_element = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[1]/div/div[2]/input')
    input_element.clear()
    input_element.send_keys("200000")
    pass

@then("Click save button")
def click_save_button(context):
  
  button = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[1]/div/div[2]/button')
  ActionChains(context.driver).move_to_element(button).click(button).perform()
  pass

@then("Input name on fullname input")
def on_input_field(context):
    
    input_element = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[2]/div[2]/div[1]/div[3]/input[1]')
    input_element.send_keys("Haikal")
    pass

@then("Input email on email input")
def on_input_field(context):
    
    input_element = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[2]/div[2]/div[1]/div[3]/input[2]')
    input_element.send_keys("haikal@gmail.com")
    pass

@then("Click select payment method")
def click_save_button(context):
  
  button = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[2]/div[2]/div[1]/div[4]')
  webcommon.set_load(context, 10)
  ActionChains(context.driver).move_to_element(button).click(button).perform()
  pass

@then("Choose one payment method")
def choose_payment(context):
  
  button = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[1]/div/div[2]/div[3]')
  ActionChains(context.driver).move_to_element(button).click(button).perform()
  pass

@then("Click I agree with the Terms & Conditions")
def click_agree(context):

  button = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[2]/div[2]/div[1]/div[5]/span[1]')
  ActionChains(context.driver).move_to_element(button).click(button).perform()
  pass

@then("Click pay and offset")
def click_pay_offset(context):
  
  button = webcommon.find_element(context, 'xpath', '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
  webcommon.set_load(context, 10)
  ActionChains(context.driver).move_to_element(button).click(button).perform()
  pass