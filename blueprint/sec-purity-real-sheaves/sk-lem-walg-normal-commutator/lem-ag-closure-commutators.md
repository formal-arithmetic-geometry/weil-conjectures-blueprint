+++
id = "lem-ag-closure-commutators"
kind = "lemma"
title = "Normality, commutators and the Lie inclusion"
lean = ["AlgebraicGeometry.GeneralLinearGroup.lie_mem_lieSubalgebra_of_commutator_mem"]
order = 4052
uses = ["d-monodromy", "def-wf-lie-algebra-derivation", "lem-wf-algebraic-component-cosets", "lem-wf-conjugation-geometric-monodromy", "lem-wf-zariski-closure-subgroup"]
+++
For a represented degree datum as in [d-monodromy], $H$ is normal in
$G$, and

$$
aba^{-1}b^{-1}\in H\quad(a,b\in G),\qquad
[\operatorname{Lie}(G^\circ),\operatorname{Lie}(G^\circ)]\subseteq\operatorname{Lie}(H^\circ).
$$
