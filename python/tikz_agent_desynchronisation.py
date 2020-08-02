import random

fig_begin = '''\\begin{figure}\\centering
\\begin{tikzpicture}[node distance=2cm, shorten >= 1pt, >=stealth', auto, scale=1, transform shape]

'''
fig_end = '''
\\end{tikzpicture}
\\caption{Agent desynchronisation when running through algorithm iterations in their respective execution loop.}
\\label{ch3:fig:agent-desynchronisation}
\\end{figure}
'''

f = open('/Users/maxi/Documents/Reading Uni [PG]/Documents/Thesis (Built Environment)/_chapter3/fig/agent-desynchronisation.tex', 'w')


f.write(fig_begin)

x_shift = 9
x_min = 2
y_max = -11

ev_num = 5
y_mean_diff = 2.0
y_jitter_start = 0.25
y_jitter_loop = 0.125

ev_start = [(random.random()*2-1)*y_jitter_start + y_mean_diff/ev_num*ev for ev in range(ev_num)]
ev_loop = [(random.random()*2-1)*y_jitter_loop + y_mean_diff for _ in range(ev_num)]

f.write('	\\draw (0, 1) node [draw, rectangle, fill=black!10](supplier) {S};\n')
f.write('	\\draw [thick] (-0.5, 0.25) to node[pos=1, right]{START} (%.2f, 0.25);\n' % (0.5 + x_min + x_shift - x_shift/ev_num))
f.write('	\\draw (0, %.2f) node [](s_end) {};\n' % (y_max))
f.write('	\\draw (%.2f, 0.25) node [](legend) {};\n' % (x_min + x_shift - x_shift/ev_num - 0.5))
f.write('	\\draw [dotted] (supplier) -- (s_end-|supplier); \n')
for ev in range(ev_num):
	ev_x = x_min + float(ev)/float(ev_num) * x_shift
	f.write('	\\draw (%.2f, 1) node [draw, rectangle, fill=black!10](ev%i) {EV$_%i$};\n' % (ev_x, ev, ev))
	f.write('	\\draw [dotted] (ev%i) -- (s_end-|ev%i); \n' % (ev, ev))

	i = 0
	while True:
		ev_y = -ev_start[ev] - i * ev_loop[ev]
		if ev_y < y_max:
			break
		f.write('	\\draw (%.2f,%.2f) node [draw, circle, inner sep=0pt, minimum size=1mm, fill=white](ev%iy%i) {};\n' % (ev_x, ev_y, ev, i))
		f.write('	\\draw (0,%.2f) node [draw, circle, inner sep=0pt, minimum size=1mm, fill=black](ss%iy%i) {};\n' % (ev_y, ev, i))
		f.write('	\\draw [->] (ev%iy%i) to (ss%iy%i);\n' % (ev, i, ev, i))
		if ev == ev_num - 1:
			if i == 0:
				f.write('	\\draw [decorate, decoration={brace,amplitude=5pt,raise=1mm}, yshift=0mm, color=black!50] (legend) -- (legend|-ev%iy%i) node[black, midway, xshift=2mm, align=left, color=black!50]{start delay};\n' % (ev, i))
			else:
				f.write('	\\draw [decorate, decoration={brace,amplitude=5pt,raise=1mm}, yshift=0mm, color=black!50] (legend|-ev%iy%i) -- (legend|-ev%iy%i) node[black, midway, xshift=2mm, align=left, color=black!50]{loop jitter};\n' % (ev, i-1, ev, i))
		i += 1



f.write(fig_end)
f.close()
