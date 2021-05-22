# Leitura_IMU
Código para leitura do txt, com a adição dos filtros de média móvel e gaussiano.


### Entrada de dados em um txt separados por "Espaço":

![image](https://user-images.githubusercontent.com/51409770/119228738-c11dc780-baea-11eb-9f99-dec772b72c55.png)

## Instalação

Pacotes necessários:

Scipy:

    pip install scipy
    
Matplotlib:

    pip install matplotlib
    
## Rodando

Para rodar deve-se setar os parametros:
- Variável para Plotar o Gráfico (XYZ) - string
- Gaussian Kernel Sigma (Sigma) - número
- Filtro Média Móvel (FMM) - número
- Nome do Arquivo Txt (TXT) - string

      $ python3 init.py XYZ Sigma FMM TXT
      
 Exemplos:
        
        $ python3 init.py x 20 50 giro_190Hz_correia.txt
        $ python3 init.py x 50 100 acel_370Hz_correia.txt



## Gráficos

![image](https://user-images.githubusercontent.com/51409770/119229247-66d23600-baed-11eb-8517-f709247f562f.png)


