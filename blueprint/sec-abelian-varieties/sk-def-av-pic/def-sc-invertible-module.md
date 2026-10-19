+++
id = "def-sc-invertible-module"
kind = "definition"
title = "Invertible modules and their duals"
lean = ["SheafOfModules.IsInvertible", "AlgebraicGeometry.Scheme.Modules.IsInvertible", "AlgebraicGeometry.Scheme.Modules.dual"]
order = 452
+++
Let $X$ be a scheme (for instance a curve $C$ as in [def-sc-curves],
in which case one speaks of invertible $\mathcal O_C$-modules). An
*invertible $\mathcal O_X$-module* is an
$\mathcal O_X$-module $\mathcal L$ which is locally free of rank
one for the Zariski topology: every point has an open neighbourhood $U$
with $\mathcal L|_U\cong\mathcal O_U$. Its
*dual* is

$$
\mathcal L^{\vee}:=\mathcal{H}om_{\mathcal O_X}(\mathcal L,\mathcal O_X).
$$
