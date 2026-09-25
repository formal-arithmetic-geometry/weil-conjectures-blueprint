+++
id = "d-central"
kind = "definition"
title = "Positive central pairs and their construction"
order = 2669
uses = ["d-monodromy", "def-wf-algebraic-components", "def-wf-arithmetic-monodromy-extension", "def-wf-degree-components", "def-wf-geometric-monodromy-group", "def-wf-geometric-semisimplicity", "def-wf-monodromy-data", "lem-wf-arith-extension-group", "lem-wf-degree-component-image", "lem-wf-degree-components-grading", "rem-ptr-wf-arithmetic-monodromy-extension-1", "rem-ptr-wf-degree-components-2"]
+++
For data $(G,H,F)$, a positive central pair is
$(N,z)$ with $N\in\mathbf Z_{>0}$ and
$z\in\hyperref[d:geometry]{Z(G)}\cap HF^N$.
Admissible choices consist of $m>0$, a factorization $F^m=ch$ with
$c\in Z(G^\circ)^\circ$, $h\in H^\circ$, and a finite list
$g_1,\ldots,g_r$ meeting every coset of $G^\circ$ exactly once.
For such choices define the ordered product

$$
N=mr,\qquad z=\prod_{i=1}^r g_i c g_i^{-1}.
$$

The coset condition does not assert that $G/H$ is infinite cyclic or
that the cosets $HF^N$ for different $N$ are distinct.

Uses: [d-monodromy], [def-wf-algebraic-components], [def-wf-arithmetic-monodromy-extension], [def-wf-degree-components], [def-wf-geometric-monodromy-group], [def-wf-geometric-semisimplicity], [def-wf-monodromy-data], [lem-wf-arith-extension-group], [lem-wf-degree-component-image], [lem-wf-degree-components-grading], [rem-ptr-wf-arithmetic-monodromy-extension-1], [rem-ptr-wf-degree-components-2]
