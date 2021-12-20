import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

def estimate_coef(x, y):

    # количество наблюдений / баллов
    n = np.size(x)

    # среднее значение вектора x и y
    m_x, m_y = np.mean(x), np.mean(y)

    # вычисление перекрестного отклонения и отклонения о х
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # вычисление коэффициентов регрессии
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return(b_0, b_1)


def plot_regression_line(x, y, b):
    # построение фактических точек в виде точечной диаграммы
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    # предсказанный вектор ответа
    y_pred = b[0] + b[1]*x

    # построение линии регрессии
    plt.plot(x, y_pred, color = "g")
    
    # нанесение ярлыков
    plt.xlabel('gazprom')
    plt.ylabel('oil in barel')
    # функция показа сюжета
    plt.show()

def main():

    # наблюдения
    gazprom = np.array([5.01,4.74,5.02,4.56,4.97,4.77,4.69,5.05,7.54,7.85,7.39,6.98,6.95,8.28,8.14,8.47,7.18,6.36,4.57,5.02,5.75,5.48,4.97,5.00,4.39,3.88,4.91,5.87,5.64,6.16,6.07,6.22,7.19,7.82,7.92,8.52,9.96])

    oil = np.array([84.98, 72.89, 61.69,54.91,62.75,65.07, 69.01, 72.18, 61.28, 65.06, 60.50, 58.66, 58.89, 61.69, 61.10, 66.39, 54.45, 52.05, 24.74, 26.44, 38.32, 41.91, 44.15, 45.58, 40.93, 38.97, 47.42,51.09, 56.35, 63.69, 64.86, 67.56, 70.25, 75.84, 72.89, 71.59, 79.28])

    # оценка коэффициентов
    b = estimate_coef(gazprom, oil)

    print("Estimated coefficients:\nb_0 = {}  \
        \nb_1 = {}".format(b[0], b[1]))

    # построение линии регрессии

    plot_regression_line(gazprom, oil, b) 
    
    #alternative way
    gazprom = np.array([5.01,4.74,5.02,4.56,4.97,4.77,4.69,5.05,7.54,7.85,7.39,6.98,6.95,8.28,8.14,8.47,7.18,6.36,4.57,5.02,5.75,5.48,4.97,5.00,4.39,3.88,4.91,5.87,5.64,6.16,6.07,6.22,7.19,7.82,7.92,8.52,9.96]).reshape((-1, 1))
    model = LinearRegression()
    model.fit(gazprom, oil)
    model = LinearRegression().fit(gazprom, oil)
    r_sq = model.score(gazprom, oil)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)


main()
