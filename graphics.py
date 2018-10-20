import matplotlib.pyplot as plt

def show_results():
    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot([1, 2, 3], [1, 2, 3])
    ax2.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [6, 2, 1, 5, 1, 7, 2, 9, 0, 8])
    plt.show()
    pass
