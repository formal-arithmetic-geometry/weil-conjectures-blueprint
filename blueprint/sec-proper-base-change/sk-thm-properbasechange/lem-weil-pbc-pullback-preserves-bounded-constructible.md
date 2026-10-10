+++
id = "lem-weil-pbc-pullback-preserves-bounded-constructible"
kind = "lemma"
title = "Pullback preserves bounded constructibility"
order = 1303
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-proetale-operations", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-inverse-image-exact"]
+++
Let $\Lambda=P_n$ be as in
[def-weil-pbc-constructible-direct-image-finiteness] and let $g:V'\to V$ be
a morphism of schemes. The derived pullback $Lg^*=g^{-1}$ restricts to an
exact triangulated functor
$$
 Lg^*:\Dbc(V_{\Proet},\Lambda)\longrightarrow\Dbc(V'_{\Proet},\Lambda),
$$
and carries the class of objects with cohomology in $[a,b]$ into the same
class.

## Proof

On the etale site, inverse image is exact and takes a constructible
$\Lambda$-module sheaf to a constructible one: in the partition description
of a constructible complex the restriction to each piece is lisse with
finite stalks, the inverse image of a lisse sheaf is lisse, and the inverse
image of a locally closed constructible subscheme is locally closed
constructible, the preimage of a finite partition being a finite partition.
Hence the bounded constructible etale complexes are preserved, with the
cohomological interval preserved by exactness. For finite constant
coefficients, the pro-etale operations identify the pro-etale inverse image
with the sheaf inverse image, and [lem-weil-pbc-comparison-pullback]
transports the etale statement to the pro-etale site.
