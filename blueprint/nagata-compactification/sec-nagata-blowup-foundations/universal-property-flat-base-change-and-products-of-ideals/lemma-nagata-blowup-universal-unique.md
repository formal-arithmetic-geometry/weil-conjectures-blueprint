+++
id = "lemma-nagata-blowup-universal-unique"
kind = "lemma"
title = "Uniqueness of the universal lift"
order = 352
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.hom_ext_of_isInvertible_comap"]
uses = ["def-nagata-blowup-universal-lift", "def-nagata-global-blowup-cover-comparison", "lemma-nagata-blowup-universal-graded-map", "lemma-nagata-chart-extended-ideal-principal", "lemma-nagata-proj-chart-ring-cocycle", "lemma-nagata-relative-proj-invertible-tensor-powers", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open"]
+++
Under the data of [def-nagata-blowup-universal-lift], every $X$-morphism
$h\colon Y\to\operatorname{Bl}_{\mathcal I}(X)$ inducing the chosen
invertible quotient equals the constructed map $\widetilde f$.

## Proof

On each affine open of $X$, let $D_+(f)$ range over the standard opens
indexed by the degree-one elements $f\in\mathcal I$; these opens cover the
blow-up Proj. The inverse image of each chart
under $h$ is determined by the degree-zero map obtained from the given
quotient $f^*\mathcal I\twoheadrightarrow\mathcal L$: on a representative
$x/f_i^n$ it is the coefficient of the corresponding quotient fraction in
$\mathcal O_Y$. The constructed lift uses exactly the same degreewise maps,
by definition of $\alpha_f$ and the tensor-power identification, so $h$ and
$\widetilde f$ agree on each inverse-image chart. These equalities are
compatible on chart overlaps because both maps send a localized fraction to
its further localization; the localization cocycle gives literal equality.
The standard charts cover the target, hence their inverse images cover $Y$,
and equality of morphisms on this cover implies $h=\widetilde f$.
