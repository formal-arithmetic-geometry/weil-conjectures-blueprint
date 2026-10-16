+++
id = "cor-wf-rank-one-punctual-purity-curve"
kind = "theorem"
title = "Punctual purity of a rank-one Weil character on a curve"
lean = ["AlgebraicGeometry.WeilGroup.frobeniusWeight_eq_of_continuous", "AlgebraicGeometry.WeilGroup.frobeniusWeight_eq_of_deg_eq_one"]
order = 2972
tags = ["latex:corollary"]
uses = ["cor-wf-rank-one-degree-factorization-curve", "def-weil-local-frobenius-trace", "def-weil-punctual-weights", "def-wf-fundamental-representation", "def-wf-weil-group", "lem-tw-root-of-unity-modulus", "p-real-operations", "thm-wf-rank-one-finite-geometric-image-curve"]
+++
In the situation of
[thm-wf-rank-one-finite-geometric-image-curve], with $c$ and
$\varepsilon$ from [cor-wf-rank-one-degree-factorization-curve]
(applicable because $\chi(\Pi)$ is finite by that theorem), fix an embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$, and use its
restriction to $E$ (equivalently, choose an embedding $E\hookrightarrow \mathbf C$ and an extension to $\overline{\mathbf Q}_\ell$). The rank-one lisse Weil sheaf
associated with $\chi$ by the
fundamental representation
is punctually $\iota$-pure of the
real weight

$$
w_\iota(\chi)=2\log_q|\iota(c)|,
$$

where $c=\chi(s)$ for any
degree-one element $s$.
The sheaf, degree, and punctual-purity conventions are those of
[def-wf-fundamental-representation], [def-wf-weil-group], [def-weil-punctual-weights].
