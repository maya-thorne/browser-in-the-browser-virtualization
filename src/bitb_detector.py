#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🔬 BITB Detector - Browser-In-The-Browser Static & Heuristic Detection Engine
===============================================================================
Author: Maya Thorne (Systems & Security Research)
License: MT-SRL (Maya Thorne Systems & Security Research License)

Forensic heuristic analyzer for detecting Browser-in-the-Browser (BITB) DOM
virtualization and fake browser chrome spoofing inside web applications.
===============================================================================
"""

import os
import re
import json
import argparse
from typing import Dict, List, Any, Optional


class BitbDetectionResult:
    """Encapsulates the forensic audit results for a scanned web document."""

    def __init__(self, target_file: str):
        self.target_file = target_file
        self.risk_score: int = 0
        self.confidence: str = "BENIGN"
        self.indicators: List[Dict[str, Any]] = []
        self.spoofed_domains: List[str] = []
        self.simulated_os: List[str] = []
        self.iframe_targets: List[str] = []
        self.draggable_logic_present: bool = False
        self.fake_address_bar_present: bool = False
        self.fake_titlebar_present: bool = False

    def add_indicator(self, rule_id: str, title: str, severity: str, weight: int, evidence: str):
        self.risk_score += weight
        self.indicators.append({
            "rule_id": rule_id,
            "title": title,
            "severity": severity,
            "weight": weight,
            "evidence": evidence.strip()[:200]
        })
        self._update_confidence()

    def _update_confidence(self):
        if self.risk_score >= 70:
            self.confidence = "CRITICAL (CONFIRMED BITB)"
        elif self.risk_score >= 45:
            self.confidence = "HIGH (SUSPICIOUS VIRTUALIZATION)"
        elif self.risk_score >= 20:
            self.confidence = "MEDIUM (POTENTIAL OVERLAY)"
        else:
            self.confidence = "LOW (BENIGN)"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "target_file": self.target_file,
            "confidence": self.confidence,
            "risk_score": min(self.risk_score, 100),
            "simulated_os": list(set(self.simulated_os)),
            "spoofed_domains": list(set(self.spoofed_domains)),
            "iframe_targets": list(set(self.iframe_targets)),
            "draggable_window": self.draggable_logic_present,
            "fake_address_bar": self.fake_address_bar_present,
            "fake_titlebar": self.fake_titlebar_present,
            "indicator_count": len(self.indicators),
            "indicators": self.indicators
        }


class BitbDetector:
    """Heuristic static analysis engine for Browser-in-the-Browser artifacts."""

    # Heuristic Regex Signatures
    SIGNATURES = [
        # 1. Fake Browser Chrome DOM Elements
        {
            "id": "BITB-DOM-001",
            "title": "Simulated Window Container with Absolute Positioning",
            "severity": "HIGH",
            "weight": 25,
            "pattern": re.compile(r'id=["\'](?:window|modal-window|fake-window|browser-window)["\']', re.IGNORECASE)
        },
        {
            "id": "BITB-DOM-002",
            "title": "Simulated Browser Title Bar with Window Control Buttons",
            "severity": "HIGH",
            "weight": 25,
            "pattern": re.compile(r'id=["\'](?:title-bar|title-bar-width)["\']|class=["\'](?:title-bar|window-controls)["\']', re.IGNORECASE)
        },
        {
            "id": "BITB-DOM-003",
            "title": "Synthetic Address Bar (URL Omnibox Emulation)",
            "severity": "CRITICAL",
            "weight": 35,
            "pattern": re.compile(r'id=["\'](?:url-bar|address-bar|fake-url)["\']|class=["\'](?:url-bar|address-bar)["\']', re.IGNORECASE)
        },
        {
            "id": "BITB-DOM-004",
            "title": "SSL Padlock SVG / Asset Emulation in Synthetic Bar",
            "severity": "HIGH",
            "weight": 20,
            "pattern": re.compile(r'(?:ssl\.svg|lock\.svg|padlock|ssl-padlock)', re.IGNORECASE)
        },
        {
            "id": "BITB-DOM-005",
            "title": "Simulated Window Minimize/Maximize/Close Control Elements",
            "severity": "MEDIUM",
            "weight": 15,
            "pattern": re.compile(r'id=["\'](?:minimize|square|exit)["\']|class=["\'](?:btn-minimize|btn-maximize|btn-close)["\']', re.IGNORECASE)
        },

        # 2. Draggable Window Physics Scripting
        {
            "id": "BITB-JS-001",
            "title": "Custom Window Dragging & Cursor Physics",
            "severity": "HIGH",
            "weight": 30,
            "pattern": re.compile(r'title\.on\(["\']mousedown["\']|addEventListener\(["\']mousedown["\'].*?(?:pageY|pageX|dr\.offset)', re.DOTALL | re.IGNORECASE)
        },
        {
            "id": "BITB-JS-002",
            "title": "Simulated Window Fullscreen Resize State Machine",
            "severity": "MEDIUM",
            "weight": 15,
            "pattern": re.compile(r'classList\.contains\(["\']enlarged["\']\)|css\(["\']width["\'],\s*["\'](?:40%|70%|100%)["\']\)', re.IGNORECASE)
        },

        # 3. Iframe Credential Container
        {
            "id": "BITB-IFRAME-001",
            "title": "Iframe Authentication Sandbox Container",
            "severity": "HIGH",
            "weight": 25,
            "pattern": re.compile(r'<iframe[^>]+id=["\']content["\'][^>]*>', re.IGNORECASE)
        }
    ]

    DOMAIN_REGEX = re.compile(r'id=["\']domain-name["\'][^>]*>([^<]+)<|XX-DOMAIN-NAME-XX', re.IGNORECASE)
    IFRAME_SRC_REGEX = re.compile(r'<iframe[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

    def __init__(self):
        pass

    def scan_file(self, filepath: str) -> BitbDetectionResult:
        """Scan a single HTML, JS, or CSS file for BITB indicators."""
        result = BitbDetectionResult(filepath)
        if not os.path.exists(filepath):
            return result

        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception as e:
            result.add_indicator("BITB-ERR", "File Read Error", "LOW", 0, str(e))
            return result

        self._analyze_content(content, result)
        return result

    def scan_directory(self, dirpath: str) -> List[BitbDetectionResult]:
        """Recursively scan a directory for web assets and aggregate results."""
        results = []
        target_exts = {".html", ".htm", ".js", ".css"}
        for root, _, files in os.walk(dirpath):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in target_exts:
                    full_path = os.path.join(root, file)
                    res = self.scan_file(full_path)
                    if res.risk_score > 0:
                        results.append(res)
        return results

    def _analyze_content(self, content: str, result: BitbDetectionResult):
        for sig in self.SIGNATURES:
            match = sig["pattern"].search(content)
            if match:
                evidence = match.group(0)
                result.add_indicator(
                    sig["id"],
                    sig["title"],
                    sig["severity"],
                    sig["weight"],
                    evidence
                )
                if sig["id"] == "BITB-DOM-002":
                    result.fake_titlebar_present = True
                elif sig["id"] == "BITB-DOM-003":
                    result.fake_address_bar_present = True
                elif sig["id"] == "BITB-JS-001":
                    result.draggable_logic_present = True

        # Extract spoofed domains
        domain_matches = self.DOMAIN_REGEX.findall(content)
        for dom in domain_matches:
            if dom and dom != "XX-DOMAIN-NAME-XX":
                result.spoofed_domains.append(dom)

        # Extract iframe targets
        iframe_matches = self.IFRAME_SRC_REGEX.findall(content)
        for src in iframe_matches:
            result.iframe_targets.append(src)

        # Infer simulated OS flavor
        if "Windows" in content or "win" in content.lower() or "Segoe UI" in content:
            result.simulated_os.append("Windows")
        if "MacOS" in content or "mac" in content.lower() or "San Francisco" in content or "-apple-system" in content:
            result.simulated_os.append("macOS")


def print_cli_report(results: List[BitbDetectionResult]):
    """Print an enterprise ANSI colored terminal forensic summary."""
    print("\n" + "=" * 78)
    print("🔬 BROWSER-IN-THE-BROWSER (BITB) HEURISTIC DETECTION REPORT")
    print("   Engineered & Audited by Maya Thorne (Systems & Security Research)")
    print("=" * 78)

    if not results:
        print("  ✅ [PASS] No Browser-In-The-Browser indicators detected across target.")
        print("=" * 78 + "\n")
        return

    for res in results:
        status_color = "\033[91m" if res.risk_score >= 70 else ("\033[93m" if res.risk_score >= 40 else "\033[92m")
        reset_color = "\033[0m"

        print(f"\nTarget File : {res.target_file}")
        print(f"Risk Score  : {status_color}{min(res.risk_score, 100)} / 100 [{res.confidence}]{reset_color}")
        print(f"OS Flavor   : {', '.join(res.simulated_os) if res.simulated_os else 'Unknown'}")
        print(f"Draggable   : {'YES' if res.draggable_logic_present else 'NO'}")
        print(f"Fake Bar    : {'YES' if res.fake_address_bar_present else 'NO'}")
        if res.spoofed_domains:
            print(f"Spoofed Dom : {', '.join(res.spoofed_domains)}")
        if res.iframe_targets:
            print(f"Iframe Src  : {', '.join(res.iframe_targets)}")

        print("-" * 78)
        print(f"{'Rule ID':<15} | {'Severity':<8} | {'Weight':<6} | {'Indicator Title'}")
        print("-" * 78)
        for ind in res.indicators:
            print(f"{ind['rule_id']:<15} | {ind['severity']:<8} | +{ind['weight']:<5} | {ind['title']}")

    print("=" * 78 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Browser-In-The-Browser (BITB) Heuristic Detector")
    parser.add_argument("--path", "-p", required=True, help="Path to file or directory to scan")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    detector = BitbDetector()
    if os.path.isdir(args.path):
        scan_results = detector.scan_directory(args.path)
    else:
        res = detector.scan_file(args.path)
        scan_results = [res] if res.risk_score > 0 else []

    if args.json:
        output_data = [r.to_dict() for r in scan_results]
        print(json.dumps(output_data, indent=2))
    else:
        print_cli_report(scan_results)
