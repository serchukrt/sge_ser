# Practica 2 - Campos relacionales

### Ejercicio:

#### model.py:

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import timedelta


class subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'subscription.subscription'

    name = fields.Char(String='Nombre')
    customer_id = fields.Many2one(
            comodel_name='res.partner',    
            required=True, String='ID Consumidor'
        )
    suscription_code = fields.Char(required=True, String='Código subscripción')
    start_date = fields.Date(required=True, String='Fecha entrada')
    end_date = fields.Date(String='Fecha salida')
    duration_months = fields.Integer(compute='_compute_duration_months', String='Meses duración') # computar

    renewal_date = fields.Date(String='Fecha renovación')
    status = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled')
    ], String='Estado')
    is_renewable = fields.Boolean(String='Renovable')
    auto_renewal = fields.Boolean(String='Autorenovación')
    price = fields.Float(String='Precio')

    usage_limit = fields.Integer(String='Límite uso')
    current_usage = fields.Integer(String='Uso actual')
    use_percent = fields.Float(compute='_compute_use_percent',String='Porcentaje uso', store=True)

    # función para calcular la duración de los meses
    @api.depends('start_date', 'end_date')
    def _compute_duration_months(self):
        for record in self:
            if record.start_date and record.end_date:
                delta = relativedelta(record.end_date, record.start_date)
                record.duration_months = delta.years * 12 + delta.months
            else:
                record.duration_months = 0
    # función para calcular el porcentaje de uso
    @api.depends('current_usage', 'usage_limit')
    def _compute_use_percent(self):
        for record in self:
            if record.usage_limit > 0:
                record.use_percent = (record.current_usage / record.usage_limit) * 100
            else:
                record.use_percent = 0.0

    # función que se llama desde views para sumarle 15 días a la fecha de finalización
    def action_extend_15_days(self):
        for record in self:
            if record.end_date:
                record.end_date = record.end_date + timedelta(days=15)
```

#### views.py:

```xml
<odoo>
  <data>

    <record id="view_subscription_tree_basic" model="ir.ui.view">
        <field name="name">subscription.tree.basic</field>
        <field name="model">subscription.subscription</field>
        <field name="arch" type="xml">
            <tree string="Suscripciones básicas" 
            decoration-danger="status=='expired'"
            decoration-warning="status=='cancelled'"
            limit="15">
                <field name="name"/>
                <field name="customer_id"/>
                <field name="suscription_code" />
                <field name="start_date"/>
                <field name="end_date" widget="remaining_days" />
                <field name="duration_months" />
                <field name="renewal_date" />
                <field name="status" widget="radio" />
                <field name="is_renewable" />
                <field name="auto_renewal" />
                <field name="price" 
                attrs="{'invisible': [('status', '=', 'cancelled')]}"/>
                <button name="action_extend_15_days" 
                        string="+15 días" 
                        type="object" 
                        class="btn-primary"/>   
                </tree>
        </field>
    </record>

    <record id="view_subscription_tree_usage" model="ir.ui.view">
        <field name="name">subscription.tree.usage</field>
        <field name="model">subscription.subscription</field>
        <field name="arch" type="xml">
            <tree string="Suscripciones por uso" limit="15">
                <field name="name"/>
                <field name="usage_limit" 
                widget="progressbar"/>
                <field name="current_usage" />
                <field name="use_percent" 
                   decoration-danger="use_percent &gt;= 80" 
                   avg="Media del uso" />
                </tree>
        </field>
    </record>

    <record id="action_subscription_basico" model="ir.actions.act_window">
        <field name="name">Suscripciones (básico)</field>
        <field name="res_model">subscription.subscription</field>
        <field name="view_mode">tree,form</field>
        <field name="view_id" ref="view_subscription_tree_basic"/>
    </record>

    <record id="action_subscription_uso" model="ir.actions.act_window">
        <field name="name">Suscripciones (uso)</field>
        <field name="res_model">subscription.subscription</field>
        <field name="view_mode">tree,form</field>
        <field name="view_id" ref="view_subscription_tree_usage"/>
    </record>

    <menuitem id="menu_subscription_root"
              name="Suscripciones"
              sequence="10"/>

    <menuitem id="menu_subscription_main"
              name="Operaciones"
              parent="menu_subscription_root"
              sequence="1"/>

    <menuitem id="menu_subscription_basico"
              name="Ver básico"
              parent="menu_subscription_main"
              action="action_subscription_basico"
              sequence="1"/>

    <menuitem id="menu_subscription_uso"
              name="Ver uso"
              parent="menu_subscription_main"
              action="action_subscription_uso"
              sequence="2"/>

  </data>
</odoo>
```

#### Actualizar __manifest__.py:

Hay que comentar las línea de templates y descomentar security
```python
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
```