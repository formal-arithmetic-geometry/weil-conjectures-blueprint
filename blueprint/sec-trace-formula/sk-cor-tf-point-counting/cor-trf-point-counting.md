+++
id = "cor-trf-point-counting"
kind = "theorem"
title = "Point-counting trace formula"
lean = ["AlgebraicGeometry.WeilSheaf.pointCount_eq_finsum_trace_compactlySupportedCohomology", "AlgebraicGeometry.WeilSheaf.pointCount_eq_finsum_trace_cohomology"]
order = 3867
tags = ["latex:corollary"]
uses = ["cor-trf-constant-stalk-trace", "def-weil-finite-field-fiber", "def-weil-ordinary-compact-cohomology", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "det-thm-tf-uniform-formula-weil"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, let $X_0$ be a
separated finite-type
$k_0$-scheme, put $X=X_0\times_{k_0}k$, and let
$K=(\Qlb)_X$ be the constant
Weil sheaf with its canonical
Weil structure $g_X^*\Qlb_X\cong\Qlb_X$ of [def-weil-weil-sheaf-complex], the
geometric Frobenius acting trivially on stalks. Then for every
$m\geq1$,

$$
\#X_0(\mathbf F_{q^m})
=
\sum_{i\in\mathbf Z}(-1)^i
\operatorname{Tr}\bigl(F^m\mid H_c^i(X,\Qlb)\bigr),
$$

and, when $X_0$ is
proper,

$$
\#X_0(\mathbf F_{q^m})
=
\sum_{i\in\mathbf Z}(-1)^i
\operatorname{Tr}\bigl(F^m\mid H^i(X,\Qlb)\bigr),
$$

compactly supported cohomology being the ordinary one. The same holds with
$\Qlb$ replaced by any finite $E/\Ql$.
