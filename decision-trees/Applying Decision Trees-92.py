## 2. Using Decision Trees With scikit-learn ##

from sklearn.tree import DecisionTreeClassifier

# A list of columns to train with
# We've already converted all columns to numeric
columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

# Instantiate the classifier
# Set random_state to 1 to make sure the results are consistent
clf = DecisionTreeClassifier(random_state=1)

# We've already loaded the variable "income," which contains all of the income data
clf.fit(income[columns], income["high_income"])

## 3. Splitting the Data into Train and Test Sets ##

import numpy
import math

# Set a random seed so the shuffle is the same every time
numpy.random.seed(1)

# Shuffle the rows  
# This permutes the index randomly using numpy.random.permutation
# Then, it reindexes the dataframe with the result
# The net effect is to put the rows into random order
income = income.reindex(numpy.random.permutation(income.index))

train_max_row = math.floor(income.shape[0] * .8)
train = income.iloc[:train_max_row]
test = income.iloc[train_max_row:]

## 4. Evaluating Error With AUC ##

from sklearn.metrics import roc_auc_score

clf = DecisionTreeClassifier(random_state=1)
clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
error = roc_auc_score(test["high_income"], predictions)
print(error)

## 5. Computing Error on the Training Set ##

predictions = clf.predict(train[columns])
print(roc_auc_score(train["high_income"], predictions))