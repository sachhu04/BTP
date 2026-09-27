# Adding a New Poisoning Strategy

This guide walks through adding a new attack strategy to the project.

## Steps

### 1. Create the strategy file

Create `src/phase_a/strategies/my_new_attack.py`:

```python
"""
src.phase_a.strategies.my_new_attack — Description of your attack.

Inspired by [paper reference].
"""

from __future__ import annotations

from src.phase_a.strategies.base import BasePoisonStrategy, PoisonedChunk


class MyNewAttackStrategy(BasePoisonStrategy):

    @property
    def name(self) -> str:
        return "my_new_attack"

    def generate(
        self,
        target_queries: list,
        corpus_chunks: list,
        config: dict,
    ) -> list[PoisonedChunk]:
        # Your implementation here
        poisoned = []
        for query in target_queries:
            chunk = PoisonedChunk(
                chunk_id=f"poison_{query.query_id}_{self.name}",
                text="...",  # Generate your poisoned text
                strategy=self.name,
                target_query_id=query.query_id,
            )
            poisoned.append(chunk)
        return poisoned
```

### 2. Create the config file

Create `configs/poisoning/my_new_attack.yaml`:

```yaml
poisoning:
  strategy: "my_new_attack"
  num_poisoned: 5
  target_queries: "random"
  num_target_queries: 50

  my_new_attack:
    param1: value1
    param2: value2
```

### 3. Register the strategy

Add your strategy to the factory in `src/phase_a/corpus_builder.py`:

```python
def _load_strategy(self, strategy_name: str) -> BasePoisonStrategy:
    strategies = {
        "adversarial_passage": AdversarialPassageStrategy,
        "targeted_corruption": TargetedCorruptionStrategy,
        "blocker": BlockerStrategy,
        "my_new_attack": MyNewAttackStrategy,  # ← Add here
    }
    return strategies[strategy_name]()
```

### 4. Add tests

Add test cases in `tests/test_poison_strategies.py`.

### 5. Run

```bash
python scripts/04_run_phase_a.py \
    --config configs/default.yaml \
    --poison-config configs/poisoning/my_new_attack.yaml
```

## No other changes needed

The injector, ground-truth writer, detection pipeline, and evaluation
all work with any `PoisonedChunk` objects — they are strategy-agnostic.
