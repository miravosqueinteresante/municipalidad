---
layout: page
title: "Reclamos ciudadanos de Asunción"
permalink: /
description: "Análisis y datos públicos de los reclamos y denuncias que recibe la Municipalidad de Asunción. Dashboard interactivo e informes a partir de datos anonimizados."
---

{% assign k = site.data.reclamos.kpis %}
{% assign m = site.data.reclamos._meta %}

<p class="page-description">
  Entre 2023 y 2026 la Municipalidad de Asunción registró <strong>{{ k.total | default: 0 }} reclamos ciudadanos</strong> — desde podas de árboles y baches hasta ruidos molestos y vertederos clandestinos. Este sitio los abre al público: <strong>qué se reclama, dónde y quién lo atiende</strong>, con datos verificables y sin datos personales.
</p>

<section class="home-section">
  <h2 class="section-title">Los números clave</h2>
  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-value">{{ k.total | default: 0 }}</div>
      <div class="kpi-label">Reclamos totales</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">{{ k.tasa_resolucion | default: 0 }}%</div>
      <div class="kpi-label">Tasa de resolución</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value kpi-value--sm">{{ k.categoria_top | default: "—" }}</div>
      <div class="kpi-label">Reclamo más frecuente</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value kpi-value--sm">{{ k.dependencia_top | default: "—" }}</div>
      <div class="kpi-label">Dependencia más solicitada</div>
    </div>
  </div>
</section>

<section class="home-section">
  <h2 class="section-title">Explorá</h2>
  <div class="explore-grid">
    <a href="{{ '/dashboard/' | relative_url }}" class="explore-card">
      <span class="explore-title">Dashboard interactivo</span>
      <span class="explore-desc">Volumen por año, tipos, dependencias y barrios, con gráficos y tablas.</span>
      <span class="explore-arrow" aria-hidden="true">→</span>
    </a>
    <a href="{{ '/informe/' | relative_url }}" class="explore-card">
      <span class="explore-title">Informe público</span>
      <span class="explore-desc">Lectura de los datos: qué revelan y qué no se sabe.</span>
      <span class="explore-arrow" aria-hidden="true">→</span>
    </a>
    <a href="https://datospublicos.muchotexto.net/datos/reclamos.json" target="_blank" rel="noopener noreferrer" class="explore-card">
      <span class="explore-title">Datos abiertos</span>
      <span class="explore-desc">Dataset agregado (JSON) con trazabilidad de la fuente.</span>
      <span class="explore-arrow" aria-hidden="true">↗</span>
    </a>
  </div>
</section>

<section class="home-section">
  <h2 class="section-title">De dónde salen estos datos</h2>
  <div class="source-note">
    <p>
      Los registros provienen del <strong>Departamento de Atención al Ciudadano</strong> de la Municipalidad de Asunción, entregados como respuesta a un pedido de acceso a la información pública (<strong>ID 106387</strong>, Ley 5282/2014, <strong>Memo D.A.C. N.º 34/2026</strong>). Son datos <strong>anonimizados</strong>: sin nombres, cédulas, teléfonos ni domicilios de los reclamantes. Cubren el período {{ m.periodo }} (fecha de corte {{ m.fecha_corte }}) y suman {{ m.registros }} registros agregados.
    </p>
    <p>
      Este proyecto es parte del ecosistema <a href="https://muchotexto.net/" target="_blank" rel="noopener noreferrer">muchotexto.net</a> y de <a href="https://datospublicos.muchotexto.net/" target="_blank" rel="noopener noreferrer">MuchoTexto Data</a>, la infraestructura de datos verificables sobre Paraguay.
    </p>
  </div>
</section>
