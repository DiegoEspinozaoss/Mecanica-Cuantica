import numpy as np
import matplotlib.pyplot as plt

def graficar_real(t):
    L=10**(-20)
    h_barra=6.6*(10**(-34))
    m=9.1*(10**(-31))
    x = np.linspace(0,L,1000)
    c=np.cos(((np.pi **2)*h_barra*t)/(2*m*(L**2))) 
    d=np.cos((2*(np.pi **2)*h_barra*t)/(m*(L**2))) 
    e=np.sin((np.pi*x)/L)
    f=np.sin((2*np.pi*x)/L)
    g=np.sqrt(2/np.sqrt(11*L))
    h=np.sqrt(3/np.sqrt(11*L))
    phi_real =  g* c *e - h* d *f
    plt.plot(x, phi_real)
    plt.xlabel('espacio 1D [m]', fontsize=20)
    plt.ylabel('$\Psi _{real}$', fontsize=20)
    plt.title('$\Psi _{real}$  vs espacio', fontsize=20)
    
def graficar_imaginario(t):
    L=10**(-20)
    h_barra=6.6*(10**(-34))
    m=9.1*(10**(-31))
    x = np.linspace(0,L,1000)
    a=np.sin(((np.pi **2)*h_barra*t)/(2*m*(L**2))) 
    b=np.sin((2*(np.pi **2)*h_barra*t)/(m*(L**2))) 
    e=np.sin((np.pi*x)/L)
    f=np.sin((2*np.pi*x)/L)
    g=np.sqrt(2/np.sqrt(11*L))
    h=np.sqrt(3/np.sqrt(11*L))
    phi_imaginario = -g* a *e + h* b *f  
    plt.plot(x, phi_imaginario)
    plt.xlabel('espacio 1D [m]', fontsize=20)
    plt.ylabel('$\Psi _{imaginario}$', fontsize=20)
    plt.title('$\Psi _{imaginario}$  vs espacio', fontsize=20)

segundos=10
def real():
    i=0
    while i<=segundos:
        graficar_real(i)
        i+=1
    plt.show()
    
def imaginario():
    k=0
    while k<=segundos:
        graficar_imaginario(k)
        k+=1
    plt.show()
    
real()
imaginario()

