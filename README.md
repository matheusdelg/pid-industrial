# PID Industrial (Módulos auxiliares)

Funções e classes úteis para o trabalho da disciplina de Controladores PID Industriais do CEFET-MG Campus V. Contém módulos para geração de gráficos e análise no domínio do tempo e frequência para sistemas descritos em função de transferência.

### Pré-requisitos

O sistema requer o Python na versão 2.7.6 (ou superior) instalado no computador. Se você utiliza SOs Linux, o Python já é instalado nativamente (verifique abrindo o terminal e entrando com o comando ```which python``` ou ```which python3```). Para sistemas Windows, confira os tutoriais de [download](https://www.python.org/downloads/) e [instalação](https://python.org.br/instalacao-windows/) do Python.

Além da linguagem, os módulos [control](http://python-control.sourceforge.net/manual/intro.html), [NumPy](http://www.numpy.org/) e [PyPlot](https://matplotlib.org/) são necessários. Para instalá-los, confira a documentação em cada link ou utilize o comando ```pip``` no Terminal, como a seguir:

```
sudo pip install control matplotlib numpy
```
Para verificar se o sistema possui todos os módulos instalados, digite ```python``` no Terminal e, em seguida, ```help('modules')```. Os pacotes listados deverão conter as bibliotecas instaladas.

### Instalação
O sistema não requer instalação. Apenas copie a pasta **pid_utils** para o diretório do seu script e faça as importações que achar necessário.

### Exemplos
São disponibilizados na pasta **test** arquivos de exemplo para cada módulo, devidamente comentados.
