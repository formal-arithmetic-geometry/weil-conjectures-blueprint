+++
id = "thm-pur-kummer-affine-line"
kind = "theorem"
title = "Kummer computations on the line and the punctured line"
order = 2934
uses = ["def-sc-curves", "def-sc-kummer-sequence", "def-sc-mu-trivialization", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "lem-pur-affine-punctured-line-algebra", "lem-pur-kummer-coefficient-base-change", "lem-sc-brauer-zero", "lem-sc-cohomological-dimension", "lem-sc-h1-gm-pic", "lem-sc-kummer-exact", "lem-sc-primitive-root"]
+++
Let $k$ be an algebraically closed field, let $N\geq1$ be prime to
$\operatorname{char}k$, and let $A$ be a finite
$\mathbf Z/\ell^N\mathbf Z$-module free of finite rank. On the
small etale site of the
smooth separated curves $\mathbf A^1_k$ and
$\mathbf G_{m,k}$ over $k$, with the twist
$\Lambda(1)=\mu_{\ell^N}\otimes_{\mathbf Z/\ell^N}A$:

1. $H^q(\mathbf A^1_k,\Lambda(1))=0$ for all $q>0$, while
$H^0(\mathbf A^1_k,\Lambda(1))=A$;
1. $H^0(\mathbf G_{m,k},\Lambda(1))=A$, and
$H^q(\mathbf G_{m,k},\Lambda(1))=0$ for all $q\neq0,1$;
1. $H^1(\mathbf G_{m,k},\Lambda(1))\cong A$, a generator of this free
rank-one module being the Kummer class $\kappa(t)$ of the coordinate $t$,
the boundary of the global unit
$t\in\Gamma(\mathbf G_{m,k},\mathbf G_m)$ under the Kummer sequence of
[def-sc-kummer-sequence] with coefficients $A$.

All cohomology groups are finite $A$-modules, and the same statements
hold after base change of the coefficients.
