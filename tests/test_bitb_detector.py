#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for BITB Detector & Heuristic Engine.
"""

import os
import unittest
import sys

# Ensure src/ is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from bitb_detector import BitbDetector, BitbDetectionResult
from frame_security_auditor import FrameSecurityAuditor
from virtual_browser_emulator import VirtualBrowserEmulator


class TestBitbDetector(unittest.TestCase):

    def setUp(self):
        self.detector = BitbDetector()
        self.templates_dir = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "references", "bitb_templates"
        ))

    def test_windows_chrome_dark_detection(self):
        target = os.path.join(self.templates_dir, "windows_chrome_dark", "index.html")
        if os.path.exists(target):
            res = self.detector.scan_file(target)
            self.assertGreaterEqual(res.risk_score, 70)
            self.assertTrue(res.fake_address_bar_present)
            self.assertTrue(res.fake_titlebar_present)
            self.assertEqual(res.confidence, "CRITICAL (CONFIRMED BITB)")

    def test_macos_chrome_dark_detection(self):
        target = os.path.join(self.templates_dir, "macos_chrome_dark", "index.html")
        if os.path.exists(target):
            res = self.detector.scan_file(target)
            self.assertGreaterEqual(res.risk_score, 70)
            self.assertTrue(res.fake_address_bar_present)

    def test_benign_html(self):
        temp_benign = "<html><head><title>Benign Page</title></head><body><h1>Hello World</h1></body></html>"
        temp_file = os.path.join(os.path.dirname(__file__), "temp_benign.html")
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(temp_benign)
        try:
            res = self.detector.scan_file(temp_file)
            self.assertEqual(res.risk_score, 0)
            self.assertEqual(res.confidence, "BENIGN")
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)


class TestFrameSecurityAuditor(unittest.TestCase):

    def setUp(self):
        self.auditor = FrameSecurityAuditor()

    def test_strict_csp_header(self):
        headers = {
            "Content-Security-Policy": "frame-ancestors 'none'; default-src 'self'",
            "X-Frame-Options": "DENY"
        }
        res = self.auditor.audit_headers("https://secure-auth.com", headers)
        self.assertTrue(res.is_framing_protected)
        self.assertIn("ROBUST", res.protection_level)

    def test_legacy_xfo_header(self):
        headers = {
            "X-Frame-Options": "SAMEORIGIN"
        }
        res = self.auditor.audit_headers("https://legacy-portal.com", headers)
        self.assertTrue(res.is_framing_protected)
        self.assertIn("MODERATE", res.protection_level)

    def test_vulnerable_headers(self):
        headers = {
            "Server": "nginx",
            "Content-Type": "text/html"
        }
        res = self.auditor.audit_headers("https://vulnerable-site.com", headers)
        self.assertFalse(res.is_framing_protected)
        self.assertIn("VULNERABLE", res.protection_level)
        self.assertGreaterEqual(len(res.recommendations), 1)


class TestVirtualBrowserEmulator(unittest.TestCase):

    def setUp(self):
        self.emulator = VirtualBrowserEmulator(1920, 1080)

    def test_contained_window(self):
        res = self.emulator.test_drag_offset((500, 300), (50, 50), (600, 400))
        self.assertTrue(res["is_fully_contained"])
        self.assertFalse(res["clipping_anomaly"])

    def test_boundary_escape(self):
        res = self.emulator.test_drag_offset((1600, 300), (500, 0), (600, 400))
        self.assertFalse(res["is_fully_contained"])
        self.assertTrue(res["clipping_anomaly"])
        self.assertTrue(res["boundary_violations"]["escaped_right"])


if __name__ == "__main__":
    unittest.main()
