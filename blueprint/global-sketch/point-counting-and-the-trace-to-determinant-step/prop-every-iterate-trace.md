+++
id = "prop-every-iterate-trace"
kind = "theorem"
title = "Every-iterate Grothendieck–Lefschetz identity"
order = 104
tags = ["latex:proposition"]
uses = ["def-global-geometric-frobenius", "def-local-frobenius-trace", "def-point-count-zeta", "def-smooth-proper-cohomological-family", "def-smooth-proper-datum", "def-weil-finite-coefficient-datum", "prop-cohomological-finiteness"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and let
$\Lambda\in\{E,\Qlb\}$. Let $Y_0/\Fq$ be separated and of finite
type, let $Y$ be its geometric fiber, and let
$K\in D^b_c(Y,\Lambda)$ be equipped with
$\theta_K:Lg_Y^*K\xrightarrow{\sim}K$. For every $n\geq1$,

$$
\sum_{x\in Y_0(\mathbf F_{q^n})}
\Tr(F_x^{(n)}\mid K_{\bar x})
=\sum_{i\in\mathbf Z}(-1)^i
\Tr\bigl(F^n\mid H_c^i(Y,K)\bigr).
$$

Both sums are finite. For the constant degree-zero object
$\Lambda_Y[0]$ with
its canonical Frobenius isomorphism, each local
alternating trace is $1$, so

$$
N_n(Y_0)=\sum_{i\in\mathbf Z}(-1)^i
\Tr\bigl(F^n\mid H_c^i(Y,\Lambda)\bigr).
$$

If $Y_0$ is proper, compactly supported cohomology may be replaced by
ordinary cohomology. In particular, if
$\mathscr X=(X_0,d,X)$ is a smooth-proper datum and
$\ell\neq p$ is prime, and $V_{i,\ell},F_{i,\ell}$ are its cohomological family,
then

$$
N_n(X_0)=\sum_{i=0}^{2d}(-1)^i
\Tr(F_{i,\ell}^n\mid V_{i,\ell}).
$$
