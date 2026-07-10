Supplementary repeated stratified 5x5 CV stability analysis.

This analysis does not replace the final held-out evaluation. It assesses metric stability across alternative partitions.

Configuration:
- N_SPLITS = 5
- N_REPEATS = 5
- PCA_THRESHOLD = 0.95
- THRESHOLD = 0.5
- Scaling/PCA fitted within each training fold only.
- Victimization: pruned decision tree with ccp_alpha selected inside each outer training fold.
- Perpetration: compact DNN with class weighting and early stopping.
- Overlap: weighted logistic regression, SW_pos1.5.

Main outputs:
- repeated_5x5_cv_fold_metrics.csv
- repeated_5x5_cv_summary_long.csv
- repeated_5x5_cv_pretty_mean_sd.csv
- repeated_5x5_cv_pretty_mean_p2_5_p97_5.csv
