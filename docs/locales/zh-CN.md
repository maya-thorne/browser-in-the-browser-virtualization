# Browser-in-the-Browser (BITB) DOM虚拟化与取证分析引擎

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/locales/zh-CN/banner.svg" alt="Browser-in-the-Browser Virtualization Hero Banner" width="100%" />
  </a>
</p>

<p align="center">
  <strong>客户端DOM虚拟化 • Chromium --app UI剥离 • 启发式检测引擎 • 防御体系架构</strong>
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

## 📌 概述 (Executive Overview)

**Browser-in-the-Browser (BITB)** 是一种先进的基于Web的客户端UI欺骗技术，它在网页的DOM内部虚拟化一个虚假的操作系统弹窗。通过高保真模拟原生标题栏、窗口控制按钮以及带有可信域名文本和SSL锁图标的合成地址栏（Omnibox），绕过用户的视觉URL审查。

---

## 🔬 核心白皮书与技术文档

<table width="100%">
  <thead>
    <tr>
      <th width="6%" align="center">#</th>
      <th width="30%" align="left">📄 文档 / 白皮书</th>
      <th width="54%" align="left">🔬 核心研究范围与取证覆盖</th>
      <th width="10%" align="center">📦 格式</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>1</strong></td>
      <td>
        🔬 <strong><a href="../whitepapers/BITB_DOM_VIRTUALIZATION_AND_CODE_TEARDOWN.md">BITB DOM虚拟化深入分析</a></strong><br>
        <code>BITB_DOM_<wbr>VIRTUALIZATION_<wbr>AND_CODE_TEARDOWN.md</code>
      </td>
      <td>
        mr.d0x BITB框架深度剖析: DOM层级结构、CSS堆叠上下文提升（z-index: 9999）、拖拽物理坐标引擎（mousedown ➔ mousemove）以及iframe凭证嵌入机制逐行解析。
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>2</strong></td>
      <td>
        ⚙️ <strong><a href="../whitepapers/CHROMIUM_APP_MODE_INTERFACE_SPOOFING.md">Chromium --app 模式取证</a></strong><br>
        <code>CHROMIUM_APP_<wbr>MODE_INTERFACE_<wbr>SPOOFING.md</code>
      </td>
      <td>
        UI剥离与快捷方式伪装: --app参数本质、地址栏与标签栏100%隐藏机制、武器化桌面快捷方式（.lnk）结构剖析与Teams/Office应用伪装取证。
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>3</strong></td>
      <td>
        🛡️ <strong><a href="../whitepapers/DEFENSE_AND_DETECTION_ENGINEERING.md">纵深防御与检测矩阵</a></strong><br>
        <code>DEFENSE_AND_<wbr>DETECTION_<wbr>ENGINEERING.md</code>
      </td>
      <td>
        4层企业级纵深防御体系: Content-Security-Policy: frame-ancestors 'none'、JavaScript反嵌入陷阱、DOM MutationObserver启发式检测与Sysmon/Sigma规则集。
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
  </tbody>
</table>

---

## 🖥️ 交互式终端演示

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/diagrams/bitb_forensics_terminal_demo.svg" alt="BITB Forensics Terminal Demo" width="100%" />
  </a>
</p>

---

## 📐 系统拓扑与架构图

### 1. DOM虚拟化层级架构
<p align="center">
  <img src="../assets/diagrams/bitb_dom_architecture.svg" alt="BITB DOM Architecture" width="100%" />
</p>

### 2. Chromium --app 运行流水线
<p align="center">
  <img src="../assets/diagrams/chromium_app_mode_flow.svg" alt="Chromium App Mode Flow" width="100%" />
</p>

### 3. 多层纵深防御拓扑
<p align="center">
  <img src="../assets/diagrams/defense_and_detection_matrix.svg" alt="Defense Matrix" width="100%" />
</p>

---

## ⚡ 快速入门与工具使用

```bash
# 1. Run static heuristic scanner on target web application
python src/bitb_detector.py --path references/bitb_templates/windows_chrome_dark/index.html

# 2. Run automated HTTP frame security auditor
python src/frame_security_auditor.py --file references/bitb_templates/windows_chrome_dark/index.html

# 3. Execute full unit test suite
python -m unittest discover -s tests -p "test_*.py"
```

---

## 📜 许可证与免责声明

Distributed under the **[Maya Thorne Systems & Security Research License (MT-SRL)](../../LICENSE)**.  
Published strictly for dual-use cybersecurity research, browser architecture analysis, and defensive engineering.
