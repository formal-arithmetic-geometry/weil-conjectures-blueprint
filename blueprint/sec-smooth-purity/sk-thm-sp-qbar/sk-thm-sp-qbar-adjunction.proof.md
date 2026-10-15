+++
kind = "proof"
of = "det-sp-qbar-adjunction"
+++
*The bijections.* The first and last are (1) and (3) of
[det-sp-qbar-finite-descent], using $Rf_{!,\Qlb}M\simeq(Rf_{!,F}M_F)_{\Qlb}$ and
$f^*_{\Qlb}K(d)[2d]\simeq(f^*_FK_F(d)[2d])_{\Qlb}$. The middle one is the colimit
of the rational adjunction bijections of [det-sp-rational-adjunction] over each
$F$; these form a map of direct systems because, by
[det-sp-field-extension-towers], the comparisons for $F\subset F'$ carry the unit
and counit over $F$ to those over $F'$, so the adjunction bijections commute
with extension of scalars.

*Independence and naturality.* Two choices of models become isomorphic over
some finite $F$, and a morphism $M\to M'$ or $K\to K'$ in $\Dbc(-,\Qlb)$, as well
as the identities required for naturality, are defined over one finite $F$ by
[det-sp-qbar-finite-descent] (2). Over that $F$ the rational adjunction is
natural in its arguments, and extension of scalars to larger $F'$ preserves the
bijections; so the colimit bijection is independent of models and natural. A
natural bijection of Hom functors defines an adjunction.

*Purity map.* The Brown adjoint $f^!_{\Qlb}$ is also right adjoint to
$Rf_{!,\Qlb}$, so [det-sp-unique-right-adjoint] gives the unique
counit-compatible isomorphism; the unit and counit of the new adjunction are
images of those over finite $F$, so the Brown unit and counit are identified
with those transported from finite extensions, and the smooth trace with
coefficients $\Qlb$ is normalized by integration at finite level.
