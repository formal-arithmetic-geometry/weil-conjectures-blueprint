+++
id = "lem-wf-stabilizer-density"
kind = "lemma"
title = "Closed stabilizers and density"
lean = ["Matrix.GeneralLinearGroup.mulVec_mem_of_mem_zeroLocus_vanishingIdeal", "Matrix.GeneralLinearGroup.forall_mulVec_mem_iff_forall_mem_zeroLocus_vanishingIdeal"]
order = 3744
uses = ["d-monodromy"]
+++
Let $S\subseteq V=k^n$ be a vector subspace. The stabilizer
$\operatorname{Stab}_{\operatorname{GL}_n}(S)$ is Zariski closed.
Consequently, for a subgroup $\Gamma\subseteq\operatorname{GL}_n(k)$,
$S$ is $\Gamma$-stable if and only if it is stable under the Zariski
closure of $\Gamma$. In particular, for a represented degree datum
([d-monodromy]), $S$ is $P$-stable if and only if it is $H$-stable, and
$W$-stable if and only if it is $G$-stable.
