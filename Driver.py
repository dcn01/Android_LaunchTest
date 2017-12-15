# coding:utf-8
"""
Created on 17/12/14
@author: xinxi
测试点：
"""
from appium import webdriver
import os

class DesiredOptions:
    DefaultAppCaps = {
        'deviceName': 'dde96254',
        'platformName': 'Android',
        'platformVersion': '7.0',
        'appPackage': 'com.wuba',
        'appActivity': 'com.wuba.activity.launch.LaunchActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset ':False,
        'fullres':True

    }

    DefaultAppiumServer = 'http://127.0.0.1:4723/wd/hub'

class AppiumWebDriver:
    @staticmethod
    def new(server=None, caps=None, **kw):
        if not server:
            server = DesiredOptions.DefaultAppiumServer
        if not caps or not isinstance(caps, dict):
            caps = DesiredOptions.DefaultAppCaps
        caps.update(kw)
        #os.system("adb shell pm clear com.wuba")
        return webdriver.Remote(command_executor=server, desired_capabilities=caps)