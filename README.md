<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" x2="1">
      <stop offset="0%" stop-color="#080e14"/>
      <stop offset="100%" stop-color="#02080d"/>
    </linearGradient>
    <linearGradient id="head" x1="0" x2="0" y1="0" y2="1">
      <stop offset="0%" stop-color="#1b2430"/>
      <stop offset="100%" stop-color="#101b27"/>
    </linearGradient>
  </defs>

  <rect width="1600" height="900" fill="url(#bg)"/>
  <text x="180" y="120" fill="#f8fafc" font-family="Segoe UI, sans-serif" font-size="58" font-weight="800">Error metrics</text>

  <rect x="150" y="170" width="1280" height="360" rx="10" fill="#0d1722" stroke="#2a3a4b"/>
  <rect x="150" y="170" width="1280" height="54" fill="url(#head)"/>

  <g font-family="Segoe UI, sans-serif" font-size="22" fill="#dfeaf5">
    <text x="220" y="205">Model</text>
    <text x="495" y="205">MAE window</text>
    <text x="680" y="205">RMSE window</text>
    <text x="900" y="205">MAPE window (%)</text>
    <text x="1110" y="205">MAE full test</text>
    <text x="1270" y="205">RMSE full test</text>
    <text x="1450" y="205">MAPE full test (%)</text>
  </g>

  <g font-family="Segoe UI, sans-serif" font-size="20" fill="#f8fafc">
    <text x="220" y="280">Baseline: same hour last week</text>
    <text x="520" y="280">1220.39</text>
    <text x="705" y="280">1486.18</text>
    <text x="930" y="280">9.81</text>
    <text x="1125" y="280">1163.47</text>
    <text x="1295" y="280">1745.25</text>
    <text x="1460" y="280">9.89</text>

    <text x="220" y="335">XGBoost (no weather)</text>
    <text x="520" y="335">462.73</text>
    <text x="705" y="335">561.57</text>
    <text x="930" y="335">4.08</text>
    <text x="1125" y="335">399.86</text>
    <text x="1295" y="335">579.01</text>
    <text x="1460" y="335">3.43</text>

    <text x="220" y="390">XGBoost (with weather)</text>
    <text x="520" y="390">233.13</text>
    <text x="705" y="390">319.11</text>
    <text x="930" y="390">2.04</text>
    <text x="1125" y="390">345.63</text>
    <text x="1295" y="390">518.08</text>
    <text x="1460" y="390">2.97</text>
  </g>

  <text x="150" y="610" fill="#dfeaf5" font-family="Segoe UI, sans-serif" font-size="28">Lower is better. "Window" covers the selected dates; "full test" covers the entire held-out period.</text>

  <rect x="150" y="660" width="290" height="72" rx="8" fill="#111c2a" stroke="#4a5c72"/>
  <text x="182" y="704" fill="#f8fafc" font-family="Segoe UI, sans-serif" font-size="30" font-weight="700">Download this window as CSV</text>
</svg>















































































































































































































































