+++
id = "lem-fin-normal-generic-constant"
kind = "lemma"
title = "A generic constant sheaf on a normal Noetherian scheme"
order = 5188
lean = ["AlgebraicGeometry.Etale.constant_iso_genericPushforward_of_isNormal"]
uses = ["def-sbc-normal-dominant-galois", "lem-fin-etale-normal-components"]
+++
Let $V$ be Noetherian, normal and integral in the sense of
[def-sbc-normal-dominant-galois], with generic inclusion
$e:\operatorname{Spec}K\to V$. For a finite abelian group $M$, the natural
map of étale sheaves $\underline M_V\to e_*\underline M_K$ is an
isomorphism.

## Proof

Evaluate on an affine étale $W\to V$. By [lem-fin-etale-normal-components],
$W$ has finitely many normal integral open-and-closed components $W_a$.
Every nonempty $W_a$ dominates $V$, since its image is a nonempty open. Its
generic fibre is the spectrum of one finite separable field extension of
$K$: it is integral and étale of finite type over $K$, so its coordinate
algebra is a zero-dimensional finite-type domain, hence a finite separable
field. Thus $W$ and $W_K$ have the same finite set of connected components.

The sections of a constant sheaf $M$ on a connected scheme are $M$;
equivalently a section is a locally constant function to the finite discrete
set $M$. Both groups of sections here are therefore $\prod_aM$, and
restriction is the identity on each factor. These are precisely the maps
defining the asserted isomorphism, on a covering basis of the site.

Unresolved dependencies: def:weil-pbc-direct-image, def:weil-pbc-etale-sheaves, lem:weil-pbc-flat-lfp-open
