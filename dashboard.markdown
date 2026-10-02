---
layout: page
title: "Dashboard — Reclamos ciudadanos"
permalink: /dashboard/
description: "Reclamos de la Municipalidad de Asunción 2023–2026: volumen, estado, categorías, dependencias y barrios. Datos anonimizados y agregados."
last_modified_at: 2026-10-02
---

<div class="dash">

<p class="dash-eyebrow"><span class="dash-dot"></span>Datos verificados · {{ site.data.reclamos._meta.periodo }}</p>

<p class="dash-intro">Todos los reclamos registrados por el Departamento de Atención al Ciudadano de la Municipalidad de Asunción entre 2023 y 2026. Cifras agregadas y anonimizadas, sin registros individuales. Usá los controles de cada gráfico para <strong>filtrar, ordenar y buscar</strong>. Fuente: <a href="https://datospublicos.muchotexto.net/datos/reclamos.json" rel="noopener noreferrer" target="_blank">datos abiertos</a> (pedido ID 106387, Ley 5282/2014 · Memo D.A.C. N.º 34/2026). Proyecto independiente, no oficial.</p>

{% assign k = site.data.reclamos.kpis %}
<div class="dash-kpis">
  <div class="dash-kpi"><div class="dash-kpi-value">{{ k.total | default: 0 }}</div><div class="dash-kpi-label">Reclamos totales</div><div class="dash-kpi-note">2023–2026</div></div>
  <div class="dash-kpi"><div class="dash-kpi-value">{{ k.pendientes | default: 0 }}</div><div class="dash-kpi-label">Pendientes</div><div class="dash-kpi-note">sin cerrar</div></div>
  <div class="dash-kpi"><div class="dash-kpi-value">{{ k.finalizados | default: 0 }}</div><div class="dash-kpi-label">Finalizados</div><div class="dash-kpi-note">cerrados</div></div>
  <div class="dash-kpi"><div class="dash-kpi-value">{{ k.tasa_resolucion | default: 0 }}%</div><div class="dash-kpi-label">Tasa de resolución</div><div class="dash-kpi-note">finalizados / total</div></div>
</div>

<section class="dash-section">
  <h2 class="dash-section-title">Reclamos por año</h2>
  <div id="bars-anio"></div>
  <p class="dash-disclaimer">Pendientes + finalizados por año de registro. 2026 incluye hasta septiembre (fecha de la respuesta al pedido).</p>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Tipos de reclamo</h2>
  <div id="bars-categoria"></div>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Dependencia responsable</h2>
  <div id="bars-dependencia"></div>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Barrios</h2>
  <p class="dash-disclaimer">Cobertura parcial: 2023 no registra barrio; 2024 mezcla barrio con dirección. Conteos menores a 5 se omiten.</p>
  <div id="bars-barrio"></div>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Qué se reclama en cada barrio</h2>
  <p class="dash-disclaimer">Seleccioná un barrio para ver sus tipos de reclamo más frecuentes.</p>
  <div class="dash-controls">
    <label>Barrio <select id="barrio-select"></select></label>
  </div>
  <div id="bars-barrio-cat"></div>
</section>

<section class="dash-section">
  <h2 class="dash-section-title">Evolución mensual</h2>
  <p class="dash-disclaimer">Total de reclamos por mes. Pasá el mouse sobre una celda para ver el detalle.</p>
  <div class="table-wrap"><div id="meses-heatmap"></div></div>
</section>

<div class="dash-note">
  <strong>Nota de método:</strong> los estados se infieren de la hoja "PENDIENTES"/"FINALIZADOS" de cada archivo anual. Desde 2025 la columna "Estado" también registra reclamos <em>anulados</em> y registros de <em>prueba</em>. Los nombres de dependencias y tipos se normalizaron (sin acentos, mayúsculas) para agrupar variantes.
</div>

<p class="dash-disclaimer">Datos agregados a {{ site.data.reclamos._meta.sincronizado }}. Sin datos personales. Descargá el dataset en <a href="https://datospublicos.muchotexto.net/datos/reclamos.json" rel="noopener noreferrer" target="_blank">datospublicos.muchotexto.net/datos/reclamos.json</a>.</p>

</div>

