+++
id = "proposition-dense-compactifications-form-cofiltered-category"
kind = "proposition"
title = "Dense compactifications form a cofiltered category"
order = 1419
lean = ["AlgebraicGeometry.Compactification.exists_isDense_isStrict_refinement", "AlgebraicGeometry.Compactification.refinement_morphisms", "AlgebraicGeometry.Compactification.DenseCategory.isCofiltered_and_isThin"]
uses = ["definition-compactification-refinement"]
+++
Let $S$ be quasi-compact and quasi-separated, and let $f:X\to S$ be separated
and of finite type. Any finite family of dense compactifications of $f$ has a
common dense refinement. Morphisms between dense compactifications that
restrict to the identity on $X$ are unique, proper, and automatically satisfy
$h^{-1}(X)=X$. The category of dense compactifications of $f$ is therefore
cofiltered.
