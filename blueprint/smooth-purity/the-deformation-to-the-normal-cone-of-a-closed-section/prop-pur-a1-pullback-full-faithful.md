+++
id = "prop-pur-a1-pullback-full-faithful"
kind = "theorem"
title = "Full faithfulness of the pullback along the affine line"
order = 3606
tags = ["latex:proposition"]
uses = ["def-pur-conventions", "def-weil-derived-tensor", "def-weil-scheme-morphism-properties", "fix-prop-adjunctions", "lem-pur-a1-direct-image", "lemma-weil-pbc-perfect-projection-formula", "prop-weil-pbc-inverse-image-derived-adjunction"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $B$ be a separated
finite-type $k$-scheme, let $\pi:\mathbf A^1_B\to B$ be the
projection, let $L\in D^b_{ctf}(B,\Lambda)$, and let $M$ be a
shift-twist of a finite free $\Lambda_B$-module, i.e. a constant
finite locally free coefficient sheaf. Then the pullback map

$$
\operatorname{Map}_B(L,M)\longrightarrow
\operatorname{Map}_{\mathbf A^1_B}(L\pi^*L,L\pi^*M),\qquad
\varphi\longmapsto L\pi^*\varphi,
$$

is a bijection. In particular $L\pi^*$ is fully faithful on such
objects: every automorphism of $L\pi^*M$ is $L\pi^*$ of a unique
automorphism of $M$, so the ambiguity of an isomorphism into a
pulled-back object is an ambiguity on the base.

## Proof

Under the pullback–direct-image adjunction of
[prop-weil-pbc-inverse-image-derived-adjunction], the pullback map
on Hom sets is the map induced by the unit

$$
\eta_M:M\longrightarrow R\pi_*L\pi^*M.
$$

The target object $M$ here is a shift of a finite locally free
coefficient sheaf, hence is site-perfect. The ordinary projection
formula [lemma-weil-pbc-perfect-projection-formula] therefore gives

$$
(R\pi_*\Lambda)\otimes^L M\xrightarrow{\sim}R\pi_*L\pi^*M.
$$

By the construction of this projection map from the pullback
counit, $\eta_M$ is the composite of this isomorphism with
$\eta_\Lambda\otimes1_M$. The latter is an isomorphism by
[lem-pur-a1-direct-image], with tensor identity as in
[def-weil-derived-tensor]. Thus the unit induces a bijection
$\operatorname{Hom}(L,M)\to\operatorname{Hom}(L,R\pi_*L\pi^*M)$
for every stated $L$, and adjunction gives the desired bijection.
Taking $L=M$ proves the automorphism assertion. No site-perfectness
of a general constructible $L$ is used.
