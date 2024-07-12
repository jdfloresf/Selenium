class Locator(object):
    email = "//*[@id='Email']"
    password = "//*[@id='Password']"
    submit = "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    dashboard = "/html/body/div[3]/div[1]/div[2]/h1"

    error = "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[1]/ul/li"
    enter_email = "//*[@id='Email-error']"
    enter_pass = "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[1]/ul/li"
    no_account = "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[1]/ul/li"
    incorrect_credentials = "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[1]/ul/li"