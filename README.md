# Proyecto Final Python Flex - Comisión 55070

--------------------------------------------------------------------------------

## Preparación de requirements y entorno virtual para el proyecto Django 
![Alt text](doc-img/django.png)

## Crear el entorno virtual

```bash
python3 -m venv .venv
```

## Activar el entorno desde VSCode

![Alt text ](doc-img/image-2.png) ![Alt text](doc-img/image-1.png)
```bash
source .venv/bin/activate
```


![Alt text](doc-img/image.png)
```bash
.\venv\Scripts\activate
```

## Instalación de requierements. Esto instalara django y los paquetes necesarios para ejecutar el proyecto.

```bash
pip3 install -r requirements.txt
```

## Servidor

```bash
python manage.py runserver
```

- Ejecuta el servidor. Para pararlo: control + c (cmd + c en Mac)

- Abrir el navegador y ejecutar el servidor Django en la dirección `127.0.0.1:8000`


## Pagina WEB - funcionalidades

## Usuarios: ##

USER: admin / PASS: 1234

USER: coder / PASS: Python1234

## Permisos ##

Se crearon dos usuarios, un superusuario y otro usuario regular. A continuacion el listado de permisos por usuario en todas las secciones de la pagina:

| Usuario  | Create  | Read | Update | Delete |
| -------- | ------- | ---- | ------ | ------ |
| admin    |    x    |  x   |   x    |   x    |
| coder    |    x    |  x   |        |        |


Se puede acceder la pagina sin esta logueado, pero solo permite acceder al About/

## Estructura ##

El sitio creado presenta la siguiente estructura:

**http://localhost:8000/** - El "HOME" de la pagina muestra una barra de navegacion en la parte superior que permite navegar entre todas las secciones disponibles, dichos accesos son parte del base.html, por lo que estaran presentes en todas las paginas del sitio. El link de "ABOUT - http://localhost:8000/about" te dirije a una pagina donde hay una breve descripcion de mi carrera profesional y hay un icono de Linkedin que permite llegar a mi perfil de Linekdin.
Todas las paginas tienen un boton para volver el index.html de la aplicacion.

**http://localhost:8000/cliente** - El link "CLIENTES" permite visualizar en su index.html un listado en formato de tabla, de los clientes registrados, en donde se implemento el concepto de **CRUD**. Todas las paginas tienen un boton para volver el index.html de la aplicacion.

**http://localhost:8000/compras** - El link "COMPRAS" permite visualizar en su index.html un listado en formato de tabla, de las compras realizadas. Dispone de dos botones, uno para ingresa una nueva compra y el otro permite realizar una busqueda por categoria de compra.Todas las paginas tienen un boton para volver el index.html de la aplicacion.

**http://localhost:8000/stock** - El link "STOCK" permite visualizar en su index.html un listado en formato de tabla, del stock disponible, en donde se implemento el concepto de **CRUD**. Dispone de dos botones, uno para agregar un nuevo articulo al stock y el otro permite realizar una busqueda por ubicacion. Todas las paginas tienen un boton para volver el index.html de la aplicacion.

## Extras

* Se utilizo el siguiente comando para realizar una carga inicial de datos en los modelos de datos de cada aplicacion.

```bash
python3 manage.py loaddata cliente/innitial_data.json
python3 manage.py loaddata compras/innitial_data.json
python3 manage.py loaddata stock/innitial_data.json
```

Ref: https://docs.djangoproject.com/en/4.2/howto/initial-data/

* Se utilizo el shortcut de VSCode para dar formato a todos los archivos html

 - MAC: ⇧⌥F
 - WINDOWS: Ctrl+Shift+I 

Ref: https://code.visualstudio.com/docs/languages/html#_formatting

* Plugins VSCode para hacernos mas facil la vida

**Name: Django**
Id: batisteo.vscode-django
Description: Beautiful syntax and scoped snippets for perfectionists with deadlines
Version: 1.13.0
Publisher: Baptiste Darthenay
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django

**Name: Django Support**
Id: almahdi.code-django
Description: Best syntax highlighter and snippets for Django
Version: 0.5.2
Publisher: Al Mahdi
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=almahdi.code-django

**Name: djLint**
Id: monosans.djlint
Description: HTML template formatter and linter (Django, Jinja, Nunjucks, Twig, Handlebars, Mustache)
Version: 2023.8.10
Publisher: monosans
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=monosans.djlint

**Name: SQLite Viewer**
Id: qwtel.sqlite-viewer
Description: SQLite Viewer for VSCode
Version: 0.3.13
Publisher: Florian Klampfer
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer

**Name: Tabnine: AI Autocomplete & Chat for Javascript, Python, Typescript, PHP, Go, Java & more**
Id: TabNine.tabnine-vscode
Description: AI coding assistant with AI code completions and AI code chat right in the IDE, helping developers by generating code, writing unit tests and documentation, explaining legacy code, and much more. Tabnine supports all major languages including JavaScript, Python, Java, Typescript c/c++ and more.
Version: 3.16.0
Publisher: TabNine
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode

**Name: HTML Boilerplate**
Id: sidthesloth.html5-boilerplate
Description: A basic HTML5 boilerplate snippet generator.
Version: 1.1.1
Publisher: sidthesloth
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=sidthesloth.html5-boilerplate

## Demo

El sitio se encuentra hosteado en [pythonanywhere](https://www.pythonanywhere.com/):

* http://rodgerema.pythonanywhere.com/

Ref: https://recursospython.com/guias-y-manuales/desplegar-un-proyecto-de-django-en-pythonanywhere/