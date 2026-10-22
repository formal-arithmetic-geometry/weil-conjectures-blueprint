+++
id = "def-sc-kahler-differentials"
kind = "definition"
title = "Kähler differentials and the canonical sheaf of a smooth curve"
lean = ["AlgebraicGeometry.Scheme.Hom.relativeDifferentials", "AlgebraicGeometry.Scheme.Hom.relativeDifferentialsRestrictFromSpecIso"]
order = 640
uses = ["def-sc-curves"]
+++
Let $C$ be a smooth curve over $k$.
The *sheaf of Kähler differentials* $\Omega^1_{C/k}$ of $C$ over $k$
is the sheafification of the presheaf
$V\mapsto\Omega^1_{\mathcal O_C(V)/k}$ of Kähler differentials, with
the universal derivation $d:\mathcal O_C\to\Omega^1_{C/k}$ induced by
the universal derivations of the $k$-algebras $\mathcal O_C(V)$. On an
affine open $U=\operatorname{Spec}A\subseteq C$, $\Omega^1_{C/k}|_U$ is
the sheaf associated with the $A$-module $\Omega^1_{A/k}$ of Kähler
differentials of the $k$-algebra $A$. (Equivalently,
$\Omega^1_{C/k}=\Delta^*(\mathcal I/\mathcal I^2)$, where
$\Delta:C\to C\times_kC$ is the diagonal immersion and
$\mathcal I\subseteq\mathcal O_{C\times_kC}$ the ideal sheaf of the
diagonal.)
The *canonical sheaf* of $C$ is

$$
\omega_C:=\Omega^1_{C/k}.
$$
