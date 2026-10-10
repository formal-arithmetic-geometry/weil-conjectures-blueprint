+++
kind  = "proof"
of    = "lem-pd-canonical-descent-datum"
+++
Write $Y=\Spec(k)$, $X=\Spec(k_s)$ as in [def-pd-separable-closure] and
let $p_0,p_1:X_2=X\times_YX\to X$ be the two projections, so that
$X_2=\Spec(k_s\otimes_kk_s)$ is the fibre product of
[def-pc-base-change]. By [cor-pd-pic0-base-change] applied to
the composite $X_2\to X\to Y$ the functor
$\operatorname{Pic}^0_{C_s/k_s}$ pulls back to
$\operatorname{Pic}^0_{C_{X_2}/X_2}$ along either projection: the two pullbacks
are the same functor $F_2$, because both are the restriction of the single
functor $\operatorname{Pic}^0_{C/k}$ on the slice over $X_2$ by
[cor-pd-pic0-base-change]. By [thm-pd-geometric-pic0] and
[def-sc-jacobian] the scheme $p_0^*J_s$ represents $F_2$, and so does
$p_1^*J_s$. Two representing objects of one functor are canonically
isomorphic, with a unique isomorphism respecting the representing
identifications: this is the uniqueness argument of
[lem-sc-jacobian-unique], applied over the base $X_2$. Let
$\varphi:p_0^*J_s\to p_1^*J_s$ be that unique isomorphism; it is an
isomorphism of schemes over $X_2$, as required in
[def-pd-descent-datum].
