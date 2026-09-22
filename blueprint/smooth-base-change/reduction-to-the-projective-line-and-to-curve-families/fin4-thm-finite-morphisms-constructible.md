+++
id = "fin4-thm-finite-morphisms-constructible"
kind = "theorem"
title = "Finite morphisms preserve constructibility"
order = 5213
lean = ["AlgebraicGeometry.Etale.isConstructible_higherDirectImage_of_isFinite"]
uses = ["sbc-def-coefficient-conventions", "lem-fin-finite-morphism"]
+++
Let $f:X\to S$ be a finite morphism with $S$ of finite type over $k$, and
let $F$ be a constructible $\Lambda$-sheaf on $X_{\Et}$. Then the higher
direct images $R^qf_*F$ are constructible on $S_{\Et}$ for every $q\geq0$,
and $R^qf_*F=0$ for $q>0$: the vanishing bound $2\cdot0$ of the zero
relative dimension.

## Proof

Apply [lem-fin-finite-morphism], which proves both constructibility of
$f_*F$ and exactness of finite direct image. It uses the finite-stalk
formula and the earlier finite-image constructibility proof, with no
cardinality or general finiteness input.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image
