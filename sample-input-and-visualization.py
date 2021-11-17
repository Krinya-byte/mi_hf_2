FELSOROLÁS-KÉRDEZÉS:
	X: célváltozó
	e[]: az evidencia változók értékei
	bn: bayes háló (Y minden, ami nem E, vagy X)
	
	Q(X) = 0
	csináld a következőt X-nek X[i] értékére:
		e[]-hez adjuk X[i]-t
		Q(X[i]) = FELSOROL-MINDET (bn, e)
		
		
# kiszámolja az X[i] valószínűségét		
FELSOROL-MINDET:

	
	
	
#####################################################################################################
3	                #Nv: csomópontok száma
2	0	0.352,0.648	#0. indexű csomópont 2 értéket vehet fel - 0 szülője van - értékei valószínűsége (ha igazak)
3	0	0.01,0.39,0.6
2	2	0	1	0,0:0.3,0.7	0,1:0.5,0.5	0,2:0.4,0.6	1,0:0.8,0.2	1,1:0.2,0.8	1,2:0.7,0.3
1	                #evidencia változók száma
2	1	            #evidencia változó indexe - felvett értéke (a tömb egy oszlopa) pl. X2[1]=0,7 0,5 ... 0,3 
1	                #X:célváltozó csomópont indexe
2	                #nd: lehetséges döntések száma
0	0	153.2       #célváltozó értéke - döntés értéke - hasznosság
0	1	-55.7       #...
1	0	50.3        #...
1	1	-125.1      #...
2	0	-15.3       #...
2	1	54.4        #célváltozó értéke - döntés értéke - hasznosság


#############################################
2	2	0	1	0,0:0.3,0.7	0,1:0.5,0.5	0,2:0.4,0.6	1,0:0.8,0.2	1,1:0.2,0.8	1,2:0.7,0.3
->
X0  X1  :   X2=0    X2=1
0,  0   :   0.3,    0.7     #P(X2=0 | X0=0, X1=0) = 0.3 és P(X2=1 | X0=0, X1=0) = 0.7
0,  1   :   0.5,    0.5
0,  2   :   0.4,    0.6
1,  0   :   0.8,    0.2
1,  1   :   0.2,    0.8
1,  2   :   0.7,    0.3
