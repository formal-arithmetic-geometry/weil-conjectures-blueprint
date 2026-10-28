+++
id = "lem-sc-normalization-exists"
kind = "lemma"
title = "Existence and finiteness of the normalization"
lean = ["AlgebraicGeometry.Scheme.surjective_fromNormalization", "AlgebraicGeometry.Scheme.isFinite_fromNormalization_of_locallyOfFiniteType", "AlgebraicGeometry.Scheme.exists_isIso_fromNormalization_restrict", "AlgebraicGeometry.Scheme.topologicalKrullDim_normalization"]
order = 1448
uses = ["def-sc-normalization"]
+++
Let $X$ be an integral scheme of finite type over a field $k$
and $\nu:X^{\nu}\to X$ its normalization in $k(X)$
([def-sc-normalization]). Then $\nu$ is finite, surjective
and birational; if $X$ is proper then $X^{\nu}$ is proper; and
$\dim X^{\nu}=\dim X$.
