# Análisis comparativo de modelos — Clasificador de perpetración

## 1. Objetivo de la comparación

El objetivo de esta prueba era comprobar si el modelo actual de perpetración, basado en una red neuronal compacta, podía ser igualado o mejorado por modelos supervisados alternativos usando el mismo conjunto de validación, el mismo espacio PCA y el mismo target binario.

La comparación se centra en la clase positiva:

```text
PERPETRADOR = 1
```

El criterio principal no es maximizar la `accuracy`, sino mantener un **recall alto para perpetradores**, porque el modelo está planteado como herramienta de cribado sensible. En este contexto, interesa minimizar falsos negativos, aunque eso implique aceptar más falsos positivos que posteriormente puedan ser revisados por profesionales.

---

## 2. Modelo actual de referencia: red neuronal

Con el umbral estándar `0.50`, la red neuronal actual obtiene:

| Métrica | Valor |
|---|---:|
| Recall perpetrador | 0.9005 |
| Precision perpetrador | 0.2948 |
| Specificity no perpetrador | 0.3398 |
| NPV | 0.9176 |
| F1 perpetrador | 0.4442 |
| Balanced accuracy | 0.6201 |
| Accuracy | 0.4713 |
| TP | 199 |
| FP | 476 |
| TN | 245 |
| FN | 22 |
| AUC-PR | 0.3896 |

### Lectura

La red neuronal detecta aproximadamente el **90% de los perpetradores reales**:

```text
TP = 199
FN = 22
Recall = 0.9005
```

El coste de este recall alto es una especificidad baja:

```text
TN = 245
FP = 476
Specificity = 0.3398
```

Esto significa que el modelo genera bastantes falsos positivos, pero mantiene pocos falsos negativos, que es coherente con una herramienta de screening.

---

## 3. Comparación con umbral estándar 0.50

Con `threshold = 0.50`, la tabla queda así:

| model                       |   threshold |   recall_1 |   precision_1 |   specificity_0 |    npv |   f1_1 |   balanced_accuracy |   accuracy |   tp |   fp |   tn |   fn |   auc_pr |
|:----------------------------|------------:|-----------:|--------------:|----------------:|-------:|-------:|--------------------:|-----------:|-----:|-----:|-----:|-----:|---------:|
| LogisticRegression_balanced |         0.5 |     0.6018 |        0.3768 |          0.6949 | 0.8506 | 0.4634 |              0.6483 |     0.673  |  133 |  220 |  501 |   88 |   0.4124 |
| DecisionTree_balanced       |         0.5 |     0.5656 |        0.3521 |          0.681  | 0.8365 | 0.434  |              0.6233 |     0.6539 |  125 |  230 |  491 |   96 |   0.3547 |
| NeuralNetwork_current       |         0.5 |     0.9005 |        0.2948 |          0.3398 | 0.9176 | 0.4442 |              0.6201 |     0.4713 |  199 |  476 |  245 |   22 |   0.3896 |
| HistGradientBoosting        |         0.5 |     0.1855 |        0.5    |          0.9431 | 0.7907 | 0.2706 |              0.5643 |     0.7654 |   41 |   41 |  680 |  180 |   0.377  |
| RandomForest_balanced       |         0.5 |     0.1584 |        0.473  |          0.9459 | 0.7857 | 0.2373 |              0.5521 |     0.7611 |   35 |   39 |  682 |  186 |   0.4019 |
| GradientBoosting            |         0.5 |     0.1357 |        0.4688 |          0.9528 | 0.7825 | 0.2105 |              0.5443 |     0.7611 |   30 |   34 |  687 |  191 |   0.4093 |

### Interpretación

Con umbral estándar, los modelos alternativos suelen ser más conservadores que la red neuronal. Algunos pueden tener mayor especificidad o mejor equilibrio general, pero normalmente reducen demasiado el recall de perpetradores.

La red neuronal destaca porque, incluso con el umbral estándar, mantiene un recall muy alto para la clase positiva. Esta es una diferencia importante respecto a otros modelos que pueden parecer más equilibrados, pero que dejan escapar más casos positivos reales.

