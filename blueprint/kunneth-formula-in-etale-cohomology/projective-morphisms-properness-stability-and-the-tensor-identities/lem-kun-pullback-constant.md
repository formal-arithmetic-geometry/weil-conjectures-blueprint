+++
id = "lem-kun-pullback-constant"
kind = "lemma"
title = "Inverse image of a constant sheaf"
order = 6075
lean = ["AlgebraicGeometry.Etale.pullback_constantSheaf"]
uses = ["def-kun-constant-sheaf", "lem-kun-stalk-as-pullback"]
+++
For a morphism of schemes $f:X\to Y$ and a $\Lambda$-module (or complex of
$\Lambda$-modules) $M$, the canonical morphism
$f^{-1}\underline{M}\to\underline{M}$ is an isomorphism on $X_{\Et}$.

## Proof

At a geometric point $\bar x$ of $X$, the stalk functor is the inverse image
of the point ([lem-kun-stalk-as-pullback]), so
$(f^{-1}\underline{M})_{\bar x}=(\underline{M})_{f(\bar x)}=M=(\underline{M})_{\bar x}$;
the canonical map is an isomorphism on every stalk hence an isomorphism of
sheaves by conservativity; for a complex the same argument applies
degreewise.

Unresolved dependencies: def:weil-pbc-inverse-image, def:weil-pbc-geometric-stalks, lem:weil-pbc-geometric-stalk-conservative
