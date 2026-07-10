S13 — Permutation importance over original engineered predictors

Generated files:
- /Users/legna/WORKSPACE/ICREA/app_overlap/results_repo/intersection_model/Version_Final/final_permutation_importance_original_predictors_S13/S13_baseline_validation.csv
- /Users/legna/WORKSPACE/ICREA/app_overlap/results_repo/intersection_model/Version_Final/final_permutation_importance_original_predictors_S13/S13_permutation_importance_long.csv
- /Users/legna/WORKSPACE/ICREA/app_overlap/results_repo/intersection_model/Version_Final/final_permutation_importance_original_predictors_S13/S13_permutation_importance_summary.csv
- /Users/legna/WORKSPACE/ICREA/app_overlap/results_repo/intersection_model/Version_Final/final_permutation_importance_original_predictors_S13/Table_S13_top10_by_balanced_accuracy.csv
- /Users/legna/WORKSPACE/ICREA/app_overlap/results_repo/intersection_model/Version_Final/final_permutation_importance_original_predictors_S13/Table_S13_top10_by_pr_auc.csv
- /Users/legna/WORKSPACE/ICREA/app_overlap/results_repo/intersection_model/Version_Final/final_permutation_importance_original_predictors_S13/Table_S13_top10_by_roc_auc.csv

Suggested supplementary table title:
Supplementary Table S13. Model-Agnostic Permutation Importance of Original Engineered Predictors.

Suggested note:
Permutation importance was computed on the held-out internal test partition using the final frozen preprocessing and modeling pipelines. Each original engineered predictor or dummy-coded predictor group was randomly permuted while all other predictors were held fixed; the frozen scaler, PCA transformation, and classifier were then reapplied. Values represent the mean decrease in performance across repeated permutations, expressed in percentage points. Larger positive values indicate greater model-dependent performance loss after permutation. These estimates should not be interpreted as causal effects or independent predictor effects.

Important validation rule:
Only report these results if S13_baseline_validation.csv shows matches_official_metrics = True for all three outcomes.