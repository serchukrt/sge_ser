# Practica 1 - Módulo con dos modelos

1. Creamos los modulos para los libros y autores

Libros:
```python

from odoo import models, fields, api

class gestion_libros(models.Model):
    _name = 'gestion_biblioteca.libros'
    _description = 'Modelo de gestión de libros'
    nombre = fields.Char()
    autor = fields.Char()
    fechapubli = fields.Date()
    ISBN = fields.Char()
    sinopsis = fields.Text()

```
Autores:
```python

from odoo import models, fields, api

class gestion_autores(models.Model):
    _name = 'gestion_biblioteca.autor'
    _description = 'Modelo de gestión de autores'
    nombre = fields.Char()
    fechanac = fields.Date()
    biografia = fields.Text()
    libros = fields.Char()

```
2. Metemos lo siguiente en el init de la carpeta models para que Odoo los utilice:
```python

from . import library_autor
from . import library_book

```
3. Creamos las views para los siguientes archivos:

- library_author_views.xml
```xml

<odoo>
    <data>
        <record model="ir.ui.view" id="gestion_biblioteca.listaautores">
        <field name="name">Lista de autores</field>
        <field name="model">gestion_biblioteca.autor</field>
        <field name="arch" type="xml">
            <tree>
                <field name="nombre"/>
                <field name="fechanac"/>
                <field name="biografia"/>
                <field name="libros"/>
            </tree>
        </field>
        </record>
    </data>
</odoo>

```

- library_book_views.xml
```xml

<odoo>
    <data>
        <record model="ir.ui.view" id="gestion_biblioteca.listalibros">
        <field name="name">Lista de libros</field>
        <field name="model">gestion_biblioteca.libros</field>
        <field name="arch" type="xml">
            <tree>
                <field name="nombre"/>
                <field name="autor"/>
                <field name="fechapubli"/>
                <field name="ISBN"/>
                <field name="sinopsis"/>
            </tree>
        </field>
        </record>
    </data>
</odoo>

```

- library_menu_views.xml
```xml

<odoo>
    <data>
        <record model="ir.actions.act_window" id="action_listalibros">
            <field name="name">Libros</field>
            <field name="res_model">gestion_biblioteca.libros</field>
            <field name="view_mode">tree,form</field>
        </record>

        <record model="ir.actions.act_window" id="action_listaautores">
            <field name="name">Autores</field>
            <field name="res_model">gestion_biblioteca.autor</field>
            <field name="view_mode">tree,form</field>
        </record>
        <menuitem name="Gestión de biblioteca" id="gestion_biblioteca.menu_root"/>
        <menuitem name="Libros" id="gestion_biblioteca.menu_1" parent="gestion_biblioteca.menu_root"/>
        <menuitem name="Lista de Libros" id="gestion_biblioteca.menu_libros_list" parent="gestion_biblioteca.menu_1" action="action_listalibros"/>
        <menuitem name="Autores" id="gestion_biblioteca.menu_2" parent="gestion_biblioteca.menu_root"/>
        <menuitem name="Lista de Autores" id="gestion_biblioteca.menu_autores_list" parent="gestion_biblioteca.menu_2" action="action_listaautores"/>
    </data>
</odoo>

```

4. Añadimos las views en el manifest

```python

 'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/library_menu_views.xml',
        'views/library_book_views.xml',
        'views/library_author_views.xml',
        #'views/templates.xml',
    ],

```

5. Rescribiremos el archivo "ir.model.access.csv" y pondremos :
```

access_gestion_biblioteca_autor,gestion_biblioteca.autor,model_gestion_biblioteca_autor,base.group_user,1,1,1,1
access_gestion_biblioteca_book,gestion_biblioteca.book,model_gestion_biblioteca_libros,base.group_user,1,1,1,1

```

6. Resultados en Odoo
