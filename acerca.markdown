---
layout: page
title: "Acerca de"
permalink: /acerca/
description: "Origen, método y límites de los datos de reclamos ciudadanos de la Municipalidad de Asunción."
---

## Qué es este sitio

`municipalidad.muchotexto.net` abre al público los reclamos y denuncias ciudadanas que recibe la Municipalidad de Asunción. Forma parte del ecosistema [muchotexto.net](https://muchotexto.net) y de [MuchoTexto Data](https://datospublicos.muchotexto.net), la infraestructura de datos verificables sobre Paraguay.

## Origen de los datos

Los registros fueron entregados por el **Departamento de Atención al Ciudadano** de la Municipalidad de Asunción, como respuesta a un pedido de acceso a la información pública (**ID 106387**), formulado al amparo de la **Ley 5282/2014** de Libre Acceso Ciudadano a la Información Pública y Transparencia Gubernamental.

El pedido solicitaba, en formato reutilizable, los reclamos del período **1 de enero de 2023 hasta la fecha de respuesta (septiembre de 2026)**, con tipo o categoría, dependencia a la que fue derivado, barrio, estado y fechas, **sin ningún dato personal**.

## Qué se publica y qué no

- **Se publica:** datos agregados y anonimizados (conteos por categoría, dependencia, barrio, estado, año y mes).
- **No se publica:** registros individuales, nombres, cédulas, teléfonos, correos ni domicilios de reclamantes.

## Método

Los cuatro archivos Excel entregados (uno por año) se consolidaron con un script Python que:

1. Mapea las columnas de cada año (que cambiaron entre 2023 y 2026) a un esquema único.
2. Infiere el estado a partir de la hoja (pendientes/finalizados) cuando la columna no existe.
3. Normaliza nombres (sin acentos, mayúsculas) para agrupar variantes de escritura de categorías y dependencias.
4. Agrega los resultados en un único dataset JSON.

El script es reproducible: `scripts/consolidar_reclamos.py` en el repositorio de datos.

## Límites conocidos

- **Barrios:** sin registro en 2023; campo mezclado con dirección en 2024.
- **Tiempos de resolución:** no hay fecha de cierre sistemática, por lo que no se mide de forma confiable cuánto tarda un reclamo en resolverse.
- **Canal de ingreso:** el registro no desagrega web, WhatsApp, teléfono ni presencial.
- **Categorías:** se agruparon variantes de escritura, pero la taxonomía municipal no está normalizada en origen.

## Contacto

Dudas, correcciones o pedidos: [muchotexto.net/contacto](https://muchotexto.net/contacto/).
