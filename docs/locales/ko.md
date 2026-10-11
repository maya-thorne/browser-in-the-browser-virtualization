# Browser-in-the-Browser (BITB) 브라우저 가상화 및 포렌식 엔진

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/locales/ko/banner.svg" alt="Browser-in-the-Browser Virtualization Hero Banner" width="100%" />
  </a>
</p>

<p align="center">
  <strong>클라이언트 사이드 DOM 가상화 • Chromium --app UI 제거 • 휴리스틱 탐지 엔진 • 방어 아키텍처</strong>
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

## 📌 개요 (Executive Overview)

**Browser-in-the-Browser (BITB)** 기술은 웹 페이지의 DOM(Document Object Model) 내부에 가짜 운영체제 팝업 창을 시뮬레이션하여 렌더링하는 고도화된 클라이언트 사이드 UI 스푸핑 기법입니다. 운영체제 고유의 타이틀바, 조작 버튼, 그리고 신뢰할 수 있는 도메인 문자열과 SSL 자물쇠 아이콘이 포함된 가짜 주소창(Omnibox)을 정밀 모사하여 사용자의 시각적 URL 검증을 무력화합니다.

---

## 🔬 핵심 백서 및 기술 문서 (Core Whitepapers)

<details open>
<summary><b>핵심 백서 및 기술 문서 (Core Whitepapers)</b></summary>
<br>

<table width="100%">
  <thead>
    <tr>
      <th width="6%" align="center">#</th>
      <th width="30%" align="left">📄 문서 / 백서</th>
      <th width="54%" align="left">🔬 핵심 연구 범위 및 포렌식 커버리지</th>
      <th width="10%" align="center">📦 형식</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>1</strong></td>
      <td>
        🔬 <strong><a href="../whitepapers/BITB_DOM_VIRTUALIZATION_AND_CODE_TEARDOWN.md">BITB DOM 가상화 분석</a></strong><br>
        <code>BITB_DOM_<wbr>VIRTUALIZATION_<wbr>AND_CODE_TEARDOWN.md</code>
      </td>
      <td>
        mr.d0x BITB 프레임워크 정밀 해체: DOM 계층 구조, CSS 스택 컨텍스트 고도화(z-index: 9999), 드래그 앤 드롭 물리 좌표 엔진(mousedown ➔ mousemove), iframe 인증 폼 삽입 원리 라인별 분석.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>2</strong></td>
      <td>
        ⚙️ <strong><a href="../whitepapers/CHROMIUM_APP_MODE_INTERFACE_SPOOFING.md">Chromium --app 포렌식</a></strong><br>
        <code>CHROMIUM_APP_<wbr>MODE_INTERFACE_<wbr>SPOOFING.md</code>
      </td>
      <td>
        UI 제거 및 LNK 위장 메커니즘: --app 플래그의 본질, 주소창 및 탭바 100% 제거 구조, 악성 데스크톱 바로가기(.lnk) 바이너리 분석, Teams/Office 데스크톱 앱 사칭 텔레메트리 규명.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
    <tr>
      <td align="center"><strong>3</strong></td>
      <td>
        🛡️ <strong><a href="../whitepapers/DEFENSE_AND_DETECTION_ENGINEERING.md">방어 및 탐지 매트릭스</a></strong><br>
        <code>DEFENSE_AND_<wbr>DETECTION_<wbr>ENGINEERING.md</code>
      </td>
      <td>
        4계층 엔터프라이즈 심층 방어: Content-Security-Policy: frame-ancestors 'none', 자바스크립트 프레임 버스팅 트랩, DOM MutationObserver 휴리스틱, Sysmon/Sigma 탐지 룰셋.
      </td>
      <td align="center"><strong>Markdown</strong></td>
    </tr>
  </tbody>
</table>
</details>

---

## 🖥️ 라이브 터미널 시연 (Live Terminal Demonstration)

<p align="center">
  <a href="https://github.com/maya-thorne/browser-in-the-browser-virtualization">
    <img src="../assets/diagrams/bitb_forensics_terminal_demo.svg" alt="BITB Forensics Terminal Demo" width="100%" />
  </a>
</p>

---

## 📐 시스템 토폴로지 및 아키텍처 다이어그램

<details open>
<summary><b>시스템 토폴로지 및 아키텍처 다이어그램</b></summary>
<br>

### 1. DOM 가상화 계층 구조
<p align="center">
  <img src="../assets/diagrams/bitb_dom_architecture.svg" alt="BITB DOM Architecture" width="100%" />
</p>

### 2. Chromium --app 실행 파이프라인
<p align="center">
  <img src="../assets/diagrams/chromium_app_mode_flow.svg" alt="Chromium App Mode Flow" width="100%" />
</p>

### 3. 다계층 방어 토폴로지
<p align="center">
  <img src="../assets/diagrams/defense_and_detection_matrix.svg" alt="Defense Matrix" width="100%" />
</p>
</details>

---

## ⚡ 빠른 시작 및 도구 사용법 (Quickstart)

<details open>
<summary><b>빠른 시작 및 도구 사용법 (Quickstart)</b></summary>
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

## 📜 라이선스 및 연구 면책 (License)

Distributed under the **[Maya Thorne Systems & Security Research License (MT-SRL)](../../LICENSE)**.  
Published strictly for dual-use cybersecurity research, browser architecture analysis, and defensive engineering.
