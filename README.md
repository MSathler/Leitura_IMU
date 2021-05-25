# Leitura_IMU
Código para leitura do txt, com a retirada e outliers e adição dos filtros de média móvel e gaussiano.



### Entrada de dados em um txt separados por "Espaço":

- txt no formato {tempo variavel_x variavel_y variavel_z}

![image](https://user-images.githubusercontent.com/51409770/119433420-98652000-bcec-11eb-81aa-0461ea87080b.png)

## Instalação

Pacotes necessários:

- Scipy:

        pip install scipy
    
- Matplotlib:

        pip install matplotlib
    
## Rodando

Para rodar deve-se setar os parametros:
- Variável para Plotar o Gráfico (XYZ) - string
- Gaussian Kernel Sigma (Sigma) - número
- Filtro Média Móvel (FMM) - número
- Nome do Arquivo Txt caso esteja na pasta, caso contrário colocar o caminho ate o txt (TXT) - string

      $ python3 init.py XYZ Sigma FMM TXT
      
 Exemplos:
        
        $ python3 init.py x 20 50 giro2_carro.txt
        
ou
        
        $ python3 Desktop/acelerometro/Leitura_IMU/init.py x 20 50 Desktop/acelerometro/Leitura_IMU/giro2_carro.txt





## Gráficos

![image](https://user-images.githubusercontent.com/51409770/119433472-b599ee80-bcec-11eb-8874-638d5f759c48.png)



