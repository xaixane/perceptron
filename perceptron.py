def AND(x,y):
    return 1 if (x==1 and y==1) else -1

def OR(x,y):
    return -1 if (x==-1 and y==-1) else 1

def NEGATE(x):
    return 1 if x==-1 else -1

def XOR(x,y):
    return -1 if x==y else 1

def printInitial(x_inputs,H_outputs,Y_output):
    print(f"{'x1':<10}{'x2':<10}{'H1':<10}{'H2':<10}{'Y':<10}")
    print('-'*45)
    for i in range(0,4):
        print(f"{x_inputs[i][0]:<10}{x_inputs[i][1]:<10}{H_outputs[i][0]:<10}{H_outputs[i][1]:<10}{Y_output[i]:<10}")

def printWeights(weights,delta_weights):
    print(f"{'delta_v1':<10}{'delta_v2':<10}{'v1':<10}{'v2':<10}")
    print('-'*45)
    for i in range(4):
        print(f"{delta_weights[i][0]:<10}{delta_weights[i][1]:<10}{weights[i][0]:<10}{weights[i][1]}")

def activatorFunction(x,v):
    h=(x[0]*v[0]) + (x[1]*v[1])
    if h<0:
        return -1
    elif h==0:
        return 0
    else:
        return 1


def calcHW(x_inputs,H_input,mode):
    h_input=[]
    if mode==1:
        for i in range(len(x_inputs)):
            x_inputs[i][0]=NEGATE(x_inputs[i][0])
            h_input.append(H_input[i][0])
    elif mode==2:
        for i in range(len(x_inputs)):
            x_inputs[i][0],x_inputs[i][1]=NEGATE(x_inputs[i][0]),NEGATE(x_inputs[i][1])
            h_input.append(H_input[i][1])
    else:
        h_input=H_input
    H_cap=[]
    v=[0,0]
    V=[]
    delta_V=[]
    for i in range(len(x_inputs)):
        temp_H=activatorFunction(x_inputs[i],v)
        if temp_H != h_input[i]:
            delta_v1=x_inputs[i][0]*h_input[i]
            delta_v2=x_inputs[i][1]*h_input[i]
            delta_V.append([delta_v1,delta_v2])
            v[0]=v[0]+delta_v1

            v[1]=delta_v2+v[1]
            V.append([v[0],v[1]])
        else:
            delta_V.append([0,0])
            V.append(V[i-1])
    return V,delta_V
        

def finaltouch(x,h,y):
    #initial
    print("\n\nInitial Table")
    print("-"*45)
    printInitial(x,h,y)

    #for h1
    print("\n\nH1 Table")
    print("-"*45)
    h1_weights,h1_deltaWeights=calcHW(x,h,1)
    printWeights(h1_weights,h1_deltaWeights)
    #for h2

    print("\n\nH2 Table")
    print("-"*45)
    h2_weights,h2_deltaWeights=calcHW(x,h,2)
    printWeights(h2_weights,h2_deltaWeights)
    #for W
    print("\n\nW Table")
    print("-"*45)
    W_weights,W_deltaWeights=calcHW(h,y,3)
    printWeights(W_weights,W_deltaWeights)

if __name__ == "__main__":
    x_inputs    = [[1,1],[-1,1],[1,-1],[-1,-1]]
    H_output    = []
    Y_output    = []
    t_output    = []
    for i in x_inputs:
        t_output.append(XOR(i[0],i[1]))
        temp1=AND(NEGATE(i[0]),i[1])
        temp2=AND(i[0],NEGATE(i[1]))
        H_output.append([temp1,temp2])
        Y_output.append(OR(temp1,temp2)) 
    finaltouch(x_inputs,H_output,Y_output)


