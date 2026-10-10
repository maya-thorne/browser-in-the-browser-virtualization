# Chromium `--app` Mode Interface Stripping & Desktop Masquerading Forensics

> **Author**: Maya Thorne (Systems & Security Research)  
> **Classification**: Dual-Use Systems Architecture & Cyber Defense Engineering  
> **License**: [MT-SRL (Maya Thorne Systems & Security Research License)](../../LICENSE)  
> **Status**: Comprehensive Forensic Reference (v1.0.0)

---

## 📌 Executive Summary

Modern web browsers are designed to provide clear, persistent visual security feedback to users: the **Omnibox** displays the active domain name, EV/DV SSL certificate lock indicators, and security warning banners; the **Tab Strip** visualizes open tabs; and the **Extension Toolbar** surfaces third-party security instruments and password managers.

However, the Chromium browser engine includes a dedicated flag designed for Progressive Web Apps (PWAs): **`--app=<URL>`**. When invoked with this parameter, Chromium strips **100% of the browser's native chrome UI**, presenting a completely bare operating system window containing only the target webpage.

This whitepaper investigates how threat actors weaponize Chromium's `--app` mode in combination with `-incognito` flags, desktop shortcuts (`.lnk`), and custom CSS to forge pixel-perfect desktop application interfaces (such as Microsoft Teams or Office 365), and provides the corresponding forensic telemetry and EDR detection strategies.

---

## ⚙️ 1. Mechanics of the `--app` Flag

### 1.1 Command-Line Execution Topology

```bash
# Standard app mode execution
brave.exe --app=https://login.microsoftonline.com

# Stealth incognito execution with local file binding
brave.exe --app=C:\Users\victim\AppData\Local\Temp\portal.html -incognito
```

```
[Normal Browser Window]
┌────────────────────────────────────────────────────────┐
│ [Tab 1] [Tab 2] [+]                           [-] [x]  │ ➔ Tab Strip
├────────────────────────────────────────────────────────┤
│ [←] [→] [↻]  🔒 https://target-site.com        [★] [🧩] │ ➔ Omnibox (Address Bar)
├────────────────────────────────────────────────────────┤
│ [Bookmarks Bar]                                        │ ➔ Bookmarks Strip
├────────────────────────────────────────────────────────┤
│                                                        │
│                    Web View Content                    │
│                                                        │
└────────────────────────────────────────────────────────┘

                        ▼  When --app is applied

[Chromium App Window]
┌────────────────────────────────────────────────────────┐
│ 🪟 Window Title (Parsed from <title> tag)       [-] [x]  │ ➔ Native OS Titlebar Only
├────────────────────────────────────────────────────────┤
│                                                        │
│                    Web View Content                    │
│                                                        │
│            • Omnibox / Address Bar: 0% Visible         │
│            • Tab Strip: 0% Visible                     │
│            • Bookmarks Bar: 0% Visible                 │
│            • Extensions Toolbar: 0% Visible            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 1.2 Impact on Client-Side Security Controls

1. **Suppression of Domain Feedback**: The victim cannot inspect the destination URL, hostname, port, or protocol scheme.
2. **Elimination of Password Manager Overlays**: Major password manager extensions (1Password, Bitwarden, LastPass) rely on the browser's top-level chrome to surface autofill badges and origin validation warnings. In `--app` mode, extension icons are completely hidden.
3. **Isolation via `-incognito`**: When combined with `-incognito`, the window opens in a fresh session devoid of existing cookies, forcing the victim to encounter a blank authentication dialog.

---

## 🎯 2. LNK Shortcut Weaponization & Masquerading

Threat actors distribute desktop shortcut files (`.lnk`) that disguise the execution of the Chromium executable:

```
[Victim Perspective]                   [Operating System Process Tree]
┌───────────────────────────┐          explorer.exe
│ 📁 Microsoft Teams.lnk    │ ───────►   │
│ Icon: teams.ico           │            └── brave.exe / chrome.exe
│ Display Name: Teams       │                  ├── --app=https://phish.net/login
└───────────────────────────┘                  └── -incognito
```

### 2.1 Shortcut Parameter Structure

Inspection of weaponized `.lnk` binaries reveals key forensic attributes:
- **Target Path**: Points to the local installation path of Chrome, Edge, or Brave:
  - `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`
  - `C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe`
- **Arguments**: `--app="https://malicious-collector.com/login" -incognito`
- **Icon Location**: Pointed to a legitimate local DLL or ICO resource (e.g., `%SystemRoot%\System32\shell32.dll` or dropped Office icons).

---

## 🎨 3. In-DOM Synthetic Omnibox Emulation

Because the browser's real Omnibox is hidden, the attacker injects an artificial address bar at the very top of the DOM:

```html
<div class="fake-omnibox">
    <div class="ssl-badge">
        <svg class="green-padlock">...</svg>
        <span>Secure | </span>
    </div>
    <span class="url-text">https://login.microsoftonline.com/common/oauth2/v2.0/authorize</span>
</div>
```

Combined with exact CSS typography matching Windows' native `Segoe UI` system font and a `440px × 520px` dialog box, the victim has zero visual indication that they are interacting with a browser window rather than the official Microsoft Teams desktop client.

---

## 🛡️ 4. EDR Telemetry & Detection Strategies

### 4.1 Sysmon Event ID 1 (Process Creation)

Security Information and Event Management (SIEM) and Endpoint Detection and Response (EDR) platforms can reliably detect suspicious `--app` invocations by inspecting command-line process parameters:

```yaml
title: Suspicious Chromium App Mode Launch via Shortcut
id: e4b2910d-71b5-4b1a-9694-850937a4c498
status: production
description: Detects Chromium-based browsers launched with the --app parameter and -incognito flag
logsource:
  category: process_creation
  product: windows
detection:
  selection_browser:
    Image|endswith:
      - '\chrome.exe'
      - '\msedge.exe'
      - '\brave.exe'
  selection_flags:
    CommandLine|contains|all:
      - '--app='
      - '-incognito'
  condition: selection_browser and selection_flags
fields:
  - CommandLine
  - ParentCommandLine
  - User
level: high
```

---

## 🔬 5. Conclusion

Chromium's `--app` mode is an indispensable tool for Progressive Web Apps, but its ability to strip all browser security chrome makes it a potent vector for desktop masquerading. By pairing endpoint telemetry with process command-line audits and network proxy inspection, enterprises can effectively detect and neutralize this attack surface.
