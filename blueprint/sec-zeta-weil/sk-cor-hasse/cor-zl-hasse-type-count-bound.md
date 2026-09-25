+++
id = "cor-zl-hasse-type-count-bound"
kind = "theorem"
title = "Hasse-type count bound"
order = 3201
tags = ["latex:corollary"]
uses = ["cor-trf-point-counting", "cor-zl-purity-smooth-proper", "cor-zl-zeta-from-weights", "def-weil-algebraically-closed-coefficients", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-reciprocal-roots", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, and a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$,
fix an isomorphism $\iota:\Qlb\xrightarrow{\sim}\mathbf C$, and interpret
the $\Qlb$-objects in the
algebraically closed
coefficient category. Let $X_0/k_0$ be
smooth, proper, geometrically
connected of pure dimension $d\in\mathbf Z_{\geq0}$, put
$X=X_0\times_{k_0}k$, let $F$ be the
global geometric Frobenius
in the geometric-Frobenius convention, and
let $(V_{i,\ell},F_{i,\ell},P_{i,\ell})_{0\leq i\leq2d}$ be the
smooth-proper
cohomological family extended to $\Qlb$. Use the
ordinary/reciprocal-root
convention and the
Frobenius-module weight
notion of the framework chapter. Put $b_i=\dim_{\Qlb}H^i(X,\Qlb)$, and let

$$
N_n:=\#X_0(\mathbf F_{q^n})
$$

in the point-count convention.
Assume that $(H^i(X,\Qlb),F_i)$ is $\iota$-pure of weight $i$ and
that $(H_c^i(X,\Qlb),F)$ is $\iota$-mixed of weights at most $i$, for
every $0\leq i\leq2d$; this is the content of
[cor-zl-purity-smooth-proper] of this chapter in the
constant-sheaf setting fixed here. Then, for every $n\geq1$,

$$
\left|N_n\right|\leq\sum_{i=0}^{2d}b_i\,q^{in/2}.
$$

## Proof

By [cor-trf-point-counting] for the
constant sheaf on the proper $X_0$,

$$
N_n=\sum_{i=0}^{2d}(-1)^i\Tr(F_i^n\mid V_i).
$$

For a fixed $i$, let $\alpha_{i,1},\ldots,\alpha_{i,b_i}$ be the
eigenvalues of $F_i$ with algebraic multiplicity, the multiplicity
being $b_i$ by [def-weil-smooth-proper-cohomological-family]
(the degree of $P_{i,\ell}$ after scalar extension). Then

$$
\iota(N_n)
=\sum_{i=0}^{2d}(-1)^i\sum_{j=1}^{b_i}\iota(\alpha_{i,j})^n,
$$

because $\iota$ is a field isomorphism and hence commutes with traces
of powers. Applying the triangle inequality in $\mathbf C$, and then
the root bound of [cor-zl-zeta-from-weights] degree by degree,

$$
|\iota(N_n)|
\leq\sum_{i=0}^{2d}\sum_{j=1}^{b_i}|\iota(\alpha_{i,j})|^n
=\sum_{i=0}^{2d}b_i\,q^{in/2}.
$$

The integer $N_n$ is rational, so it is fixed by $\iota$, which
restricts to the identity on $\mathbf Q$; hence $|\iota(N_n)|=|N_n|$.
