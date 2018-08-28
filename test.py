from control_utils import Plotter, Controller, Analysis;
import control as ctrl;

plot_specs = {'title' : 'Resposta ao degrau unitario',
              'xlab'  : 'tempo (s)', 'ylab'  : 'saida (V)',
	      'grid'  : True };

pid_specs = {'name' : 'controlador',
	       'Kc' : 1.3, 'Ti' : 0.7};

G = ctrl.tf (2, [1.23, 1.15, 3.76]);
C = Controller(pid_specs).tf;

Analysis.time (G);

L1 = ctrl.feedback (C * G);
tl, yl = ctrl.step_response (L1);
tg, yg = ctrl.step_response (G);

p = Plotter (plot_specs);
p.plot ([(tl, yl), (tg, yg)], ["Feedback", "Open Loop"]);
