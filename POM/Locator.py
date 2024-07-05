class Locator(object):
    """Clase que contiene los selectores de elementos de la interfaz de usuario.
       Esta clase almacena las rutas XPath y selectores CSS de varios elementos
       que se utilizan en la automatización de pruebas.
    """

    # Selectores de "https://www.saucedemo.com/"
    user_input = "//*[@id='user-name']"
    password_input = "//*[@id='password']"
    login_btn = "//*[@id='login-button']"

   # Selectores de "https://demo.seleniumeasy.com/"
    lt = "//*[@id='select-demo']"
    checkbox = "#isAgeSelected" 
    checkbox2 = "//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[2]/label/input"
    check_all = "//*[@id='check1']"

   # Selectores de "https://testpages.herokuapp.com/styled/file-upload-test.html"
    select_file = "#fileinput"
    submit_file = "body > div > div.centered > form > div:nth-child(4) > input"