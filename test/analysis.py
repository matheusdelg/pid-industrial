from pid_libs import Controller, Analysis
import control as ctrl 	

# Spec para um controlador PI de Kp = 0.6 e Ki = 0.857:
pid_specs = {'Kc' : 0.6, 'Ti' : 0.7}

# Funcoes de transferencia:
G = ctrl.tf (2, [1, 1.15, 3.76])   # G(s) = 2 / (s^2 + 1.15s + 3.76)
C = Controller(pid_specs).tf	   # C(s) = 0.6 + 0.857 / s
L = ctrl.feedback (C * G)          # Realimentacao em serie

# Respostas no dominio do tempo de da frequencia
Analysis.time (G, method = 'impulse')  # Resposta ao impulso da malha aberta
Analysis.time (L, plot = True)	       # Resposta ao degrau da malha fechada
Analysis.bode (G, plot = True)	       # Resposta em frequencia da malha aberta
Analysis.bode (L, plot = True)	       # Dados de estabilidade marginal da malha fechada
