+++
id = "cor-zl-hasse-bound"
kind = "theorem"
title = "Hasse–Weil bound"
order = 2915
tags = ["latex:corollary"]
uses = ["cor-trf-point-counting", "def-sc-curves", "def-sc-genus", "def-weil-algebraically-closed-coefficients", "def-weil-derived-complete-integral-detailed", "def-weil-finite-field-fiber", "def-weil-frobenius-coefficient-twists", "def-weil-geometric-hypotheses", "def-weil-rationalization-karoubi", "prop-cohomological-finiteness", "prop-endpoints", "prop-weight-purity-roots", "thm-sc-proper-cohomology"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, choose a prime $\ell\neq p$, fix an
isomorphism $\iota:\Qlb\xrightarrow{\sim}\mathbf C$, and let
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
