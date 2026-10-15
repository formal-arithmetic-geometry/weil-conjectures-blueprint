+++
id = "lem-weil-coefficient-frobenius"
kind = "lemma"
title = "Coefficient biduality at finite and integral stages"
order = 2464
uses = ["def-weil-derived-complete-integral-detailed", "def-weil-finite-torsion-constructibility"]
+++
For the coefficient stages of
[def-weil-finite-torsion-constructibility] and
[def-weil-derived-complete-integral-detailed], the following distinctions hold.

1. If $\Lambda=A_{E,n},E$, or
$\overline{\mathbf Q}_\ell$, then $\Lambda$ is self-injective and
quasi-Frobenius. Ordinary duality $\operatorname{Hom}_\Lambda(-,\Lambda)$
is exact, preserves finite modules, and for every finite
$\Lambda$-module $M$ the evaluation map
$$
M\longrightarrow
\operatorname{Hom}_\Lambda\bigl(\operatorname{Hom}_\Lambda(M,\Lambda),\Lambda\bigr)
$$
is an isomorphism. Consequently derived coefficient duality is an
anti-equivalence on bounded complexes with finite cohomology.
1. The discrete valuation ring $R=\mathcal O_E$ is not
quasi-Frobenius. Ordinary evaluation is an isomorphism for finite
projective $R$-modules, but not for all finite $R$-modules.
Every $K\in D^b(R)$ with finite cohomology is perfect, and the
*derived* evaluation
$$
K\longrightarrow
R\operatorname{Hom}_R\bigl(R\operatorname{Hom}_R(K,R),R\bigr)
$$
is an isomorphism.
1. More generally, derived evaluation into the coefficient double dual
is an isomorphism for every perfect complex over any ring. In particular,
the finite-Tor point case does not require self-injectivity of the
coefficient ring.
