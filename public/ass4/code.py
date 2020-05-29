Code:
## for calculation. 
import sqlite3

conn = sqlite3.connect('SE3.db')
cp=conn.cursor()

cp.execute('CREATE TABLE IF NOT EXISTS genetic(a REAL,t REAL,g REAL,c REAL,div REAL,comm REAL)')

def number_calculation(amino):
	a1=0
	t1=0
	g1=0
	c1=0
	g_c=0
	g3=0
	div=0
	comm=n
	for i in amino:
		if i == 'a':
			a1 = a1 + 1
		elif i == 't':
			t1 = t1 + 1
		elif i == 'g':
			g1 = g1 + 1
		elif i == 'c':
			c1 = c1 + 1
		
	g_c=g1-c1
	g3=g1+c1
	div=g_c/g3
	comm=comm+div
	print(a1,t1,g1,c1,div,comm)

	cp.execute("INSERT INTO genetic(a,t,g,c,div,comm) VALUES(?,?,?,?,?,?)",(a1,t1,g1,c1,div,comm))
	conn.commit()
	return 0



amino=[]
count=0
n=0
comm=0
amino_file = open("test_demo.txt", "w")
with open("test.txt","r") as f:
	while True:

		#data_size=60
		f.content=f.read(1)
		if f.content==">":
			f.readline()
			#break
		#elif f.content==" ":
		#	break
		amino.append(f.content)

		count=count+1
		if count==68:
			count=0
			print("Amino",amino,end='\n')
			number_calculation(amino)
			amino.clear()
	#count=0	

		if f.content=='':
			break
	
#,g-c int,g+c int,g-c/g+c float,commulative_frequency float
