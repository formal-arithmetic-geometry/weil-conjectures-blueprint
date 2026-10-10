+++
id = "lem-pc-serre-vanishing"
kind = "lemma"
title = "Serre vanishing"
order = 629
uses = ["def-pc-projective-space-twist", "def-sc-ample", "def-sc-invertible-module", "lem-pc-closed-immersion-coherent-cohomology", "lem-pc-projective-space-serre-vanishing", "pqf-def-coherent"]
lean = ["AlgebraicGeometry.Scheme.Modules.exists_subsingleton_H_tensorObj_tensorPow"]
+++
Let $k$ be a field, let $X$ be a scheme over $k$, let $\mathcal{L}$ be an
ample invertible $\mathcal{O}_X$-module (in the sense of [def-sc-ample]), and let $\mathcal{F}$ be a
coherent $\mathcal{O}_X$-module. Then there exists $n_0\geq0$ such that

$$
H^p(X,\;\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{L}^{\otimes n})=0
\qquad\text{for all }n\ge n_0\text{ and all }p>0 .
$$
