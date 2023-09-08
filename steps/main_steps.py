from behave import given
from selenium import webdriver
from tests.departure.steps import departure_steps
from BDDCommon.CommonFuncs import webcommon

@given('Open Browser')
def open_browser(context):
  webcommon.go_to(context=context)
