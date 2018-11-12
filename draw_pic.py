import matplotlib.pyplot as plt
import numpy as np


def draw_origin():
    x = np.linspace(0, 6, 61)
    y = x*x + 1
    feasible_set = np.linspace(2, 4, 21)

    plt.figure('1')
    plt.plot(x, y)
    plt.xlabel('x')
    plt.axis([0, 6, 0, 40])
    plt.plot(2, 5, 'ro')
    plt.text(1.8, 7, r'$p^{*}=5$')
    plt.text(1.8, 1, r'$x^{*}=2$')
    plt.plot(feasible_set, np.zeros(21), 'r')
    plt.annotate('feasible set', xy=(3, 0), xytext=(4, 4),
                 arrowprops=dict(facecolor='red', shrink=0.01),
                 )
    fig = plt.gcf()
    fig.savefig('origin.eps', format='eps')
    plt.show()


def draw_lambda(lam):
    x = np.linspace(0, 6, 61)
    y = x*x + 1
    penalty = (x-2)*(x-4)
    plt.figure('2')
    num = 220
    for item in lam:
        num = num + 1
        l = y + item * penalty
        plt.subplot(str(num))
        plt.axis([0, 6, 0, 40])
        plt.xlabel('x')
        plt.ylabel('L')
        plt.plot(x, l)
        plt.text(1, 30, r'$\lambda$='+str(item))
    fig = plt.gcf()
    fig.savefig('compare_fig.eps', format='eps')
    plt.show()


if __name__ == '__main__':
    lam = [0.2, 0.5, 1, 2]
    draw_lambda(lam)
    draw_origin()

