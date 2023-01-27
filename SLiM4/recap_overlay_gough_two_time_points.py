import tskit, msprime, pyslim, time, gzip, sys
import numpy as np
# import matplotlib.pyplot as plt

# ts1 = pyslim.load(sys.argv[1]).simplify()
# No simplify for Recap
ts_decap = tskit.load(sys.argv[1])
# ts_new = pyslim.SlimTreeSequence(ts_decap)
ts_recap = pyslim.recapitate(ts_decap, recombination_rate=5e-9, ancestral_Ne=100000, random_seed=sys.argv[2])
# ts_recap_simp = ts_recap.simplify()
# mutated = msprime.mutate(ts_recap_annot, rate=0.000000005, random_seed=sys.argv[2], keep=True)

mutated = msprime.sim_mutations(ts_recap, rate=5e-9, random_seed=sys.argv[2], model=msprime.SLiMMutationModel(type=1), keep=True, discrete_genome=True)
# mutated_annot = pyslim.annotate(mutated, model_type="WF", tick=1, reference_sequence=None, annotate_mutations=True)
mutated.dump(sys.argv[3])
        
