+++
id = "cor-fin-deligne-open-over-field"
kind = "theorem"
title = "Higher open direct images over a field"
order = 5812
tags = ["latex:corollary"]
lean = ["AlgebraicGeometry.Etale.mem_Dbc_derivedPushforward_of_isOpenImmersion_overField"]
uses = ["thm-fin-deligne-generic-open"]
+++
Let $k$ be a field of characteristic different from $\ell$, let
$j:X\hookrightarrow Y$ be an open immersion of finite-type $k$-schemes, and
let $F$ be a constructible $\mathbf F_\ell$-sheaf. Then
$Rj_*F\in\Dbc(Y,\mathbf F_\ell)$.

## Proof

Apply [thm-fin-deligne-generic-open] with $S=\operatorname{Spec}k$. Its only
nonempty open is $S$ itself, so the generic conclusion is the assertion on
all of $Y$. No stratification of $Y$ and no closed-base-change assertion for
$Rj_*$ is needed here.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-derived-categories
