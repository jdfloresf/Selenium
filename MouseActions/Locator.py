class Locator(object):
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    submit = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    # Despues de ingresar las credenciales
    admin = "#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a"
    job = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
    categories = "Job Categories"

    