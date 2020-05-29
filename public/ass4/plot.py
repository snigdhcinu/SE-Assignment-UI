##  for plotting

import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
conn = sqlite3.connect('SE3.db')
cp=conn.cursor()

def read_from_db():
    x=[]
    cp.execute("SELECT comm FROM genetic")
    data = cp.fetchall()
    
    p=len(data)
    
   
    for i in range(p):
        x.append(i)

    
  
 #   plt.bar(x,y1,label='row[0]',color='g',width=0.2)
  #  plt.bar(x,y2,label='row[1]',color='r',width=0.1)
    plt.plot(x,data,'r')
    plt.title('plot')
    plt.ylabel('cumulative frequency')
    plt.xlabel('')
    plt.legend()
    plt.show()


read_from_db()
