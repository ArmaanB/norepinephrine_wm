dt = 0.001             # Time step
t_cue = 1.0            # Duration of cue presentation
cue_scale = 1.0        # How strong the cuelus is from the visual system
perceived = 0          # ???
time_scale = 0.4       # ???
steps = 100            # How fine to run the outer loop of the simulation
noise_wm = 0.005       # Standard deviation of white noise added to WM
noise_decision = 0.005 # Standard deviation of white noise added to decision
neurons_decide = 100   # Number of neurons for decision
neurons_inputs = 100   # Number of neurons for inputs ensemble
neurons_wm = 100       # Number of neurons for working memory ensemble
tau_wm = 0.1           # Synapse on recurrent connection in wm
tau = 0.01             # Synaptic time constant between ensembles
dt_sample = 0.01       # Timestep for data recording through probes
t_delay = 8.0          # Duration of delay period between cue and decision
