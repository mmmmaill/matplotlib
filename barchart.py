from itertools import count
import matplotlib.pyplot as plt

#กราฟแท่งแนวตั้ง
def bary():
    x = range(4)
    y = (20,25,40,30)
    # ค่าเฉลี่ย
    avg = sum(y)/4
    # กำหนดค่าแกน x 
    xtick = ("mocha","latte", "espreeso", "tea")
    # พล็อตกราฟแท่งแนวนอน 
    plt.bar(x, y, color="pink")
    plt.xticks(x, xtick)
    # เส้นเขต
    plt.axhline(avg, color = 'red', linestyle='--')
    #ชื่อกราฟ
    plt.title("Order by menu\nof coffe shop",color="red", fontsize=20)
    #ตั้งชื่อแยวแกน y
    plt.ylabel("# order")
    plt.xlabel("# menu")
    plt.show()

#กราฟแท่งแนวนอน
def barhori():
    x = range(4)
    y = (20,25,45,30)
    xtick = ("mocha","latte", "espreeso", "tea")
    plt.yticks(x, xtick) 
    plt.barh(x,y)
    plt.show()

def bar_subplot():
    x = range(4)
    y = (20,25,45,30)
    xtick = ("mocha","latte", "espreeso", "tea")
    
    #พล็อต 2 กราฟ กำหนด 1 แถว 2 คอลัมน์
    fig, ax = plt.subplots(1,2)
    ax[0].bar(x,y, color='pink')
    ax[1].barh(x,y, color='green')
    
    #ตัวบอกจะเซตค่ากราฟแรก
    plt.sca(ax[0])
    plt.xticks(x, xtick)
    #ตัวบอกจะเซตค่ากราฟตัวที่ 2
    plt.sca(ax[1])
    plt.yticks(x, xtick)
    
    #กำหนด layout ของกราฟ
    fig.tight_layout()
    plt.show()
    
    
    
    
if __name__=='__main__':
    #bary()
    #barhori()
    bar_subplot()
    

  

