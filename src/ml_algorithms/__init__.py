from ml_algorithms.algorithms import MLAlgorithms
from ml_algorithms.algorithms import MLResults as mr


def get_comparison(data_path: str):
    """[summary]

    Args:
        data_path (str): [description]
    """
    algorithm = MLAlgorithms(data_path)

    knn_result = algorithm.k_nearest_neighbors(n_neighbors=4)
    decision_tree_result = algorithm.decision_tree()
    logistic_regression_result = algorithm.logistic_regression()
    naive_bayes_result = algorithm.naive_bayes()
    random_forest_result = algorithm.random_forest(n_estimators=100)
    # support_vector_machines_results =
    # algorithm.support_vector_machines(kernel='linear')

    print("#####################################################")
    print("KNN results")
    print("#####################################################")
    mr.get_accuracy(algorithm.y_test, knn_result, verbose=True)
    mr.get_class_report(algorithm.y_test, knn_result, verbose=True)
    mr.get_confusion_matrix(algorithm.y_test, knn_result, verbose=True)

    print("#####################################################")
    print("decision_tree results")
    print("#####################################################")
    mr.get_accuracy(algorithm.y_test, decision_tree_result, verbose=True)
    mr.get_class_report(algorithm.y_test, decision_tree_result, verbose=True)
    mr.get_confusion_matrix(
        algorithm.y_test, decision_tree_result, verbose=True
    )

    print("#####################################################")
    print("logistic_regression results")
    print("#####################################################")
    mr.get_accuracy(algorithm.y_test, logistic_regression_result, verbose=True)
    mr.get_class_report(
        algorithm.y_test, logistic_regression_result, verbose=True
    )
    mr.get_confusion_matrix(
        algorithm.y_test, logistic_regression_result, verbose=True
    )

    print("#####################################################")
    print("naive_bayes results")
    print("#####################################################")
    mr.get_accuracy(algorithm.y_test, naive_bayes_result, verbose=True)
    mr.get_class_report(algorithm.y_test, naive_bayes_result, verbose=True)
    mr.get_confusion_matrix(algorithm.y_test, naive_bayes_result, verbose=True)

    print("#####################################################")
    print("random_forest results")
    print("#####################################################")
    mr.get_accuracy(algorithm.y_test, random_forest_result, verbose=True)
    mr.get_class_report(algorithm.y_test, random_forest_result, verbose=True)
    mr.get_confusion_matrix(
        algorithm.y_test, random_forest_result, verbose=True
    )

    print("Algorithms compared successfuly!")
