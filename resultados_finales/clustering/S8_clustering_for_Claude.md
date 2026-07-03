# S8 clustering inputs for Supplementary

Use these data to complete Supplementary Table S8.

## Important source decision

The clustering outputs are based on **n = 4,024**, not on the final analytical modelling sample of n = 3,767 used for S6/model predictors. Do not force S8 to n = 3,767 unless the manuscript explicitly decides to rerun clustering on the final analytical subset.

The files labelled `cluster_victima.csv` and `cluster_perpetrators.csv` are cross-tabs with outcome labels. They are not item-level cluster profile tables.

- `comb_56_results.csv` = selected **victimization clustering** solution, with 9 clusters.
- `cluster_perpetrators.csv` = perpetrator status within those 9 victimization clusters.
- `comb_130_results.csv` = selected **perpetration clustering** solution, with 5 clusters.
- `cluster_victima.csv` = victimization status within those 5 perpetration clusters.

Substantive labels such as “polyvictimization”, “online/sexual victimization”, or “high perpetration” should only be assigned if item-level profiles/loadings are available. With the files provided here, we can safely report cluster size and enrichment in the opposite outcome.

## S8A. Clustering solution summary

| Analysis                 | Selected artefact   |   Sample n |   Selected iteration | Dimensionality reduction   |   UMAP n_neighbors |   UMAP min_dist |   UMAP spread | Clustering algorithm   |   DBSCAN eps |   DBSCAN min_samples |   Number of clusters |   Silhouette | Cross-tab available                         | Interpretive note                                                                                                                                                                              |
|:-------------------------|:--------------------|-----------:|---------------------:|:---------------------------|-------------------:|----------------:|--------------:|:-----------------------|-------------:|---------------------:|---------------------:|-------------:|:--------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Victimization clustering | comb_56             |       4024 |                   56 | UMAP with Gower distance   |                 50 |            0.01 |           0.5 | DBSCAN                 |           10 |                    3 |                    9 |        0.913 | PERPETRADOR status by victimization cluster | Use for cluster sizes and perpetration enrichment. Substantive labels require item-level profiles.                                                                                             |
| Perpetration clustering  | comb_130            |       4024 |                  130 | UMAP with Gower distance   |                100 |            0.01 |           0.5 | DBSCAN                 |           10 |                    3 |                    5 |        0.93  | VÍCTIMA status by perpetration cluster      | Use for cluster sizes and victimization enrichment. Substantive labels require item-level profiles. Iteration 130 selected; iteration 131 tied on silhouette but is not the artefact provided. |

## S8B. Victimization cluster solution: cluster size and perpetration enrichment

|   cluster |    n |   % sample |   PERPETRADOR=1 n |   PERPETRADOR=1 % |   PERPETRADOR=0 n |   PERPETRADOR=0 % |
|----------:|-----:|-----------:|------------------:|------------------:|------------------:|------------------:|
|         0 | 2025 |       50.3 |               183 |              9.04 |              1842 |             90.96 |
|         1 |  206 |        5.1 |                57 |             27.67 |               149 |             72.33 |
|         2 |  125 |        3.1 |                35 |             28    |                90 |             72    |
|         3 | 1092 |       27.1 |               524 |             47.99 |               568 |             52.01 |
|         4 |   94 |        2.3 |                24 |             25.53 |                70 |             74.47 |
|         5 |  101 |        2.5 |                34 |             33.66 |                67 |             66.34 |
|         6 |  143 |        3.6 |                40 |             27.97 |               103 |             72.03 |
|         7 |  168 |        4.2 |                34 |             20.24 |               134 |             79.76 |
|         8 |   70 |        1.7 |                19 |             27.14 |                51 |             72.86 |

Suggested neutral description:

Victimization clustering identified nine groups. Cluster 0 was the largest group (n = 2,025; 50.3%) and showed the lowest perpetration rate (9.0%). Cluster 3 was the second largest group (n = 1,092; 27.1%) and showed the highest perpetration rate (48.0%). Smaller clusters showed perpetration rates between 20.2% and 33.7%.

## S8C. Perpetration cluster solution: cluster size and victimization enrichment

|   cluster |    n |   % sample |   VÍCTIMA=1 n |   VÍCTIMA=1 % |   VÍCTIMA=0 n |   VÍCTIMA=0 % |
|----------:|-----:|-----------:|--------------:|--------------:|--------------:|--------------:|
|         0 | 3121 |       77.6 |          1267 |         40.6  |          1854 |         59.4  |
|         1 |  149 |        3.7 |           106 |         71.14 |            43 |         28.86 |
|         2 |  266 |        6.6 |           237 |         89.1  |            29 |         10.9  |
|         3 |  297 |        7.4 |           264 |         88.89 |            33 |         11.11 |
|         4 |  191 |        4.7 |           139 |         72.77 |            52 |         27.23 |

Suggested neutral description:

Perpetration clustering identified five groups. Cluster 0 was the largest group (n = 3,121; 77.6%) and showed the lowest victimization rate (40.6%). Clusters 2 and 3 showed the highest victimization rates, approximately 89.1% and 88.9%, respectively. Clusters 1 and 4 also showed elevated victimization rates, approximately 71.1% and 72.8%.

## Recommended wording for the Supplementary note

Cluster analyses were conducted using UMAP with Gower distance followed by DBSCAN. For victimization, the selected solution corresponded to iteration 56, yielding nine clusters (silhouette = 0.913). For perpetration, the selected solution corresponded to iteration 130, yielding five clusters (silhouette = 0.930). Cluster labels are reported numerically because the available artefacts provide cluster membership and cross-tabulations with the opposite outcome, but not item-level profiles sufficient for definitive substantive labelling.

## What remains pending if stronger labels are required

To assign substantive labels to each cluster, the following is needed:

1. A table with item-level prevalence or mean scores by cluster.
2. The original victimization/perpetration items used before UMAP.
3. Or a cluster profile report listing the most discriminating items per cluster.

Without that, S8 should remain neutral and report cluster numbers, size, and victimization/perpetration enrichment.
