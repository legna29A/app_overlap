import pandas as pd
import numpy as np

# Archivos
pred = pd.read_csv("predictions_with_probs.csv")
mapping = pd.read_csv("analytical_sample_item_counts_mapping.csv")

# idx_original en predictions_with_probs.csv corresponde al índice filtrado/analítico
idx = pred["idx_original"].astype(int).values
y_true_model = pred["y_true"].astype(int).values

# Definiciones candidatas
y_count_based = mapping.iloc[idx]["overlap_ge1_count_based"].astype(int).values
y_target_flag = mapping.iloc[idx]["target_overlap_flag"].astype(int).values

print("Count-based matches:", (y_true_model == y_count_based).sum(), "/", len(y_true_model))
print("Target flag matches:", (y_true_model == y_target_flag).sum(), "/", len(y_true_model))

print("Model test positives:", y_true_model.sum())
print("Count-based test positives:", y_count_based.sum())
print("Target flag test positives:", y_target_flag.sum())

# Casos discrepantes entre target flag y y_true del modelo
mismatch = idx[y_true_model != y_target_flag]
print("Mismatching filtered indices:", mismatch)
print(mapping.iloc[mismatch][[
    "filtered_idx",
    "original_idx",
    "victim_count",
    "perp_count",
    "overlap_ge1_count_based",
    "target_overlap_flag"
]])