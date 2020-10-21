import pickle
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import category_encoders as ce
from sklearn.impute import SimpleImputer

df = pd.read_csv('./data.csv')
df = df[:2000]

target = 'danceability'
features = df.columns.drop(target)

def build_model(df, target, features):
    X = df[features]
    y = df[target]
    X_train, y_train, x_test, y_test = train_test_split(X, y,
    test_size=0.33, random_state=42)

    model = make_pipeline(
      ce.OrdinalEncoder(),
      SimpleImputer(strategy='median'),
      RandomForestRegressor(random_state=42)
    )

    model.fit(X,y)

    print("Train model score:", model.score(X_train, y_train))
    print("Validation model score:", model.score(X_val, y_val))
    print("Test model score:", model.score(X_test, y_test))

if __name__ == '__main__':
    build_model(df, target, features)