<script>
(function () {
  var DATA = {{ site.data.reclamos | jsonify }};
  var fmt = new Intl.NumberFormat('es-PY');
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
    });
  }

  function renderBars(list, opts) {
    var host = document.getElementById(opts.id);
    var state = { top: 10, sort: 'desc', q: '' };
    var total = list.reduce(function (s, i) { return s + i.total; }, 0);

    var controlsEl = document.createElement('div');
    controlsEl.className = 'dash-controls';
    var countEl = document.createElement('div');
    countEl.className = 'dash-count';
    var barsEl = document.createElement('div');
    barsEl.className = 'dash-bars';

    function option(sel, val, text) {
      var o = document.createElement('option');
      o.value = val; o.textContent = text;
      sel.appendChild(o);
    }

    if (!opts.noControls) {
      var topSel = document.createElement('select');
      option(topSel, '5', 'Top 5');
      option(topSel, '10', 'Top 10');
      option(topSel, '25', 'Top 25');
      option(topSel, 'all', 'Todos');
      topSel.value = '10';
      topSel.addEventListener('change', function () { state.top = topSel.value; draw(); });
      var topLabel = document.createElement('label');
      topLabel.appendChild(document.createTextNode('Mostrar'));
      topLabel.appendChild(topSel);

      var sortSel = document.createElement('select');
      option(sortSel, 'desc', 'Mayor a menor');
      option(sortSel, 'asc', 'Menor a mayor');
      option(sortSel, 'name', 'A → Z');
      sortSel.addEventListener('change', function () { state.sort = sortSel.value; draw(); });
      var sortLabel = document.createElement('label');
      sortLabel.appendChild(document.createTextNode('Orden'));
      sortLabel.appendChild(sortSel);

      controlsEl.appendChild(topLabel);
      controlsEl.appendChild(sortLabel);

      if (opts.searchable) {
        var q = document.createElement('input');
        q.type = 'search';
        q.placeholder = 'Filtrar por nombre…';
        q.setAttribute('aria-label', 'Filtrar por nombre');
        q.addEventListener('input', function () { state.q = q.value; draw(); });
        controlsEl.appendChild(q);
      }
    }

    host.innerHTML = '';
    host.appendChild(controlsEl);
    host.appendChild(countEl);
    host.appendChild(barsEl);

    function draw() {
      var items = list.slice();
      if (opts.searchable && state.q) {
        var needle = state.q.toLowerCase();
        items = items.filter(function (i) { return i.nombre.toLowerCase().indexOf(needle) !== -1; });
      }
      if (state.sort === 'asc') items.sort(function (a, b) { return a.total - b.total; });
      else if (state.sort === 'name') items.sort(function (a, b) { return a.nombre.localeCompare(b.nombre, 'es'); });
      else items.sort(function (a, b) { return b.total - a.total; });

      var shown = items;
      if (state.top !== 'all') shown = items.slice(0, parseInt(state.top, 10));
      var max = Math.max.apply(null, shown.map(function (i) { return i.total; }).concat([1]));

      countEl.textContent = shown.length + ' de ' + list.length + (opts.searchable && state.q ? ' (filtrado)' : '');

      if (!shown.length) {
        barsEl.innerHTML = '<p class="dash-empty">Sin resultados para el filtro.</p>';
        return;
      }
      barsEl.innerHTML = shown.map(function (i) {
        var pct = (i.total / total * 100).toFixed(1);
        var w = (i.total / max * 100).toFixed(1);
        return '<div class="dash-bar" data-tip="' + esc(fmt.format(i.total) + ' reclamos · ' + pct + '% del total') + '">' +
          '<span class="dash-bar-label">' + esc(i.nombre) + '</span>' +
          '<div class="dash-bar-track"><div class="dash-bar-fill" style="width:' + w + '%"></div></div>' +
          '<span class="dash-bar-value">' + fmt.format(i.total) + '</span>' +
          '</div>';
      }).join('');
    }

    draw();
  }

  renderBars(DATA.por_categoria, { id: 'bars-categoria', searchable: true });
  renderBars(DATA.por_dependencia, { id: 'bars-dependencia', searchable: true });
  renderBars(DATA.por_barrio, { id: 'bars-barrio', searchable: true });
  renderBars(DATA.por_anio.map(function (a) { return { nombre: String(a.anio), total: a.total }; }), { id: 'bars-anio', noControls: true });
  renderBarrioCategoria();
  renderHeatmap();

  function renderBarrioCategoria() {
    var sel = document.getElementById('barrio-select');
    var out = document.getElementById('bars-barrio-cat');
    var data = DATA.por_barrio_categoria || [];
    if (!data.length) { out.innerHTML = '<p class="dash-empty">Sin datos por barrio.</p>'; return; }

    data.forEach(function (b) {
      var o = document.createElement('option');
      o.value = b.barrio;
      o.textContent = b.barrio + ' (' + fmt.format(b.total) + ')';
      sel.appendChild(o);
    });

    function drawBarrio() {
      var b = null;
      for (var i = 0; i < data.length; i++) { if (data[i].barrio === sel.value) { b = data[i]; break; } }
      if (!b) { out.innerHTML = ''; return; }
      var max = Math.max.apply(null, b.top.map(function (t) { return t.total; }).concat([1]));
      out.innerHTML = b.top.map(function (t) {
        var w = (t.total / max * 100).toFixed(1);
        var pct = (t.total / b.total * 100).toFixed(1);
        return '<div class="dash-bar" data-tip="' + esc(fmt.format(t.total) + ' reclamos · ' + pct + '% del barrio') + '">' +
          '<span class="dash-bar-label">' + esc(t.nombre) + '</span>' +
          '<div class="dash-bar-track"><div class="dash-bar-fill" style="width:' + w + '%"></div></div>' +
          '<span class="dash-bar-value">' + fmt.format(t.total) + '</span>' +
          '</div>';
      }).join('');
    }

    sel.addEventListener('change', drawBarrio);
    drawBarrio();
  }

  function renderHeatmap() {
    var el = document.getElementById('meses-heatmap');
    if (!el) return;
    var byMonth = {};
    DATA.por_mes.forEach(function (m) { byMonth[m.mes] = m.total; });
    var years = [2023, 2024, 2025, 2026];
    var months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
    var max = Math.max.apply(null, DATA.por_mes.map(function (m) { return m.total; }).concat([1]));

    var html = '<div class="mes-grid">';
    html += '<div class="mes-year"></div>';
    months.forEach(function (mm) { html += '<div class="mes-head">' + mm + '</div>'; });
    years.forEach(function (y) {
      html += '<div class="mes-year">' + y + '</div>';
      for (var mi = 1; mi <= 12; mi++) {
        var key = y + '-' + (mi < 10 ? '0' + mi : mi);
        var v = byMonth[key];
        if (v == null) {
          html += '<div class="mes-cell mes-empty" aria-hidden="true"></div>';
        } else {
          var a = (0.15 + 0.85 * (v / max)).toFixed(2);
          html += '<div class="mes-cell" style="background:rgba(92,201,138,' + a + ')" title="' + key + ': ' + fmt.format(v) + ' reclamos">' + fmt.format(v) + '</div>';
        }
      }
    });
    html += '</div>';
    el.innerHTML = html;
  }
})();
</script>
