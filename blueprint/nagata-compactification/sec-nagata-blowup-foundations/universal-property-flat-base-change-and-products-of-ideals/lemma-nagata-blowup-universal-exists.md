+++
id = "lemma-nagata-blowup-universal-exists"
kind = "lemma"
title = "The constructed lift lies over $X$"
order = 353
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup"]
uses = ["def-nagata-blowup-universal-lift", "def-nagata-global-blowup-cover-comparison", "lemma-nagata-blowup-universal-graded-map", "lemma-nagata-blowup-universal-unique", "lemma-nagata-global-blowup-glue-data-valid", "lemma-nagata-global-blowup-local-maps-agree", "prop-nagata-global-blowup-cover-independent"]
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