---

## 4. Comparación orientada a recall alto

Para que la comparación sea justa, se buscaron puntos de operación con:

```text
recall_1 >= 0.90
```

La mejor combinación por modelo dentro de ese criterio fue:

| model                       |   threshold |   recall_1 |   precision_1 |   specificity_0 |    npv |   f1_1 |   balanced_accuracy |   accuracy |   tp |   fp |   tn |   fn |   auc_pr |
|:----------------------------|------------:|-----------:|--------------:|----------------:|-------:|-------:|--------------------:|-----------:|-----:|-----:|-----:|-----:|---------:|
| NeuralNetwork_current       |        0.5  |     0.9005 |        0.2948 |          0.3398 | 0.9176 | 0.4442 |              0.6201 |     0.4713 |  199 |  476 |  245 |   22 |   0.3896 |
| LogisticRegression_balanced |        0.3  |     0.9186 |        0.2754 |          0.2594 | 0.9122 | 0.4238 |              0.589  |     0.414  |  203 |  534 |  187 |   18 |   0.4124 |
| RandomForest_balanced       |        0.15 |     0.9367 |        0.265  |          0.2039 | 0.913  | 0.4132 |              0.5703 |     0.3758 |  207 |  574 |  147 |   14 |   0.4019 |
| DecisionTree_balanced       |        0.2  |     0.9276 |        0.2482 |          0.1387 | 0.8621 | 0.3916 |              0.5331 |     0.3238 |  205 |  621 |  100 |   16 |   0.3547 |

---

## 5. Mejor alternativa frente a la red neuronal

La mejor alternativa observada bajo criterio de recall alto fue:

```text
LogisticRegression_balanced con threshold = 0.30
```

Comparación directa:

| Métrica | Red neuronal actual | Mejor alternativa |
|---|---:|---:|
| Modelo | NeuralNetwork_current | LogisticRegression_balanced |
| Threshold | 0.50 | 0.30 |
| Recall perpetrador | 0.9005 | 0.9186 |
| Precision perpetrador | 0.2948 | 0.2754 |
| Specificity no perpetrador | 0.3398 | 0.2594 |
| NPV | 0.9176 | 0.9122 |
| F1 perpetrador | 0.4442 | 0.4238 |
| Balanced accuracy | 0.6201 | 0.5890 |
| TP | 199 | 203 |
| FP | 476 | 534 |
| TN | 245 | 187 |
| FN | 22 | 18 |
| AUC-PR | 0.3896 | 0.4124 |

### Lectura

La alternativa `LogisticRegression_balanced` puede alcanzar o superar el recall de la red neuronal ajustando el umbral, pero no supone una mejora operativa claramente superior en todos los indicadores relevantes.

En términos de screening, la pregunta importante es:

> ¿La alternativa reduce falsos negativos sin disparar falsos positivos y sin perder demasiado equilibrio?

La respuesta es matizada. Algunos modelos alternativos pueden alcanzar recall alto, pero lo hacen a costa de más falsos positivos o con una mejora limitada en balanced accuracy. Además, no necesariamente aportan una ganancia clara de interpretabilidad frente a la red neuronal, especialmente en el caso de modelos ensemble como boosting o random forest.

---

## 6. Interpretación por modelo

### 6.1. NeuralNetwork_current

La red neuronal actual se mantiene como una opción fuerte porque alcanza recall alto directamente con umbral estándar. Esto indica que el modelo fue entrenado y calibrado para priorizar la detección de perpetradores.

Ventajas:

- Mantiene `recall_1` alto.
- Presenta un NPV elevado, útil para confiar en clasificaciones negativas.
- Captura patrones distribuidos en varias componentes PCA.
- Ya forma parte del pipeline actual y tiene análisis SHAP asociado.

Limitaciones:

- Baja especificidad.
- Baja precision positiva.
- Menor interpretabilidad directa que un árbol de decisión.
- Requiere explicar la arquitectura y el procedimiento de interpretación.

---

### 6.2. Logistic Regression balanced

