+++
kind  = "proof"
of    = "prop-sfb-module-right-derived-lower-star-iso"
+++
By definition $f_*=\operatorname{Res}_{\eta_f}\circ\operatorname{mapMod}(f^{\Ab}_*)$
([def-sfb-module-lower-star]), and restriction of scalars is exact
([sk-def-sfb-change-of-scalars]). For an exact functor $G$ and an additive functor $F$
on a category with K-injective resolutions, $R(G\circ F)\cong D(G)\circ RF$: both are
computed on a K-injective resolution $I$ of the argument, by $G(F(I))$, and
$D(G)\circ RF$ satisfies the universal property of the right derived functor of
$G\circ F$ since its comparison map is an isomorphism on K-injective complexes
([sk-def-sfb-derived-categories]). Apply this with $F=\operatorname{mapMod}(f^{\Ab}_*)$
and $G=\operatorname{Res}_{\eta_f}$.
