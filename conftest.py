from appium import webdriver
import pytest



@pytest.fixture(scope="class")
def Samsungsetup(request):

    # subprocess.Popen('appium', shell=False)
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'Motorolo one power'
    desired_caps['appPackage'] = 'com.inmobi.app.kitchensink10520170508'
    desired_caps['appActivity'] = 'com.inmobi.app.kitchensink.MainActivity'
    desired_caps['udid'] = "ZF622466FM"
    desired_caps['automationName'] = "UiAutomator2"
    desired_caps['autoDismissAlerts'] = True

    driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

    driver.implicitly_wait(10)

    print 'starting appium server'

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.close_app()



@pytest.fixture(scope="class")
def MotoGsetup(request):

    # subprocess.Popen('appium', shell=False)

    # desired_caps = {}
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '8.1.0'
    # desired_caps['deviceName'] = 'Redmi'
    # desired_caps['appPackage'] = 'com.inmobi.app.kitchensink10420170208'
    # desired_caps['appActivity'] = 'com.inmobi.app.kitchensink.MainActivity'
    # desired_caps['udid']="4c16c4f6"
    # desired_caps['autoDismissAlerts'] = True

    desired_caps1 = {}
    desired_caps1['platformName'] = 'Android'
    desired_caps1['platformVersion'] = '7.0'
    desired_caps1['deviceName'] = 'LG G6'
    desired_caps1['appPackage'] = 'com.inmobi.app.kitchensink10520170508'
    desired_caps1['appActivity'] = 'com.inmobi.app.kitchensink.MainActivity'
    desired_caps1['udid'] = "LGH870DS82337983"
    desired_caps1['automationName'] = "UiAutomator2"
    desired_caps1['autoDismissAlerts'] = True

    dd = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps1)

    dd.implicitly_wait(10)


    print 'starting appium server'

    if request.cls is not None:
        request.cls.driver = dd

    yield dd

    dd.close_app()
