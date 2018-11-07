
import numpy
from gurobipy import *
import csv


infile = open("data.txt",'r')

reader = csv.reader(open("spells.csv","r"),delimiter=";")
l = list(reader)

#A matriz de feitiços contem as magias nas primeiras linhas que vão de 0 a n_spells-1
#A partir de n_spells em diante, cada linha é composta por [x][0] = ID da magia desencadeadora  e [x][y] = IDs de magias desencadeadas ( y>0 )
spells = numpy.array(l).astype("float")


lines = infile.readlines()
n_spells = int(lines[0])
MRR = int(lines[1])
TF = int(lines[2])
TT = int(lines[3])

infile.close()
var = []
t_var = []

print(spells)


#Setting FMi to default spells
for x in range(0,n_spells):
    if(spells[x][7] < 0):
        spells[x][7] = (1.0/(spells[x][1]+spells[x][3]))


try:
    # Create a new model
    m = Model("games")

    # Create variables
    for x in range(0,n_spells):
        var.append(m.addVar(vtype=GRB.INTEGER, name="x" + str(x)))
        t_var.append(m.addVar(name="t"+str(x)))

    # Set objective
    expr = LinExpr()
    for x in range(0,n_spells):
        expr += var[x]*spells[x][2]/TT  #Define somatorio onde spells[x][1] = Dmgx
    m.setObjective(expr,GRB.MAXIMIZE)   
    
    # Add constraints:
    cc = 1  #Constraints counter 
    for x in range(0,n_spells):
        m.addConstr(var[x]*spells[x][1] + (var[x]-1)*spells[x][3] <= t_var[x],"c" + str(cc))     #Define Ni*Casti + (Ni-1) * CDi <= ti
        cc += 1

    expr = LinExpr()
    for x in range(0,n_spells):
        expr += t_var[x]                             #Define  sum(ti) <= TT 
    m.addConstr(expr <= TT , "c" + str(cc))
    cc += 1
    
    for x in range(0,n_spells):
        m.addConstr(var[x]/TT >= spells[x][6],"c"+str(cc))#Define Ni/TT >= Fmi
        cc += 1
    for x in range(0,n_spells):
        m.addConstr(var[x]/TT <= spells[x][7],"c"+str(cc))#Define Ni/TT <= FMi
        cc += 1
    expr = LinExpr()
    for x in range(0,n_spells):
        expr += var[x] * (spells[x][4]/TT)
    m.addConstr(expr <= MRR, "c" + str(cc))                     #Define Sum(i) Ni*(MPi/TT) <= MRR
    cc += 1
    expr = LinExpr()
    for x in range(0,n_spells):
        expr += var[x] * (spells[x][5]/TT)
    m.addConstr(expr >= TF, "c" + str(cc))                      #Define Sum(i) Ni*(HPi/TT) >= TF
    cc += 1
    for x in range (n_spells, len(spells)):                     #Define Ni >= Nj se i desencadeia j 
        for y in range(1, len(spells[x])):
            if(spells[x][y] > -0.00001):
                m.addConstr(var[int(spells[x][0])] >= var[int(spells[x][y])],"c"+str(cc))
                cc += 1
    print(var)
    m.write("model.lp")
    
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')

