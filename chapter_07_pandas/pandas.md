# Pandas

![panda](docs/kung_fu_panda.jpg)

Pandas is quite useful when there is no need for classes.
When we get tabular data from data storage, we could map
each row to a class object, like we do in OO programming,
or we could use these rows in the table container directly.
These 2 case make up roughly 90% of the usage, the rest of
the cases are customization, e.g., using a namedtuple.

Pandas steps further with more tabular operations, such
as aggregation, pivoting, etc. These operations are tabular 
data generic, we may carry out them in SQL or Pandas.

Pandas is built on top of NumPy.

https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html

## Data Input and Output

can read csv, excel, database, json
pandas is python's version of excel, and more.

[imdb 2006-2016](https://www.kaggle.com/PromptCloudHQ/imdb-data),

find good data sets
not too big
big enough to demo
common sense operations


IO performance
missing data
drop_duplicates

## Slice and Dice
cell level ops
row level ops,

## Index & Filter
table level ops.
sorting

## Data Combining
merge join concatenation append

## Reshape
stack, melt, reshape
performance - use built in functions whenever possible.

## Aggregation
group by, pivot
cumsum, row sum
https://www.dezyre.com/recipes/get-descriptive-statistics-of-pandas-dataframe

To address multi-core/parallel and big data size issues,  
dask, vaex, modin  
https://github.com/databricks/koalas  
https://arrow.apache.org/


## Modin
https://modin.readthedocs.io/en/latest/
https://discuss.modin.org/t/profile-modin-line-by-line/65
Use exsiting.
https://www.pluralsight.com/guides/explore-python-libraries:-make-your-dataframes-parallel-with-modin

https://www.kdnuggets.com/2019/11/speed-up-pandas-4x.html
https://pythondata.com/quick-tip-speed-up-pandas-using-modin/
https://sefiks.com/2019/04/23/how-modin-can-keep-data-scientists-from-pandas/
https://softwareengineeringdaily.com/2020/08/26/in-with-the-new-python-plotting-and-data-wrangling-libraries/
https://vaex.io/blog/beyond-pandas-spark-dask-vaex-and-other-big-data-technologies-battling-head-to-head

Dask does not work, gets errors and hangs.
```pip install modin[dask]``` or ```conda install -c conda-forge modin```

This works
```pip install modin[ray]```

https://blog.dask.org/2019/01/13/dask-cudf-first-steps

https://cloudpy.io/

## Parallel

## References

Tutorials:
- https://www.tutorialspoint.com/python_pandas/index.htm
- https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
- https://www.geeksforgeeks.org/pandas-tutorial/
- https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
- https://www.kaggle.com/learn/pandas
- https://www.dataquest.io/blog/pandas-python-tutorial/
- https://www.w3resource.com/pandas/index.php

Books:
- Python Data Science Handbook


pyspark

Airflow
petl:
https://www.cdata.com/kb/tech/rest-python-petl.rst
https://www.sentia.com.au/blog/a-quick-dive-into-data-transformation-and-migration-with-petl
https://www.linkedin.com/pulse/easy-etl-python-beginners-oscar-valles/
https://www.xplenty.com/blog/comparison-of-the-top-python-etl-tools/

https://github.com/jtablesaw/tablesaw


 






