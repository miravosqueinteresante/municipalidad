---
layout: page
title: "Acerca de"
permalink: /acerca/
description: "Origen, método, licencia y límites de los datos de reclamos ciudadanos de la Municipalidad de Asunción."
---

## Qué es este sitio

`municipalidad.muchotexto.net` abre al público los reclamos y denuncias ciudadanas que recibe la Municipalidad de Asunción. Forma parte del ecosistema [muchotexto.net](https://muchotexto.net) y de [MuchoTexto Data](https://datospublicos.muchotexto.net), la infraestructura de datos verificables sobre Paraguay.

**Es un proyecto independiente, no oficial.** No está afiliado a la Municipalidad de Asunción.

## Origen de los datos

Los registros fueron entregados por el **Departamento de Atención al Ciudadano** de la Municipalidad de Asunción, como respuesta a un pedido de acceso a la información pública (**ID 106387**, Ley 5282/2014 de Libre Acceso Ciudadano a la Información Pública y Transparencia Gubernamental), respondido mediante el **Memo D.A.C. N.º 34/2026** de fecha 11 de septiembre de 2026.

El pedido solicitaba, en formato reutilizable, los reclamos del período **1 de enero de 2023 hasta la fecha de corte (11/09/2026)**, con tipo o categoría, dependencia a la que fue derivado, barrio, estado y fechas, **sin ningún dato personal**.

## Qué se publica y qué no

- **Se publica:** datos agregados y anonimizados (conteos por categoría, dependencia, barrio, estado, año y mes).
- **No se publica:** registros individuales, nombres, cédulas, teléfonos, correos ni domicilios de reclamantes.
- Los conteos de barrio menores a 5 se omiten para reducir el riesgo de reidentificación.

## Método

Los cuatro archivos Excel entregados (uno por año) se consolidaron con un script Python que:

1. Mapea las columnas de cada año (que cambiaron entre 2023 y 2026) a un esquema único.
2. Infiere el estado a partir de la hoja (pendientes/finalizados) cuando la columna no existe.
3. Normaliza nombres (sin acentos, mayúsculas) para agrupar variantes de escritura de categorías y dependencias.
4. Agrega los resultados en un único dataset JSON.

El script es reproducible: `scripts/consolidar_reclamos.py` en el repositorio de datos.

**Alcance:** el Departamento recibe y **deriva** los reclamos a las dependencias según el canal — WEB (PMT, Policía Fiscalizadora de Negocios, Vigilancia, Vialidad) y LIBRO (PCI, Defensa del Consumidor, Desarrollo Urbano, Gestión Ambiental, Obras Particulares). No gestiona expedientes ni resuelve reclamos: la ejecución y el cierre corresponden a cada dependencia, y algunos casos pueden pasar al **Juzgado de Faltas** sin quedar reflejados en este registro.

## Licencia

El procesamiento y análisis derivados se publican bajo **Creative Commons BY 4.0**. La licencia se aplica al trabajo propio de agregación y normalización, no a la titularidad de los datos originales, que corresponden a su fuente.

## Diccionario de datos

El dataset `reclamos.json` contiene:

- `_meta` — fuente, número de pedido, memo, período, fecha de corte, licencia y nota de independencia.
- `kpis` — totales, pendientes, finalizados, anulados y tasa de resolución.
- `por_anio` / `por_mes` — conteos por año y por mes (pendientes, finalizados, anulados, total).
- `por_categoria` / `por_dependencia` — listas `{nombre, total}` por tipo de reclamo y dependencia.
- `por_barrio` — lista `{nombre, total}`, sin conteos menores a 5.

## Límites conocidos

- **Barrios:** sin registro en 2023; campo mezclado con dirección en 2024.
- **Tiempos de resolución:** no hay fecha de cierre sistemática, por lo que no se mide de forma confiable cuánto tarda un reclamo en resolverse.
- **Canal de ingreso:** el registro no desagrega web, WhatsApp, teléfono ni presencial.
- **Categorías:** se agruparon variantes de escritura, pero la taxonomía municipal no está normalizada en origen.
- **No comparables entre canales** ni representativos de la totalidad de reclamos de la ciudad.

## Correcciones

¿Encontraste un error o un dato sensible? Escribinos y lo corregimos. Ver <a href="{{ '/contacto/' | relative_url }}">Contacto y correcciones</a>.
