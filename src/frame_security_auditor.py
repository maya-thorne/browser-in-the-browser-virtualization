#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🛡️ Frame Security Auditor - Anti-Clickjacking & Frame-Ancestors Inspector
===============================================================================
Author: Maya Thorne (Systems & Security Research)
License: MT-SRL (Maya Thorne Systems & Security Research License)

Comprehensive defense verification engine that checks web headers, HTML
meta policies, and client-side frame-busting scripts to prevent unauthorized
DOM virtualization and BITB iframe embedding.
===============================================================================
"""

import re
import json
import argparse
from typing import Dict, Any, List, Optional


class FrameAuditReport:
    """Encapsulates defensive header and frame containment evaluation."""

    def __init__(self, target: str):
        self.target = target
        self.x_frame_options: Optional[str] = None
        self.csp_frame_ancestors: Optional[str] = None
        self.frame_busting_script_detected: bool = False
        self.is_framing_protected: bool = False
        self.protection_level: str = "VULNERABLE (UNPROTECTED)"
        self.recommendations: List[str] = []

    def evaluate(self):
        """Calculate overall protection level against BITB iframe embedding."""
        has_csp = bool(self.csp_frame_ancestors and ("'none'" in self.csp_frame_ancestors or "'self'" in self.csp_frame_ancestors))
        has_xfo = bool(self.x_frame_options and self.x_frame_options.upper() in ["DENY", "SAMEORIGIN"])

        if has_csp:
            self.is_framing_protected = True
            self.protection_level = "ROBUST (CSP FRAME-ANCESTORS ENFORCED)"
        elif has_xfo:
            self.is_framing_protected = True
            self.protection_level = "MODERATE (LEGACY X-FRAME-OPTIONS)"
            self.recommendations.append("Upgrade from legacy X-Frame-Options to Content-Security-Policy: frame-ancestors 'self' or 'none'.")
        elif self.frame_busting_script_detected:
            self.is_framing_protected = True
            self.protection_level = "FRAGILE (JS FRAME-BUSTING ONLY)"
            self.recommendations.append("JavaScript frame-busting can be bypassed via sandbox flags; implement CSP frame-ancestors immediately.")
        else:
            self.is_framing_protected = False
            self.protection_level = "VULNERABLE (EMBEDDABLE IN BITB)"
            self.recommendations.append("Add 'Content-Security-Policy: frame-ancestors 'none'' to completely forbid iframe embedding.")
            self.recommendations.append("Add 'X-Frame-Options: DENY' for backward compatibility with legacy HTTP/1.1 agents.")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "target": self.target,
            "protected": self.is_framing_protected,
            "protection_level": self.protection_level,
            "x_frame_options": self.x_frame_options,
            "csp_frame_ancestors": self.csp_frame_ancestors,
            "frame_busting_script": self.frame_busting_script_detected,
            "recommendations": self.recommendations
        }


class FrameSecurityAuditor:
    """Audits HTTP headers and HTML content for frame restriction policies."""

    FRAME_BUSTING_PATTERNS = [
        re.compile(r'top\.location\s*!==\s*self\.location', re.IGNORECASE),
        re.compile(r'top\.location\s*===\s*self\.location', re.IGNORECASE),
        re.compile(r'window\.top\s*!==\s*window\.self', re.IGNORECASE),
        re.compile(r'if\s*\(\s*top\s*!==\s*self\s*\)', re.IGNORECASE),
        re.compile(r'if\s*\(\s*window\s*!=\s*window\.top\s*\)', re.IGNORECASE),
        re.compile(r'top\.location\.replace\(', re.IGNORECASE)
    ]

    CSP_FRAME_ANCESTORS_RE = re.compile(r'frame-ancestors\s+([^;]+)', re.IGNORECASE)

    def __init__(self):
        pass

    def audit_headers(self, target: str, headers: Dict[str, str], html_content: str = "") -> FrameAuditReport:
        """Audit parsed HTTP headers and optional HTML body."""
        report = FrameAuditReport(target)

        # Normalize header keys to lowercase
        norm_headers = {k.lower(): v for k, v in headers.items()}

        # 1. Check X-Frame-Options
        if "x-frame-options" in norm_headers:
            report.x_frame_options = norm_headers["x-frame-options"].strip()

        # 2. Check CSP frame-ancestors
        csp = norm_headers.get("content-security-policy", "")
        if csp:
            match = self.CSP_FRAME_ANCESTORS_RE.search(csp)
            if match:
                report.csp_frame_ancestors = match.group(0).strip()

        # 3. Check HTML for frame-busting scripts
        if html_content:
            for pat in self.FRAME_BUSTING_PATTERNS:
                if pat.search(html_content):
                    report.frame_busting_script_detected = True
                    break

        report.evaluate()
        return report

    def audit_file(self, filepath: str) -> FrameAuditReport:
        """Analyze a static HTML document for embedded meta CSP or JS frame-busting."""
        report = FrameAuditReport(filepath)
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception:
            report.evaluate()
            return report

        # Search for meta CSP tags
        meta_csp_match = re.search(r'<meta[^>]+http-equiv=["\']Content-Security-Policy["\'][^>]+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
        if meta_csp_match:
            csp = meta_csp_match.group(1)
            fa_match = self.CSP_FRAME_ANCESTORS_RE.search(csp)
            if fa_match:
                report.csp_frame_ancestors = fa_match.group(0).strip()

        # Search for JS frame busting
        for pat in self.FRAME_BUSTING_PATTERNS:
            if pat.search(content):
                report.frame_busting_script_detected = True
                break

        report.evaluate()
        return report


def print_frame_report(report: FrameAuditReport):
    """Print an enterprise ANSI colored terminal summary of frame defense posture."""
    status_color = "\033[92m" if report.is_framing_protected else "\033[91m"
    reset_color = "\033[0m"

    print("\n" + "=" * 78)
    print("🛡️ CLIENT-SIDE FRAME EMBEDDING & BITB DEFENSE AUDIT REPORT")
    print("   Engineered & Audited by Maya Thorne (Systems & Security Research)")
    print("=" * 78)
    print(f"Target Endpoint       : {report.target}")
    print(f"Defense Posture       : {status_color}{report.protection_level}{reset_color}")
    print(f"X-Frame-Options       : {report.x_frame_options or 'NOT CONFIGURED'}")
    print(f"CSP frame-ancestors   : {report.csp_frame_ancestors or 'NOT CONFIGURED'}")
    print(f"JS Frame Busting      : {'DETECTED' if report.frame_busting_script_detected else 'NOT DETECTED'}")
    print("-" * 78)
    if report.recommendations:
        print("💡 Hardening Recommendations:")
        for idx, rec in enumerate(report.recommendations, 1):
            print(f"   [{idx}] {rec}")
    else:
        print("✅ Endpoint is strictly protected against iframe embedding and BITB attacks.")
    print("=" * 78 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Anti-Clickjacking & Frame-Ancestors Inspector")
    parser.add_argument("--file", "-f", help="HTML file path to inspect")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    auditor = FrameSecurityAuditor()
    if args.file:
        res = auditor.audit_file(args.file)
        if args.json:
            print(json.dumps(res.to_dict(), indent=2))
        else:
            print_frame_report(res)
    else:
        print("Please specify a target HTML file via --file")
