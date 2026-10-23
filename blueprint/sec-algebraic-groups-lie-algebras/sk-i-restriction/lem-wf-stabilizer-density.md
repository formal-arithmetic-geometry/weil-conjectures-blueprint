+++
id = "lem-wf-stabilizer-density"
kind = "lemma"
title = "Closed stabilizers and density"
lean = ["Matrix.GeneralLinearGroup.mulVec_mem_of_mem_zeroLocus_vanishingIdeal", "Matrix.GeneralLinearGroup.forall_mulVec_mem_iff_forall_mem_zeroLocus_vanishingIdeal"]
order = 3748
uses = ["def-wf-geometric-monodromy-group"]
+++
Let $S\subseteq V$ be a vector subspace. The stabilizer
$\operatorname{Stab}_{\operatorname{GL}(V)}(S)$ is Zariski closed.
Consequently $S$ is $\Pi$-stable if and only if it is
$H_{\mathrm{geom}}$-stable.
