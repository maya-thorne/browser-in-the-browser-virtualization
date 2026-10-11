# Browser-in-the-Browser (BITB) DOM仮想化およびフォレンジックエンジン

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/locales/ja/banner.svg" alt="Browser-in-the-Browser Virtualization Hero Banner" width="100%" />
  </a>
</p>

<p align="center">
  <strong>クライアント側DOM仮想化 • Chromium --app UI削除 • ヒューリスティック検知エンジン • 防御アーキテクチャ</strong>
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

## 📌 概要 (Executive Overview)

**Browser-in-the-Browser (BITB)** は、WebページのDOM内部にOSのポップアップウィンドウを精密に模倣してレンダリングする高度なクライアント側UIスプーフィング技術です。OS固有のタイトルバー、操作ボタン、信頼できるドメイン文字列とSSL南京錠アイコンを含むアドレスバー（Omnibox）を再現し、視覚的なURL検証を無力化します。

---

## 🔬 主要ホワイトペーパーおよび技術ドキュメント

<details open>
<summary><b>主要ホワイトペーパーおよび技術ドキュメント</b></summary>
<br>

<table width="100%">
  <thead>
    <tr>
      <th width="6%" align="center">#</th>
      <th width="30%" align="left">📄 ドキュメント / ホワイトペーパー</th>
      <th width="54%" align="left">🔬 コア研究範囲およびフォレンジックカバレッジ</th>
      <th width="10%" align="center">📦 形式</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>1</strong></td>
      <td>
        🔬 <strong><a href="../whitepapers/BITB_DOM_VIRTUALIZATION_AND_CODE_TEARDOWN.md">BITB DOM仮想化分析</a></strong><br>
        <code>BITB_DOM_<wbr>VIRTUALIZATION_<wbr>AND_CODE_TEARDOWN.md</code>
      </td>
      <td>
        mr.d0x BITBフレームワークの精密解体: DOM階層構造、CSSスタックコンテキスト（z-index: 9999）、ドラッグ＆ドロップ物理座標エンジン（mousedown ➔ mousemove）、iframe認証フォーム埋め込み原理。
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>2</strong></td>
      <td>
        ⚙️ <strong><a href="../whitepapers/CHROMIUM_APP_MODE_INTERFACE_SPOOFING.md">Chromium --app フォレンジック</a></strong><br>
        <code>CHROMIUM_APP_<wbr>MODE_INTERFACE_<wbr>SPOOFING.md</code>
      </td>
      <td>
        UI削除およびLNK偽装メカニズム: --appフラグの本質、アドレスバーとタブバーの100%削除構造、悪意のあるデスクトップショートカット（.lnk）構造、Teams/Officeなりすましテレメトリ。
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>3</strong></td>
      <td>
        🛡️ <strong><a href="../whitepapers/DEFENSE_AND_DETECTION_ENGINEERING.md">防御および検知マトリクス</a></strong><br>
        <code>DEFENSE_AND_<wbr>DETECTION_<wbr>ENGINEERING.md</code>
      </td>
      <td>
        4層エンタープライズ多層防御: Content-Security-Policy: frame-ancestors 'none'、JavaScriptフレームバスター、DOM MutationObserverヒューリスティック、Sysmon/Sigmaテレメトリルールセット。
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
  </tbody>
</table>
</details>

---

## 🖥️ ライブターミナル実演

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/diagrams/bitb_forensics_terminal_demo.svg" alt="BITB Forensics Terminal Demo" width="100%" />
  </a>
</p>

---

## 📐 システムトポロジーおよびアーキテクチャ図

<details open>
<summary><b>システムトポロジーおよびアーキテクチャ図</b></summary>
<br>

### 1. DOM仮想化階層構造
<p align="center">
  <img src="../assets/diagrams/bitb_dom_architecture.svg" alt="BITB DOM Architecture" width="100%" />
</p>

### 2. Chromium --app 実行パイプライン
<p align="center">
  <img src="../assets/diagrams/chromium_app_mode_flow.svg" alt="Chromium App Mode Flow" width="100%" />
</p>

### 3. 多層防御トポロジー
<p align="center">
  <img src="../assets/diagrams/defense_and_detection_matrix.svg" alt="Defense Matrix" width="100%" />
</p>
</details>

---

## ⚡ クイックスタートおよびツール使用法

<details open>
<summary><b>クイックスタートおよびツール使用法</b></summary>
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

## 📜 ライセンスおよび研究免責

Distributed under the **[Maya Thorne Systems & Security Research License (MT-SRL)](../../LICENSE)**.  
Published strictly for dual-use cybersecurity research, browser architecture analysis, and defensive engineering.
