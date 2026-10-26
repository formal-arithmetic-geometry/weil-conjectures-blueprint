+++
id = "lem-weil-coefficient-frobenius"
kind = "lemma"
title = "Coefficient biduality at finite and integral stages"
lean = ["IsDiscreteValuationRing.injective_quotient_pow", "IsDiscreteValuationRing.isReflexive_quotient_pow", "IsDiscreteValuationRing.dual_quotient_eq_zero", "IsDiscreteValuationRing.not_isReflexive_quotient"]
order = 2823
uses = ["det-def-sfb-condensed-ring"]
+++
Consider the coefficient rings $A_{E,n}=\mathcal O_E/\pi_E^n$, $\mathcal O_E$,
$E$ and $\Qlb$ as ordinary rings; they are the rings of sections over the
point of the corresponding condensed coefficient rings
([det-def-sfb-condensed-ring]). The following distinctions hold.

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
