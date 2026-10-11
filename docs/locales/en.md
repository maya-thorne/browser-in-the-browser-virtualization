# Browser-in-the-Browser (BITB) DOM Virtualization & Forensic Engine

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/locales/en/banner.svg" alt="Browser-in-the-Browser Virtualization Hero Banner" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Client-Side DOM Virtualization • Chromium --app UI Stripping • Heuristic Detection Engine • Defense Architecture</strong>
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

## 📌 Executive Overview

**Browser-in-the-Browser (BITB)** is an advanced web-based client-side UI spoofing technique that virtualizes a fake operating system popup window inside a webpage's Document Object Model (DOM). By replicating the native title bar, window controls, and synthetic address bar (Omnibox) with trusted domain text and SSL padlock icons, BITB bypasses visual URL inspection.

---

## 🔬 Core Whitepapers & Technical Documentation

<details open>
<summary><b>Core Whitepapers & Technical Documentation</b></summary>
<br>

<table width="100%">
  <thead>
    <tr>
      <th width="6%" align="center">#</th>
      <th width="30%" align="left">📄 Document / Whitepaper</th>
      <th width="54%" align="left">🔬 Core Scope & Forensic Coverage</th>
      <th width="10%" align="center">📦 Format</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>1</strong></td>
      <td>
        🔬 <strong><a href="../whitepapers/BITB_DOM_VIRTUALIZATION_AND_CODE_TEARDOWN.md">BITB DOM Virtualization</a></strong><br>
        <code>BITB_DOM_<wbr>VIRTUALIZATION_<wbr>AND_CODE_TEARDOWN.md</code>
      </td>
      <td>
        mr.d0x BITB Framework Dissection: Line-by-line teardown of DOM structure, CSS stacking context elevation (z-index: 9999), draggable coordinate physics (mousedown ➔ mousemove), and iframe credential embedding.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>2</strong></td>
      <td>
        ⚙️ <strong><a href="../whitepapers/CHROMIUM_APP_MODE_INTERFACE_SPOOFING.md">Chromium --app Forensics</a></strong><br>
        <code>CHROMIUM_APP_<wbr>MODE_INTERFACE_<wbr>SPOOFING.md</code>
      </td>
      <td>
        UI Stripping & LNK Masquerading: Mechanics of the --app flag, total Omnibox and tab strip elimination, weaponized desktop shortcut structures, and Office/Teams masquerading telemetry.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>3</strong></td>
      <td>
        🛡️ <strong><a href="../whitepapers/DEFENSE_AND_DETECTION_ENGINEERING.md">Defense & Detection Matrix</a></strong><br>
        <code>DEFENSE_AND_<wbr>DETECTION_<wbr>ENGINEERING.md</code>
      </td>
      <td>
        4-Tier Enterprise Defense-in-Depth: Content-Security-Policy: frame-ancestors 'none', JavaScript frame-busting traps, DOM MutationObserver heuristics, and Sysmon/Sigma telemetry rulesets.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
  </tbody>
</table>
</details>

---

## 🖥️ Live Terminal Demonstration

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/diagrams/bitb_forensics_terminal_demo.svg" alt="BITB Forensics Terminal Demo" width="100%" />
  </a>
</p>

---

## 📐 Systems Topology & Architecture Diagrams

<details open>
<summary><b>Systems Topology & Architecture Diagrams</b></summary>
<br>

### 1. DOM Virtualization Hierarchy
<p align="center">
  <img src="../assets/diagrams/bitb_dom_architecture.svg" alt="BITB DOM Architecture" width="100%" />
</p>

### 2. Chromium --app Execution Pipeline
<p align="center">
  <img src="../assets/diagrams/chromium_app_mode_flow.svg" alt="Chromium App Mode Flow" width="100%" />
</p>

### 3. Multi-Tier Defense Topology
<p align="center">
  <img src="../assets/diagrams/defense_and_detection_matrix.svg" alt="Defense Matrix" width="100%" />
</p>
</details>

---

## ⚡ Quickstart & Tool Usage

<details open>
<summary><b>Quickstart & Tool Usage</b></summary>
<br>

```bash
# 1. Run static heuristic scanner on target web application
python src/bitb_detector.py --path references/bitb_templates/windows_chrome_dark/index.html

# 2. Run automated HTTP frame security auditor
python src/frame_security_auditor.py --file references/bitb_templates/windows_chrome_dark/index.html

# 3. Execute full unit test suite
python -m unittest discover -s tests -p "test_*.py"
```
</details>

---

## 📜 License & Research Notice

Distributed under the **[Maya Thorne Systems & Security Research License (MT-SRL)](../../LICENSE)**.  
Published strictly for dual-use cybersecurity research, browser architecture analysis, and defensive engineering.
