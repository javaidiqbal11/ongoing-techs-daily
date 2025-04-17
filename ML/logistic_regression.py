<<<<<<< HEAD
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X, y = X[y != 2], y[y != 2]  # binary classification
X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()
model.fit(X_train, y_train)
print("Accuracy:", model.score(X_test, y_test))

print("R^2 Score:", model.score(X_test, y_test))
=======
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X, y = X[y != 2], y[y != 2]  # binary classification
X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()
model.fit(X_train, y_train)
print("Accuracy:", model.score(X_test, y_test))

print("R^2 Score:", model.score(X_test, y_test))
>>>>>>> fe3148d6ec5888d057b34926b5c4db1ea0d9d59b
