# Browser-in-the-Browser (BITB) DOM-Virtualisierung & Forensik-Engine

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/locales/de/banner.svg" alt="Browser-in-the-Browser Virtualization Hero Banner" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Client-seitige DOM-Virtualisierung • Chromium --app UI-Entfernung • Heuristische Erkennung • Abwehrarchitektur</strong>
</p>

<p align="center">
  <a href="./en.md">English</a> &bull;
  <a href="./ko.md">한국어</a> &bull;
  <a href="./ja.md">日本語</a> &bull;
  <a href="./zh-CN.md">简体中文</a> &bull;
  <a href="./es.md">Español</a> &bull;
  <a href="./fr.md">Français</a> &bull;
  <a href="./ru.md">Русский</a> &bull;
  <a href="./pt-BR.md">Português</a> &bull;
  <a href="./de.md">Deutsch</a> &bull;
  <a href="./ar.md">العربية</a>
</p>

---

## 📌 Überblick (Executive Overview)

**Browser-in-the-Browser (BITB)** ist eine fortschrittliche UI-Spoofing-Technik, die ein gefälschtes Betriebssystem-Popup-Fenster im DOM einer Webseite virtualisiert und visuelle Sicherheitsprüfungen umgeht.

---

## 🔬 Zentrale Whitepaper & Technische Dokumentation

<table width="100%">
  <thead>
    <tr>
      <th width="6%" align="center">#</th>
      <th width="30%" align="left">📄 Dokument / Whitepaper</th>
      <th width="54%" align="left">🔬 Kernbereich & Forensische Abdeckung</th>
      <th width="10%" align="center">📦 Format</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>1</strong></td>
      <td>
        🔬 <strong><a href="../whitepapers/BITB_DOM_VIRTUALIZATION_AND_CODE_TEARDOWN.md">BITB DOM-Virtualisierung</a></strong><br>
        <code>BITB_DOM_<wbr>VIRTUALIZATION_<wbr>AND_CODE_TEARDOWN.md</code>
      </td>
      <td>
        Zerlegung des mr.d0x Frameworks: DOM-Struktur, CSS-Stapelebenen (z-index: 9999), ziehbare Koordinatenphysik und Iframe-Einbettung.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>2</strong></td>
      <td>
        ⚙️ <strong><a href="../whitepapers/CHROMIUM_APP_MODE_INTERFACE_SPOOFING.md">Chromium --app Forensik</a></strong><br>
        <code>CHROMIUM_APP_<wbr>MODE_INTERFACE_<wbr>SPOOFING.md</code>
      </td>
      <td>
        UI-Entfernung und LNK-Verschleierung: Mechanik des --app Flags, vollständige Ausblendung der Adressleiste und Teams/Office-Spoofing-Telemetrie.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>3</strong></td>
      <td>
        🛡️ <strong><a href="../whitepapers/DEFENSE_AND_DETECTION_ENGINEERING.md">Abwehr- und Erkennungsmatrix</a></strong><br>
        <code>DEFENSE_AND_<wbr>DETECTION_<wbr>ENGINEERING.md</code>
      </td>
      <td>
        4-stufige Enterprise Defense-in-Depth: Content-Security-Policy: frame-ancestors 'none', JavaScript Frame-Buster und Sysmon/Sigma-Regeln.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
  </tbody>
</table>

---

## 🖥️ Live-Terminal-Demonstration

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/diagrams/bitb_forensics_terminal_demo.svg" alt="BITB Forensics Terminal Demo" width="100%" />
  </a>
</p>

---

## 📐 Systemtopologie & Architekturdiagramme

### 1. DOM-Virtualisierungshierarchie
<p align="center">
  <img src="../assets/diagrams/bitb_dom_architecture.svg" alt="BITB DOM Architecture" width="100%" />
</p>

### 2. Chromium --app Ausführungspipeline
<p align="center">
  <img src="../assets/diagrams/chromium_app_mode_flow.svg" alt="Chromium App Mode Flow" width="100%" />
</p>

### 3. Mehrstufige Abwehrtopologie
<p align="center">
  <img src="../assets/diagrams/defense_and_detection_matrix.svg" alt="Defense Matrix" width="100%" />
</p>

---

## ⚡ Schnellstart

```bash
# 1. Run static heuristic scanner on target web application
python src/bitb_detector.py --path references/bitb_templates/windows_chrome_dark/index.html

# 2. Run automated HTTP frame security auditor
python src/frame_security_auditor.py --file references/bitb_templates/windows_chrome_dark/index.html

# 3. Execute full unit test suite
python -m unittest discover -s tests -p "test_*.py"
```

---

## 📜 Lizenz & Forschungshinweis

Distributed under the **[Maya Thorne Systems & Security Research License (MT-SRL)](../../LICENSE)**.  
Published strictly for dual-use cybersecurity research, browser architecture analysis, and defensive engineering.
