---
layout: page
title: "Dashboard — Reclamos ciudadanos"
permalink: /dashboard/
description: "Reclamos de la Municipalidad de Asunción 2023–2026: volumen, estado, categorías, dependencias y barrios. Datos anonimizados y agregados."
last_modified_at: 2026-10-02
---

<style>
.dash-page .container { max-width: 1120px; }
.dash { font-family: var(--body-font-family); margin-bottom: var(--spacer-3); }
.dash-eyebrow { font-family: var(--code-font-family); font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--oc-cyan-4); display: flex; align-items: center; gap: 8px; margin: 0 0 var(--spacer) 0; }
.dash-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--oc-cyan-4); box-shadow: 0 0 0 3px rgba(34,184,207,0.18); animation: dash-pulse 2.4s ease-in-out infinite; }
@keyframes dash-pulse { 0%,100%{opacity:1;} 50%{opacity:0.35;} }
.dash-intro { font-size: 0.92em; line-height: 1.6; opacity: 0.85; margin: 0 0 var(--spacer-2) 0; }
.dash-kpis { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: var(--spacer-3); }
@media (min-width: 40rem) { .dash-kpis { grid-template-columns: repeat(4, 1fr); } }
.dash-kpi { background: var(--code-bg-color); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px; }
.dash-kpi-value { font-family: var(--code-font-family); font-size: 22px; font-weight: 600; color: var(--oc-cyan-4); line-height: 1.1; }
.dash-kpi-label { font-size: 0.8em; font-weight: 600; color: var(--heading-color); margin-top: 4px; }
.dash-kpi-note { font-size: 0.72em; opacity: 0.6; margin-top: 2px; }
.dash-section { margin-bottom: var(--spacer-3); }
.dash-section-title { font-size: 0.95em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.6; margin: 0 0 var(--spacer) 0; padding-bottom: var(--spacer); border-bottom: 1px solid var(--border-color); }
.dash-bar { display: grid; grid-template-columns: 190px 1fr 72px; align-items: center; gap: 12px; margin-bottom: 8px; }
@media (max-width: 40rem) { .dash-bar { grid-template-columns: 120px 1fr 56px; } }
.dash-bar-label { font-size: 0.82em; color: var(--heading-color); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.dash-bar-track { height: 16px; background: var(--oc-gray-8); border: 1px solid var(--border-color); border-radius: 4px; overflow: hidden; }
.dash-bar-fill { height: 100%; background: linear-gradient(90deg, var(--oc-cyan-6), var(--oc-cyan-4)); border-radius: 3px 0 0 3px; min-width: 2px; }
.dash-bar-value { font-family: var(--code-font-family); font-size: 0.8em; color: var(--oc-gray-3); text-align: right; }
.dash-table { width: 100%; border-collapse: collapse; font-size: 0.85em; }
.dash-table th, .dash-table td { text-align: left; padding: 6px 10px; border-bottom: 1px solid var(--border-color); }
.dash-table th { font-size: 0.78em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.55; font-weight: 600; }
.dash-table td:last-child { font-family: var(--code-font-family); color: var(--oc-cyan-4); }
.dash-note { background: rgba(34,184,207,0.06); border: 1px solid rgba(34,184,207,0.18); border-radius: 8px; padding: 12px 14px; margin-top: var(--spacer); font-size: 0.82em; line-height: 1.6; opacity: 0.85; }
.dash-disclaimer { margin-top: var(--spacer-2); font-size: 0.8em; opacity: 0.65; line-height: 1.6; }
</style>

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
  <table class="dash-table">
    <thead><tr><th>Mes</th><th>Pendientes</th><th>Finalizados</th><th>Total</th></tr></thead>
    <tbody>
    {% for m in site.data.reclamos.por_mes %}
      <tr><td>{{ m.mes }}</td><td>{{ m.pendientes }}</td><td>{{ m.finalizados }}</td><td>{{ m.total }}</td></tr>
    {% endfor %}
    </tbody>
  </table>
</section>

<div class="dash-note">
  <strong>Nota de método:</strong> los estados se infieren de la hoja "PENDIENTES"/"FINALIZADOS" de cada archivo anual. Desde 2025 la columna "Estado" también registra reclamos <em>anulados</em> y registros de <em>prueba</em>. Los nombres de dependencias y tipos se normalizaron (sin acentos, mayúsculas) para agrupar variantes.
</div>

<p class="dash-disclaimer">Datos agregados a {{ site.data.reclamos._meta.sincronizado }}. Sin datos personales. Descargá el dataset en <a href="https://datospublicos.muchotexto.net/datos/reclamos.json" rel="noopener noreferrer" target="_blank">datospublicos.muchotexto.net/datos/reclamos.json</a>.</p>

</div>
</div>
