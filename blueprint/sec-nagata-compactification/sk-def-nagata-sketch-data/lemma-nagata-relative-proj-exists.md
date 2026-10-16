+++
id = "lemma-nagata-relative-proj-exists"
kind = "lemma"
title = "Existence and affine compatibility of relative Proj"
lean = ["AlgebraicGeometry.Scheme.GradedAlgebraData.existsUnique_relProjIso", "AlgebraicGeometry.Scheme.GradedAlgebraData.isColimitRestrict", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProj\u03b9_relProjHom", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjHom_preimage", "AlgebraicGeometry.Scheme.GradedAlgebraData.isPullback_relProj\u03b9", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjFunctor_map_relProj\u03b9", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjRestrictIso", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjRestrictIso_hom_naturality"]
order = 21
uses = ["def-nagata-affine-proj", "def-nagata-relative-proj", "lemma-nagata-proj-chart-ring-cocycle"]
+++
The relative Proj construction in
[def-nagata-relative-proj] exists as a scheme, is independent up to a
unique isomorphism compatible with the chosen affine-chart
identifications, and restricts over every affine open $V\subseteq X$ to
$\operatorname{Proj}(\Gamma(V,\mathcal A))$. These restriction
isomorphisms commute with further restriction and with the structural maps.
