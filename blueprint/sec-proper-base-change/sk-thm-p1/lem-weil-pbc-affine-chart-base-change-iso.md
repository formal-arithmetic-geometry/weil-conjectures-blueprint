+++
id = "lem-weil-pbc-affine-chart-base-change-iso"
kind = "lemma"
title = "Projection-compatible spectrum presentation of a base-changed affine chart"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.exists_affineChart_baseChangeIso"]
order = 1658
+++
Let $z:Z\to S$ and $t:T\to S$ be morphisms of schemes [def-pc-scheme]. Let $W\subset S$, $V\subset Z$ be opens with $V\subset z^{-1}(W)$. Let $R$ be a commutative ring and $A,B$ commutative $R$-algebras. Suppose $e_0:W\cong\operatorname{Spec}R$, $e_B:V\cong\operatorname{Spec}B$ and $e:t^{-1}(W)\cong\operatorname{Spec}A$ are isomorphisms commuting with the maps to $W$ and the specified structure maps to $\operatorname{Spec}R$. Write $p:Z\times_ST\to Z$, $q:Z\times_ST\to T$ for the projections. There is an isomorphism $i:p^{-1}(V)\cong\operatorname{Spec}(A\otimes_R B)$ such that $p\circ\iota\circ i^{-1}=\iota_V\circ e_B^{-1}\circ\operatorname{Spec}(b\mapsto1\otimes b)$ and $q\circ\iota\circ i^{-1}=\iota_{t^{-1}(W)}\circ e^{-1}\circ\operatorname{Spec}(a\mapsto a\otimes1)$, where $\iota$ denotes the open-subscheme inclusion. Zero rings and empty opens are allowed.
