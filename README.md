# cc-proyecto-final
Proyecto Final de Cloud Computing

## Integrantes:
- Sebastián Hurtado
- Francisco Mejía

## Descripción
La aplicación a utilizar es un ecommerce hecho previamente por los integrantes utilizando el framework web Django. 

## Arquitectura

![Arquitectura](cloud.png)

## Funcionalidad

Las principales funcionalidades de la aplicación son las siguientes

- Registro de usuarios
- Creación de estudiantes
- Compra de talleres
- Creación de talleres
- Dashboard para manipular la base de datos de la aplicación

## Referencias

## Motivación

Esta aplicación fue seleccionada principalmente pues los integrantes entienden a fondo los componentes que la integran. Además, tiene una complejidad intermedia y es fácilmente adaptable a las demás necesidades del proyecto, como el procesamientoe de data para analítica. Además de esto, las herramientas con las que fue hecha la aplicación cuentan con suficiente documentación para realizar la migración de los diferentes componentes a kubernetes.

## Conceptos de cloud

- Multicontainer: la aplicación será desplegada en Kubernetes
- Procesamiento de datos: la información relacionada a las compras en la aplicación será procesada en paralelo mediante Celery para realizar analítica.
  - Generar data con Django Factory
  - Al día, los talleres con fecha de inicio pasada se vuelven inactivos.
  - Al día, se revisa qué talleres con descuentos están a una semana de empezar y se quita el descuento.
  - A la semana, se revisa quiénes se han quedado con carritos sin pagar.
  - Se borran los carritos inactivos.
  - Se revisan los talleres más comprados por mes y el resultado de la query se guarda en un modelo con json field.
  - Se revisan los usuarios por país que han comprado talleres por mes y se guardan en un modelo con json field.
- Modelo de programación en la nube: el procesamiento anterior aprovechará el uso de In Memory Processing para acelerar los resultados de analítica.
- Almacenamiento dinámico: 
- Escalabilidad: mediante las herramientas de administración de Kubernetes, se proporcionarán reglas para garantizar la escalabilidad de la aplicación.
- Testeo y monitoreo: para testear la carga de la aplicación, se utilizará la herramienta [Locust](https://locust.io/), mientras que para el monitoreo se utilizará [Prometheus](https://prometheus.io/)

## Ejecución
