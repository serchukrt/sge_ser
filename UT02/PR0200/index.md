# Practica 1 - Entorno de producción de desarrollo contenerizado

### Ejercicios:

1.

```

version: '3.8'
 
services:
  # ENTORNO DE DESARROLLO
  db_dev:
    image: postgres:14
    container_name: db_dev
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=paso
    ports:
      - '5432:5432'
    volumes:
      - ./OdooDesarrollo/dataPG:/var/lib/postgresql/data
 
  odoo_dev:
    image: odoo:16
    container_name: odoo_dev
    environment:
      - HOST=db_dev
      - USER=odoo
      - PASSWORD=paso
    ports:
      - '8069:8069'
    volumes:
      - ./OdooDesarrollo/volumesOdoo/addons:/mnt/extra-addons
      - ./OdooDesarrollo/volumesOdoo/filestore:/var/lib/odoo/filestore
    depends_on:
      - db_dev
    command: --dev=all
 
  # ENTORNO DE PRODUCCIÓN
  db_prod:
    image: postgres:14
    container_name: db_prod
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=paso
    ports:
      - '5433:5432'
    volumes:
      - ./OdooProduccion/dataPG:/var/lib/postgresql/data
 
  odoo_prod:
    image: odoo:16
    container_name: odoo_prod
    environment:
      - HOST=db_prod
      - USER=odoo
      - PASSWORD=paso
    ports:
      - '8070:8069'
    volumes:
      - ./OdooProduccion/volumesOdoo/addons:/mnt/extra-addons
      - ./OdooProduccion/volumesOdoo/filestore:/var/lib/odoo/filestore
    depends_on:
      - db_prod
 

```