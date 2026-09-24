+++
id = "lemma-nagata-blowup-universal-exists"
kind = "lemma"
title = "The constructed lift lies over $X$"
order = 353
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-universal-lift", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-invertible-ideal", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-blowup-universal-graded-map", "lemma-nagata-blowup-universal-unique", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-glue-data-valid", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
Under the data of [def-nagata-blowup-universal-lift], the constructed
map $\widetilde f$ is an $X$-morphism: its composite with
$b_{X,\mathcal I}$ is $f$.

## Proof

On each standard chart, the degree-zero component of
[lemma-nagata-blowup-universal-graded-map] is the canonical map to
$\mathcal O_Y$, hence the composite with the blow-up structure map is $f$.
The chart maps agree on overlaps by functoriality of localization, and the
glued equality is therefore the specified equality over $X$.
