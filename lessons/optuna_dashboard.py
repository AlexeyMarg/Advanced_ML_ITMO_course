# pip install optuna-dashboard


import optuna


def objective(trial):
    x = trial.suggest_float("x", -100, 100)
    y = trial.suggest_categorical("y", [-1, 0, 1])
    return x**2 + y


if __name__ == "__main__":
    study = optuna.create_study(
        storage="sqlite:///db.sqlite3",
        study_name="quadratic-simple-1",
    )
    study.optimize(objective, n_trials=100)
    print(f"Best value: {study.best_value} (params: {study.best_params})")


# optuna-dashboard sqlite:///db.sqlite3 --port 8090