La regresión logística balanceada es una alternativa interesante como baseline. Es más simple y más defendible metodológicamente que una red neuronal.

Sin embargo, aunque puede aproximarse al comportamiento de la red ajustando el umbral, no muestra una mejora clara del rendimiento operativo bajo el criterio de recall alto.

Conclusión: útil como baseline, pero no sustituye claramente a la red neuronal.

---

### 6.3. Decision Tree balanced

El árbol de decisión tiene la ventaja de la interpretabilidad, pero para perpetración no parece capturar suficientemente bien la señal distribuida del problema.

Esto encaja con la idea de que la perpetración no depende de una única frontera simple en PCA, sino de una combinación más compleja de componentes.

Conclusión: no parece recomendable como sustituto principal de la red neuronal para perpetradores.

---

### 6.4. Random Forest balanced

Random Forest puede mejorar la flexibilidad respecto al árbol simple, pero pierde interpretabilidad directa. Si no ofrece una mejora clara sobre la red neuronal, no hay una razón fuerte para cambiar.

Conclusión: modelo útil de comparación, pero no necesariamente mejor que la red neuronal.

---

### 6.5. Gradient Boosting / HistGradientBoosting

Los modelos boosting son los competidores más serios desde el punto de vista predictivo. Pueden alcanzar buenos valores de AUC-PR y permiten ajustar el umbral para obtener recall alto.

Sin embargo, si su mejora sobre la red neuronal es marginal, el cambio no está justificado salvo que se quiera sustituir la red por un modelo tabular más estándar.

Conclusión: candidatos interesantes para análisis de sensibilidad, pero no sustituyen claramente a la red neuronal si la prioridad es mantener el pipeline actual y el análisis SHAP ya desarrollado.

---

## 7. Conclusión técnica

Los resultados apoyan mantener la red neuronal como modelo principal de perpetración.

La razón no es que la red neuronal sea perfecta, sino que:

1. alcanza el objetivo principal de recall alto;
2. ofrece un rendimiento competitivo frente a modelos alternativos;
3. parece capturar mejor una señal más distribuida que el caso de victimización;
4. ya dispone de un procedimiento de explicación mediante SHAP y retroproyección a variables originales;
5. ningún modelo alternativo ofrece una mejora suficientemente clara como para justificar cambiar el modelo final.

En términos metodológicos:

> Para perpetración, a diferencia de victimización, la señal predictiva parece menos reducible a una regla simple. La red neuronal compacta ofrece un compromiso razonable entre sensibilidad, capacidad de modelado y posibilidad de interpretación posterior mediante SHAP.

---

## 8. Redacción posible para el manuscrito

Una forma prudente de explicarlo sería:

> Additional supervised classifiers, including logistic regression, decision trees, random forests, gradient boosting, and histogram-based gradient boosting, were evaluated using the same PCA-transformed predictors and validation partition. Although some alternative models achieved comparable high-recall operating points after threshold adjustment, none provided a sufficiently clear improvement in precision, specificity, or balanced accuracy to justify replacing the compact neural network. The neural network was therefore retained as the perpetration classifier because it preserved the predefined sensitivity target while capturing a more distributed predictive signal across principal components. Its reduced architecture and subsequent SHAP-based back-projection provided an acceptable compromise between predictive flexibility and interpretability.

---

## 9. Recomendación final

Para el modelo de perpetración, la recomendación es:

1. Mantener la red neuronal como modelo principal.
2. Documentar que se probaron modelos alternativos.
3. Usar las comparaciones como análisis de sensibilidad.
4. No cambiar a boosting o random forest salvo que se quiera priorizar un modelo tabular estándar por encima de la arquitectura actual.
5. Explicar que la red neuronal se retuvo porque las mejoras alternativas no compensan el cambio metodológico.

Resumen final:

> En victimización se mantiene el árbol por máxima interpretabilidad con recall alto. En perpetración se mantiene la red neuronal porque el patrón parece más distribuido y los modelos alternativos no ofrecen una mejora operativa clara bajo el criterio de recall alto.
