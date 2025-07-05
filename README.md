# band_gap_prediction_in_perovskite

This project uses the `castelli_perovskites` dataset from **matminer** to predict the band gap of perovskite materials using a Random Forest Regressor.

## 📊 Features

- Element extraction from chemical formulas (A, B, X sites)
- One-hot encoding of categorical features
- Random forest regression model
- Mean Absolute Error (MAE) evaluation

## Output

Number of entries: 18928
Columns: ['fermi level', 'fermi width', 'e_form', 'gap is direct', 'structure', 'mu_b', 'formula', 'vbm', 'cbm', 'gap gllbsc']
   fermi level  fermi width  e_form  ...       vbm       cbm  gap gllbsc
0     0.312138     0.001837    2.16  ...  6.187694  6.187694         0.0
1     0.297083     0.001837    1.52  ...  6.033125  6.033125         0.0
2     0.191139     0.003675    1.48  ...  6.602253  6.602253         0.0
3     0.316346     0.001837    1.24  ...  5.738462  5.738462         0.0
4     0.312658     0.003675    0.62  ...  6.074736  6.074736         0.0
5     0.216044     0.003675    1.48  ...  5.592776  5.592776         0.0
6     0.199250     0.003675    1.56  ...  6.621218  6.621218         0.0
7     0.370045     0.001837    1.20  ...  5.924195  5.924195         0.0
8     0.295014     0.001837    1.62  ...  6.053350  6.053350         0.0
9     0.117971     0.001837    3.16  ...  4.876054  4.876054         0.0

[10 rows x 10 columns]
        fermi level   fermi width  ...           cbm    gap gllbsc
count  18928.000000  18928.000000  ...  18928.000000  18928.000000
mean       0.213770      0.002362  ...      5.782879      0.070813
std        0.082382      0.000830  ...      0.530577      0.459684
min       -0.096153      0.001837  ...      1.474852      0.000000
25%        0.163024      0.001837  ...      5.475086      0.000000
50%        0.216352      0.001837  ...      5.819146      0.000000
75%        0.267705      0.003675  ...      6.128552      0.000000
max        0.524917      0.003675  ...      7.222349      7.000000

[8 rows x 7 columns]
<class 'pandas.core.frame.DataFrame'>
Index: 18928 entries, 0 to 18927
Data columns (total 10 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   fermi level    18928 non-null  float64
 1   fermi width    18928 non-null  float64
 2   e_form         18928 non-null  float64
 3   gap is direct  18928 non-null  bool   
 4   structure      18928 non-null  object 
 5   mu_b           18928 non-null  float64
 6   formula        18928 non-null  object 
 7   vbm            18928 non-null  float64
 8   cbm            18928 non-null  float64
 9   gap gllbsc     18928 non-null  float64
dtypes: bool(1), float64(7), object(2)
memory usage: 1.5+ MB
None
fermi level      0
fermi width      0
e_form           0
gap is direct    0
structure        0
mu_b             0
formula          0
vbm              0
cbm              0
gap gllbsc       0
dtype: int64
Filtered dataset size: 18928
Features shape: (18928, 9)
Target shape: (18928,)
Encoded features shape: (18928, 121)
Mean Absolute Error: 0.005 eV
