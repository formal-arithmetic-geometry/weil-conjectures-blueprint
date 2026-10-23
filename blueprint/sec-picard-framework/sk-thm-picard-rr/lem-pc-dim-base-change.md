+++
id = "lem-pc-dim-base-change"
kind = "lemma"
title = "Dimension is unchanged under base change along field extensions"
lean = ["ringKrullDim_tensorProduct_of_finiteType", "AlgebraicGeometry.topologicalKrullDim_pullback_eq_of_field"]
order = 731
uses = ["def-pc-curve", "def-pc-dimension", "def-pc-field-tower", "def-pc-morphism-conventions"]
+++
Let $k$ be a field, $A$ a $k$-algebra of finite type and $K/k$ a field
extension. Then $\dim(A\otimes_kK)=\dim A$; hence for a
curve $X$ over $k$, the scheme
$X_K=X\times_{\operatorname{Spec} k}\operatorname{Spec} K$ has dimension $1$.
