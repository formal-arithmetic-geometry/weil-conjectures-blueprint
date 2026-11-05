+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas--4"
order = 829008
uses = ["theorem-exceptional-inverse-image", "proposition-forgetting-supports-composition", "proposition-composition-base-change-rf-shriek", "proposition-proper-direct-image-constructible-complexes"]
+++
Use $Rf_!\simeq Rf_*$ for proper $f$
[proposition-forgetting-supports-composition] to regard $f^!$ as a right
adjoint of $Rf_*$. Composition of exceptional inverse images gives
$\gamma:f^!\omega_Y\simeq\omega_X$. Its inverse and the counit define
the trace $t:Rf_*\omega_X\to\omega_Y$.

The adjunction $f^*\dashv Rf_*$ makes $Rf_*$ lax monoidal; the braiding
hypothesis makes it lax braided. For every $M$ form the comparison

$$
c_M:Rf_*\cHom_X(M,\omega_X)
\longrightarrow\cHom_Y(Rf_*M,Rf_*\omega_X)
\xrightarrow{\cHom_Y(Rf_*M,t)}\cHom_Y(Rf_*M,\omega_Y).
$$

The unbounded proper projection formula at finite coefficients makes
$c_M$ an isomorphism: after the tensor–Hom and the two functor
adjunctions, composition with $c_M$ becomes precomposition with the
projection isomorphism. This is
`CategoryTheory.Adjunction.isIso_dualComparison_of_isIso_projection`,
using `AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarProjectionMap_of_finite`.

Uncurrying both sides and using compatibility with the braidings gives

$$
c_{\mathbb D_XK}\circ Rf_*\delta_K
=\mathbb D_Y(c_K)\circ\delta_{Rf_*K}.
$$

This is the general identity
`CategoryTheory.MonoidalClosed.map_toIhomIhom_comp_dualComparison`.
Since both comparison maps are isomorphisms, the identity identifies
the two double-dual maps up to isomorphism of arrows, and proves the
criterion. The argument uses the comparisons $c_M$ defined above;
it does not identify them with the chosen tensor–Hom exchange of
[lemma-internal-adjunction-two-exchange-formulas--1].
