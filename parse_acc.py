import matplotlib.pyplot as plt
from collections import deque
from scipy.ndimage import gaussian_filter1d
import time
from tqdm import tqdm, trange

class parse_data():
    def __init__(self,filter_sigma = 20,filter_m_movel = 200, posicao_corte = 0, file_name = 'acel_370Hz_correia.txt'):
        self._posicao_corte = posicao_corte
        self._t_experimento = []
        self.x_deg =  0
        self.__soma = []
        self.tan_x,self.tan_y = [], []
        self._infls = []
        self._altura_tanque = []
        self._tensao = []
        self.ls = []
        self._filtrado_x,self._filtrado_y,self._filtrado_z = [], [], []
        self.filter_len = int(filter_m_movel)
        self._deque_x,self._deque_y,self._deque_z = deque(maxlen=int(self.filter_len)),deque(maxlen=int(self.filter_len)),deque(maxlen=int(self.filter_len))
        self._csv_file = open(file_name,'r')
        self.filter_sigma = int(filter_sigma)
        self.X,self.Y,self.Z = [],[],[]
        # self.last_x,self.last_y,self.last_z = 0,0,0
        
        #t = time.clock_gettime(time.CLOCK_MONOTONIC)       
        
        
        for row in self._csv_file:
            self._row = row.split('\n')
            # print(self._row)
            self._row = self._row[0].split('\t')
            # print(self._row)
            
            if float(self._row[0]) <= self._posicao_corte:
                self.last_x,self.last_y,self.last_z = float(self._row[1]),float(self._row[2]),float(self._row[3])#pass 
            else:
                
                self.outlier()
 
        for w in range(self.filter_len-1):
            self._filtrado_x.append(self.a)
            self._filtrado_y.append(self.b)
            self._filtrado_z.append(self.c)
        #print("tempo " + str(time.clock_gettime(time.CLOCK_MONOTONIC) - t))
        # print(self._filtrado)
        self._V_filtrado_x = gaussian_filter1d(self.X ,self.filter_sigma)
        self._V_filtrado_y = gaussian_filter1d(self.Y ,self.filter_sigma)
        self._V_filtrado_z = gaussian_filter1d(self.Z ,self.filter_sigma)
        self._csv_file.close()
       
       
       
    def outlier(self):
        self._t_experimento.append(float(self._row[0]))
        if abs(abs(self.last_x) - abs(float(self._row[1]))) <= 100:
            self.last_x = float(self._row[1])
            self.X.append(float(self._row[1]))
            self._deque_x.append(float(self._row[1]))
            if len(self._deque_x) == self.filter_len:
                self.a = sum(self._deque_x)/self.filter_len
                self._filtrado_x.append(sum(self._deque_x)/self.filter_len)
        else:
            self.X.append(self.last_x)
            self._deque_x.append(self.last_x)
            if len(self._deque_x) == self.filter_len:
                self.a = sum(self._deque_x)/self.filter_len
                self._filtrado_x.append(sum(self._deque_x)/self.filter_len)
        
        
        if abs(abs(self.last_y) - abs(float(self._row[2]))) <= 100:
            self.last_y = float(self._row[2])
            self.Y.append(float(self._row[2]))
            self._deque_y.append(float(self._row[2]))
            if len(self._deque_x) == self.filter_len:
                self.b = sum(self._deque_y)/self.filter_len
                self._filtrado_y.append(sum(self._deque_y)/self.filter_len)
        else:
            self.Y.append(self.last_y)
            self._deque_y.append(self.last_y)
            if len(self._deque_x) == self.filter_len:
                self.b = sum(self._deque_y)/self.filter_len
                self._filtrado_y.append(sum(self._deque_y)/self.filter_len)
                 
        if abs(abs(self.last_z) - abs(float(self._row[3]))) <= 100:
            self.last_z = float(self._row[3])
            self.Z.append(float(self._row[3]))
            self._deque_z.append(float(self._row[3]))   
            if len(self._deque_x) == self.filter_len:
                self.c = sum(self._deque_z)/self.filter_len
                self._filtrado_z.append(sum(self._deque_z)/self.filter_len)
        else:
            self.Z.append(self.last_z)
            self._deque_z.append(self.last_z)   
            if len(self._deque_x) == self.filter_len:
                self.c = sum(self._deque_z)/self.filter_len
                self._filtrado_z.append(sum(self._deque_z)/self.filter_len)            
        
    def plot(self,eixo):
        if str(eixo).upper() == "X":
            plt.subplot(131)
            plt.title("Raw data")
            plt.plot(self.X)
            plt.ylim([min(self.X),max(self.X)])
            plt.subplot(132)
            plt.title(f"Filtro Média Móvel Período {self.filter_len}")
            plt.plot(self._t_experimento,self._filtrado_x, color='r')
            plt.ylim([min(self.X ),max(self.X )])
            plt.subplot(133)
            plt.title(f"Filtro Gaussiano Sigma = {self.filter_sigma}")
            plt.plot(self._t_experimento,self._V_filtrado_x, color='green')
            plt.ylim([min(self.X ),max(self.X)])

        elif str(eixo).upper() == "Y":
            plt.subplot(131)
            plt.title("Raw data")
            plt.plot(self.Y)
            plt.ylim([min(self.Y),max(self.Y)])
            plt.subplot(132)
            plt.title(f"Filtro Média Móvel Período {self.filter_len}")
            plt.plot(self._t_experimento,self._filtrado_y, color='r')
            plt.ylim([min(self.Y),max(self.Y)])
            plt.subplot(133)
            plt.title(f"Filtro Gaussiano Sigma = {self.filter_sigma}")
            plt.plot(self._t_experimento,self._V_filtrado_y, color='green')
            plt.ylim([min(self.Y),max(self.Y)])

        elif str(eixo).upper() == "Z":
            plt.subplot(131)
            plt.title("Raw data")
            plt.plot(self.Z)
            plt.ylim([min(self.Z),max(self.Z)])
            plt.subplot(132)
            plt.title(f"Filtro Média Móvel Período {self.filter_len}")
            plt.plot(self._t_experimento,self._filtrado_z, color='r')
            plt.ylim([min(self.Z),max(self.Z)])
            plt.subplot(133)
            plt.title(f"Filtro Gaussiano Sigma = {self.filter_sigma}")
            plt.plot(self._t_experimento,self._V_filtrado_z, color='green')
            plt.ylim([min(self.Z),max(self.Z)])
        
        plt.show()
        
        
