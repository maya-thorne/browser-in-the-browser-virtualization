# Browser-in-the-Browser (BITB) DOM Virtualization & Forensic Engine

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="./docs/assets/banner.svg" alt="Browser-in-the-Browser Virtualization Hero Banner" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Client-Side DOM Virtualization &bull; Chromium --app UI Stripping &bull; Heuristic Detection Engine &bull; Multi-Tier Defense Architecture</strong>
</p>

<p align="center">
  <a href="./docs/locales/en.md">English</a> &bull;
  <a href="./docs/locales/ko.md">한국어</a> &bull;
  <a href="./docs/locales/ja.md">日本語</a> &bull;
  <a href="./docs/locales/zh-CN.md">简体中文</a> &bull;
  <a href="./docs/locales/es.md">Español</a> &bull;
  <a href="./docs/locales/fr.md">Français</a> &bull;
  <a href="./docs/locales/ru.md">Русский</a> &bull;
  <a href="./docs/locales/pt-BR.md">Português</a> &bull;
  <a href="./docs/locales/de.md">Deutsch</a> &bull;
  <a href="./docs/locales/ar.md">العربية</a>
</p>

---

## 📌 Executive Overview

**Browser-in-the-Browser (BITB)** is an advanced web-based client-side UI spoofing technique that virtualizes a fake operating system popup window inside a webpage's Document Object Model (DOM). By replicating the native title bar, window controls, and synthetic address bar (Omnibox) with trusted domain text and SSL padlock icons, BITB bypasses visual URL inspection.

In tandem, Chromium's native **`--app` flag** strips 100% of the browser's Omnibox, tab strip, and extension controls, allowing malicious desktop shortcuts (`.lnk`) to masquerade as native applications (e.g., Microsoft Teams, Office 365) with custom in-DOM address bars.

This repository provides an enterprise systems architecture analysis, code-level forensic teardown, automated static heuristic scanner, defensive HTTP header auditor, and physical coordinate verification engine.

---

## 🔬 Core Whitepapers & Technical Documentation

<details open>
<summary><b>📄 View Core Whitepapers &amp; Forensic Dissection Registry (3 Papers)</b></summary>
<br>

<table width="100%">
  <thead>
    <tr>
      <th width="6%" align="center">#</th>
      <th width="30%" align="left">📄 Document / Whitepaper</th>
      <th width="54%" align="left">🔬 Core Scope &amp; Forensic Coverage</th>
      <th width="10%" align="center">📦 Format</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>1</strong></td>
      <td>
        🔬 <strong><a href="./docs/whitepapers/BITB_DOM_VIRTUALIZATION_AND_CODE_TEARDOWN.md">BITB DOM Virtualization</a></strong><br>
        <code>BITB_DOM_<wbr>VIRTUALIZATION_<wbr>AND_CODE_TEARDOWN.md</code>
      </td>
      <td>
        <strong>mr.d0x BITB Framework Dissection</strong>: Line-by-line teardown of DOM structure, CSS stacking context elevation (<code>z-index: 9999</code>), draggable coordinate physics (<code>mousedown ➔ mousemove</code>), and iframe credential embedding.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>2</strong></td>
      <td>
        ⚙️ <strong><a href="./docs/whitepapers/CHROMIUM_APP_MODE_INTERFACE_SPOOFING.md">Chromium --app Forensics</a></strong><br>
        <code>CHROMIUM_APP_<wbr>MODE_INTERFACE_<wbr>SPOOFING.md</code>
      </td>
      <td>
        <strong>UI Stripping &amp; LNK Masquerading</strong>: Mechanics of the <code>--app</code> flag, total Omnibox and tab strip elimination, weaponized desktop shortcut structures, and Office/Teams masquerading telemetry.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>3</strong></td>
      <td>
        🛡️ <strong><a href="./docs/whitepapers/DEFENSE_AND_DETECTION_ENGINEERING.md">Defense &amp; Detection Matrix</a></strong><br>
        <code>DEFENSE_AND_<wbr>DETECTION_<wbr>ENGINEERING.md</code>
      </td>
      <td>
        <strong>4-Tier Enterprise Defense-in-Depth</strong>: <code>Content-Security-Policy: frame-ancestors 'none'</code>, JavaScript frame-busting traps, DOM MutationObserver heuristics, and Sysmon/Sigma telemetry rulesets.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
  </tbody>
</table>
</details>

---

