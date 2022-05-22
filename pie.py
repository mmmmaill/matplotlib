import matplotlib.pyplot as plt
import numpy as np


def piechart():
    label = ("China", "Russia", "Japan", "Korea")
    value = (1.8, 2, 2.1, 0.8)
    plt.title("travel count")
    plt.pie(value, labels=label, startangle=90, autopct="%1.2f%%", explode=(0,0,0.1,0))
    
    #ปรับสัดส่วนของกราฟให้เหมาะสม สมมาตร
    plt.axis("equal")
    plt.show()
    
def piechart2():
    label = np.array(["China", "Russia", "Japan", "Korea"])
    value = (1.8, 2, 2.1, 0.8)
    explode = np.zeros(label.size)
    
    #explode[2] = 0.1
    explode[np.where(label == "Japan")] = 0.1
    explode[np.where(label == "Russia")] = 0.1
     
    colors = ["red", "green", "pink", "yellow"]
    plt.title("travel count")
    plt.pie(value, labels=label, startangle=90, autopct="%1.2f%%", explode=explode, colors=colors)
    plt.axis("equal")
    plt.show()
    
    
if __name__=='__main__':

    #piechart()
    piechart2()

