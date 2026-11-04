+++
kind = "proof"
of = "lemma-kunneth-finite-direct-image"
order = 706
uses = ["lemma-base-change-along-product-projection"]
+++
Both sides are additive in $Q$, so we may assume $Q=\pi_*A_{T'}$. Set

$$
v=\operatorname{id}_Y\times\pi,\qquad
w=\operatorname{id}_X\times\pi,\qquad
h'=f\times\operatorname{id}_{T'}.
$$

Direct image along a finite morphism is exact and commutes with pullback, and by the
projection formula we have

$$
Rf_*M\boxtimes\pi_*A_{T'}
\simeq v_*p_{Y,T'}^*Rf_*M,
\qquad
M\boxtimes\pi_*A_{T'}\simeq w_*p_{X,T'}^*M.
$$

Since $hw=vh'$, the comparison between these two expressions is
$v_*$ of the base change map of
Lemma [lemma-base-change-along-product-projection] for $h'$. Hence it
is an isomorphism.
This comparison is the Künneth map, because under the adjunction
$h^*\dashv Rh_*$ and the adjunctions for the finite maps, both correspond to the counit
$\varepsilon_f\otimes^{\mathbf L}1$ displayed in (8.4).
