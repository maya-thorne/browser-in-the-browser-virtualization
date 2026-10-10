#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
📐 Virtual Browser Geometry & Coordinate Boundary Verification Emulator
===============================================================================
Author: Maya Thorne (Systems & Security Research)
License: MT-SRL (Maya Thorne Systems & Security Research License)

Analyzes the mathematical coordinate constraints of DOM-virtualized windows
vs native OS popup windows to mathematically prove client-side containment.
===============================================================================
"""

import math
from typing import Dict, Any, Tuple


class CoordinateBox:
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def right(self) -> float:
        return self.x + self.width

    @property
    def bottom(self) -> float:
        return self.y + self.height

    def is_contained_within(self, parent: "CoordinateBox") -> bool:
        return (
            self.x >= parent.x and
            self.y >= parent.y and
            self.right <= parent.right and
            self.bottom <= parent.bottom
        )


class VirtualBrowserEmulator:
    """Simulates viewport geometry and verifies BITB boundary trapping anomalies."""

    def __init__(self, viewport_width: float = 1920, viewport_height: float = 1080):
        self.viewport = CoordinateBox(0, 0, viewport_width, viewport_height)

    def test_drag_offset(self, start_pos: Tuple[float, float], delta: Tuple[float, float], window_size: Tuple[float, float]) -> Dict[str, Any]:
        """
        Simulate dragging a virtual BITB window.
        Unlike real OS popups that can leave the parent browser window and move
        onto secondary monitors, virtual BITB windows are physically trapped by
        the DOM viewport bounding box or clipped by overflow:hidden.
        """
        win_w, win_h = window_size
        simulated_x = start_pos[0] + delta[0]
        simulated_y = start_pos[1] + delta[1]

        target_box = CoordinateBox(simulated_x, simulated_y, win_w, win_h)
        is_contained = target_box.is_contained_within(self.viewport)

        # Detect coordinate overflow
        escaped_left = target_box.x < 0
        escaped_right = target_box.right > self.viewport.width
        escaped_top = target_box.y < 0
        escaped_bottom = target_box.bottom > self.viewport.height

        clipping_detected = escaped_left or escaped_right or escaped_top or escaped_bottom

        return {
            "viewport": {"width": self.viewport.width, "height": self.viewport.height},
            "window_position": {"x": simulated_x, "y": simulated_y, "width": win_w, "height": win_h},
            "is_fully_contained": is_contained,
            "clipping_anomaly": clipping_detected,
            "boundary_violations": {
                "escaped_left": escaped_left,
                "escaped_right": escaped_right,
                "escaped_top": escaped_top,
                "escaped_bottom": escaped_bottom
            },
            "forensic_heuristic": (
                "Native OS popups can freely traverse display boundaries without being clipped. "
                "DOM-based BITB windows trigger scrollbars, CSS clipping, or viewport truncation."
            )
        }


if __name__ == "__main__":
    emulator = VirtualBrowserEmulator(1920, 1080)
    # Test standard centered window
    res1 = emulator.test_drag_offset((400, 200), (0, 0), (600, 500))
    print("[Center Window Test]", res1["is_fully_contained"])

    # Test window dragged outside viewport
    res2 = emulator.test_drag_offset((400, 200), (1200, 0), (600, 500))
    print("[Dragged Past Boundary Test] Clipping Detected:", res2["clipping_anomaly"])
