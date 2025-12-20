# Practica 1 - Campos del modelo

### Ejercicio:

## 1. Estructura del Módulo

El módulo se ha organizado siguiendo la estructura estándar de directorios de Odoo:

gestion_productos/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── producto.py
├── security/
│   └── ir.model.access.csv
└── views/
    └── producto_view.xml

---

## 2. Código Fuente y Desarrollo

A continuación se detalla el contenido de cada archivo creado para cumplir con los requisitos funcionales.

### 2.1. Manifiesto (__manifest__.py)
Define los metadatos del módulo, las dependencias y carga los archivos de vistas y seguridad.

CODIGO:
{
    'name': 'Gestión de Productos',
    'version': '1.0',
    'summary': 'Gestión de inventario con categorías y precios',
    'description': 'Módulo para administrar productos con campos de jardín, hogar y electrodomésticos, control de stock y precios.',
    'category': 'Inventory',
    'author': 'Estudiante',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/producto_view.xml',
    ],
    'installable': True,
    'application': True,
}

### 2.2. Inicializadores (__init__.py)

Archivo: gestion_productos/__init__.py
CODIGO:
from . import models

Archivo: gestion_productos/models/__init__.py
CODIGO:
from . import producto

### 2.3. Modelo (models/producto.py)
Se ha definido la clase GestionProducto. Se han implementado las siguientes características técnicas:
- Campos Obligatorios: "code" y "name" tienen required=True.
- Selección: Campo "category" con opciones predefinidas (Jardín, Hogar, Electrodomésticos).
- Precisión Decimal: Campo "weight" con digits=(10, 2).
- Automatización:
  - creation_date: Valor por defecto fields.Datetime.now.
  - last_update: Se actualiza automáticamente al sobrescribir el método write.

CODIGO:
from odoo import models, fields, api

class GestionProducto(models.Model):
    _name = 'gestion.producto'
    _description = 'Modelo para la gestión de productos'

    # --- Información básica del producto ---
    name = fields.Char(string='Nombre del producto', required=True)
    description = fields.Text(string='Descripción del producto')
    code = fields.Char(string='Código de producto', required=True)
    image = fields.Binary(string='Imagen del producto')

    # --- Categoría y tipo de producto ---
    category = fields.Selection([
        ('jardin', 'Jardín'),
        ('hogar', 'Hogar'),
        ('electro', 'Electrodomésticos')
    ], string='Categoría')
    
    is_featured = fields.Boolean(string='Producto destacable', default=False)

    # --- Información económica ---
    sale_price = fields.Float(string='Precio de venta')
    stock = fields.Integer(string='Stock disponible')

    # --- Fechas y disponibilidad ---
    creation_date = fields.Datetime(
        string='Fecha de creación', 
        default=fields.Datetime.now,
        readonly=True
    )
    last_update = fields.Datetime(
        string='Fecha de última actualización',
        readonly=True
    )

    # --- Información adicional ---
    active = fields.Boolean(string='Activo', default=True)
    weight = fields.Float(string='Peso del producto (kg)', digits=(10, 2))

    # Sobreescritura del método write para actualizar la fecha de modificación
    def write(self, vals):
        vals['last_update'] = fields.Datetime.now()
        return super(GestionProducto, self).write(vals)


### 2.4. Vistas (views/producto_view.xml)
Se ha diseñado una interfaz intuitiva utilizando:
- Form View: Uso de sheet, group y notebook para organizar la información.
- Tree View: Lista resumen con los datos clave.
- Actions & Menus: Integración en el menú principal de Odoo.

CODIGO:
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="view_gestion_producto_form" model="ir.ui.view">
        <field name="name">gestion.producto.form</field>
        <field name="model">gestion.producto</field>
        <field name="arch" type="xml">
            <form string="Ficha de Producto">
                <sheet>
                    <div class="oe_title">
                        <label for="name" class="oe_edit_only"/>
                        <h1><field name="name"/></h1>
                    </div>
                    <group>
                        <group string="Datos Principales">
                            <field name="code"/>
                            <field name="category"/>
                            <field name="is_featured"/>
                            <field name="image" widget="image" class="oe_avatar"/>
                        </group>
                        <group string="Datos Económicos">
                            <field name="sale_price" widget="monetary"/>
                            <field name="stock"/>
                        </group>
                    </group>
                    <group string="Descripción">
                        <field name="description"/>
                    </group>
                    <notebook>
                        <page string="Información Adicional">
                            <group>
                                <field name="creation_date"/>
                                <field name="last_update"/>
                                <field name="weight"/>
                                <field name="active"/>
                            </group>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>

    <record id="view_gestion_producto_tree" model="ir.ui.view">
        <field name="name">gestion.producto.tree</field>
        <field name="model">gestion.producto</field>
        <field name="arch" type="xml">
            <tree string="Listado de Productos">
                <field name="code"/>
                <field name="name"/>
                <field name="category"/>
                <field name="sale_price"/>
                <field name="stock"/>
                <field name="is_featured"/>
                <field name="active" widget="boolean_toggle"/>
            </tree>
        </field>
    </record>

    <record id="action_gestion_producto" model="ir.actions.act_window">
        <field name="name">Productos</field>
        <field name="res_model">gestion.producto</field>
        <field name="view_mode">tree2,form</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Crea tu primer producto en el sistema
            </p>
        </field>
    </record>

    <menuitem id="menu_gestion_productos_root" name="Gestión Productos" sequence="10"/>
    <menuitem id="menu_gestion_producto_list" parent="menu_gestion_productos_root" action="action_gestion_producto" name="Lista de Productos"/>
</odoo>


### 2.5. Seguridad (security/ir.model.access.csv)
Se configuran los permisos de acceso (CRUD) para el grupo de usuarios base.

CODIGO:

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_gestion_producto,access_gestion_producto,model_gestion_producto,base.group_user,1,1,1,1
```

---

## 3. Resultado Final


![](./fotos/Captura%20de%20pantalla%202025-12-19%20103747.png)