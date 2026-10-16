+++
id = "lem-pc-projective-coherent-higher-images"
kind = "lemma"
title = "Coherent higher direct images of a projective morphism"
lean = ["AlgebraicGeometry.Scheme.Modules.isFinitePresentation_higherDirectImage_of_isClosedImmersion", "AlgebraicGeometry.Scheme.Modules.isZero_higherDirectImage_of_isClosedImmersion"]
order = 663
uses = ["def-pc-derived-direct-image", "def-pc-projective-morphism", "def-pc-projective-space-twist", "lem-pc-cech-computes", "lem-pc-projective-coherent-finiteness", "pqf-def-coherent", "pqf-lem-coherent-ft-locnoeth"]
+++
Let $S$ be locally Noetherian, let $f:X\to S$ be
projective, and let
$\mathcal F$ be a coherent module.
Then each higher direct image
$R^qf_*\mathcal F$ is coherent.
For an embedding $X\hookrightarrow\mathbf P^n_S$, it is zero for $q>n$.
