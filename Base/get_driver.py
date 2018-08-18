from appium import webdriver


def get_driver():
    # server 启动参数
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '5.1',
                    'deviceName': '192.168.56.101:5555',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'appPackage': 'com.android.settings',
                    'appActivity': '.Settings'
                    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver