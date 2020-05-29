## for plot

	Import sqlite3
import matplotlib.pyplot as plt
	from matplotlib import style
	style.use('ggplot')
	conn = sqlite3.connect('SE.db')
	c1=conn.cursor()
	
	def read_from_db():
	    c1.execute("SELECT per_a,per_c,per_d,per_e,per_f,per_g,per_h,per_i,per_j,per_k,per_l,per_m,per_n,per_p,per_q,per_r,per_s,per_t,per_v,per_w,per_y FROM genetic")
	    data = c1.fetchall()
	    print(data)
	    per=[]
	    
	    y1=data[0]
	    y2=data[3]
	    y3=data[4]
	    x=['Alanine','Cysteine','Aspartic_acid','Glutemic _acid', 'phenylalanine','Glycine','Histidine','Boleucine', 'Lysine','Leucine','Methionine','Asparagine', 'Proline','Glutamine','Arginine','Serine', 'Theronine','Valine','Tryptophan','Tyrosine' ]
	    plt.plot(x,y1,'c')
	    plt.plot(x,y2,'g')
	    plt.plot(x,y3,'r')
	    
	    plt.ylabel('************quantity*****************************')
	    plt.xlabel('element of amino acid')
	    plt.show()
	
	
	read_from_db()
