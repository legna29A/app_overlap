SMART AND common-split benchmark — FINAL clean version
The benchmark used a common 75/25 split stratified by the four-category victimization/perpetration role profile.
Overlap was defined count-wise as V.SUM.TOTAL >= 1 AND P.SUM.TOTAL >= 1.
Scaler and PCA were fitted on the common training partition only.
The Smart AND strategy classified adolescents as overlap-positive only when both role-specific predictions were positive.
This is a strategy-level benchmark, not the direct combination of separately optimized saved final classifiers.

                          strategy                                                model                      threshold_type  victim_threshold  perp_threshold  overlap_threshold                    label    n  positive_support  negative_support  TP  FP  TN  FN recall_sensitivity specificity precision_ppv   npv balanced_accuracy f1_positive accuracy average_precision_pr_auc roc_auc
         Direct overlap classifier               Weighted logistic regression SW_pos1.5            direct overlap threshold               NaN             NaN                0.5           direct_overlap 1006               193               813 152 373 440  41              78.8%       54.1%         29.0% 91.5%             66.4%       42.3%    58.8%                    38.3%   73.4%
Smart AND recall-matched benchmark Victimization prediction AND perpetration prediction recall-matched benchmark thresholds              0.05           0.395                NaN smart_and_recall_matched 1006               193               813 155 433 380  38              80.3%       46.7%         26.4% 90.9%             63.5%       39.7%    53.2%                    32.7%   69.4%