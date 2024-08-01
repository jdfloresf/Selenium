# Curso de Selenium
![selenium](https://upload.wikimedia.org/wikipedia/commons/9/9f/Selenium_logo.svg)

Durante el curso de Selenium con Python, adquirí conocimientos fundamentales para la automatización de pruebas en aplicaciones web. Aprendí que Selenium es una herramienta poderosa para automatizar navegadores, principalmente usada para pruebas automatizadas. Con Selenium WebDriver, se pueden controlar navegadores e interactuar con elementos de la página web.

Entendí la importancia de los selectores, como `ID, Name, Class Name, Tag Name, CSS Selectors y XPath`, para localizar elementos en una página web. También aprendí a estructurar proyectos usando el Page Object Model (POM), que organiza el código de prueba de manera más mantenible y escalable, agrupando interacciones específicas de cada página en clases.

Además, el curso cubrió la creación de pruebas unitarias utilizando `unittest` y `pytest`. unittest es el framework integrado en Python para pruebas unitarias, mientras que pytest ofrece características adicionales como la ejecución paralela y una sintaxis más flexible.

Finalmente, aprendí a generar reportes detallados de las pruebas. Usando `Allure`, pude crear reportes elegantes y detallados que incluyen capturas de pantalla y gráficos de resumen. También aprendí a generar reportes HTML con `pytest-html`, proporcionando un resumen claro y accesible de los resultados de las pruebas.



### Selenium y WebDriver en Python

[Selenium](https://www.selenium.dev/) es una herramienta potente y popular para la automatización de navegadores web. Se utiliza principalmente para pruebas automatizadas de aplicaciones web, pero también puede ser útil para tareas de web scraping y otras interacciones con el navegador. Selenium WebDriver es una API que permite controlar un navegador de forma programática.

Con Selenium y WebDriver, puedes:

- Abrir y cerrar navegadores.
- Navegar a URL específicas.
- Interactuar con elementos de la página (como hacer clic, llenar formularios, subir archivos, etc.).
- Capturar y verificar el estado de la aplicación web.

### Pruebas Automatizadas

Las pruebas automatizadas son esenciales para asegurar la calidad y fiabilidad del software. Con las pruebas automatizadas, puedes ejecutar un conjunto de pruebas repetidamente con poco esfuerzo, detectando rápidamente errores y regresiones en el código.

En este proyecto, utilizamos dos frameworks de pruebas en Python:

- `unittest`: El framework de pruebas unitarias integrado en Python, que proporciona una estructura básica para escribir y ejecutar pruebas.
- `pytest`: Un framework de pruebas más avanzado que ofrece características adicionales como la ejecución paralela, fixtures, y una sintaxis más flexible y concisa.

## Estructura del Proyecto

- **POM**: Este módulo contiene funciones personalizadas que realicé utilizando Selenium. Incluye funciones como navegar a una URL, hacer click, subir archivos, etc. El módulo está organizado siguiendo el patrón de diseño Page Object Model.
- **Unittest**: Este módulo contiene pruebas unitarias utilizando el framework `unittest`.
- **env**: Variables de entorno usadas en el módulo de `unittest`.
- **pytest**: Este módulo contiene pruebas unitarias utilizando el framework `pytest`. También incluye los siguientes directorios:
  - **allure_reports**: Directorios que contiene los reportes generados por Allure.
  ![report](https://res.cloudinary.com/dqa2kd0vc/image/upload/v1722554555/report_nopcommerce_w6ksat.png)
  - **html_reports**: Archivo generado con los reportes después de ejecutar las pruebas.
  ![html_report](https://res.cloudinary.com/dqa2kd0vc/image/upload/v1722554861/report_html_odqgt1.png)
  - **Archivos de prueba**: Archivos de prueba que utilizan `pytest` para ejecutar pruebas automatizadas.
- **BDD**: Este módulo contiene archivos relacionados con el desarrollo guiado por comportamiento (BDD).
  - **features**: Directorio que contiene los archivos `.feature` escritos en Gherkin, que describen los escenarios de prueba.
  - **steps**: Directorio que contiene los archivos `.py` con la implementación de los pasos (`steps`) para los escenarios de prueba definidos en los archivos `.feature`.
- **.gitignore**: Archivo de configuración para excluir archivos y directorios específicos del control de versiones.
- **select_upload.py**: Archivo de prueba.
- **test_formulario.py**: Archivo de prueba.

## Links

Sitios web utilizados durante el curso
- [Swag Labs](https://www.saucedemo.com/)
- [seleniumeasy](https://demo.seleniumeasy.com/)
- [ToolQA](https://demoqa.com/)
- [OrangeHRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
- [Herokuapp upload file](https://testpages.herokuapp.com/styled/file-upload-test.html)
- [jQuery draggable](https://jqueryui.com/draggable/)
