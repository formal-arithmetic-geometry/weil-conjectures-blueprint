+++
id = "lem-pc-twist"
kind = "lemma"
title = "The twist lemma"
order = 848
uses = ["def-pc-curve", "def-pc-degree-line-bundle", "def-pc-derived-category", "def-pc-genus", "def-pc-rational-point", "def-pc-separably-closed", "def-pc-smooth-projective-curve", "def-pc-zero-scheme", "def-sc-ample", "def-nagata-invertible-ideal", "lem-pc-ample-positive-degree", "lem-pc-closed-imm-base-change", "lem-pc-degree-base-change", "lem-pc-dim-base-change", "lem-pc-euler-additive", "lem-pc-flat-base-change-cohom", "lem-pc-serre-vanishing", "lem-pc-vanishing-above-dim", "lem-pc-very-ample-ample", "lem-sc-point-cartier", "prop-pc-xk-integral", "thm-picard-serre-a"]
lean = ["AlgebraicGeometry.Scheme.exists_isInvertible_twist"]
+++
Let $k$ be a separably closed field,
let $X$ be a connected smooth proper curve of genus $g$ over $k$, let $K/k$ be
a field extension and let $\mathcal{L}$ be an invertible sheaf on $X_K$. Then
there exists an invertible sheaf $\mathcal{L}_0$ on $X$ such that

$$
\dim_KH^0\bigl(X_K,\;\mathcal{L}\otimes\mathcal{L}_0|_{X_K}\bigr)=1
\qquad\text{and}\qquad
\dim_KH^1\bigl(X_K,\;\mathcal{L}\otimes\mathcal{L}_0|_{X_K}\bigr)=0 .
$$
