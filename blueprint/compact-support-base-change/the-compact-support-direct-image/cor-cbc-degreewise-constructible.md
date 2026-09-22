+++
id = "cor-cbc-degreewise-constructible"
kind = "theorem"
title = "Degreewise and constructible forms"
order = 6612
lean = ["AlgebraicGeometry.Etale.compactSupportExchange_isIso_cohomology", "AlgebraicGeometry.Etale.compactSupportExchange_isIso_constructible"]
tags = ["latex:corollary"]
uses = ["def-compact-support-direct-image", "prop-finite-compact-support-constructibility", "def-cbc-exchange-map", "thm-cbc-finite-torsion", "def-cbc-compact-support-square"]
+++
Let $\square$ be a compact-support base-change square
([def-cbc-compact-support-square]) with $f$ separated of finite type and
$\Lambda$ finite.

1. For every abelian sheaf $F$ of $\Lambda$-modules on $X_{\Et}$ and every
   $q\geq0$, the $q$-th cohomology of $\Ex_!(F)$ of
   [def-cbc-exchange-map] is an isomorphism
   $$
    g^{-1}R^qf_!F\xrightarrow{\ \sim\ }R^qf'_!g'^{-1}F.
   $$
2. If, moreover, $f$ and $f'$ satisfy the bounded constructibility and
   amplitude conditions of the finite-coefficient compact-support
   constructibility statement (so that $Rf_!$ and $Rf'_!$ are defined on the
   bounded constructible categories), then for every
   $K\in D^b_c(X_{\Et},\Lambda)$ the isomorphism of [thm-cbc-finite-torsion]
   is one in $D^b_c(Y'_{\Et},\Lambda)$.

## Proof

For the first assertion, view $F$ as a complex concentrated in degree $0$
and apply [thm-cbc-finite-torsion] to $F\in D^+(X_{\Et},\Lambda)$: the
exchange map $\Ex_!(F)$ of [def-cbc-exchange-map] is an isomorphism in
$D^+(Y'_{\Et},\Lambda)$. An isomorphism in the derived category induces an
isomorphism on every cohomology sheaf; the $q$-th cohomology sheaf of
$g^{-1}Rf_!F$ is $g^{-1}R^qf_!F$ by the exactness of the inverse image, and
that of $Rf'_!g'^{-1}F$ is $R^qf'_!g'^{-1}F$ by the definition of the
compact-support direct image, so the displayed isomorphisms of (1) follow.

For the second assertion, apply [thm-cbc-finite-torsion] to
$K\in D^b_c(X_{\Et},\Lambda)\subset D^+(X_{\Et},\Lambda)$. By the
compact-support constructibility statement the two compact-support direct
images restrict to the bounded constructible categories of the statement, and
the inverse image of $g'$ is exact and preserves bounded constructibility, so
both sides of the isomorphism are objects of $D^b_c(Y'_{\Et},\Lambda)$; since
$D^b_c(Y'_{\Et},\Lambda)$ is a full subcategory of $D^+(Y'_{\Et},\Lambda)$,
the isomorphism of [thm-cbc-finite-torsion] is one there, which proves
(2).

Unresolved dependencies: def:weil-pbc-constructible-complexes, def:weil-pbc-etale-sheaves, def:weil-derived-cohomology-sheaves, def:weil-pbc-inverse-image
