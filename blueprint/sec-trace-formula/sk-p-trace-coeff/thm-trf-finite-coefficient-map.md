+++
id = "thm-trf-finite-coefficient-map"
kind = "theorem"
title = "Compatibility with a finite coefficient map"
order = 2383
uses = ["def-exchange-projection", "def-trf-coefficient-conventions", "def-trf-frobenius-operators", "def-weil-derived-tensor", "def-weil-finite-field-fiber", "prop-trf-trace-formal-laws"]
+++
Fix the global finite-field datum
and the coefficient
conventions, and let $\rho:A\to B$ be a homomorphism of finite
commutative rings annihilated by integers invertible in $k$. Derived
scalar extension $-\otimes_A^LB:D(X,A)\to D(X,B)$ preserves bounded
constructibility and finite Tor amplitude, there are natural
isomorphisms

$$
(Rf_!K)\otimes_A^LB\xrightarrow{\ \sim\ }Rf_!\bigl(K\otimes_A^LB\bigr),
\qquad
(Lf^*L)\otimes_A^LB\xrightarrow{\ \sim\ }Lf^*\bigl(L\otimes_A^LB\bigr)
$$

for $f:X\to Y$ separated finite type and admissible, and the
scalar-extension law of the
categorical trace identifies

$$
\rho\bigl(\operatorname{tr}_A(v\mid P)\bigr)
=\operatorname{tr}_B\bigl(v\otimes_A^LB\mid P\otimes_A^LB\bigr).
$$

Consequently the finite-ring trace formula over $A$ maps to the
finite-ring trace formula over $B$; in particular, for a strict Weil
complex $(K_A,\varphi_A)$, its scalar extension $(K_B,\varphi_B)$
has $R\Gamma_c(X,K_A)\otimes_A^LB\simeq R\Gamma_c(X,K_B)$ and
$(K_A)_{\bar y}\otimes_A^LB\simeq(K_B)_{\bar y}$ with matching
Frobenius operators, and

$$
\rho\bigl(\operatorname{tr}_A(F_{y,m}\mid K_{A,\bar y})\bigr)
=\operatorname{tr}_B\bigl(F_{y,m}\mid K_{B,\bar y}\bigr).
$$
