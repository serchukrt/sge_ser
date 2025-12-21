# Practica 2 - Campos relacionales

### Ejercicio:


- `autores.py`

```python
from odoo import models, fields, api


class autores(models.Model):
    _name = 'library_srp.autores'
    _description = 'Módulo para los autores'

    nombre = fields.Char()
    pais = fields.Many2one('res.country')
    genero = fields.Selection([
                                ('novela', 'Novela'),
                                ('drama', 'Drama'),
                                ('cienciaficcion', 'Ciencia ficción'),
                                ('misterio', 'Misterio'),
                                ('terror', 'Terror'),
                                ('historico', 'Histórico')
                            ],String ='Género')
    libro_ids = fields.One2many(
        comodel_name  = 'library_srp.libros',
        inverse_name = 'autor_id',
        string = "Libros publicados"
    )
```

- `libros.py`

```python
from odoo import models, fields, api


class libros(models.Model):
    _name = 'library_srp.libros'
    _description = 'Módulo para los libros'

    titulo = fields.Char()
    autor = fields.Char()
    genero = fields.Selection([
                                ('novela', 'Novela'),
                                ('drama', 'Drama'),
                                ('cienciaficcion', 'Ciencia ficción'),
                                ('misterio', 'Misterio'),
                                ('terror', 'Terror'),
                                ('historico', 'Histórico')
                            ],String ='Género')
    socios_ids = fields.One2many(
        comodel_name='library_srp.socios',
        inverse_name='libro_prestado_id',
        string='Socios prestados'
    )
    autor_id = fields.Many2one(
        comodel_name = 'library_srp.autores',
        string = 'Autor',
        required=True
    )
```

- `socios.py`

```python
from odoo import models, fields, api


class socios(models.Model):
    _name = 'library_srp.socios'
    _description = 'Módulo para los socios'

    nombre = fields.Char()
    telefono = fields.Integer()
    libro_prestado_id = fields.Many2one(
        comodel_name='library_srp.libros',
        string='Libro prestado'
    )
```

### Añadir las views

- `library_author_views.xml`

```xml
<odoo>
    <data>
        <record id="action_library_srp_autores" model="ir.actions.act_window">
            <field name="name">Autores</field>
            <field name="res_model">library_srp.autores</field>
            <field name="view_mode">tree,form</field>
        </record>
    </data>
</odoo>
```

- `library_book_views.xml`

```xml
<odoo>
    <data>
        <record id="action_library_srp_libros" model="ir.actions.act_window">
            <field name="name">Libros</field>
            <field name="res_model">library_srp.libros</field>
            <field name="view_mode">tree,form</field>
        </record>
    </data>
</odoo>
```

- `library_socio_views.xml`

```xml
<odoo>
    <data>
        <record id="action_library_srp_socios" model="ir.actions.act_window">
            <field name="name">Socios</field>
            <field name="res_model">library_srp.socios</field>
            <field name="view_mode">tree,form</field>
        </record>
    </data>
</odoo>
```

### Importar los modelos

- `__init__.py`

```python
from . import autores
from . import libros
from . import socios
```

### Configurar `manifest.py` para cargar las views

```python
'data': [
        'security/ir.model.access.csv',
        #'views/views.xml',
        'views/library_menu_views.xml',
        'views/library_book_views.xml',
        'views/library_socio_views.xml',
        'views/library_author_views.xml',
        #'views/templates.xml',
    ],
```

### Configurar la seguridad de la aplicación

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_library_srp_libros,access.library.srp.libros,model_library_srp_libros,base.group_user,1,1,1,1
access_library_srp_autores,access.library.srp.autores,model_library_srp_autores,base.group_user,1,1,1,1
access_library_srp_socios,access.library.srp.socios,model_library_srp_socios,base.group_user,1,1,1,1
```

## Aplicación funcionando
<br>

![Imagen1](./fotos/Captura%20de%20pantalla%202025-12-21%20164001.png)