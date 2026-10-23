+++
id = "lem-weil-pbc-linear-equation-localization-polynomial-core"
kind = "lemma"
title = "Core localization polynomial equivalence"
lean = ["MvPolynomial.linearEquationLocalizationPolynomialCore"]
order = 1880
+++
Let $A$ be a commutative ring, $r\ge1$, $f_1,\dots,f_r\in A$ and $1\le i\le r$. Put
$$
B=A[X_1,\dots,X_r]\Big/\Bigl(\textstyle\sum_{j=1}^rf_jX_j-1\Bigr),
$$
let $A_{f_i}=A[1/f_i]$, and let $B_{f_i}$ be the localization of $B$ at the image of $f_i$,
an $A_{f_i}$-algebra via the map induced by $A\to B$. Write $x_j\in B_{f_i}$ for the image of
$X_j$. Then there is an isomorphism of $A_{f_i}$-algebras
$$
\varphi\colon A_{f_i}[Y_j : j\ne i]\xrightarrow{\ \sim\ }B_{f_i}
$$
from the polynomial ring in the $r-1$ variables $Y_j$, $j\ne i$, such that $\varphi$ is the
evaluation homomorphism $Y_j\mapsto x_j$ $(j\ne i)$ and $\varphi^{-1}(x_j)=Y_j$ for every
$j\ne i$.
