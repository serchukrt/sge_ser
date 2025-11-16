# Practica 1 - Entorno de producción de desarrollo contenerizado

### Ejercicios:

1.

```

version: '3.8'

services:
  # Entorno de Desarrollo
  postgres_dev:
    image: postgres:14
    container_name: db_dev
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo_dev
      - POSTGRES_PASSWORD=paso_dev
    volumes:
      # 1. Volumen de Desarrollo (Base de Datos)
      - ~/OdooDev/dev/dataPG:/var/lib/postgresql/data
    networks:
      - odoo_network

  odoo_dev:
    image: odoo:16
    container_name: odoo_dev
    environment:
      - HOST=postgres_dev 
      - USER=odoo_dev
      - PASSWORD=paso_dev
    ports:
      # Puerto 8069 del host para desarrollo
      - '8069:8069'
    volumes:
      # 2. Volumen de Desarrollo (Addons)
      - ~/OdooDev/dev/addons:/mnt/extra-addons
      # 3. Volumen de Desarrollo (Filestore)
      - ~/OdooDev/dev/filestore:/var/lib/odoo/filestore
      # 4. Volumen de Desarrollo (Sessions)
      - ~/OdooDev/dev/sessions:/var/lib/odoo/sessions
    depends_on:
      - postgres_dev
    command: --dev=all
    networks:
      - odoo_network

  # Entorno de Producción
  postgres_prod:
    image: postgres:14
    container_name: db_prod
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo_prod
      - POSTGRES_PASSWORD=paso_prod
    volumes:
      # Volumen de BBDD de producción (separado del de desarrollo)
      - ~/OdooDev/prod/dataPG:/var/lib/postgresql/data
    networks:
      - odoo_network

  odoo_prod:
    image: odoo:16
    container_name: odoo_prod
    environment:
      - HOST=postgres_prod 
      - USER=odoo_prod
      - PASSWORD=paso_prod
    ports:
      # Puerto 8070 del host para producción (evita conflicto con dev)
      - '8070:8069'
    volumes:
      # Único volumen mapeado para producción, según el objetivo
      - ~/OdooDev/prod/addons:/mnt/extra-addons
    depends_on:
      - postgres_prod
    networks:
      - odoo_network

# Red Común
networks:
  odoo_network:
    driver: bridge

```