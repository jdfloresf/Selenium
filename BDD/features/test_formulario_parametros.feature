Feature: Test formulario con parametros

    Background: 
        Given Abriendo navegador

    Scenario Outline: Ejecutando test
        When Cargando nombre de "<usuario>"
        Then Cargando "<email>"
        Then Cargando direccion "<dir1>"
        Then Cargando nueva "<dir2>"
        Then Subiendo informacion
        Then Cerrando sesion

    Examples:
    | usuario | email | dir1 | dir2 |
    | jonathan | jonathan@asdrome.com | Qumichin1 | Qumichin12 |
    | sebastian | sebastian@asdrome.com | Qumichin1 | Qumichin12 |
    | isaac |isaac@asdrome.com | Qumichin1 | Qumichin12 |
    | seleny | seleny@asdrome.com | Qumichin1 | Qumichin12 |
    | victor |victor@asdrome.com | Qumichin1 | Qumichin12 |