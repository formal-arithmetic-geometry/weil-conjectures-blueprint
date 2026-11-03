+++
kind  = "proof"
of    = "det-def-sfb-coefficient-comparisons"
uses = ["det-prop-sfb-module-derived-factorization"]
+++
*Formal input.* For a lax monoidal functor and a commutative square of ring objects,
restriction of scalars commutes with "transport, then restrict along the vertical maps"
([def-sfb-comap-mapmod-square], identity on underlying objects by
[lem-sfb-comap-mapmod-square-underlying]). In a square of adjunctions, an isomorphism between the
composites of right adjoints has a conjugate isomorphism between the composites of left adjoints
([def-sfb-conjugate-pull-iso]) and a mate ([def-sfb-mate-push-hom]). Restriction of scalars
commutes with extension of scalars along isomorphisms ([def-sfb-extend-comap-iso-of-iso]) and
with the linearization of a functor satisfying a projection formula
([def-sfb-projection-formula-comap]).

*Pushforward and pullback.* The second square of [det-def-sfb-coefficient-change] gives
$\operatorname{Res}_{a_Y}\circ f_*\cong f_*\circ\operatorname{Res}_{a_X}$
([def-sfb-comap-lower-star-iso]); its conjugate and mate are the underived (Pull) and (Push)
([def-sfb-pull-iso], [def-sfb-push-hom]). Since every $\alpha_f$ is invertible
([sk-prop-sfb-cartesian-coefficients]), restriction of scalars also commutes with $f^*$
([def-sfb-comap-upper-star-iso]), levelwise also on derived categories
([def-sfb-derived-comap-upper-star-iso]).

*Derived (Pull) and (Push).* Under the flatness assumption $\operatorname{Ext}_{a_X}$ is exact
([lem-sfb-extend-scalars-preserves-homology]) and $\operatorname{Res}_{a_X}$ preserves
K-injective complexes ([lem-sfb-comap-preserves-k-injectives]), so restriction of scalars
commutes with $Rf_*$ ([def-sfb-derived-comap-lower-star-iso]). Its conjugate along
$Lf^*\dashv Rf_*$ and $T\dashv D(\operatorname{Res})$ is (Pull) ([def-sfb-derived-pull-iso]), and
its mate along $T\dashv D(\operatorname{Res})$ is (Push) ([def-sfb-derived-push-hom]).

*Extension by zero.* Restriction of scalars commutes with $j_!$
([def-sfb-comap-open-immersion-shriek-iso]); the extension-by-zero isomorphisms are the
conjugates of the commutation of restriction of scalars with $j^*$ along $j_!\dashv j^*$, resp.
$D(j_!)\dashv D(j^*)$ ([def-sfb-open-immersion-shriek-iso],
[def-sfb-derived-open-immersion-shriek-iso]); no flatness is needed.

*(Shriek).* [def-sfb-derived-lower-shriek-hom], and the isomorphism criterion is
[lem-sfb-derived-lower-shriek-hom-iso].
