---
layout: page
title: "Dashboard — Reclamos ciudadanos"
permalink: /dashboard/
description: "Reclamos de la Municipalidad de Asunción 2023–2026: volumen, estado, categorías, dependencias y barrios. Datos anonimizados y agregados."
last_modified_at: 2026-10-02
---

<div class="dash-page">
<div class="dash">

<p class="dash-eyebrow"><span class="dash-dot"></span>Datos verificados · {{ site.data.reclamos._meta.periodo }}</p>

<p class="dash-intro">Todos los reclamos registrados por el Departamento de Atención al Ciudadano de la Municipalidad de Asunción entre 2023 y 2026. Cifras agregadas y anonimizadas, sin registros individuales. Fuente: <a href="https://datospublicos.muchotexto.net/datos/reclamos.json" rel="noopener noreferrer" target="_blank">datos abiertos</a> (pedido ID 106387, Ley 5282/2014).</p>

{% assign k = site.data.reclamos.kpis %}
<div class="dash-kpis">
  <div class="dash-kpi"><div class="dash-kpi-value">{{ k.total | default: 0 }}</div><div class="dash-kpi-label">Reclamos totales</div><div class="dash-kpi-note">2023–2026</div></div>
  <div class="dash-kpi"><div class="dash-kpi-value">{{ k.pendientes | default: 0 }}</div><div class="dash-kpi-label">Pendientes</div><div class="dash-kpi-note">sin cerrar</div></div>
  <div class="dash-kpi"><div class="dash-kpi-value">{{ k.finalizados | default: 0 }}</div><div class="dash-kpi-label">Finalizados</div><div class="dash-kpi-note">cerrados</div></div>
  <div class="dash-kpi"><div class="dash-kpi-value">{{ k.tasa_resolucion | default: 0 }}%</div><div class="dash-kpi-label">Tasa de resolución</div><div class="dash-kpi-note">finalizados / total</div></div>
</div>

<section class="dash-section">
  <h2 class="dash-section-title">Reclamos por año</h2>
  {% assign max_anio = site.data.reclamos.por_anio.first.total %}
  {% for a in site.data.reclamos.por_anio %}
  <div class="dash-bar">
    <span class="dash-bar-label">{{ a.anio }}</span>
    <div class="dash-bar-track"><div class="dash-bar-fill" style="width: {{ a.total | times: 100.0 | divided_by: max_anio | round: 0 }}%"></div></div>
    <span class="dash-bar-value">{{ a.total }}</span>
  </div>
  {% endfor %}
  <p class="dash-disclaimer">Pendientes + finalizados por año de registro. 2026 incluye hasta septiembre (fecha de la respuesta al pedido).</p>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Top 12 — tipos de reclamo</h2>
  {% assign max_cat = site.data.reclamos.por_categoria.first.total %}
  {% for c in site.data.reclamos.por_categoria limit: 12 %}
  <div class="dash-bar">
    <span class="dash-bar-label" title="{{ c.nombre }}">{{ c.nombre }}</span>
    <div class="dash-bar-track"><div class="dash-bar-fill" style="width: {{ c.total | times: 100.0 | divided_by: max_cat | round: 0 }}%"></div></div>
    <span class="dash-bar-value">{{ c.total }}</span>
  </div>
  {% endfor %}
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Top 12 — dependencia responsable</h2>
  {% assign max_dep = site.data.reclamos.por_dependencia.first.total %}
  {% for d in site.data.reclamos.por_dependencia limit: 12 %}
  <div class="dash-bar">
    <span class="dash-bar-label" title="{{ d.nombre }}">{{ d.nombre }}</span>
    <div class="dash-bar-track"><div class="dash-bar-fill" style="width: {{ d.total | times: 100.0 | divided_by: max_dep | round: 0 }}%"></div></div>
    <span class="dash-bar-value">{{ d.total }}</span>
  </div>
  {% endfor %}
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Top 12 — barrios</h2>
  {% assign max_bar = site.data.reclamos.por_barrio.first.total %}
  {% for b in site.data.reclamos.por_barrio limit: 12 %}
  <div class="dash-bar">
    <span class="dash-bar-label" title="{{ b.nombre }}">{{ b.nombre }}</span>
    <div class="dash-bar-track"><div class="dash-bar-fill" style="width: {{ b.total | times: 100.0 | divided_by: max_bar | round: 0 }}%"></div></div>
    <span class="dash-bar-value">{{ b.total }}</span>
  </div>
  {% endfor %}
  <p class="dash-disclaimer">Cobertura parcial: 2023 no registra barrio; 2024 mezcla barrio con dirección. El ranking se apoya sobre todo en 2025–2026.</p>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Evolución mensual</h2>
  <div class="table-wrap">
    <table class="dash-table">
      <thead><tr><th>Mes</th><th>Pendientes</th><th>Finalizados</th><th>Total</th></tr></thead>
      <tbody>
      {% for m in site.data.reclamos.por_mes %}
        <tr><td>{{ m.mes }}</td><td>{{ m.pendientes }}</td><td>{{ m.finalizados }}</td><td>{{ m.total }}</td></tr>
      {% endfor %}
      </tbody>
    </table>
  </div>
</section>

<div class="dash-note">
  <strong>Nota de método:</strong> los estados se infieren de la hoja "PENDIENTES"/"FINALIZADOS" de cada archivo anual. Desde 2025 la columna "Estado" también registra reclamos <em>anulados</em> y registros de <em>prueba</em>. Los nombres de dependencias y tipos se normalizaron (sin acentos, mayúsculas) para agrupar variantes.
</div>

<p class="dash-disclaimer">Datos agregados a {{ site.data.reclamos._meta.sincronizado }}. Sin datos personales. Descargá el dataset en <a href="https://datospublicos.muchotexto.net/datos/reclamos.json" rel="noopener noreferrer" target="_blank">datospublicos.muchotexto.net/datos/reclamos.json</a>.</p>

</div>
</div>
