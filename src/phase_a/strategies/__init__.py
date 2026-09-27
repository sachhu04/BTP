"""
src.phase_a.strategies — Pluggable poisoning strategy implementations.

Each strategy is a subclass of BasePoisonStrategy and implements the
`generate()` method. To add a new attack strategy:

1. Create a new file in this directory (e.g., `my_attack.py`).
2. Implement a class inheriting from BasePoisonStrategy.
3. Add a corresponding config file in configs/poisoning/.
4. See docs/adding_a_poison_strategy.md for a full walkthrough.
"""
