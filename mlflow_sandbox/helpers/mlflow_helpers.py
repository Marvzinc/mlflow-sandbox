from datetime import datetime
from typing import Optional, Tuple

import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
from sklearn.pipeline import Pipeline


def create_experiment(base_name: str) -> mlflow.entities.experiment.Experiment:
    uid = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    experiment_id = mlflow.create_experiment(name=f"{base_name}_{uid}")
    return mlflow.get_experiment(experiment_id=experiment_id)


def get_experiment(
    experiment_name: Optional[str],
) -> mlflow.entities.experiment.Experiment:

    client = MlflowClient()
    experiments = client.list_experiments()

    # Return most recent experiment if the user did not provide an experiment
    if not experiment_name:
        return max(
            [experiment for experiment in experiments],
            key=lambda exp: int(exp.experiment_id),
        )

    # Return the experiment provided by the user if it exists
    experiment = [
        experiment for experiment in experiments if experiment.name == experiment_name
    ]

    if not experiment:
        raise ValueError(f"Experiment {experiment_name} does not exist")

    return experiment[0]


def get_best_model(experiment_id: str) -> Tuple[str, Pipeline]:
    run_id = mlflow.search_runs(
        experiment_ids=experiment_id, filter_string="tag.best_model='True'"
    ).run_id[0]
    return run_id, mlflow.sklearn.load_model(f"runs:/{run_id}/model")
