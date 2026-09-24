+++
id = "cor-zl-functional-equation-sign"
kind = "theorem"
title = "The normalized sign of the functional equation"
order = 4353
tags = ["latex:corollary"]
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-smooth-proper-cohomological-family", "def-weil-weil-sheaf-complex", "lem-weil-alternating-form-dimension", "lem-zl-poincare-duality-roots", "prop-poincare-pairing"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, and a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$,
and interpret the $\Qlb$-objects in the
algebraically closed
coefficient category. Let $X_0/k_0$ be
smooth, proper, geometrically
connected of pure dimension $d\in\mathbf Z_{\geq0}$, put
$X=X_0\times_{k_0}k$, let $(\Qlb)_X$ be the constant
Weil sheaf, and let $F$ be the
global geometric Frobenius
in the geometric-Frobenius convention.
Let $(V_{i,\ell},F_{i,\ell},P_{i,\ell})_{0\leq i\leq2d}$ be the
smooth-proper
cohomological family extended to $\Qlb$, and put

$$
b_i=\dim_{\Qlb}H^i(X,\Qlb),\qquad
\chi=\sum_{i=0}^{2d}(-1)^ib_i,\qquad
D_i=\det\bigl(F\mid H^i(X,\Qlb)\bigr),
$$

$$
\Delta_\ell=\prod_{i=0}^{2d}D_i^{(-1)^i},\qquad
\varepsilon=(-1)^\chi q^{-d\chi/2}\Delta_\ell .
$$

Assume, for every $0\leq i\leq2d$, the duality identities

$$
b_{2d-i}=b_i,\qquad D_iD_{2d-i}=q^{db_i},
$$

which are item (d) of [lem-zl-poincare-duality-roots] (the duality
root reciprocity of the preceding lemma, whose input is the Poincare
duality of the zeta chapter). Then the normalized sign satisfies

$$
\varepsilon^2=1,
$$

hence $\varepsilon\in\{1,-1\}$.

## Proof

By [lem-zl-poincare-duality-roots],
item (d), $b_i=b_{2d-i}$ and $D_iD_{2d-i}=q^{db_i}$; multiplying the
second identities over the pairs $\{i,2d-i\}$, $i<d$, and using the
middle degree $i=d$ separately,

$$
\Delta_\ell^2=q^{d\chi}.
$$

Moreover $d\chi$ is even: when $d$ is even this is immediate, and
when $d$ is odd, pairing the degrees $i$ and $2d-i$ for $i<d$
gives $\chi\equiv b_d\pmod2$, while the middle pairing is
$(-1)^d$-symmetric, hence alternating for odd $d$, by
[prop-poincare-pairing]; trivializing the value line
$\Qlb(-d)$ (an invertible rank-one coefficient space) turns the
restriction of the pairing to $H^d(X,\Qlb)$ into a nondegenerate
alternating $\Qlb$-valued form, so [lem-weil-alternating-form-dimension]
gives that $b_d$ is even, and therefore $d\chi$ is even. Hence
$h:=d\chi/2\in\mathbf Z$, and with $\varepsilon=(-1)^\chi q^{-h}\Delta_\ell$
one has $\varepsilon^2=q^{-2h}\Delta_\ell^2=q^{-d\chi}q^{d\chi}=1$, so
$\varepsilon\in\{1,-1\}$.
