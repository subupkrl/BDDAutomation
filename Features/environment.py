from selenium import webdriver
from selenium.webdriver import Chrome

def before_scenario(context, scenario):
    # Install and set up the Chrome driver automatically
    context.driver = Chrome()
    context.driver.get("https://www.facebook.com/r.php")
    context.driver.implicitly_wait(10) # Optional: set a wait time

def after_scenario(context, scenario):
    # Close the browser after the scenario runs
    context.driver.close()
