+++
id = "sbc-cor-bounded-constructible-categories"
kind = "theorem"
title = "Smooth base change in bounded constructible categories"
order = 1687
tags = ["latex:corollary"]
uses = ["def-sbc-smooth-morphisms", "def-weil-pbc-constructible-complexes", "def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-proetale-modules", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-restriction-direct-image", "sbc-def-base-change-map", "sbc-def-base-change-square", "sbc-thm-bounded-derived-smooth-base-change", "thm-dg-finite-type-constructibility", "thm-weil-pbc-site-comparison"]
+++
In the Cartesian square
$Y=X\times_S T$, with projections $h:Y\to X$, $e:Y\to T$,
let $f:X\to S$ be smooth
and let $g:T\to S$ be quasi-compact and quasi-separated.
Suppose the schemes are Noetherian and the
direct-image
finiteness conditions hold for $g,h$. The
exchange map is an isomorphism

$$
f^*Rg_*\xrightarrow{\sim}Rh_*e^*:
D^b_c(T,\Lambda)\longrightarrow D^b_c(X,\Lambda).
$$

In particular this conclusion holds when the square consists of
finite-type schemes over a field with finite coefficients of
exponent invertible in that field.
The notation refers to bounded constructible complexes.
The direct images displayed are the etale ones and the finiteness
conditions assumed are the pro-etale ones of
[def-weil-pbc-constructible-direct-image-finiteness]; the transport
between the two sites is Step 2 of the proof.

## Proof

*Step 1: the exchange map.* The ambient etale exchange is an
isomorphism for $K\in\Dbc(T_{\Et},\Lambda)$ by
[sbc-thm-bounded-derived-smooth-base-change].

*Step 2: the finiteness conditions, transported to the etale site.*
The conditions $\mathrm{FIN}(g,\Lambda;c)$ and
$\mathrm{FIN}(h,\Lambda;c)$ of
[def-weil-pbc-constructible-direct-image-finiteness] are stated on
the pro-etale sites, and they imply the corresponding etale statement.
Indeed, for $L\in\Dbc(T_{\Et},\Lambda)$ the comparison isomorphism of
[prop-weil-pbc-comparison-direct-image] reads
$\nu_X^*Rg_{\Et,*}L\cong Rg_{\Proet,*}\nu_T^*L$; the right hand side
lies in $\Dbc(T_{\Proet},\Lambda)$ by
[prop-weil-pbc-restriction-direct-image] applied to the finiteness
conditions, and the objects of $\Dbc(T_{\Proet},\Lambda)$ are by
definition the pullbacks of the bounded constructible etale complexes
([def-weil-pbc-proetale-modules]); since $\nu_X^*$ is fully
faithful on bounded-below complexes,
[thm-weil-pbc-site-comparison], full faithfulness identifies
$Rg_{\Et,*}L$ with a bounded constructible etale complex. The same
argument applies to $h$.

*Step 3: the isomorphism in the subcategory.* Both sides of the
exchange map of Step 1 lie in the displayed full subcategory: the terms
$Rg_*$ and $Rh_*$ by Step 2, and the terms $f^*$ and $e^*$
because pullback is exact and preserves finite locally constant sheaves
and finite stratifications, hence bounded constructibility, by
[def-weil-pbc-constructible-complexes]. An isomorphism in the
ambient derived category between objects of a full triangulated
subcategory is an isomorphism of that subcategory, which is the
assertion.

*Step 4: the finite-type case.* For finite-type schemes over a
field, [thm-dg-finite-type-constructibility] proves directly that
$Rg_*$ and $Rh_*$ preserve $\Dbc$, so no finiteness hypothesis
beyond the standing ones is needed there.
