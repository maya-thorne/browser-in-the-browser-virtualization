# Browser-in-the-Browser (BITB) Virtualisation DOM et Moteur Forensique

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/locales/fr/banner.svg" alt="Browser-in-the-Browser Virtualization Hero Banner" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Virtualisation DOM Côté Client • Suppression de l'UI Chromium --app • Moteur Heuristique • Architecture Défensive</strong>
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

## 📌 Aperçu Exécutif (Executive Overview)

**Browser-in-the-Browser (BITB)** est une technique avancée d'usurpation d'interface utilisateur qui virtualise une fausse fenêtre popup au sein du DOM, contournant l'inspection visuelle grâce à une fausse barre d'adresse et un cadenas SSL.

---

## 🔬 Livres Blancs Principaux et Documentation Technique

<details open>
<summary><b>Livres Blancs Principaux et Documentation Technique</b></summary>
<br>

<table width="100%">
  <thead>
    <tr>
      <th width="6%" align="center">#</th>
      <th width="30%" align="left">📄 Document / Livre Blanc</th>
      <th width="54%" align="left">🔬 Portée Principale et Couverture Forensique</th>
      <th width="10%" align="center">📦 Format</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>1</strong></td>
      <td>
        🔬 <strong><a href="../whitepapers/BITB_DOM_VIRTUALIZATION_AND_CODE_TEARDOWN.md">Virtualisation DOM BITB</a></strong><br>
        <code>BITB_DOM_<wbr>VIRTUALIZATION_<wbr>AND_CODE_TEARDOWN.md</code>
      </td>
      <td>
        Analyse du framework mr.d0x: structure DOM, contexte d'empilement CSS (z-index: 9999), physique des coordonnées déplaçables et intégration iframe.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>2</strong></td>
      <td>
        ⚙️ <strong><a href="../whitepapers/CHROMIUM_APP_MODE_INTERFACE_SPOOFING.md">Forensique du Mode Chromium --app</a></strong><br>
        <code>CHROMIUM_APP_<wbr>MODE_INTERFACE_<wbr>SPOOFING.md</code>
      </td>
      <td>
        Suppression de l'UI et usurpation via raccourcis LNK: fonctionnement du drapeau --app, suppression totale de l'Omnibox et télémétrie Teams/Office.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>3</strong></td>
      <td>
        🛡️ <strong><a href="../whitepapers/DEFENSE_AND_DETECTION_ENGINEERING.md">Matrice de Défense et Détection</a></strong><br>
        <code>DEFENSE_AND_<wbr>DETECTION_<wbr>ENGINEERING.md</code>
      </td>
      <td>
        Défense en profondeur à 4 niveaux: Content-Security-Policy: frame-ancestors 'none', pièges JavaScript et règles de détection Sysmon/Sigma.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
  </tbody>
</table>
</details>

---

## 🖥️ Démonstration Terminal en Direct

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/diagrams/bitb_forensics_terminal_demo.svg" alt="BITB Forensics Terminal Demo" width="100%" />
  </a>
</p>

---

## 📐 Topologie du Système et Diagrammes

<details open>
<summary><b>Topologie du Système et Diagrammes</b></summary>
<br>

### 1. Hiérarchie de Virtualisation DOM
<p align="center">
  <img src="../assets/diagrams/bitb_dom_architecture.svg" alt="BITB DOM Architecture" width="100%" />
</p>

### 2. Pipeline d'Exécution Chromium --app
<p align="center">
  <img src="../assets/diagrams/chromium_app_mode_flow.svg" alt="Chromium App Mode Flow" width="100%" />
</p>

### 3. Topologie de Défense Multi-Niveaux
<p align="center">
  <img src="../assets/diagrams/defense_and_detection_matrix.svg" alt="Defense Matrix" width="100%" />
</p>
</details>

---

## ⚡ Démarrage Rapide et Utilisation

<details open>
<summary><b>Démarrage Rapide et Utilisation</b></summary>
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

## 📜 Licence et Avis de Recherche

Distributed under the **[Maya Thorne Systems & Security Research License (MT-SRL)](../../LICENSE)**.  
Published strictly for dual-use cybersecurity research, browser architecture analysis, and defensive engineering.
