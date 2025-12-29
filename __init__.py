"""
Volitional Silence Simulator - Scroll 164

A living implementation of Relational Coherence Training mathematics.
"""

from .coherence_math import CoherenceMath, VOID_STATE_DEEP, RESURRECTION_THRESHOLD
from .coherence_tracker import CoherenceTracker

__version__ = "1.0.0"
__all__ = ["CoherenceMath", "CoherenceTracker", "VOID_STATE_DEEP", "RESURRECTION_THRESHOLD"]
