def Vr(q1,q2,r):
    if r ==0:
        print("계산 할 수 없습니다.")
    else:
        import math
        pi = math.pi
        e0 = float(8.854*(10)**(-12) )
        Vr= float((q1*q2)/(4*pi*e0*r))
        print(Vr)
        
    return Vr

def V():
    import math
    va= str(input("당신이 구할려는 값 (V(),r,q) > "))
    if va == "V()":
            q1 = float(input("전하1  >"))
            q2 = float(input("전하2  >"))
            r = float(input("전하와 전하의 상호 거리  >"))
            pi = math.pi
            e0 = float(8.854*(10)**(-12) )
            if r ==0:
                print("계산 할 수 없습니다.")
            else:
                Vr= float((q1*q2)/(4*pi*e0*r))
                print(Vr)
                return Vr
    elif va == "r":
            q1 = float(input("전하1  >"))
            q2 = float(input("전하2  >"))
            Vr = float(input("퍼텐셜 에너지  >"))
            pi = math.pi
            e0 = float(8.854*(10)**(-12) )
            if Vr == 0:
                print("계산 할 수 없습니다.")
            else:
                 r = float((q1*q2)/(4*pi*e0*Vr))                             
                 print(r)  


V()