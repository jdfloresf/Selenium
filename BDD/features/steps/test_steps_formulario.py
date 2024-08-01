from behave import *
from selenium import webdriver

from POM.Functions import Functions
from Locators import Locator

@given(u'Abriendo navegador')
def step_impl(context):
    global driver, f, t
    t = 0.1
    context.driver = webdriver.Edge()
    f = Functions(context.driver)
    f.navigate("https://demoqa.com/text-box", t)

@when(u'Cargando nombre de "{user}"')
def step_impl(context, user):
    print(u'STEP: When Cargando nombre del usuario')
    f.validate_and_send_keys("xpath", Locator.name, user, t)


@then(u'Cargando "{email}"')
def step_impl(context, email):
    print(u'STEP: Then Cargando email')
    f.validate_and_send_keys("xpath", Locator.email, email, t)


@then(u'Cargando direccion "{dir1}"')
def step_impl(context, dir1):
    print(u'STEP: Then Cargando direccion 1')
    f.validate_and_send_keys("xpath", Locator.curren_address, dir1, t)


@then(u'Cargando nueva "{dir2}"')
def step_impl(context, dir2):
    print(u'STEP: Then Cargando nueva "Qumichin12"')
    f.validate_and_send_keys("xpath", Locator.permanent_address, dir2, t)


@then(u'Subiendo informacion')
def step_impl(context):
    print(u'STEP: Then Subiendo informacion')
    f.click("xpath", Locator.submit, t)


@then(u'Cerrando sesion')
def step_impl(context):
    print(u'STEP: Then Cerrando sesion')