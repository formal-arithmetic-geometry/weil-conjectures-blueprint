+++
id = "cor-cbc-degreewise-constructible"
kind = "theorem"
title = "Degreewise and constructible forms"
order = 3127
tags = ["latex:corollary"]
uses = ["def-cbc-compact-support-square", "def-cbc-exchange-map", "def-compact-support-direct-image-detailed", "def-weil-derived-cohomology-sheaves", "def-weil-pbc-constructible-complexes", "def-weil-pbc-etale-sheaves", "def-weil-pbc-inverse-image", "prop-finite-compact-support-constructibility", "thm-cbc-finite-torsion"]
+++
Let $\square$ be a
compact-support
base-change square with $f$ separated of finite type and $\Lambda$
finite.

1. For every abelian sheaf $F$ of $\Lambda$-modules on $X_{\Et}$
and every $q\geq0$, the $q$-th cohomology of
$\operatorname{Ex}_!(F)$ of [def-cbc-exchange-map] is an
isomorphism
$$
g^{-1}R^qf_!F\xrightarrow{\ \sim\ }R^qf'_!g'^{-1}F.
$$
1. If, moreover, $f$ and $f'$ satisfy the bounded
constructibility and amplitude conditions of
[prop-finite-compact-support-constructibility] (so that
$Rf_!$ and $Rf'_!$ are defined on the
bounded constructible
categories), then for every
$K\in D^b_c(X_{\Et},\Lambda)$ the isomorphism of
[thm-cbc-finite-torsion] is one in
$D^b_c(Y'_{\Et},\Lambda)$.

## Proof

For the first assertion, view $F$ as a complex concentrated in
degree $0$ and apply [thm-cbc-finite-torsion] to
$F\in D^+(X_{\Et},\Lambda)$: the exchange map
$\operatorname{Ex}_!(F)$ of [def-cbc-exchange-map] is an
isomorphism in $D^+(Y'_{\Et},\Lambda)$. An isomorphism in the
derived category induces an isomorphism on every cohomology sheaf
([def-weil-derived-cohomology-sheaves]); the $q$-th
cohomology sheaf of $g^{-1}Rf_!F$ is $g^{-1}R^qf_!F$ by the
exactness of the inverse image of [def-weil-pbc-inverse-image],
and that of $Rf'_!g'^{-1}F$ is $R^qf'_!g'^{-1}F$ by the
definition of the compact-support direct image, so the displayed
isomorphisms of (1) follow.

For the second assertion, apply [thm-cbc-finite-torsion] to
$K\in D^b_c(X_{\Et},\Lambda)\subset D^+(X_{\Et},\Lambda)$. By
[prop-finite-compact-support-constructibility] the two
compact-support direct images restrict to the bounded constructible
categories of the statement, and the inverse image of $g'$ is
exact and preserves bounded constructibility, so both sides of the
isomorphism are objects of $D^b_c(Y'_{\Et},\Lambda)$; since
$D^b_c(Y'_{\Et},\Lambda)$ is a full subcategory of
$D^+(Y'_{\Et},\Lambda)$, the isomorphism of
[thm-cbc-finite-torsion] is one there, which proves (2).
