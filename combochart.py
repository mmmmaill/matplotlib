from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

def demo():
    labels = np.array(["Jan", "Feb", "Mar", "Apr", "Mar", "Jun"])
    x = np.arange(labels.size)
    y1 = np.random.normal(80,10, x.size)
    y2 = np.random.normal(95,12, x.size)
    plt.bar(x, y1, color="deepskyblue", alpha=.5, label="we")
    plt.plot(x, y2, color="blue", label="industry", marker="x")
    plt.xticks(x, labels)
    plt.legend()
    plt.ylabel("Sales of month")
    plt.show()
    

if __name__=='__main__':
    demo()