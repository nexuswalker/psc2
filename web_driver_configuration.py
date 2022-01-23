from selenium import webdriver


def installFirefoxDriver():
    # Browser services imports
    from selenium.webdriver.firefox.service import Service as FirefoxService

    # Installing browser driver
    from webdriver_manager.firefox import GeckoDriverManager
    service = FirefoxService(GeckoDriverManager().install())

    return service


def installChromeDriver():
    # Browser services imports
    from selenium.webdriver.chrome.service import Service as ChromeService

    # Installing browser drivers
    from webdriver_manager.chrome import ChromeDriverManager
    service = ChromeService(ChromeDriverManager().install())

    return service


def define_driver(url, browser):
    # Override the variable browser to use firefox by regardless of the input
    #browser = "firefox"
    # Defining browser
    if browser == "firefox":
        # Install and define the driver
        driver = webdriver.Firefox(service=installFirefoxDriver())
    elif browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        driver = webdriver.Chrome(service=installChromeDriver())
    else:
        print("Invalid browser name, please use the words firefox or chrome as arguments")
        input("press any key to exit")

    # Maximize window
    driver.maximize_window()

    # Going to webpage
    driver.get(url)

    return driver
