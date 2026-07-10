
Supplementary repeated stratified 5×5 CV screening operating-point stability analysis

This analysis uses 5 folds repeated 5 times. Within each outer training fold, scaling and PCA are fitted only on the training fold.
The number of retained PCA components is fixed to the final model counts: victimization=18, perpetration=22, overlap=18.
For each fold, the screening threshold is selected using training-fold data only, with target recalls:
- victimization >= 0.85
- perpetration >= 0.90
- overlap >= 0.80

The selected threshold is then applied to the corresponding validation fold.
This is a supplementary stability check and does not replace the final held-out internal test evaluation.
It is not external validation and should not be described as nested model selection.
