+++
id = "lem-pc-closed-immersion-coherent-cohomology"
kind = "lemma"
title = "Coherent modules under a closed immersion"
lean = ["AlgebraicGeometry.Scheme.Modules.exists_H_addEquiv_pushforward_of_isAffineHom", "AlgebraicGeometry.Scheme.Modules.nonempty_cohomologyFunctor_iso_pushforward_of_isAffineHom", "AlgebraicGeometry.Scheme.Modules.isIso_projectionHom", "AlgebraicGeometry.Scheme.Modules.nonempty_pushforward_tensorObj_pullback_iso", "AlgebraicGeometry.Scheme.Modules.isQuasicoherent_pushforward_of_isClosedImmersion", "AlgebraicGeometry.Scheme.Modules.isFinitePresentation_pushforward_of_isClosedImmersion"]
order = 612
uses = ["def-pc-morphism-conventions", "def-sc-invertible-module", "lem-pc-affine-morphism-hi", "pqf-def-coherent", "pqf-def-cohomology", "pqf-lem-coherent-ft-locnoeth", "pqf-lem-leray"]
+++
Let $i:X\hookrightarrow Y$ be a
closed immersion of locally
Noetherian schemes, and let $\mathcal F$ be a
coherent module on $X$.
Then $i_*\mathcal F$ is coherent, and
$H^q(Y,i_*\mathcal F)\cong H^q(X,\mathcal F)$ for every $q$.
For an invertible module
$\mathcal L$ on $Y$, the natural map
$i_*\mathcal F\otimes\mathcal L\to i_*(\mathcal F\otimes i^*\mathcal L)$ is an isomorphism.
