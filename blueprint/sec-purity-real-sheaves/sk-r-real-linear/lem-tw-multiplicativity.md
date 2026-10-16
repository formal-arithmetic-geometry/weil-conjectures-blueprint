+++
id = "lem-tw-multiplicativity"
kind = "lemma"
title = "Weights multiply under tensor product"
lean = ["AlgebraicGeometry.WeilGroup.IsOfWeight.mul", "AlgebraicGeometry.WeilGroup.IsOfWeight.inv"]
order = 2942
uses = ["def-tw-eigenvalue"]
+++
If $\alpha,\beta$ are eigenvalues of weights $w_1,w_2$ (as in
[def-tw-eigenvalue]), then $\alpha\beta$ has weight
$w_1+w_2$, and $\alpha^{-1}$ has weight $-w_1$ when
$\alpha\neq0$.
