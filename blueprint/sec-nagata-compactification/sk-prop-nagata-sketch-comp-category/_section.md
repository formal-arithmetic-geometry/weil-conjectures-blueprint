+++
id = "sk-prop-nagata-sketch-comp-category"
kind = "proposition"
title = "Common dense refinements"
order = 6
uses = ["sk-def-nagata-sketch-data", "sk-thm-nagata-compactification"]
lean = ["AlgebraicGeometry.Compactification.category", "AlgebraicGeometry.Compactification.isCofiltered", "AlgebraicGeometry.Compactification.exists_common_refinement", "AlgebraicGeometry.Compactification.baseChange"]
tags = ["sketch"]
+++
For the morphism $f:X\to S$ of [sk-thm-nagata-compactification] ($S$ qcqs,
$f$ separated of finite type), any finite family of dense compactifications
has a common dense refinement ([sk-def-nagata-sketch-data]). Morphisms between
dense compactifications restricting to the identity on $X$ are unique,
proper, and automatically satisfy $h^{-1}(X)=X$. The category of dense
compactifications is therefore cofiltered.
