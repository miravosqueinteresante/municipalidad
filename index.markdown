---
layout: page
title: "Reclamos ciudadanos de Asunción"
permalink: /
description: "Análisis y datos públicos de los reclamos y denuncias que recibe la Municipalidad de Asunción. Dashboard interactivo e informes a partir de datos anonimizados."
---

{% assign k = site.data.reclamos.kpis %}
{% assign m = site.data.reclamos._meta %}

<p class="page-description" style="font-size:1.05em;line-height:1.6;">
  Entre 2023 y 2026 la Municipalidad de Asunción registró <strong>{{ k.total | default: 0 }} reclamos ciudadanos</strong> — desde podas de árboles y baches hasta ruidos molestos y vertederos clandestinos. Este sitio los abre al público: <strong>qué se reclama, dónde y quién lo atiende</strong>, con datos verificables y sin datos personales.
</p>

<section style="margin:2rem 0;">
  <h2 style="margin-bottom:1rem;">Los números clave</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;">
    <div style="background:var(--code-bg-color);border:1px solid var(--border-color);border-radius:10px;padding:14px 16px;">
      <div style="font-family:var(--code-font-family);font-size:22px;font-weight:600;color:var(--oc-cyan-4);">{{ k.total | default: 0 }}</div>
      <div style="font-size:0.8em;font-weight:600;color:var(--heading-color);margin-top:4px;">Reclamos totales</div>
    </div>
    <div style="background:var(--code-bg-color);border:1px solid var(--border-color);border-radius:10px;padding:14px 16px;">
      <div style="font-family:var(--code-font-family);font-size:22px;font-weight:600;color:var(--oc-cyan-4);">{{ k.tasa_resolucion | default: 0 }}%</div>
      <div style="font-size:0.8em;font-weight:600;color:var(--heading-color);margin-top:4px;">Tasa de resolución</div>
    </div>
    <div style="background:var(--code-bg-color);border:1px solid var(--border-color);border-radius:10px;padding:14px 16px;">
      <div style="font-family:var(--code-font-family);font-size:16px;font-weight:600;color:var(--oc-cyan-4);line-height:1.2;">{{ k.categoria_top | default: "—" }}</div>
      <div style="font-size:0.8em;font-weight:600;color:var(--heading-color);margin-top:4px;">Reclamo más frecuente</div>
    </div>
    <div style="background:var(--code-bg-color);border:1px solid var(--border-color);border-radius:10px;padding:14px 16px;">
      <div style="font-family:var(--code-font-family);font-size:16px;font-weight:600;color:var(--oc-cyan-4);line-height:1.2;">{{ k.dependencia_top | default: "—" }}</div>
      <div style="font-size:0.8em;font-weight:600;color:var(--heading-color);margin-top:4px;">Dependencia más solicitada</div>
    </div>
  </div>
</section>

<section style="margin:2rem 0;">
  <h2 style="margin-bottom:1rem;">Explorá</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;">
    <a href="{{ '/dashboard/' | relative_url }}" style="background:var(--code-bg-color);border:1px solid var(--border-color);border-radius:10px;padding:18px;color:var(--heading-color);text-decoration:none;">
      <div style="font-size:1.05em;font-weight:600;margin-bottom:6px;">Dashboard interactivo</div>
      <div style="font-size:0.85em;opacity:0.7;line-height:1.5;">Volumen por año, tipos, dependencias y barrios, con gráficos y tablas.</div>
    </a>
    <a href="{{ '/informe/' | relative_url }}" style="background:var(--code-bg-color);border:1px solid var(--border-color);border-radius:10px;padding:18px;color:var(--heading-color);text-decoration:none;">
      <div style="font-size:1.05em;font-weight:600;margin-bottom:6px;">Informe público</div>
      <div style="font-size:0.85em;opacity:0.7;line-height:1.5;">Lectura de los datos: qué revelan y qué no se sabe.</div>
    </a>
    <a href="https://datospublicos.muchotexto.net/datos/reclamos.json" target="_blank" rel="noopener noreferrer" style="background:var(--code-bg-color);border:1px solid var(--border-color);border-radius:10px;padding:18px;color:var(--heading-color);text-decoration:none;">
      <div style="font-size:1.05em;font-weight:600;margin-bottom:6px;">Datos abiertos</div>
      <div style="font-size:0.85em;opacity:0.7;line-height:1.5;">Dataset agregado (JSON) con trazabilidad de la fuente.</div>
    </a>
  </div>
</section>

<section style="margin:2rem 0;">
  <h2 style="margin-bottom:1rem;">De dónde salen estos datos</h2>
  <p style="font-size:0.9em;line-height:1.7;opacity:0.85;">
    Los registros provienen del <strong>Departamento de Atención al Ciudadano</strong> de la Municipalidad de Asunción, entregados como respuesta a un pedido de acceso a la información pública (<strong>ID 106387</strong>, Ley 5282/2014). Son datos <strong>anonimizados</strong>: sin nombres, cédulas, teléfonos ni domicilios de los reclamantes. Cubren el período {{ m.periodo }} y suman {{ m.registros }} registros agregados.
  </p>
  <p style="font-size:0.9em;line-height:1.7;opacity:0.85;">
    Este proyecto es parte del ecosistema <a href="https://muchotexto.net/" target="_blank" rel="noopener noreferrer">muchotexto.net</a> y de <a href="https://datospublicos.muchotexto.net/" target="_blank" rel="noopener noreferrer">MuchoTexto Data</a>, la infraestructura de datos verificables sobre Paraguay.
  </p>
</section>
