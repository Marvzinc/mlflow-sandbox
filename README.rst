MLflow Sandbox
==============

Train a ML model in Scikit-learn for sentiment classification, while keeping track of the performance of the different models via MLflow.
The optimal model is found by exploring the model search space through GridSearch (Bayesian optimization is on the TODO list..).

The search space has two dimensions:

- Different vectorizer settings: ngram sizes
- Different classifiers and classifier settings: Naive Bayes, Random Forest and Support Vector Machines.


After evaluating all the models their performance, the best model is selected. This model then trained on the complete corpus.


============
Dependencies
============
This project has the following dependencies:

- Dependencies
    - `Large Movie Review Dataset <http://ai.stanford.edu/~amaas/data/sentiment/>`_ from Stanford (already included in the repo)
    - `Git LFS <https://git-lfs.github.com/>`_
    - Python >= 3.7
    - `Docker <https://www.docker.com/>`_
    - Optional: `Poetry <https://python-poetry.org/>`_

=====
Setup
=====

1. Install Git LFS on your machine

.. code-block:: bash

   $ git lfs install --system --skip-repo

2. Clone the repo

3. Create a virtual environment with at least Python 3.7 via the tool of your choice (conda, venv, etc.)

4. Install the Python dependencies

Using poetry:

.. code-block:: bash

   $ poetry install

Not using poetry:

.. code-block:: bash

   $ pip install -r requirements.txt


5. Create the directories :code:`database` and :code:`artifact` in the :code:`data` directory

.. code-block:: bash

   $ cd data
   $ mkdir database
   $ mkdir artifacts

============
Train models
============

1. Run MLflow server via the code shown below. This Makefile command starts up the Postgres database and the MLflow server.
The MLflow server is accessible via *localhost:5000*.

.. code-block:: bash

   $ make mlflow-server

With the current configuration the statistics are stored in the Postgres database, whereas the artifacts are stored on your disk.
For production I would recommend using a SQL instance in the Cloud for the statistics and blob storage for the artifacts.


2. Train the different ML models using Scikit-learn.
After the run is finished the parameters and metrics (performance) of each models is
visible in the corresponding experiment in the MLFlow dashboard

.. code-block:: bash

   $ python train_hp_optimizer.py

3. Train the best model on the complete dataset and evaluate performance on the test dataset

.. code-block:: bash

   $ python train_best_model.py

4. The best model is stored in the directory :code:`trained_model` in the subdirectory with the corresponding experiment name.
The :code:`model.pkl` is your trained ML model that can be utilized to make predictions!

