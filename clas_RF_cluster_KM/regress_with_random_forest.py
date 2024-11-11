
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def regress_with_random_forest(X_train, X_test, y_train, y_test):
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X_train, y_train)
    y_pred = rf_regressor.predict(X_test)
    metrics = {
        "mse": mean_squared_error(y_test, y_pred),
        "r2_score": r2_score(y_test, y_pred)
    }
    return metrics
