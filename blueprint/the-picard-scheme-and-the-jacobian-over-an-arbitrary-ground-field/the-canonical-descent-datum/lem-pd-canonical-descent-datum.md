+++
id = "lem-pd-canonical-descent-datum"
kind = "lemma"
title = "The Picard functor produces a canonical descent datum"
order = 4714
lean = ["AlgebraicGeometry.Curve.jacobian_descentDatum"]
uses = ["def-pd-separable-closure", "def-pd-descent-datum", "thm-pd-geometric-pic0", "cor-pd-pic0-base-change"]
+++
Let $k$ be a field, let $C$ be a smooth projective curve over $k$ which is
geometrically integral, let $k_s$ be a separable closure
[def-pd-separable-closure] of $k$, put $C_s=C_{k_s}$ for the base change, and
let $J_s$ be the representing object of $\operatorname{Pic}^0_{C_s/k_s}$ of
[thm-pd-geometric-pic0]. Then $J_s$ carries a descent datum
[def-pd-descent-datum] over $\Spec(k_s)/\Spec(k)$.

## Proof

Write $Y=\Spec(k)$, $X=\Spec(k_s)$ and let $p_0,p_1:X_2=X\times_YX\to X$ be
the two projections, so that $X_2=\Spec(k_s\otimes_kk_s)$.

By [cor-pd-pic0-base-change] applied to the composite $X_2\to X\to Y$ the
functor $\operatorname{Pic}^0_{C_s/k_s}$ pulls back to
$\operatorname{Pic}^0_{C_{X_2}/X_2}$ along either projection: the two
pullbacks are the same functor $F_2$, because both are the restriction of the
single functor $\operatorname{Pic}^0_{C/k}$ on the slice over $X_2$.

By [thm-pd-geometric-pic0] the scheme $p_0^*J_s$ represents $F_2$, and so
does $p_1^*J_s$. Two representing objects of one functor are canonically
isomorphic, with a unique isomorphism respecting the representing
identifications: this is the uniqueness argument for Jacobians, applied over
the base $X_2$. Let $\varphi:p_0^*J_s\to p_1^*J_s$ be that unique
isomorphism; it is an isomorphism of schemes over $X_2$, as required in
[def-pd-descent-datum].

Unresolved dependencies: def:pc-smooth-projective-curve, def:pc-geometrically-irreducible, def:pc-base-change, def:sc-jacobian, lem:sc-jacobian-unique
