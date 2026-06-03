# Análisis comparativo de modelos — Clasificador de victimización

## 1. Objetivo de la comparación

El objetivo de esta prueba era comprobar si otros modelos supervisados podían mejorar el rendimiento del árbol de decisión actual para la clasificación de victimización, usando exactamente los mismos conjuntos de entrenamiento y test:

- `X_train.csv`
- `X_test.csv`
- `y_train.csv`
- `y_test.csv`

Esto permite una comparación justa, ya que todos los modelos usan el mismo espacio PCA, el mismo split y el mismo objetivo binario.

El criterio principal no es maximizar la accuracy, sino mantener una sensibilidad alta para la clase víctima (`recall_1`), porque el modelo está pensado como herramienta de cribado. En este contexto, perder casos reales de victimización es más problemático que generar falsos positivos que luego puedan ser revisados por profesionales.

---

## 2. Resultado con umbral estándar 0.50

Con el umbral estándar de clasificación (`threshold = 0.50`), los modelos alternativos muestran un comportamiento más equilibrado que el árbol de decisión, pero con un recall bastante más bajo para la clase víctima.

| Modelo | Recall víctima | Precision víctima | Specificity no víctima | F1 víctima | Balanced accuracy | AUC-PR |
|---|---:|---:|---:|---:|---:|---:|
| GradientBoosting | 0.6694 | 0.6822 | 0.6963 | 0.6757 | 0.6828 | 0.7199 |
| LogisticRegression balanced | 0.6478 | 0.6847 | 0.7094 | 0.6657 | 0.6786 | 0.7217 |
| HistGradientBoosting | 0.6613 | 0.6525 | 0.6571 | 0.6569 | 0.6592 | 0.7262 |
| RandomForest balanced | 0.6855 | 0.6391 | 0.6230 | 0.6615 | 0.6543 | 0.7217 |
| DecisionTree actual | 0.9113 | 0.5415 | 0.2487 | 0.6794 | 0.5800 | 0.5373 |

### Lectura

A umbral 0.50, los modelos alternativos son claramente mejores en:

- `precision_1`
- `specificity_0`
- `balanced_accuracy`
- `AUC-PR`

Sin embargo, todos bajan mucho el recall de víctima, quedándose aproximadamente entre 0.65 y 0.69. Esto significa que detectarían bastantes menos víctimas reales que el árbol actual.

Por tanto, si se usa el umbral estándar, los modelos alternativos parecen mejores en equilibrio general, pero peores para el objetivo principal de screening sensible.

---

## 3. Análisis con umbrales orientados a recall alto

Como el árbol actual está claramente optimizado para recall, la comparación relevante no es solo con umbral 0.50, sino buscando umbrales que mantengan `recall_1 >= 0.90`.

Los mejores candidatos con recall alto son:

| Modelo | Threshold | Recall víctima | Precision víctima | Specificity no víctima | F1 víctima | Balanced accuracy | TP | FP | TN | FN | AUC-PR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DecisionTree actual | 0.30–0.50 | 0.9113 | 0.5415 | 0.2487 | 0.6794 | 0.5800 | 339 | 287 | 95 | 33 | 0.5373 |
| LogisticRegression balanced | 0.30 | 0.9005 | 0.5395 | 0.2513 | 0.6747 | 0.5759 | 335 | 286 | 96 | 37 | 0.7217 |
| HistGradientBoosting | 0.25 | 0.9301 | 0.5389 | 0.2251 | 0.6824 | 0.5776 | 346 | 296 | 86 | 26 | 0.7262 |
| RandomForest balanced | 0.30 | 0.9086 | 0.5382 | 0.2408 | 0.6760 | 0.5747 | 338 | 290 | 92 | 34 | 0.7217 |
| GradientBoosting | 0.30 | 0.9328 | 0.5347 | 0.2094 | 0.6797 | 0.5711 | 347 | 302 | 80 | 25 | 0.7199 |

---

## 4. Interpretación de los modelos alternativos

### 4.1. Logistic Regression balanced

La regresión logística balanceada consigue un comportamiento muy parecido al árbol:

- Recall víctima: 0.9005
- Precision víctima: 0.5395
- Specificity: 0.2513
- Balanced accuracy: 0.5759

Su ventaja es que tiene una AUC-PR mucho mayor que el árbol (`0.7217` frente a `0.5373`), lo que indica que sus probabilidades ordenan mejor los casos positivos y negativos. Sin embargo, en el punto operativo de recall alto no mejora realmente al árbol.

Conclusión: buen baseline, pero no sustituye claramente al árbol.

---

### 4.2. Random Forest balanced

Random Forest con threshold 0.30 también queda muy cerca del árbol:

- Recall víctima: 0.9086
- Precision víctima: 0.5382
- Specificity: 0.2408
- Balanced accuracy: 0.5747

No mejora al árbol en el punto de recall alto. Además, pierde interpretabilidad, porque ya no hay una regla simple como la del árbol actual.

