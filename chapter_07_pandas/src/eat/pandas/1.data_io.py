import pandas

# use csv in this example
imdb_df = pandas.read_csv('IMDB-Movie-Data_2006-2016.csv')
print(imdb_df.info())
print(imdb_df.shape)

print(imdb_df.head(10))
print(imdb_df.tail(10))
# output is truncated, want to see more

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html
pandas.set_option('display.max_rows', 20)
pandas.set_option('display.max_columns', 20)
pandas.set_option('display.width', 120)

print(imdb_df.head(10))
print(imdb_df.tail(10))
# more data showed

print(imdb_df.describe())  # we can call this on columns as well
print(imdb_df.columns)
print(imdb_df['Title'])  # select column

# missing data, could be '', ' ', NaN, nan, '-', etc
print('-' * 80)
print(imdb_df.isnull().sum())  # we can call this on columns too

# first, we need to detect missing values
# secondly, we need to evaluate the impact on later operations in order to
# know how to deal with missing values, remove them or keep them, and if
# we keep them, what proper values they should be.


# duplicated data
print('-' * 80)
print(imdb_df['Title'].duplicated())
print(imdb_df[imdb_df['Title'].duplicated()])  # The Host is duplicated.

print('-' * 80)
print(imdb_df.duplicated(['Title', 'Director']))
print(imdb_df[imdb_df.duplicated(['Title', 'Director'])])

# data clean
# https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b

imdb_df.to_csv('/tmp/imdb_1000.csv')

# create new data frames
# pandas is column based
