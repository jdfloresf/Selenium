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

    catalog = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a"
    products = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a"
    product_name1 = "//*[@id='SearchProductName']"
    search = "//*[@id='search-products']"

    add_new = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    product_name2 = "//*[@id='Name']"
    sku = "//*[@id='Sku']"
    price = "//*[@id='Price']"
    inventory = "//*[@id='ManageInventoryMethodId']"
    save_button = "//*[@id='product-form']/div[1]/div/button[1]"

    picture = "#products-grid_wrapper > div:nth-child(1) > div > div > div.dataTables_scrollHead > div > table > thead > tr > th:nth-child(2)"
    edit_button = "#products-grid > tbody > tr > td.button-column > a"
    upload =  "input[type='file'][id^='picture']"
    label = "//*[@id='tab-pictures']/div/div[4]/div[2]/div/div[1]/div/label"