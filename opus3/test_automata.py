from automata import TransitionAutomata, ShadeAutomata, plot_grooves

ta = TransitionAutomata()
sa = ShadeAutomata()

plot_grooves(ta.grooves, 'ta')
plot_grooves(sa.grooves, 'sa')

for n in range(15):
    print sa.get_groove(7)
    print ta.get_groove(n)
