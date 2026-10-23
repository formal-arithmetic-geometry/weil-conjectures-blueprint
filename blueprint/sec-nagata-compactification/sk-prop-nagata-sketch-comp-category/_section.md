+++
id = "sk-prop-nagata-sketch-comp-category"
kind = "proposition"
title = "Common dense refinements"
order = 130
uses = ["sk-def-nagata-sketch-data", "sk-thm-nagata-compactification"]
lean = ["AlgebraicGeometry.Compactification.exists_isDense_isStrict_refinement", "AlgebraicGeometry.Compactification.refinement_morphisms", "AlgebraicGeometry.Compactification.DenseCategory.isCofiltered_and_isThin"]
tags = ["sketch"]
+++
For a quasi-compact morphism $f:X\to S$, any finite nonempty family of
compactifications has a common dense strict refinement
([sk-def-nagata-sketch-data]). Morphisms out of a dense compactification
restricting to the identity on $X$ are unique, proper, and automatically
strict, i.e. $h^{-1}(X)=X$. For the morphism $f$ of
[sk-thm-nagata-compactification] ($S$ qcqs, $f$ separated of finite type) the
category of dense compactifications with strict refinements is therefore
cofiltered, and it is thin.
