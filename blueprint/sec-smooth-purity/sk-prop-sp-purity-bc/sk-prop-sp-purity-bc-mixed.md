+++
id = "det-sp-mixed-base-change"
kind = "lemma"
title = "Base change commutes with change of finite coefficients"
uses = ["det-sp-reduction-direct-image", "det-sp-reduction-exceptional"]
+++
In a Cartesian square $f\circ u=v\circ f'$ as in the sketch, with $f$ smooth of
pure relative dimension $d$, let $A\to B$ be a map of finite commutative rings
killed by a power of $\ell$. Let $b^f,c^f_{A,B}$ (and $b^{f'},c^{f'}_{A,B}$) be the
coefficient comparisons of [det-sp-reduction-direct-image] and
[det-sp-reduction-exceptional], $\beta_{f,A}(M):v_A^*Rf_{!,A}M\xrightarrow{\sim}R(f')_{!,A}u_A^*M$
compact-support base change, and $e_{f,A}(K):u_A^*f_A^!K\xrightarrow{\sim}(f')_A^!v_A^*K$
exceptional base change (the transpose of
$v_A^*(\varepsilon_{f,A}(K))\circ\beta_{f,A}(f^!_AK)^{-1}$). Then for
$M\in\Dctf(X_{\mathrm{proét}},A)$ and $K\in\Dctf(Y_{\mathrm{proét}},A)$:

$$
\beta_{f,B}(M_B)\circ v_B^*(b^f(M))
=b^{f'}(u_A^*M)\circ\bigl(\beta_{f,A}(M)\bigr)_B
\quad\text{in }\Dctf(Y'_{\mathrm{proét}},B),
$$

$$
c^{f'}_{A,B}(v_A^*K)\circ(e_{f,A}(K))_B
=e_{f,B}(K_B)\circ u_B^*c^f_{A,B}(K)
\quad\text{in }\Dctf(X'_{\mathrm{proét}},B),
$$

the sources and targets being identified by the evident commutations of
pullback with extension of scalars.
