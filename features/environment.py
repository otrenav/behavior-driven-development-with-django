from selenium import webdriver

def before_all(context):
    # PhantomJS is used (headless browser)
    # For debugging, you can use the Firefox driver
    context.browser = webdriver.PhantomJS()
    # context.browser = webdriver.Firefox()

    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'

def after_all(context):
    # Explicitly quit the browser, otherwise it
    # won't know that we have finished
    context.browser.quit()

def before_feature(context, feature):
    # Code to be executed each time
    # a feature is gonig to be tested
    pass
