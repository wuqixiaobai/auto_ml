# This file is just to test passing a bunch of different parameters into train to make sure that things work
# At first, it is not necessarily testing whether those things have the intended effect or not

import os
import sys
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path

from auto_ml import Predictor

import dill
from nose.tools import assert_equal, assert_not_equal, with_setup
from sklearn.model_selection import train_test_split

import utils_testing as utils


# Tests on regression models:

# Right now this hangs when I run it locally. Some kind of parallelization bug with scikit-learn's GridSearchCV, since we have already run GridSearchCV for classifiers
# def test_optimize_final_model_regression():
#     df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

#     column_descriptions = {
#         'MEDV': 'output'
#         , 'CHAS': 'categorical'
#     }

#     ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

#     ml_predictor.train(df_boston_train, optimize_final_model=True)

#     test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

#     print('test_score')
#     print(test_score)

#     assert -3.2 < test_score < -2.8


def test_perform_feature_selection_true_regression():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    ml_predictor.train(df_boston_train, perform_feature_selection=True)

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    # Bumping this up since without these features our score drops
    assert -4.0 < test_score < -2.8

def test_perform_feature_selection_false_regression():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    ml_predictor.train(df_boston_train, perform_feature_selection=False)

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    assert -3.2 < test_score < -2.8


def test_perform_feature_scaling_true_regression():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    ml_predictor.train(df_boston_train, perform_feature_scaling=True)

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    assert -3.2 < test_score < -2.8

def test_perform_feature_scaling_false_regression():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    ml_predictor.train(df_boston_train, perform_feature_scaling=False)

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    assert -3.2 < test_score < -2.8


def test_optimize_entire_pipeline_regression():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    ml_predictor.train(df_boston_train, optimize_entire_pipeline=True)

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    assert -3.2 < test_score < -2.8


def test_X_test_and_y_test_regression():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    print(df_boston_test)
    ml_predictor.train(df_boston_train, X_test=df_boston_test, y_test=df_boston_test.MEDV)
    print(df_boston_test)

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    assert -3.2 < test_score < -2.8


def test_compute_power_1_regression():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    ml_predictor.train(df_boston_train, compute_power=1)

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    assert -3.2 < test_score < -2.8

def test_all_algos_regression():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    ml_predictor.train(df_boston_train, model_names=['LinearRegression', 'RandomForestRegressor', 'Ridge', 'GradientBoostingRegressor', 'ExtraTreesRegressor', 'AdaBoostRegressor', 'SGDRegressor', 'PassiveAggressiveRegressor'])

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    assert -3.2 < test_score < -2.8

# If the user passes in X_test and y_test, we will use those to determine the best model, rather than CV scores
def test_select_from_multiple_regression_models_using_X_test_and_y_test():
    df_boston_train, df_boston_test = utils.get_boston_regression_dataset()

    column_descriptions = {
        'MEDV': 'output'
        , 'CHAS': 'categorical'
    }

    ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)

    ml_predictor.train(df_boston_train, model_names=['LinearRegression', 'RandomForestRegressor', 'Ridge', 'GradientBoostingRegressor', 'ExtraTreesRegressor', 'AdaBoostRegressor', 'SGDRegressor', 'PassiveAggressiveRegressor'], X_test=df_boston_test, y_test=df_boston_test.MEDV)

    test_score = ml_predictor.score(df_boston_test, df_boston_test.MEDV)

    print('test_score')
    print(test_score)

    assert -3.2 < test_score < -2.8



# def test_compute_power_10():
#     df_titanic_train, df_titanic_test = utils.get_titanic_binary_classification_dataset()

#     # This test tries something like 2,000 different combinations of hyperparameters for the pipeline
#     # To make this more reasonable, we'll cut down the data size to be a fraction of it's full size, so we are just testing whether everything runs
#     df_titanic_train, df_titanic_train_ignore = train_test_split(df_titanic_train, train_size=0.1, random_state=42)


#     column_descriptions = {
#         'survived': 'output'
#         , 'embarked': 'categorical'
#         , 'pclass': 'categorical'
#     }

#     ml_predictor = Predictor(type_of_estimator='classifier', column_descriptions=column_descriptions)

#     ml_predictor.train(df_titanic_train, compute_power=10)

#     test_score = ml_predictor.score(df_titanic_test, df_titanic_test.survived)

#     print('test_score')
#     print(test_score)

#     assert -0.215 < test_score < -0.17


# TODO: run tests for each of the different models
# TODO: test for picking the best model automatically
# optimize_entire_pipeline
# X_test, y_test
# take_log_of_y
# ideally something about XGB not needing to be installed, but running if it is installed
# Dates
# NLP
# train ml ensemble
# ideally use XGB
# print results for linear model
# Try passing in a list of dictionaries everywhere (train, predict, predict_proba, score, on both the saved pipeline and the ml_predictor object)
# call predict and predict_proba on the ml_predictor object, not just the final pipeline
# Test the num_features for standard problem (should be all of them). Then test num_features if we pass in a ton of duplicate columns where it should be removing some features. then same thing, but perform_feature_selection=False. we can get the num_features from the final trained model. even if some features are not useful, we should be able to see the number of features the model has considered.

