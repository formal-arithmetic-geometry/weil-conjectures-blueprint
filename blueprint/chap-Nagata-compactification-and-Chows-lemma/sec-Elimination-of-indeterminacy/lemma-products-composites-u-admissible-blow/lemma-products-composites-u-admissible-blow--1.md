+++
id = "lemma-products-composites-u-admissible-blow--1"
kind = "lemma"
title = "Products and composites of $U$-admissible blow-ups (1)"
name_showing = false
order = 1430001
aliases = ["bp-r445-1"]
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso"]
uses = ["definition-admissible-blow-up"]
+++
Lean constructs common refinements using the following product comparison,
bypassing a separate statement for finite families of admissible blow-ups.
Let $T$ be a scheme, let $\mathcal I,\mathcal J\subseteq\mathcal O_T$ be
quasi-coherent ideals, and write
$\pi:T_1=\operatorname{Bl}_{\mathcal I}(T)\to T$. There is an isomorphism

$$
e:\operatorname{Bl}_{\mathcal I\mathcal J}(T)
\xrightarrow{\sim}
\operatorname{Bl}_{\mathcal J\mathcal O_{T_1}}(T_1)
$$

over $T$: if $q$ is the second blow-up map and $c$ the product blow-up
map, then $\pi\circ q\circ e=c$. No finite-type hypothesis on the ideals,
or quasi-compactness or quasi-separatedness hypothesis on $T$, is needed
for this comparison.
