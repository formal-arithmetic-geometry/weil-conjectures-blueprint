+++
id = "lem-weil-pbc-curve-constructible-reduction"
kind = "lemma"
title = "Reduction to constructible prime torsion"
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_forall_isReduced"]
order = 1340
uses = ["def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-sheaves", "lemma-weil-pbc-curve-filtered-cohomology", "lemma-weil-pbc-eight-curve-devissage", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $k$ be an algebraically closed field. Suppose that for every reduced
proper curve $X$ over $k$ (separated of finite type, $\dim X\leq1$), every
prime $r$ and every constructible sheaf $G$ of $\mathbf F_r$-modules on
$X_{\Et}$, assertion $\mathcal C_7(X,G)$ of
[def-weil-pbc-eight-curve-assertions] holds. Then $\mathcal C_7(C,F)$ holds
for every proper curve $C$ over $k$ and every torsion sheaf $F$ on $C_{\Et}$:
for every algebraically closed extension $k'/k$ and every $q$, the pullback
map $H^q(C,F)\to H^q(C_{k'},F_{k'})$ is an isomorphism.
