+++
id = "lem-kun-finite-closed-subscheme"
kind = "lemma"
title = "Closed subsets consisting of closed points"
order = 6065
lean = ["AlgebraicGeometry.finite_of_isClosed_of_all_closedPoints"]
uses = ["def-kun-support"]
+++
Let $X$ be a scheme of finite type over a field $K$. A closed subset of $X$
all of whose points are closed [def-kun-support] is a finite set of
points.

## Proof

A scheme of finite type over a field is Noetherian, so a closed subset
$E\subseteq X$ has finitely many irreducible components $E_1,\dots,E_n$.
Write $\eta_j$ for the generic point of $E_j$; by hypothesis $\eta_j$ is a
closed point, so $E_j=\overline{\{\eta_j\}}=\{\eta_j\}$, whence $E$ is a
finite set of points.
