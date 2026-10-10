+++
id = "lem-weil-pbc-curve-constructible-reduction"
kind = "lemma"
title = "Reduction to constructible prime torsion"
order = 1153
uses = ["def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-sheaves", "lemma-weil-pbc-curve-filtered-cohomology", "lemma-weil-pbc-eight-curve-devissage", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $C$ be a proper curve over an algebraically closed field $k$ (separated
of finite type, $\dim C\leq1$), and suppose that for every prime $r$ and every
constructible sheaf $G$ of $\mathbf F_r$-modules on the reduction
$C_{\mathrm{red}}$, assertion $\mathcal C_7(C_{\mathrm{red}},G)$ of
[def-weil-pbc-eight-curve-assertions] holds. Then $\mathcal C_7(C,F)$ holds for
every torsion sheaf $F$ on $C_{\Et}$: for every algebraically closed
extension $k'/k$ and every $q$, the pullback map
$H^q(C,F)\to H^q(C_{k'},F_{k'})$ is an isomorphism.

## Proof

Let $C$ be a proper finite-type curve and $F$ a torsion sheaf. The reduction
$C_{\mathrm{red}}\hookrightarrow C$ is a universal homeomorphism, so by
invariance of the etale site under universal homeomorphisms we may replace $C$
by its reduction. The sheaf $F$ is the filtered colimit of its constructible
torsion subsheaves (the constructible approximation on a quasi-compact
quasi-separated scheme), so [lemma-weil-pbc-curve-filtered-cohomology] and the
naturality of the maps $\rho^q_{k'/k}$ reduce $\mathcal C_7(C,F)$ to its
instances for constructible $F$; the finite primary decomposition and the
exact sequences $0\to F[r]\to F\to F/F[r]\to0$ (iterated over the prime factors
of the torsion orders) reduce constructible $F$ to the instances with $\mathbf
F_r$-coefficients, since by [lemma-weil-pbc-eight-curve-devissage] (the five
lemma on the two long exact cohomology sequences, linked by the pullback maps)
$\mathcal C_7$ passes from the outer terms of a short exact sequence to the
middle term. The reduction step is compatible with the field extension,
because $(C_{\mathrm{red}})_{k'}\to C_{k'}$ is again a universal
homeomorphism.
