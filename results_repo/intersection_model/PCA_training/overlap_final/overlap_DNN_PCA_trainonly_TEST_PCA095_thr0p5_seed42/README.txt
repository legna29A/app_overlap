Modelo overlap/intersection guardado.

PCA_THRESHOLD = 0.95
PCA_SCOPE = train_only
THRESHOLD = 0.5
RANDOM_STATE = 42
OUTPUT_DIR = overlap_final/overlap_DNN_PCA_trainonly_TEST_PCA095_thr0p5_seed42

Para reproducir sin reentrenar:
1) cargar model/best_model.keras o model/best_model.h5 si se ha generado por condición de grid-search;
2) cargar model/scaler_minmax.pkl, model/modelo_pca.pkl y model/columns.json;
3) usar outputs/y_test_predictions.csv para recalcular métricas y barrer thresholds sin reentrenar.

No sobrescribir esta carpeta si el resultado es el definitivo.
