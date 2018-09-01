from pid_libs import Plotter
import numpy as np

# Spec para um grafico com titulo 'Senoides' e eixo y 'Amplitude':
pl_spec = {'title' : 'Senoides', 'ylab' : 'Amplitude'}

t  = np.linspace(0, 8, 100) # Gera 100 amostras de 0 a 8
y1 = np.sin (t)
y2 = np.sin (2*t)
y4 = np.sin (3*t)

# Objeto do tipo Plotter com as specs definidas
plt = Plotter (pl_spec)
plt.plot ([(t, y1), (t, y2), (t, y4)], ["sin (t)", "sin (2t)", "sin (4t)"])
# Imprime as tres curvas no mesmo grafico, com as devidas legendas

