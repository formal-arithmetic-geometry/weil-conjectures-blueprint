+++
id = "lem-sc-tsen"
kind = "lemma"
title = "Tsen's theorem"
lean = ["RatFunc.isQuasiAlgClosed", "IsQuasiAlgClosed.of_trdeg_le_one", "IsQuasiAlgClosed.of_isAlgebraic", "AlgebraicGeometry.IsCurve.isQuasiAlgClosed_functionField", "AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup_functionField"]
order = 1358
uses = ["def-sc-cr-field", "def-sc-curves", "def-sc-function-field", "lem-sc-c1-brauer-trivial", "lem-sc-c1-finite-extension"]
+++
Let $k$ be an algebraically closed field. Then the rational function
field $k(t)$ is a $C_1$ field in the sense of [def-sc-cr-field], and
more generally every field $K\supseteq k$ of transcendence degree at
most one over $k$ is $C_1$: every homogeneous form of degree $d$ in
$N>d$ variables over $K$ has a nontrivial zero. In particular, for an
integral curve $C$ over $k$ ([def-sc-curves]) the function field $k(C)$
([def-sc-function-field]) is $C_1$, and consequently

$$
\operatorname{Br}(k(C))=H^2(\operatorname{Spec}k(C)_{\Et},\mathbf G_m)=0 .
$$
