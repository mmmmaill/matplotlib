import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 

def scatterplot():
    x = [170, 165, 180, 155, 163, 160, 175]
    y = [80, 65, 75, 47, 50, 52, 74]
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print(slope, intercept, r_value**2, p_value)
    
    #สร้างสมการเส้นตรง
    l = slope * min(x) + intercept, slope * max(x) + intercept
   
   #พล็อตกราฟ สีอ่อนใช้ alpha
    plt.scatter(x, y)
    plt.plot([min(x), max(x)], l, linestyle="--", alpha=.5, color="red")
   
    
    #ใส่สมการด้านบนกราฟ
    t = r"${} = {:.2f} + {:.2f}x, r^2 = {:.4f}, p = {:.4}$".format("\^{y}", intercept, slope, r_value**2, p_value)
    plt.title(t)
    plt.show()
    
if __name__=='__main__':
    scatterplot()