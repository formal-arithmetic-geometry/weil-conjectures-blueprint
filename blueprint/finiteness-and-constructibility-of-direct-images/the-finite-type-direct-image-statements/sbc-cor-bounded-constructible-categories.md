+++
id = "sbc-cor-bounded-constructible-categories"
kind = "theorem"
title = "Smooth base change in bounded constructible categories"
order = 5819
tags = ["latex:corollary"]
lean = ["AlgebraicGeometry.smooth_base_change_Dbc"]
uses = ["thm-dg-finite-type-constructibility"]
+++
In the Cartesian square $Y=X\times_ST$, with projections $h:Y\to X$,
$e:Y\to T$, let $f:X\to S$ be smooth and let $g:T\to S$ be quasi-compact and
quasi-separated. Suppose the schemes are Noetherian and the direct-image
finiteness conditions hold for $g,h$. The exchange map is an isomorphism
$$
f^*Rg_*\xrightarrow{\ \sim\ }Rh_*e^*:\Dbc(T,\Lambda)\longrightarrow\Dbc(X,\Lambda).
$$
In particular this conclusion holds when the square consists of finite-type
schemes over a field with finite coefficients of exponent invertible in that
field.

The direct images displayed are the étale ones and the finiteness conditions
assumed are the pro-étale ones; the transport between the two sites is Step
2 of the proof.

## Proof

*Step 1: the exchange map.* The ambient étale exchange is an isomorphism for
$K\in\Dbc(T_{\Et},\Lambda)$ by the bounded derived smooth base-change
theorem.

*Step 2: the finiteness conditions, transported to the étale site.* The
conditions $\mathrm{FIN}(g,\Lambda;c)$ and $\mathrm{FIN}(h,\Lambda;c)$ are
stated on the pro-étale sites, and they imply the corresponding étale
statement. Indeed, for $L\in\Dbc(T_{\Et},\Lambda)$ the comparison
isomorphism reads
$\nu_X^*Rg_{\Et,*}L\cong Rg_{\Proet,*}\nu_T^*L$; the right-hand side lies in
$\Dbc(T_{\Proet},\Lambda)$ by the restriction proposition applied to the
finiteness conditions, and the objects of $\Dbc(T_{\Proet},\Lambda)$ are by
definition the pullbacks of the bounded constructible étale complexes; since
$\nu_X^*$ is fully faithful on bounded-below complexes, full faithfulness
identifies $Rg_{\Et,*}L$ with a bounded constructible étale complex. The
same argument applies to $h$.

*Step 3: the isomorphism in the subcategory.* Both sides of the exchange map
of Step 1 lie in the displayed full subcategory: the terms $Rg_*$ and
$Rh_*$ by Step 2, and the terms $f^*$ and $e^*$ because pullback is exact
and preserves finite locally constant sheaves and finite stratifications,
hence bounded constructibility. An isomorphism in the ambient derived
category between objects of a full triangulated subcategory is an
isomorphism of that subcategory, which is the assertion.

*Step 4: the finite-type case.* For finite-type schemes over a field,
[thm-dg-finite-type-constructibility] proves directly that $Rg_*$ and
$Rh_*$ preserve $\Dbc$, so no finiteness hypothesis beyond the standing ones
is needed there.

*Import note.* The source records that an earlier version of this proof
mixed the two coefficient sites — the ambient exchange isomorphism is the
étale statement, while the finiteness conditions and the restriction
statement are stated on the pro-étale sites. Step 2 above supplies the
missing transport along the comparison morphism $\nu$; no new input is
needed.

Unresolved dependencies: sbc-def-base-change-square, sbc-def-base-change-map, def:sbc-smooth-morphisms, def:weil-pbc-constructible-complexes, def:weil-pbc-constructible-direct-image-finiteness, sbc-thm-bounded-derived-smooth-base-change, prop:weil-pbc-restriction-direct-image, prop:weil-pbc-comparison-direct-image, thm:weil-pbc-site-comparison, def:weil-pbc-proetale-modules
