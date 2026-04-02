Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
df = pd.read_csv("C:/Users/KUSHAL/Downloads/mcd.csv")
print("original DataFrame:")
original DataFrame:
print(df.head())
     Item  Calories  Price  Rating
0  Burger     250.0    5.0     4.2
1   Fries     300.0    3.0     4.0
2    Coke       NaN    2.0     3.8
3   Pizza     400.0    NaN     4.5
4    Wrap     350.0    4.5     NaN
>>> print("\n missing values in each column:")

 missing values in each column:
>>> print(df.insull().sum())
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(df.insull().sum())
  File "C:\Users\KUSHAL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'insull'. Did you mean: 'isnull'?
>>> print(df.isnull().sum())
Item        0
Calories    1
Price       1
Rating      1
dtype: int64
>>> df_filled = df.fillna(df.mean(numeric_only=True))
>>> print("\nDataFrame after filling missing values:")

DataFrame after filling missing values:
>>> print(df_filled.head())
     Item  Calories  Price  Rating
0  Burger     250.0  5.000   4.200
1   Fries     300.0  3.000   4.000
2    Coke     325.0  2.000   3.800
3   Pizza     400.0  3.625   4.500
4    Wrap     350.0  4.500   4.125
