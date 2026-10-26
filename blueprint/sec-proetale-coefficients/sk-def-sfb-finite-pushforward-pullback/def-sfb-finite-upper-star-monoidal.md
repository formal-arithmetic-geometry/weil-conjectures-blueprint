+++
id = "def-sfb-finite-upper-star-monoidal"
kind = "definition"
title = "Strong monoidal structure on $g^*$"
order = 887
uses = ["def-sfb-finite-lower-star-lax-monoidal", "def-sfb-finite-upper-lower-star-adjunction", "lem-sfb-finite-upper-star-tensor", "lem-sfb-finite-upper-star-unit"]
lean = ["AlgebraicGeometry.ProEtale.oplaxMonoidal_upperStar", "AlgebraicGeometry.ProEtale.isIso_upperStar_η", "AlgebraicGeometry.ProEtale.isIso_upperStar_δ", "AlgebraicGeometry.ProEtale.monoidal_upperStar"]
+++
Let $\mathcal A$ and $g$ be as in [def-sfb-finite-lower-star-lax-monoidal], and assume
moreover that tensoring with a fixed object of $\mathcal A$ commutes with filtered colimits
(for instance $\mathcal A$ closed). The *monoidal structure* on $g^*$ is the oplax monoidal
structure mate, under $g^*\dashv g_*$ ([def-sfb-finite-upper-lower-star-adjunction]), of the
lax structure of [def-sfb-finite-lower-star-lax-monoidal]. Its structure maps
$g^*\mathbf 1\to\mathbf 1$ and $g^*(F\otimes G)\to g^*F\otimes g^*G$ are invertible, so
$g^*$ is a strong monoidal functor. For $\mathcal A$ closed this is
[lem-sfb-finite-upper-star-unit] and [lem-sfb-finite-upper-star-tensor]; their proofs use
closedness only through the commutation of $\otimes$ with filtered colimits, so they apply
verbatim under the present hypothesis.
