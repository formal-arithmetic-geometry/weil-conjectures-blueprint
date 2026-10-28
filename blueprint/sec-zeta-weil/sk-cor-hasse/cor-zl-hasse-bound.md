+++
id = "cor-zl-hasse-bound"
kind = "theorem"
title = "Hasse–Weil bound"
lean = ["AlgebraicGeometry.Scheme.Hom.abs_pointCount_sub_le_two_mul_genus"]
order = 4401
tags = ["latex:corollary"]
uses = ["cor-trf-point-counting", "def-sc-curves", "def-sc-genus", "def-weil-finite-field-fiber", "def-weil-frobenius-coefficient-twists", "def-weil-geometric-hypotheses", "det-def-sfb-pulled-back-coefficients", "sk-prop-scalar-six", "prop-cohomological-finiteness", "prop-endpoints", "prop-weight-purity-roots"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, choose a prime $\ell\neq p$, fix a
field embedding $\iota:\Qlb\hookrightarrow\mathbf C$, and let
$C_0/k_0$ be a smooth, proper,
geometrically connected scheme of pure dimension $1$. Put
$C=C_0\times_{k_0}k$, and let

$$
g=g(C)=\dim_kH^1(C,\mathcal O_C)
$$

be the genus of the
smooth proper connected curve $C$ over the
algebraically closed field $k$. Then, for every integer $n\geq1$,

$$
\boxed{
\left|\#C_0(\mathbf F_{q^n})-(q^n+1)\right|\leq2g\,q^{n/2}}.
$$
