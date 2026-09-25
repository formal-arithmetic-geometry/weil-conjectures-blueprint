+++
id = "d-central"
kind = "definition"
title = "Positive central pairs and their construction"
order = 2716
uses = ["d-monodromy", "def-wf-algebraic-components"]
+++
For the monodromy data $(G,H,F)$ of a represented degree datum
([d-monodromy]), a positive central pair is
$(N,z)$ with $N\in\mathbf Z_{>0}$ and
$z\in Z(G)\cap HF^N$, where $Z(G)$ is the centre of $G$.
Admissible choices consist of $m>0$, a factorization $F^m=ch$ with
$c\in Z(G^\circ)^\circ$, $h\in H^\circ$ (identity components as in
[def-wf-algebraic-components]), and a finite list
$g_1,\ldots,g_r$ meeting every coset of $G^\circ$ exactly once.
For such choices define the ordered product

$$
N=mr,\qquad z=\prod_{i=1}^r g_i c g_i^{-1}.
$$

The coset condition does not assert that $G/H$ is infinite cyclic or
that the cosets $HF^N$ for different $N$ are distinct.

Uses: [d-monodromy], [def-wf-algebraic-components]
