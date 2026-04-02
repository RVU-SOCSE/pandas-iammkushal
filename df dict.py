Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, 90, 78, 92],
    'Age': [20, 21, 19, 22]
   }
df = pd.DataFrame(data)
print(original DataFrame:")
      
SyntaxError: unterminated string literal (detected at line 1)
print("original DataFrame:")
      
original DataFrame:
print(df)
      
      Name  Marks  Age
0    Alice     85   20
1      Bob     90   21
2  Charlie     78   19
3    David     92   22
df['Final Marks'] = df['marks'] + 5
      
Traceback (most recent call last):
  File "C:\Users\KUSHAL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'marks'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    df['Final Marks'] = df['marks'] + 5
  File "C:\Users\KUSHAL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\KUSHAL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'marks'
>>> df['Final Marks'] = df['Marks'] + 5
>>> print("\nDataFrames after adding new column:")

DataFrames after adding new column:
>>> print(df)
      Name  Marks  Age  Final Marks
0    Alice     85   20           90
1      Bob     90   21           95
2  Charlie     78   19           83
3    David     92   22           97
