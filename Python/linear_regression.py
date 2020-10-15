import numpy as np

def lin_reg_pred(x1, x2, y_train, x_test1, x_test2):
    """
    linear regression
    input : training data in list of float
    output : list of total user prediction in float
    >>> lin_reg_pred([2,3,4,5], [3,1,2,4],[5,3,4,6], [2,1], [2,2])
    5.000000000000003
    """
    x = []
    for i in range(len(x1)):
        x.append([1, x1[i], x2[i]])
    x = np.array(x)
    y = np.array(y_train)
    beta = np.dot(np.dot(np.linalg.inv(np.dot(x.transpose(), x)), x.transpose()), y)
    prediction = abs(beta[0] + x_test1[0] * beta[1] + x_test2[0] + beta[2])
    return [prediction]


temp = lin_reg_pred([2,3,4,5], [3,1,2,4],[5,3,4,6], [2,1], [2,2])
print(temp)
