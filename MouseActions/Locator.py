class Locator(object):

    # Selectores de https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    submit = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    # Despues de ingresar las credenciales
    admin = "#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a"
    job = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
    categories = "Job Categories"
    
    # Selectores de https://demoqa.com/buttons
    double_click = "//*[@id='doubleClickBtn']"
    right_click = "//*[@id='rightClickBtn']"

    # Selectores de https://demo.seleniumeasy.com/drag-and-drop-demo.html
    drop1 = "//*[@id='todrag']/span[1]"
    drop2 = "//*[@id='todrag']/span[2]"
    drop3 = "//*[@id='todrag']/span[3]"
    drop_zone = "//*[@id='mydropzone']"

    # Selectores de https://testpages.herokuapp.com/styled/drag-drop-javascript.html
    dr = "//*[@id='draggable1']"
    pz = "//*[@id='droppable1']"

    # Selectores de https://jqueryui.com/draggable/
    drag = "//*[@id='draggable']"
    
    # Selectores de https://demoqa.com/automation-practice-form
    first_name = "//*[@id='firstName']"
    last_name = "//*[@id='lastName']"

    
