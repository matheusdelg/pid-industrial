## Documentação

Os módulos presentes são explicitados a seguir, explicando cada funcionalidade e parâmetro de configuração necessário.

### Introdução
Alguns dos módulos presentes são configurados por _specs_, [dicionários](https://www.w3schools.com/python/python_dictionaries.asp) com chaves pré-definidas a serem lidas pelo construtor da classe. Os módulos __Controller__ e __Plotter__ são configurados por _specs_.

### Controller
Classe responsável por gerar controladores PID na forma de função de transferência <img src="https://latex.codecogs.com/gif.latex?C(s)=K_p+\frac{K_i}{s}+T_ds" /> . Possui as seguintes especificações:
* Kc : Constante proporcional do controlador
* Ti : Constante de tempo integral para <img src="https://latex.codecogs.com/gif.latex?K_i=K_p/T_i"/>
* Td : Valor <img src="https://latex.codecogs.com/gif.latex?T_d"/> em <img src="https://latex.codecogs.com/gif.latex?K_d=K_pT_d"/>

Considerando ainda que o sinal de controle é determinado por uma ponderação da referência, 
*  b : Ponderação <img src="https://latex.codecogs.com/gif.latex?b"/> no sinal de controle
*  c : Ponderação <img src="https://latex.codecogs.com/gif.latex?c"/>  no sinal de controle

Caso algumas das especificações não for mencionada, a classe assume valores padrão:
* Kc : 1.0
* Ti : np.inf (requer ```numpy``` instalado)
* Td : 0.0
* b : 1.0
* c : 1.0

Após instanciado, você pode chamar a função de transferência resultante pelo campo ```.tf```, como mostra o exemplo a seguir:
```python
from pid_utils import Controller, Analysis
c_specs = {'Kc' : 1.1} # Controlador Proporcional de Kp = 1.1
C = Controller (c_specs).tf

Analysis.time (C, plot = True)
```

### Plotter
Classe auxiliar para geração de gráficos no Python, utilizando o pacote ```PyPlot```. Confira os códigos de exemplo para melhores informações sobre os métodos inseridos. Possui as seguintes especificações:
* title : Título do gráfico 
* xlab  : Texto no eixo X   
* ylab  : Texto no eixo Y   
* grid  : Plot com grade    
* type  : Plot linear ou logarítmico

Caso algumas das especificações não for mencionada, a classe assume valores padrão:
* title : 'Standard Plot'
* xlab  : 'Time (s)'
* ylab  : 'Signal' 
* grid  : False
* type  : 'linear'
