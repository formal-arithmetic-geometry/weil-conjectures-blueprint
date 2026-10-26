+++
id = "def-sc-mu-trivialization"
kind = "definition"
title = "The canonical trivialization of the constant sheaf"
lean = ["IsPrimitiveRoot.zmodAddEquivRootsOfUnity", "AlgebraicGeometry.Scheme.constantZModToRootsOfUnitySheaf", "AlgebraicGeometry.Scheme.isIso_constantZModToRootsOfUnitySheaf", "AlgebraicGeometry.Scheme.constantZModIsoRootsOfUnitySheaf"]
order = 1394
uses = ["def-sc-curves", "def-weil-pbc-etale-sheaves"]
+++
Let $k$ be a field, let $C$ be a scheme over $k$ (for instance a
curve as in [def-sc-curves]), let $n\geq1$, and let

$$
\mu_n(U):=\{x\in\mathcal O_U(U):x^n=1\},\qquad U\to C\text{ etale},
$$

be the etale sheaf of $n$-th roots of unity ([def-weil-pbc-etale-sheaves]).
Given a primitive $n$-th root of unity $\zeta\in k$ (which exists, for
instance, if $k$ is algebraically closed and $n$ is prime to
$\operatorname{char}k$), the *canonical trivialization associated to
$\zeta$* is the isomorphism of etale sheaves on $C$

$$
\theta_\zeta:\mathbf Z/n\mathbf Z\xrightarrow{\ \sim\ }\mu_n,
\qquad a\longmapsto\zeta^a.
$$
