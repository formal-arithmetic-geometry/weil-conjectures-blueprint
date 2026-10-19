+++
id = "def-nagata-two-open-boundary-loci"
kind = "definition"
title = "The four boundary loci"
order = 273
lean = ["AlgebraicGeometry.TwoOpenSide.forbiddenBoundary", "AlgebraicGeometry.TwoOpenSide.selfBoundary"]
uses = ["def-nagata-two-open-graph-extensions"]
+++
For $\{i,j\}=\{1,2\}$, define the closed subsets

$$
Z_i=U\setminus U_j\subseteq U_i,
\qquad
Z_{i,k}=\psi_i^{-1}(Z_k)\subseteq V_i
\quad(k=1,2).
$$

The *forbidden boundary* of the $i$-th side is the closure
$\overline Z_{i,j}$ of $Z_{i,j}=\psi_i^{-1}(U\setminus U_i)$ in $X_i$, and
its *self boundary* is the closure $\overline Z_{i,i}$ of
$Z_{i,i}=\psi_i^{-1}(U\setminus U_j)$ in $X_i$.
