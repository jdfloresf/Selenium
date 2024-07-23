# Curso de Selenium

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

- **POM**: Este módulo contiene funciones personalizadas que realicé utilizando Selenium. Incluye funciones como navegar a una URL, hacer clic, subir archivos, etc. El módulo está organizado siguiendo el patrón de diseño Page Object Model.
- **Unittest**: Este módulo contiene pruebas unitarias utilizando el framework `unittest`.
- **env**: Variables de entorno usadas en el módulo de `unittest`.
- **pytest**: Pruebas unitarias utilizando el framework `pytest`.
- **.gitignore**: Archivo de configuración para excluir archivos y directorios específicos del control de versiones.
- **select_upload.py**: Archivo de prueba.
- **test_formulario.py**: Archivo de prueba.
