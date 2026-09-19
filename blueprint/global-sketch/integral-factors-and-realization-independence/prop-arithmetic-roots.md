+++
id = "prop-arithmetic-roots"
kind = "theorem"
title = "Arithmetic roots and realization-independent degrees"
order = 113
tags = ["latex:proposition"]
uses = ["def-canonical-cohomological-factors", "def-frobenius-characteristic-factors", "def-ordinary-reciprocal-roots", "def-smooth-proper-cohomological-family", "def-smooth-proper-datum", "def-weil-finite-coefficient-datum", "def-weil-numbers", "prop-integral-recovery", "prop-weight-purity"]
+++
Let $\mathscr X=(X_0,d,X)$ be a smooth-proper datum, let $\Omega$ be an
algebraic closure of $\mathbf Q$, fix $0\leq i\leq2d$, and put
$r_i=\deg P_i$. The polynomial

$$
P_i^\#(U)=U^{r_i}P_i(U^{-1})\in\mathbf Z[U]
$$

is the reciprocal polynomial of $P_i$; it is monic, and its roots in
$\Omega$, with multiplicity, are exactly the
reciprocal roots of $P_i$. Every such root
$\alpha\in\Omega$ is an algebraic integer and, for every
embedding $\tau:\mathbf Q(\alpha)\hookrightarrow\mathbf C$,

$$
|\tau(\alpha)|=q^{i/2}.
$$

Thus $\alpha$ is a $q$-Weil number of weight $i$. For every prime
$\ell\neq p$, choose an algebraic closure $\Qlb$ of $\Ql$ and a
$\mathbf Q$-isomorphism

$$
\jmath:\Omega\xrightarrow{\sim}
\{a\in\Qlb:a\text{ is algebraic over }\mathbf Q\}.
$$

Then $\jmath(\alpha)$ is an
eigenvalue, with its algebraic multiplicity, of geometric Frobenius
$F_{i,\ell}\otimes_{\Ql}1$ on

$$
V_{i,\ell}\otimes_{\Ql}\Qlb\cong H^i(X,\Qlb).
$$

Equivalently, it is a reciprocal root of $P_{i,\ell}$, not an ordinary
root. If $\beta\in\Omega$ is an ordinary root of $P_i$, then
$\alpha:=\beta^{-1}$ is a root of $P_i^\#$, equivalently a reciprocal
root of $P_i$, and

$$
|\tau(\beta)|=q^{-i/2}
$$

for every $\tau:\mathbf Q(\beta)\hookrightarrow\mathbf C$. Finally

$$
r_i=\dim_{\Ql}H^i(X,\Ql)
$$

for every prime $\ell\neq p$.
