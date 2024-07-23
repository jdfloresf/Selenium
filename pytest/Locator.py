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
    search_products = "//*[@id='search-products']"

    add_new = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    product_info = "//*[@id='product-info']/div[1]/div[2]/button/i"
    product_name2 = "//*[@id='Name']"
    sku = "//*[@id='Sku']"
    prices = "//*[@id='product-price']/div[1]/div[2]/button/i"
    price = "//*[@id='Price']"
    inventory = "//*[@id='ManageInventoryMethodId']"
    save_button = "//*[@id='product-form']/div[1]/div/button[1]"

    picture = "#products-grid_wrapper > div:nth-child(1) > div > div > div.dataTables_scrollHead > div > table > thead > tr > th:nth-child(2)"
    edit_button = "#products-grid > tbody > tr > td.button-column > a"
    upload =  "(//input[contains(@name,'qqfile')])[1]"
    label = "//*[@id='tab-pictures']/div/div[4]/div[2]/div/div[1]/div/label"

    costumers = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    costumers_form = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    search_first_name = "//*[@id='SearchFirstName']"
    search_costumers = "//*[@id='search-customers']"
    add_costumer = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    email_costumer = "//*[@id='Email']"
    password_costumer = '//*[@id="Password"]'
    first_name = '//*[@id="FirstName"]'
    last_name = '//*[@id="LastName"]'
    gender_male = '//*[@id="Gender_Male"]'
    gender_female = '//*[@id="Gender_Male"]'
    date_birth = '//*[@id="DateOfBirth"]'
    roles = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input'
    company = '//*[@id="Company"]'
    save_costumer = '/html/body/div[3]/div[1]/form/div[1]/div/button[1]/i'
    email_register_error = '/html/body/div[3]/div[1]/form/div[2]/ul/li/text()'