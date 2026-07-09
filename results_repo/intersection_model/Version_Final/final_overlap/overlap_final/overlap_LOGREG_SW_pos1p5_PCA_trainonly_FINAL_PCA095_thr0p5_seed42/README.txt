Modelo final overlap/intersection guardado.

PCA_THRESHOLD = 0.95
PCA_SCOPE = train_only
THRESHOLD = 0.5
RANDOM_STATE = 42
OUTPUT_DIR = overlap_final/overlap_LOGREG_SW_pos1p5_PCA_trainonly_FINAL_PCA095_thr0p5_seed42

Para reproducir sin reentrenar:
1) cargar model/final_overlap_logreg_SW_pos1p5.joblib;
2) cargar model/scaler_minmax.pkl, model/modelo_pca.pkl y model/medias_escalado.csv;
3) usar outputs/predictions_with_probs.csv para recalcular métricas y barrer thresholds sin reentrenar.

No sobrescribir esta carpeta si el resultado es el definitivo.
