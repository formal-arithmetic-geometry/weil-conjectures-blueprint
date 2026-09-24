+++
id = "cor-zl-zeta-from-weights"
kind = "theorem"
title = "Root bound"
order = 4343
tags = ["latex:corollary"]
uses = ["cor-zl-purity-smooth-proper", "def-weil-algebraically-closed-coefficients", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-reciprocal-roots", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "prop-weil-operations", "prop-weil-reciprocal-roots-eigenvalues"]
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
constant-sheaf setting fixed here. Then every
reciprocal
root $\alpha\in\Qlb$ of $P_{i,\ell}$ satisfies

$$
|\iota(\alpha)|=q^{i/2}.
$$

## Proof

Step 1: the hypotheses are in place. The purity and mixedness
assumptions of the statement are retained verbatim; they are the
conclusions of [cor-zl-purity-smooth-proper], and item (4) of
[prop-weil-operations] identifies $H_c^i$ with $H^i$ in the proper
setting.

Step 2: the root bound. By [prop-weil-reciprocal-roots-eigenvalues],
the reciprocal roots of $P_{i,\ell}$ are exactly the eigenvalues of
$F_{i,\ell}$ after scalar extension to $\Qlb$, counted with algebraic
multiplicity; and by [def-weil-frobenius-module-weights],
$\iota$-purity of weight $i$ of $(H^i(X,\Qlb),F_i)$ says precisely
that every such eigenvalue $\alpha$ satisfies
$|\iota(\alpha)|=q^{i/2}$. This is the asserted bound.
