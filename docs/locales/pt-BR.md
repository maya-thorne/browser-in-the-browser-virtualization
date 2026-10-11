# Browser-in-the-Browser (BITB) Virtualização DOM e Motor Forense

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/locales/pt-BR/banner.svg" alt="Browser-in-the-Browser Virtualization Hero Banner" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Virtualização DOM no Cliente • Supressão de UI no Chromium --app • Motor Heurístico • Arquitetura de Defesa</strong>
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

## 📌 Visão Geral (Executive Overview)

**Browser-in-the-Browser (BITB)** é uma técnica avançada de spoofing de interface que virtualiza uma janela pop-up do sistema operacional dentro do DOM, burlando a verificação visual com barra de endereços falsa e cadeado SSL.

---

## 🔬 Artigos Técnicos e Documentação

<details open>
<summary><b>Artigos Técnicos e Documentação</b></summary>
<br>

<table width="100%">
  <thead>
    <tr>
      <th width="6%" align="center">#</th>
      <th width="30%" align="left">📄 Documento / Artigo Técnico</th>
      <th width="54%" align="left">🔬 Escopo Principal e Cobertura Forense</th>
      <th width="10%" align="center">📦 Formato</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>1</strong></td>
      <td>
        🔬 <strong><a href="../whitepapers/BITB_DOM_VIRTUALIZATION_AND_CODE_TEARDOWN.md">Virtualização DOM BITB</a></strong><br>
        <code>BITB_DOM_<wbr>VIRTUALIZATION_<wbr>AND_CODE_TEARDOWN.md</code>
      </td>
      <td>
        Desmontagem do framework mr.d0x: estrutura DOM, empilhamento CSS (z-index: 9999), física de coordenadas e incorporação de iframe.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>2</strong></td>
      <td>
        ⚙️ <strong><a href="../whitepapers/CHROMIUM_APP_MODE_INTERFACE_SPOOFING.md">Forense do Modo Chromium --app</a></strong><br>
        <code>CHROMIUM_APP_<wbr>MODE_INTERFACE_<wbr>SPOOFING.md</code>
      </td>
      <td>
        Remoção de UI e camuflagem de LNK: mecanismo do sinalizador --app, eliminação do Omnibox e telemetria de falsificação do Teams/Office.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>3</strong></td>
      <td>
        🛡️ <strong><a href="../whitepapers/DEFENSE_AND_DETECTION_ENGINEERING.md">Matriz de Defesa e Detecção</a></strong><br>
        <code>DEFENSE_AND_<wbr>DETECTION_<wbr>ENGINEERING.md</code>
      </td>
      <td>
        Defesa em profundidade corporativa em 4 níveis: Content-Security-Policy: frame-ancestors 'none', armadilhas JS e regras Sysmon/Sigma.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
  </tbody>
</table>
</details>

---

## 🖥️ Demonstração no Terminal ao Vivo

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/diagrams/bitb_forensics_terminal_demo.svg" alt="BITB Forensics Terminal Demo" width="100%" />
  </a>
</p>

---

## 📐 Topologia do Sistema e Diagramas

<details open>
<summary><b>Topologia do Sistema e Diagramas</b></summary>
<br>

### 1. Hierarquia de Virtualização DOM
<p align="center">
  <img src="../assets/diagrams/bitb_dom_architecture.svg" alt="BITB DOM Architecture" width="100%" />
</p>

### 2. Fluxo de Execução do Chromium --app
<p align="center">
  <img src="../assets/diagrams/chromium_app_mode_flow.svg" alt="Chromium App Mode Flow" width="100%" />
</p>

### 3. Topologia de Defesa Multinível
<p align="center">
  <img src="../assets/diagrams/defense_and_detection_matrix.svg" alt="Defense Matrix" width="100%" />
</p>
</details>

---

## ⚡ Início Rápido

<details open>
<summary><b>Início Rápido</b></summary>
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

## 📜 Licença e Aviso de Pesquisa

Distributed under the **[Maya Thorne Systems & Security Research License (MT-SRL)](../../LICENSE)**.  
Published strictly for dual-use cybersecurity research, browser architecture analysis, and defensive engineering.
