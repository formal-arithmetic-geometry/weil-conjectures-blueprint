+++
id = "lem-kun-inverse-image-monoidal"
kind = "lemma"
title = "Monoidality of the derived inverse image"
order = 6097
lean = ["AlgebraicGeometry.Etale.pullback_monoidal"]
uses = ["def-kun-derived-tensor"]
+++
Let $u:U\to V$ be a morphism of schemes and $\Lambda$ a commutative ring.
For $K,L\in D(V_{\Et},\Lambda)$ the canonical comparison morphism
$$
u^{-1}K\otimes^{\mathbf L}_\Lambda u^{-1}L\longrightarrow u^{-1}\bigl(K\otimes^{\mathbf L}_\Lambda L\bigr)
$$
is an isomorphism, bifunctorial in $K$ and $L$.

(*Source:* Stacks Project, Lemma 21.18.4, [Tag
07A4](https://stacks.math.columbia.edu/tag/07A4), for the morphism of ringed
topoi induced by $u$.)

## Proof

This is the recorded classical input named in the statement, Stacks Project,
Lemma 21.18.4 ([Tag 07A4](https://stacks.math.columbia.edu/tag/07A4)), for
the morphism of ringed topoi induced by the morphism of schemes: the inverse
image is monoidal for the derived tensor product. No separate proof is
given.

Unresolved dependencies: def:weil-pbc-inverse-image
