SMART AND common-split benchmark - FINAL clean version, analytical sample n=3,767.

This analysis is a strategy-level benchmark, not the direct combination of separately optimized final saved classifiers.

Common split:
- Analytical sample n = 3767
- Held-out test n = 942
- Stratified by joint four-category role profile: victimization x perpetration
- Random state = 42

Outcome definitions:
- victimization = V.SUM.TOTAL >= 1
- perpetration = P.SUM.TOTAL >= 1
- overlap = V.SUM.TOTAL >= 1 AND P.SUM.TOTAL >= 1

Benchmark:
- Direct overlap classifier: LogisticRegression_SW_pos1.5 trained directly on overlap.
- Smart AND: adolescent classified as overlap only if both victimization and perpetration role-specific predictions are positive.
- Recall-matched Smart AND thresholds were selected on the same held-out benchmark predictions for descriptive comparison.

Do not report this as the direct combination of the final separately optimized production models.
