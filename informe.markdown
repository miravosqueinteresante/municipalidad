---
layout: page
title: "Informe: qué reclaman los vecinos de Asunción"
permalink: /informe/
description: "Lectura pública de los reclamos ciudadanos 2023–2026: arbolado, ambiente, tránsito y barrios. Qué revelan los datos y qué limitaciones tienen."
last_modified_at: 2026-10-02
---

{% assign k = site.data.reclamos.kpis %}
{% assign cat1 = site.data.reclamos.por_categoria.first %}

## En una frase

La ciudad reclama, sobre todo, **por sus árboles**. La poda de árboles en la vía pública es el pedido más repetido de Asunción ({{ cat1.total }} reclamos entre 2023 y 2026), muy por encima de cualquier otra categoría. Le siguen las casas abandonadas, la limpieza de baldíos, el retiro de chatarra y el destronque.

## El arbolado urbano como demanda dominante

La concentración en "Poda de árboles en la vía pública" no es casual. Los árboles son, al mismo tiempo, un activo ambiental de la ciudad y una fuente constante de fricción con el espacio público: ramas que tocan cables, veredas rotas por raíces, árboles que necesitan intervención y autorización municipal.

La categoría se desdobla además en varias modalidades que, sumadas, agrandan el fenómeno: **destronque**, **poda interior con notificación** y **autorización de poda por cuenta propia**. Es decir, el manejo del arbolado es el eje transversal de la demanda ciudadana a la municipalidad.

## A quién le toca responder

Casi la mitad de todos los reclamos recae en dos dependencias:

- **Dirección General de Gestión Ambiental** — {{ site.data.reclamos.por_dependencia[0].total }} reclamos, la más solicitada.
- **Dirección de la Policía Municipal de Vigilancia** — {{ site.data.reclamos.por_dependencia[1].total }} reclamos.

Les siguen la Policía Municipal de Tránsito, la Dirección de Vialidad (baches y pavimentos) y Desarrollo Urbano. La estructura del dato refleja la división de competencias: ambiente y control urbano concentran el grueso, mientras vialidad y tránsito se reparten lo relativo a la infraestructura vial.

## Dónde se concentra

Los barrios con más reclamos registrados son, en orden: **San Pablo, Recoleta, San Vicente, Vista Alegre, Villa Morra, Mburucuyá, Obrero y Ciudad Nueva**. Es una mezcla de barrios residenciales consolidados y de alta densidad, lo que es esperable: a más viviendas y más arbolado, más fricciones que reportar.

## La tasa de resolución, leída con cuidado

Globalmente, {{ k.tasa_resolucion }}% de los reclamos figura como **finalizado**. Pero esa cifra hay que leerla con cautela, por dos razones:

1. **El año en curso distorsiona.** 2026 está incompleto (los datos llegan hasta septiembre), con apenas 275 finalizados sobre 2.937 registros: los reclamos más recientes todavía no tuvieron tiempo de cerrarse.
2. **"Finalizado" no siempre es "resuelto a favor".** En los campos de texto libre se documentan finalizaciones como "no se constató lo denunciado", es decir, el cierre puede significar una verificación que descartó el problema, no una reparación.

Dicho esto, mirando años completos (2023–2024), la proporción de finalizados se mantiene en torno al 40–45%, lo que da una idea más realista del ritmo de cierre que la cifra global.

## Lo que los datos no dicen

Estos registros tienen límites importantes que conviene nombrar:

- **No hay trazabilidad fina de tiempos.** No se registra de forma sistemática la fecha de resolución, así que no es posible medir de manera confiable cuánto tarda un reclamo en cerrarse.
- **El barrio es incompleto.** 2023 no registra barrio; 2024 lo mezcla con la dirección. El ranking de barrios se apoya sobre todo en 2025–2026.
- **Las categorías no están normalizadas.** Hubo que agrupar variantes de escritura; quedan matices que una taxonomía municipal más rigurosa resolvería.
- **No hay subcategoría ni canal de ingreso.** El pedido original solicitaba el medio por el que se recibió el reclamo (web, WhatsApp, teléfono); el registro entregado no lo desagrega.

## Para qué sirve

Aun con esas limitaciones, el conjunto permite responder preguntas que antes no se podían responder en público: **qué le preocupa a la ciudad, qué área tiene más demanda y en qué barrios**. Es la base para pedir cuentas con datos, no con percepciones. Y es reproducible: el dataset está publicado y su método está documentado.

<div style="margin-top:2rem;padding:12px 14px;background:rgba(34,184,207,0.06);border:1px solid rgba(34,184,207,0.18);border-radius:8px;font-size:0.85em;line-height:1.6;">
  <strong>Fuente:</strong> Departamento de Atención al Ciudadano, Municipalidad de Asunción, vía pedido de acceso a la información pública ID 106387 (Ley 5282/2014). Datos anonimizados y agregados. <a href="https://datospublicos.muchotexto.net/datos/reclamos.json" target="_blank" rel="noopener noreferrer">Dataset en datos abiertos</a>.
</div>