## 🖥️ Live Forensics Terminal Demonstration

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="./docs/assets/diagrams/bitb_forensics_terminal_demo.svg" alt="BITB Forensics Terminal Demo" width="100%" />
  </a>
</p>

---

## 📐 Systems Topology & Architecture Diagrams

<details open>
<summary><b>📐 View 3 Interactive Architecture &amp; Execution Topologies</b></summary>
<br>

### 1. DOM Virtualization Hierarchy & Stacking Model
<p align="center">
  <img src="./docs/assets/diagrams/bitb_dom_architecture.svg" alt="BITB DOM Architecture" width="100%" />
</p>

### 2. Chromium `--app` Mode Interface Stripping Pipeline
<p align="center">
  <img src="./docs/assets/diagrams/chromium_app_mode_flow.svg" alt="Chromium App Mode Flow" width="100%" />
</p>

### 3. Multi-Tier Defensive Countermeasures & Detection Topology
<p align="center">
  <img src="./docs/assets/diagrams/defense_and_detection_matrix.svg" alt="Defense Matrix" width="100%" />
</p>
</details>

---

## ⚙️ Core Engineering Modules (`src/`)

<details>
<summary><b>⚙️ View Core Forensic Modules &amp; Verification Status</b></summary>
<br>

| Module Path | Primary Architecture & Forensic Responsibility | Verification Status |
| :--- | :--- | :---: |
| [`src/bitb_detector.py`](./src/bitb_detector.py) | Pure-Python static & heuristic scanner detecting synthetic titlebars, fake Omniboxes, and draggable coordinate loops. | **Verified (100%)** |
| [`src/frame_security_auditor.py`](./src/frame_security_auditor.py) | Audits web server HTTP response headers for strict CSP `frame-ancestors 'none'` and legacy `X-Frame-Options` defense. | **Verified (100%)** |
| [`src/virtual_browser_emulator.py`](./src/virtual_browser_emulator.py) | Mathematical emulator testing coordinate boundary traps, clipping anomalies, and physical multi-monitor escape limits. | **Verified (100%)** |
</details>

---

## ⚡ Quickstart & CLI Usage

<details open>
<summary><b>⚡ Quickstart &amp; Execution Commands</b></summary>
<br>

### 1. Scan Web Application for BITB Artifacts
```bash
# Scan a specific HTML/JS file
python src/bitb_detector.py --path references/bitb_templates/windows_chrome_dark/index.html

# Output machine-readable JSON forensic telemetry
python src/bitb_detector.py --path references/bitb_templates/ --json
```

### 2. Audit HTTP Headers & Anti-Framing Defense
```bash
python src/frame_security_auditor.py --file references/bitb_templates/windows_chrome_dark/index.html
```

### 3. Run Automated Unit Test Suite
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
</details>

---

## 📁 Repository Directory Structure

<details>
<summary><b>📁 View Repository Directory Tree &amp; Component Inventory</b></summary>
<br>

```
browser-in-the-browser-virtualization/
├── docs/                      # 📁 Architecture whitepapers, multilingual guides, SVG assets
│   ├── assets/                # Hero banners and high-resolution diagrams
│   │   ├── diagrams/          # Vector SVG architecture schematics
│   │   └── locales/           # Localized hero banners across 10 languages
│   ├── locales/               # 10 localized documentation guides (ko.md, ja.md, etc.)
│   └── whitepapers/           # In-depth technical engineering research papers
├── references/                # 📁 Analyzed reference templates and PoC shortcuts
│   ├── app_mode_poc/          # Chromium --app shortcut telemetry and screenshots
│   └── bitb_templates/        # 5 audited OS/browser theme templates (Windows/macOS)
├── src/                       # 📁 Core Python detection and emulation engines
│   ├── bitb_detector.py       # Heuristic static DOM analyzer
│   ├── frame_security_auditor.py # Anti-framing & CSP auditor
│   └── virtual_browser_emulator.py # Coordinate boundary mathematical emulator
├── tests/                     # 📁 Comprehensive unit tests (100% passing)
├── LICENSE                    # 📜 Maya Thorne Systems & Security Research License (MT-SRL)
└── README.md                  # 🌟 First-viewport master showcase
```
</details>

---

## 📜 License & Research Notice

Distributed under the **[Maya Thorne Systems & Security Research License (MT-SRL)](./LICENSE)**.  
Published strictly for dual-use cybersecurity research, browser architecture analysis, and defensive engineering.
