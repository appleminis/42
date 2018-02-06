import matplotlib.pyplot as plt
import numpy as np
import cv2

d0=2**11
d1=2**11

Ne=5
Ni=int(1e6)
b=1.0/Ni
Nis=int(1e2)

for j in range(Nis):
    
    im = np.zeros((d0,d1),np.float32)
    
    rot=np.exp(2.j*np.pi/Ne)
    Sn=1.j
    Ss=[Sn*pow(rot,e) for e in range(Ne)]
    
    av=0
    Xn=np.empty(Ni,np.complex)
    Xi=0.1
    
 
    
    for i in range(Ni):
        #if (np.mod(i,2)==0):#thank "think twice" hehe 
        #    av=np.random.randint(0,Ne)
            
        av=av+np.random.randint(-1,2)
        if (av<0):
            av=Ne-1
        if (av>Ne-1):
            av=0
        
        #av=4*av*(1-av)
        #av=np.mod(av,Ne)*Ne
        #av=av/4.0-1.0/av
        
        dc = np.abs(Xi)
    
                
        Xi = (Xi+Ss[(np.mod(int(av),Ne))])*(np.sin(dc*(1+j*1.0/Nis)))
        
    
        Xn[i] = Xi
    #plt.plot(np.real(Xn),np.imag(Xn),'.')

    c0=np.min(np.real(Xn))
    c1=np.min(np.imag(Xn))
    
    e0=np.max(np.real(Xn))
    e1=np.max(np.imag(Xn))
    
    
    for i in range(Ni):
        u=np.real(Xn[i])
        v=np.imag(Xn[i]) 
        im[int((u-c0)*(d0-1)/(e0-c0)),int((v-c1)*(d1-1)/(e1-c1))]+=b
        
    iml=np.log(cv2.pyrDown((cv2.pyrDown(im.T+1e-7))))
    iml/=np.max(iml)
    cv2.imwrite("/home/jrt/wmf"+str(j)+".png",(iml*254).astype('uint8'))



#cv2.imwrite("/home/jrt/fract5.png",(np.log(im+1e-6)*24).astype(np.uint8))
