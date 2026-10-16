+++
id = "lem-sc-genus-invariant"
kind = "lemma"
title = "The genus is invariant under extension"
lean = ["AlgebraicGeometry.Scheme.Hom.genus_baseChangeField"]
order = 1038
uses = ["def-sc-curves", "def-sc-genus", "def-sc-jacobian", "lem-sc-flat-base-change-coherent", "thm-sc-jacobian-representability"]
+++
Let $C$ be a proper smooth connected curve over
$k$ and let $k\subseteq k'$ be algebraically closed. Then

$$
g(C_{k'})=g(C),
$$

compatibly with the Jacobian of
[thm-sc-jacobian-representability] (i.e. $J_{C_{k'}}\cong(J_C)_{k'}$, and the identifications of
[def-sc-jacobian] are compatible with base change).
