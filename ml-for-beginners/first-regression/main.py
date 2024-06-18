import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, model_selection


def main():
    X, y = datasets.load_diabetes(return_X_y=True)

    X = X[:, 2]
    X = X.reshape(-1, 1)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33)

    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    plt.scatter(X_test, y_test, color='black')
    plt.plot(X_test, y_pred, color='blue', linewidth=3)
    plt.xlabel('Scale BMIs')
    plt.ylabel('Disease Progression')
    plt.title('A Graph Plot Showing Diabetes Porgression Against BMI')
    
    plt.show()

main()
