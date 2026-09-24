+++
id = "lemma-nagata-blowup-universal-unique"
kind = "lemma"
title = "Uniqueness of the universal lift"
order = 352
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.hom_ext_of_isInvertible_comap"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-universal-lift", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-affine-restriction-map", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-invertible-ideal", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-blowup-universal-graded-map", "lemma-nagata-chart-extended-ideal-principal", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-proj-chart-ring-cocycle", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-relative-proj-invertible-tensor-powers", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
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
