+++
id = "def-sc-mu-trivialization"
kind = "definition"
title = "The canonical trivialization of the constant sheaf"
order = 3404
lean = ["AlgebraicGeometry.Etale.rootsOfUnity", "AlgebraicGeometry.Etale.zmodEquivRootsOfUnity"]
uses = ["def-sc-curves"]
+++
Let $k$ be algebraically closed, let $C$ be a curve [def-sc-curves] over
$k$, let $n\geq1$ be prime to $\operatorname{char}k$, and let
$$
 \mu_n(U):=\{x\in\mathcal O_U(U):x^n=1\},\qquad U\to C\text{ etale},
$$
be the etale sheaf of $n$-th roots of unity. Given a root of unity
$\zeta\in\mu_n(k)$, the *canonical trivialization associated to $\zeta$* is
the isomorphism of etale sheaves
$$
 \theta_\zeta:\mathbf Z/n\mathbf Z\xrightarrow{\ \sim\ }\mu_n,
 \qquad a\longmapsto\zeta^a.
$$

Unresolved dependencies: def:weil-pbc-etale-sheaves
