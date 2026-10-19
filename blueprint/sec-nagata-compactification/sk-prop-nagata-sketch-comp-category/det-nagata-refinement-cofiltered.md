+++
id = "det-nagata-refinement-cofiltered"
kind = "corollary"
title = "The category of dense compactifications is cofiltered"
lean = ["AlgebraicGeometry.Compactification.DenseCategory.isCofiltered_and_isThin"]
uses = ["det-nagata-refinement-common-dense", "det-nagata-refinement-morphisms"]
+++
Let $S$ be qcqs and $f:X\to S$ separated of finite type. The category whose
objects are the dense compactifications of $f$ and whose morphisms are the
refinements ([det-nagata-definition-refinement]) is a cofiltered preorder:
it is nonempty, any two objects admit a common refinement, and between any
two objects there is at most one morphism.
