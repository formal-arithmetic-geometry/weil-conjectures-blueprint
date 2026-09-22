+++
id = "thm-cbc-qbar"
kind = "theorem"
title = "$\Qlb$ compact-support base change"
order = 6627
lean = ["AlgebraicGeometry.Proetale.compactSupportExchange_isIso_qlBar"]
uses = ["thm-cbc-finite-extension", "lem-cbc-extension-zero-projection-formula"]
+++
Let $f:X\to Y$ be separated of finite type, $g:Y'\to Y$ arbitrary and
$K\in\Dbc(X,\Qlb)$, with the finite-level hypotheses of
[thm-cbc-finite-extension] at every finite stage. The descended exchange
transformation is an isomorphism
$$
 Lg^*Rf_!K\xrightarrow{\ \sim\ }Rf'_!Lg'^*K
 \quad\text{in }\Dbc(Y',\Qlb).
$$
If $K$ is represented by a pair $(E,K_E)$ with $K_E\in\Dbc(X,E)$, the map is
represented after a finite overfield $M$ by the $M$-coefficient isomorphism of
[thm-cbc-finite-extension] applied to $T_{M/E}K_E$; the result is independent
of $E$, $M$, and the representative.

## Proof

The scalar-extension compatibilities for the functors $Rf_!$ and $Lg^*$
hold: for the direct image factor, scalar extension commutes with $Rp_*$ of
the proper $p$, and with $j_!$ by the projection formula
[lem-cbc-extension-zero-projection-formula] (whose scalar-extension instance
is $F\otimes^L_{\mathcal O_E}j_!K\cong j_!(F\otimes^L_{\mathcal O_E}K)$ for a
finite field $F/E$, as $j^*$ of the constant coefficient is the restriction);
hence the family $(Rf_{!,E})_E$ with the exchange transformations descends by
the descent proposition for functors, and at every finite stage it is an
isomorphism by [thm-cbc-finite-extension]. The common stage colimit of the
$\Qlb$-category, triangulated and idempotent complete, preserves the
isomorphism, giving the assertion, with the stated independence as in
[thm-cbc-finite-extension].

Unresolved dependencies: prop:weil-pbc-descent-functors, def:weil-pbc-scheme-conventions, def:weil-pbc-qbar-category, prop:weil-pbc-scalar-extension, thm:weil-pbc-idempotent-complete-triangulation