Conclusión: no parece aportar suficiente mejora para justificar el cambio.

---

### 4.3. Gradient Boosting

Gradient Boosting con threshold 0.30 consigue mayor recall que el árbol:

- Recall víctima: 0.9328
- TP: 347 frente a 339 del árbol
- FN: 25 frente a 33 del árbol

Pero esa mejora en sensibilidad se consigue aumentando falsos positivos:

- FP: 302 frente a 287 del árbol
- Specificity: 0.2094 frente a 0.2487 del árbol

Es decir, detecta 8 víctimas adicionales, pero genera 15 falsos positivos más.

Conclusión: puede ser interesante si se quiere maximizar aún más la detección de víctimas, pero empeora la especificidad y no mejora mucho la utilidad operativa.

---

### 4.4. HistGradientBoosting

HistGradientBoosting con threshold 0.25 parece el candidato alternativo más interesante:

- Recall víctima: 0.9301
- Precision víctima: 0.5389
- F1 víctima: 0.6824
- Balanced accuracy: 0.5776
- AUC-PR: 0.7262

Comparado con el árbol:

| Métrica | Decision Tree actual | HistGradientBoosting 0.25 |
|---|---:|---:|
| Recall víctima | 0.9113 | 0.9301 |
| Precision víctima | 0.5415 | 0.5389 |
| Specificity no víctima | 0.2487 | 0.2251 |
| F1 víctima | 0.6794 | 0.6824 |
| Balanced accuracy | 0.5800 | 0.5776 |
| TP | 339 | 346 |
| FP | 287 | 296 |
| TN | 95 | 86 |
| FN | 33 | 26 |
| AUC-PR | 0.5373 | 0.7262 |

HistGradientBoosting detecta 7 víctimas más que el árbol y reduce los falsos negativos de 33 a 26. Sin embargo, aumenta los falsos positivos de 287 a 296 y reduce algo la especificidad.

Conclusión: es el mejor candidato alternativo si el objetivo es aumentar ligeramente el recall manteniendo un rendimiento parecido. Pero la mejora es modesta y se pierde interpretabilidad.

---

## 5. Comparación principal: árbol actual vs mejor alternativa

El árbol actual tiene una gran ventaja metodológica: es extremadamente interpretable. Según las reglas exportadas, el modelo final se reduce a una única decisión sobre `PC2`:

```text
PC2 <= 0.54  → clase víctima
PC2 >  0.54  → clase no víctima
```

Esto facilita mucho la explicación del modelo en un artículo y ante profesionales no técnicos.

El mejor modelo alternativo observado es probablemente `HistGradientBoosting` con threshold 0.25. Su ventaja es que detecta más víctimas reales:

- 346 TP frente a 339 TP
- 26 FN frente a 33 FN

Pero esta mejora es pequeña y tiene costes:

- más falsos positivos;
- menor especificidad;
- menor transparencia;
- explicación más compleja;
- necesidad de justificar ajuste de umbral.

---

## 6. Conclusión técnica

Los modelos alternativos muestran mejor capacidad discriminativa global que el árbol cuando se observa AUC-PR o rendimiento con umbral 0.50. Sin embargo, cuando se ajustan los umbrales para mantener recall alto, las diferencias operativas respecto al árbol son pequeñas.

La principal conclusión es:

> Otros modelos como Logistic Regression, Random Forest, Gradient Boosting e HistGradientBoosting pueden alcanzar un recall similar o ligeramente superior al árbol, pero no ofrecen una mejora suficientemente clara en balanced accuracy, precision o specificity como para compensar la pérdida de interpretabilidad.

Por tanto, mantener el árbol de decisión como modelo final de victimización sigue siendo defendible, especialmente porque el objetivo del estudio no es únicamente maximizar rendimiento predictivo, sino construir una herramienta de cribado sensible e interpretable.

---

## 7. Redacción posible para el manuscrito

Una forma prudente de explicarlo sería:

> Additional supervised classifiers, including logistic regression, random forest, gradient boosting, and histogram-based gradient boosting, were explored using the same train/test partition and PCA-transformed predictors. Although ensemble-based models showed higher global ranking performance according to AUC-PR, their operating points under a high-recall screening criterion yielded performance very similar to the pruned decision tree. Given the marginal nature of these gains and the substantial loss of interpretability, the cost-complexity-pruned decision tree was retained as the final victimization classifier.

---

## 8. Recomendación final

Para el modelo de victimización, no cambiaría todavía el árbol por otro modelo.

La recomendación sería:

1. Mantener el Decision Tree como modelo principal por interpretabilidad.
2. Mencionar que se probaron modelos alternativos.
3. Usar los resultados de HistGradientBoosting como sensibilidad/comparación adicional.
4. No cambiar el modelo final salvo que se priorice estrictamente detectar algunos casos más a costa de más falsos positivos y menor explicabilidad.

En términos prácticos:

> El árbol actual no es el modelo con mejor AUC-PR, pero sí es el modelo más transparente que consigue el objetivo principal de recall alto.
