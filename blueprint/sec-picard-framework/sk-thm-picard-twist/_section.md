+++
id = "sk-thm-picard-twist"
kind = "theorem"
title = "The twist lemma"
order = 754
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-thm-picard-serre-a"]
lean = ["AlgebraicGeometry.Scheme.exists_isInvertible_twist"]
tags = ["sketch"]
+++
Let $k$ be separably closed, $X$ a connected smooth proper curve over $k$,
$K/k$ a field extension and $\cL$ a line bundle on $X_K$. Then
there exists a line bundle $\cL_0$ on $X$ such that

$$
h^0\bigl(X_K,\cL\otimes\cL_0|_{X_K}\bigr)=1\qquad\text{and}\qquad
h^1\bigl(X_K,\cL\otimes\cL_0|_{X_K}\bigr)=0 .
$$
