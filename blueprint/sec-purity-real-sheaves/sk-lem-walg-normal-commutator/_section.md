+++
id = "sk-lem-walg-normal-commutator"
kind = "lemma"
title = "The monodromy groups and their commutators"
lean = ["Matrix.GeneralLinearGroup.instIsHopfIdealVanishingIdeal", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromy_le_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.normal_zeroLocus_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.commutator_zeroLocus_le_zeroLocus_geometricMonodromy", "AlgebraicGeometry.IsMonHom.ContainsCommutators", "AlgebraicGeometry.IsMonHom.Normal.of_containsCommutators", "AlgebraicGeometry.GeneralLinearGroup.containsCommutators_subgroupSchemeHom", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.containsCommutators_subgroupSchemeHom_arithmeticMonodromy_le_geometricMonodromy", "AlgebraicGeometry.GeneralLinearGroup.derivedIdeal", "AlgebraicGeometry.GeneralLinearGroup.containsCommutators_iff_le_derivedIdeal", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.geometricMonodromy_le_derivedIdeal_arithmeticMonodromy"]
order = 4050
uses = ["sk-d-real-weil", "sk-i-restriction", "sk-i-cartier", "sk-p-geometry", "sec-algebraic-groups-lie-algebras"]
tags = ["sketch"]
+++
Let $\rho:W(U_0)\to\GL(V)$ be a Weil representation, as in
[sk-i-restriction]. Its *geometric* and *arithmetic monodromy groups* are
the Zariski closures $H$ of $\rho(\pi_1(U))$ and $G$ of $\rho(W(U_0))$ in
$\GL(V)$. We keep the letters $H$ and $G$ for these two groups.

The groups $H$ and $G$ are reduced closed algebraic subgroups of $\GL(V)$,
and $H\trianglelefteq G$. Moreover every commutator of two elements of $G$
lies in $H$.

*Complement.* For a rational action, invariance under a Zariski-dense
subgroup is equivalent to invariance under its closure: the stabilizer
equations are closed. Invariant subspaces and quotients carry induced
rational actions; direct sums, tensor products, exterior powers and
determinants of rational actions are rational. For a representation
$\rho\colon W\to\GL_n(k)$ of a group $W=P\rtimes\langle s\rangle$ over a
field $k$ put $H=\overline{\rho(P)}$, $G=\overline{\rho(W)}$ (Zariski
closures in $\GL_n$) and $F=\rho(s)$. These are closed subgroup schemes of
$\GL_n$ with $H\subseteq G$; for every $k$-algebra $R$, $H(R)$ is normal in
$G(R)$, and $aba^{-1}b^{-1}\in H(R)$ for $a,b\in G(R)$. Thus $H$ contains
the commutators of $G$ as group schemes; equivalently, $H$ contains the
derived subgroup $[G,G]$, the smallest closed subgroup scheme of $G$
containing the commutators of $G$. More generally, if $H\subseteq G$ are
closed subgroup schemes of $\GL_n$ such that the commutators of $G(R)$ lie
in $H(R)$ for every $k$-algebra $R$, then $H$ contains the commutators of
$G$ as group schemes, hence is normal in $G$.
