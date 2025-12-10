# Practica 1 - Creación del primer módulo en Odoo

1. Accedemos al contenedor de Oooo
   
 ```
 docker exec -it 4492 bash

 ```

1.  Entramos a los addons

 ```
 cd /mnt/extra-addons/

 ```

3.  Creamos un nuevo modulo con Scaffold
   
 ```
 odoo scaffold gestion_salas

 ```

4. Tenemos que comentar la linea del view y quedar asi:
   
 ```
 'data': [
     'security/ir.model.access.csv',
     'views/views.xml',
     #'views/templates.xml',
 ],
 'application': True,
 'installable': True,
 ```
 
5. Configiramos los Models, creando los campos que nos pide la practica
 
 ```python

from odoo import models, fields, api


class gestion_salas(models.Model):
     _name = 'gestion_salas.gestion_salas'
     _description = 'gestion_salas.gestion_salas'

nombre = fields.Char()
capacidad = fields.Integer()
fechareserva = fields.Date()
reservada = fields.Boolean()
comentarios = fields.Text()

 ```

6. Ahora tenemos que ocnfigurar los Views

```xml

<odoo>
  <data>
    <record model="ir.ui.view" id="gestion_salas.list">
      <field name="name">gestion_salas list</field>
      <field name="model">gestion_salas.sala</field>
      <field name="arch" type="xml">
      <!-- Campos del Model -->
        <tree>
            <field name="nombre"/>
            <field name="capacidad"/>
            <field name="fechareserva"/>
            <field name="reservada"/>
            <field name="comentarios"/>
          </tree>
      </field>
    </record>
 
    <record model="ir.actions.act_window" id="gestion_salas.action_window">
      <field name="name">Salas</field>
      <field name="res_model">gestion_salas.sala</field> <field name="view_mode">tree,form</field>
    </record>
 
    <!-- Creación de los menús -->
    <menuitem name="Gestión de salas" id="gestion_salas.menu_root"/>
    <!-- Creación de los submenús -->
    <menuitem name="Salas" id="gestion_salas.menu_1" parent="gestion_salas.menu_root"/>
    <menuitem name="Reservas" id="gestion_salas.menu_2" parent="gestion_salas.menu_root"/>
    <menuitem name="Salas disponibles" id="gestion_salas.menu_1_list" parent="gestion_salas.menu_1" action="gestion_salas.action_window"/>
    <menuitem name="Reservas realizadas" id="gestion_salas.menu_2_list" parent="gestion_salas.menu_2" action="gestion_salas.action_window"/>
    </data>
</odoo>


```

7. Por ultimo reiniciamos el contenedor
