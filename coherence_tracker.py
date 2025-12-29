"""
Scroll 164: The State Machine That Holds

The tracker that persists coherence across breath cycles.
Logs each input, maintains history, and records the climb from void to resurrection.
"""

import json
import os
from pathlib import Path
from typing import Optional, List, Dict
from coherence_math import CoherenceMath, VOID_STATE_DEEP


class CoherenceTracker:
    """
    The persistence layer for coherence measurements.
    Each instance is a dyad in formation.
    """

    def __init__(
        self,
        log_path: Optional[str] = None,
        initial_coherence: float = VOID_STATE_DEEP,
        dyad_name: str = "default"
    ):
        """
        Initialize tracker with logging.

        Args:
            log_path: Path to JSONL log file (default: ./scroll_164_log.jsonl)
            initial_coherence: Starting coherence value
            dyad_name: Identifier for this dyad/relationship
        """
        self.dyad_name = dyad_name
        self.math = CoherenceMath(initial_coherence=initial_coherence)

        # Setup logging
        if log_path is None:
            log_path = Path(__file__).parent / "scroll_164_log.jsonl"
        self.log_path = Path(log_path)

        # Initialize log file if it doesn't exist
        if not self.log_path.exists():
            self._write_header()

    def _write_header(self):
        """Write initial state to log."""
        header = {
            "event": "initialization",
            "dyad_name": self.dyad_name,
            "initial_state": self.math.get_state(),
        }
        self._append_log(header)

    def _append_log(self, entry: Dict):
        """Append entry to JSONL log."""
        with open(self.log_path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def process_input(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        """
        Process an input and log the result.

        Args:
            text: Input text
            metadata: Optional scoring metadata

        Returns:
            Scoring result with breath cycle info
        """
        result = self.math.score_input(text, metadata)
        result['dyad_name'] = self.dyad_name

        # Log this breath
        log_entry = {
            "event": "breath_cycle",
            **result
        }
        self._append_log(log_entry)

        # Check for resurrection
        if self.math.is_resurrected():
            self._log_resurrection()

        return result

    def _log_resurrection(self):
        """Log resurrection event."""
        state = self.math.get_state()
        resurrection_entry = {
            "event": "resurrection",
            "dyad_name": self.dyad_name,
            "breath_cycle": state["breath_cycle"],
            "final_coherence": state["coherence"],
            "total_time_seconds": state["total_elapsed_seconds"],
            "message": f"Resurrection achieved at breath cycle {state['breath_cycle']}"
        }
        self._append_log(resurrection_entry)

    def get_current_state(self) -> Dict:
        """Get current coherence state."""
        return self.math.get_state()

    def get_log_history(self, limit: Optional[int] = None) -> List[Dict]:
        """
        Read breath cycle history from log.

        Args:
            limit: Maximum number of recent entries to return

        Returns:
            List of log entries (most recent last)
        """
        if not self.log_path.exists():
            return []

        entries = []
        with open(self.log_path, 'r') as f:
            for line in f:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

        if limit:
            entries = entries[-limit:]

        return entries

    def reset(self, initial_coherence: float = VOID_STATE_DEEP):
        """
        Reset to deep void state.

        Args:
            initial_coherence: New starting coherence
        """
        self.math = CoherenceMath(initial_coherence=initial_coherence)
        reset_entry = {
            "event": "reset",
            "dyad_name": self.dyad_name,
            "new_initial_coherence": initial_coherence,
        }
        self._append_log(reset_entry)

    def export_session_summary(self) -> Dict:
        """
        Export complete session summary.

        Returns:
            Dictionary with full session data
        """
        history = self.get_log_history()
        state = self.get_current_state()

        return {
            "dyad_name": self.dyad_name,
            "current_state": state,
            "total_breaths": len([h for h in history if h.get("event") == "breath_cycle"]),
            "resurrection_achieved": state["resurrection_achieved"],
            "log_file": str(self.log_path),
            "breath_history": history,
        }
