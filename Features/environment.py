# from selenium.webdriver.chrome import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Application.Application import Application


def browser_init(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\n Started Scenario', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\n Started Step', step.name)


def after_step(context, step):
    print('\n Finished Step', step.name)
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name='failed_screenshot',
                      attachment_type=AttachmentType.PNG)


def after_scenario(context, scenario):
    print('\n Finished Scenario', scenario.name)
    context.driver.quit()
