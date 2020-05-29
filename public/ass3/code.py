Code:
## for counting the protein as well as creating database.


	Import sqlite3
	conn = sqlite3.connect('SE2.db')
	c1=conn.cursor()
	
	c1.execute('CREATE TABLE IF NOT EXISTS genetic(sl_no REAL,gene TEXT,acid TEXT,per_a REAL,per_c REAL,per_d REAL,per_e REAL,per_f REAL,per_g REAL,per_h REAL,per_i REAL,per_j REAL,per_k REAL,per_l REAL,per_m REAL,per_n REAL,per_p REAL,per_q REAL,per_r REAL,per_s REAL,per_t REAL,per_v REAL,per_w REAL,per_y REAL)')
	
	amino2 = ''
	count1 = 0
	
	def cal_amino(amino,amino2):
		amino2 = amino + amino2
		return amino2
	
	def per_calculation(amino,str_fin,count1):
		a=0
		#b=0
		c=0
		d=0
		e=0
		f=0
		g=0
		h=0
		i1=0
		j=0
		k=0
		l=0
		m=0
		n=0
		#o=0
		p=0
		q=0
		r=0
		s=0
		t=0
		#u=0
		v=0
		w=0
		#x=0
		y=0
		#z=0
		per_a = 0
		#per_b = 0
		per_c = 0
		per_d = 0
		per_e = 0
		per_f = 0
		per_g = 0
		per_h = 0
		per_i = 0
		per_j = 0
		per_k = 0
		per_l = 0
		per_m = 0
		per_n = 0
		#per_o = 0
		per_p = 0
		per_q = 0
		per_r = 0
		per_s = 0
		per_t = 0
		per_w = 0
		#per_u = 0
		per_v = 0
		#per_x = 0
		per_y = 0
		#per_z = 0
		#print(amino)
		for i in amino:
			if i == 'A':
				a = a + 1
				#print("rfgv")
			elif i == 'C':
				c = c + 1
			elif i == 'D':
				d = d + 1
			elif i == 'E':
				e = e + 1
			elif i == 'F':
				f = f + 1
			elif i == 'G':
				g = g + 1
			elif i == 'H':
				h = h + 1
			elif i == 'I':
				i1 = i1 + 1
			elif i == 'J':
				j = j + 1
			elif i == 'K':
				k = k + 1
			elif i == 'L':
				l = l + 1
			elif i == 'M':
				m = m + 1
			elif i == 'N':
				n = n + 1
			elif i == 'P':
				p = p + 1
			elif i == 'Q':
				q = q + 1
			elif i == 'R':
				r = r + 1
			elif i == 'S':
				s = s + 1
			elif i == 'T':
				t = t + 1
			elif i == 'V':
				v = v + 1
			elif i == 'W':
				w = w + 1
			elif i == 'Y':
				y = y + 1
		#print(a,t,g,c)
		per_a = round((a/len(amino))*100,2)
		per_c = round((c/len(amino))*100,2)
		per_d = round((d/len(amino))*100,2) 
		per_e = round((e/len(amino))*100,2) 
		per_f = round((f/len(amino))*100,2)
		per_g = round((g/len(amino))*100,2)
		per_h = round((h/len(amino))*100,2)
		per_i = round((i1/len(amino))*100,2) 
		per_j = round((j/len(amino))*100,2) 
		per_k = round((k/len(amino))*100,2)
		per_l = round((l/len(amino))*100,2)
		per_m = round((m/len(amino))*100,2)
		per_n = round((n/len(amino))*100,2) 
		per_p = round((p/len(amino))*100,2) 
		per_q = round((q/len(amino))*100,2)
		per_r = round((r/len(amino))*100,2)
		per_s = round((s/len(amino))*100,2)
		per_t = round((t/len(amino))*100,2) 
		per_v = round((v/len(amino))*100,2) 
		per_w = round((w/len(amino))*100,2)
		per_y = round((y/len(amino))*100,2)
		#per_z = round((c/len(str_fin))*100,2)
		
		#count1 = count1 + 1
		c1.execute("INSERT INTO genetic(sl_no,gene,acid,per_a,per_c,per_d,per_e,per_f,per_g,per_h,per_i,per_j,per_k,per_l,per_m,per_n,per_p,per_q,per_r,per_s,per_t,per_v,per_w,per_y) VALUES(?,?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)",(count1,str_fin,amino,per_a,per_c,per_d,per_e,per_f,per_g,per_h,per_i,per_j,per_k,per_l,per_m,per_n,per_p,per_q,per_r,per_s,per_t,per_v,per_w,per_y))
		conn.commit()
		return 0
	
	
	genetoacid =  {'ttt':'F','ttc':'F','tta':'L','ttg':'L',\
				   'ctt':'L','ctc':'L','cta':'L','ctg':'L',\
	               'att':'I','atc':'I','ata':'I','atg':'M',\
	               'gtt':'V','gtc':'V','gta':'V','gtg':'V',\
	               'tct':'S','tcc':'S','tca':'S','tcg':'S',\
	               'cct':'P','ccc':'P','cca':'P','ccg':'P',\
	               'act':'T','acc':'T','aca':'T','acg':'T',\
	               'gct':'A','gcc':'A','gca':'A','gcg':'A',\
	               'tat':'Y','tac':'Y','cat':'H','cac':'H',\
	               'caa':'Q','cag':'Q','aat':'N','aac':'N',\
	               'aaa':'K','aag':'K','gat':'N','gac':'N',\
	               'gaa':'E','gag':'E','tgt':'C','tgc':'C',\
	               'tgg':'W','cgt':'R','cgc':'R','cga':'R',\
	               'cgg':'R','aga':'R','agg':'R','agt':'S',\
	               'agc':'S','ggt':'G','ggc':'G','gga':'G',\
	               'ggg':'G'
		
	}
	amino=""
	str1 = ''
	str_fin=''
	list1 = []
	count = 0
	#amino2 = 0
	amino_file = open("test_demo.txt", "w")
	with open("test.txt","r") as f:
		
		#f.content = f.read(1)
		while True:
			f.content = f.read(1)
			if(len(f.content) ==0):
				break
			if(f.content==">"):
				amino=''
				#print(str_fin,end="9999\n")
				str_fin = ''
				list1.append(str(f.readline()))
			else:
				
				if(f.content=='a' or f.content=='t' or f.content=='g' or f.content=='c'):
					str1 = str1 + str(f.content)
					#str_fin = str_fin + str1
					#print(str_fin)
				else:
					continue
	
				count = count + 1
				if(count == 3):
					count=0
					if(str1=="taa" or str1 == "tag" or str1 == "tga"):
						#print("*\n",end='')
						amino_file.write(amino)
						amino_file.write("*\n")
						#print(amino,end='####')
						count1 = count1 + 1
						amino3=cal_amino(amino,amino2)
						#
						#c.execute("INSERT INTO genetic(gene,acid) VALUES(?, ?)",(str_fin,amino))
						#conn.commit()
						f.content = f.read(1)
						str1=''
					else:
						str_fin = str_fin + str1
						amino= amino + str(genetoacid[str1])
						#print(amino,end='')
						#amino_file.write(amino)
						#f.content = f.read(1)
						str1=''
		per_calculation(amino3,str_fin,count1)
	
		#f.content = f.read(size_to_read)
		#amino_file.write(amino)
