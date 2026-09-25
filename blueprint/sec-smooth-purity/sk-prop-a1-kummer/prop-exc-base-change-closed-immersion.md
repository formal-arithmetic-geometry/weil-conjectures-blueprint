+++
id = "prop-exc-base-change-closed-immersion"
kind = "theorem"
title = "Base change for a closed immersion, against an open immersion"
order = 1967
tags = ["latex:proposition"]
uses = ["def-cbc-exchange-map", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lem-exc-closed-ambient", "lem-exc-closed-support-triangle", "lem-exc-open-locality-direct-image"]
+++
Let $i:Z\hookrightarrow T$ be a closed immersion with open complement
$j:U\hookrightarrow T$, let $g:V\hookrightarrow T$ be an open
immersion, and form the Cartesian square with
$i':Z\cap V\hookrightarrow V$, $j':U\cap V\hookrightarrow V$ and
$g':Z\cap V\hookrightarrow Z$. Then for every
$K\in D(T_{\mathrm{et}},A)$ the base-change comparison

$$
\beta:\ Lg'^*Ri^{\times}K\xrightarrow{\ \sim\ }R(i')^{\times}Lg^*K
$$

of the ambient right adjoints of [lem-exc-closed-ambient] is an
isomorphism.

## Proof

Let $Lg^*$ act on the closed-support triangle
[lem-exc-closed-support-triangle] of the pair $(i,j)$,

$$
Lg^*i_*Ri^{\times}K\longrightarrow Lg^*K
\longrightarrow Lg^*Rj_*j^*K\xrightarrow{+1}.
$$

Pullback along the open immersion $g'$ is exact, and compact-support
base change [def-cbc-exchange-map] — for the closed immersion
$i$, which is proper, this is proper base change — identifies the
first term with
$i'_*Lg'^*Ri^{\times}K$; [lem-exc-open-locality-direct-image]
identifies the third term with $Rj'_*L(g'')^*j^*K$, and pullback
composition turns that into $Rj'_*j'^*Lg^*K$. The result is therefore
the triangle

$$
i'_*Lg'^*Ri^{\times}K\longrightarrow Lg^*K
\longrightarrow Rj'_*j'^*Lg^*K\xrightarrow{+1},
$$

which has the same second and third terms as the closed-support triangle
of the pair $(i',j')$,

$$
i'_*R(i')^{\times}Lg^*K\longrightarrow Lg^*K
\longrightarrow Rj'_*j'^*Lg^*K\xrightarrow{+1},
$$

and whose connecting maps are the canonical ones. Two such triangles are
compared by a canonical isomorphism of their first terms, and this
comparison is precisely $\beta$; the exact faithful $i'_*$ detects
it. Hence $\beta$ is an isomorphism.
