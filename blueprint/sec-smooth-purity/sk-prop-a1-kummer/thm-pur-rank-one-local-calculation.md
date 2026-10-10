+++
id = "thm-pur-rank-one-local-calculation"
kind = "theorem"
title = "Rank-one local calculation"
order = 1928
uses = ["def-coefficient-twists-detailed", "def-pur-affine-line-datum", "def-pur-conventions", "def-pur-support-cohomology", "def-sbc-smooth-morphisms", "def-sc-curves", "def-sc-mu-trivialization", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "def-weil-scheme-morphism-properties", "lem-sc-primitive-root", "thm-pur-kummer-affine-line", "thm-pur-with-support-exactness", "thm-weil-pbc-site-comparison"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
$A=A_{E,n}$, let $\bar y\to Y$ be a
geometric point of $Y$ with
algebraically closed field $\Omega$, put
$Z=s(\bar y)\subset\mathbf A^1_{\bar y}=\mathbf A^1_k\times_k\Omega$, and
let $A(1)$ be the finite-level twist
$A(1)=\mu_{\ell^N}\otimes_{\mathbf Z/\ell^N}A$ on the
smooth separated curve $\mathbf A^1_{\bar y}$
over $\Omega$. Then there is a canonical isomorphism

$$
H^2_Z\bigl(\mathbf A^1_{\bar y},A(1)\bigr)\xrightarrow{\ \sim\ }A,
$$

under which the boundary of the
Kummer class of the coordinate $t$
corresponds to $1\in A$; equivalently, the boundary map of the
support long exact sequence

$$
\partial:\ H^1\bigl(\mathbf G_{m,\bar y},A(1)\bigr)
\longrightarrow H^2_Z\bigl(\mathbf A^1_{\bar y},A(1)\bigr)
$$

is the *residue* homomorphism and its value on $\kappa(t)$ is
the residue $1$, given by the normalization
$\operatorname{ord}_0(t)=1$ (the order of a unit of the completed
local ring at the origin is the exponent of $t$, so the boundary
of the Kummer class of the coordinate is the class of the orbit
$t\cdot(\mathbf G_m^\wedge)^{(N)}$); all other supported cohomology
groups of $A(1)$ vanish:

$$
H^q_Z(\mathbf A^1_{\bar y},A(1))=0\qquad(q\neq2).
$$

The statements are those of the etale site, transported to the pro-etale
site by [thm-weil-pbc-site-comparison], the coefficients being
finite-torsion. (The identification of the $H^0$-terms and of
$A(1)_{\bar y}\cong A$ uses a primitive $\ell^N$-th root of unity in
$\Omega$, in the sense of [def-sc-mu-trivialization], and
[lem-sc-primitive-root] for its existence.)
