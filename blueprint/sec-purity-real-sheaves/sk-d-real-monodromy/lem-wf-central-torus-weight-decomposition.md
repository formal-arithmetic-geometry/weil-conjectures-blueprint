+++
id = "lem-wf-central-torus-weight-decomposition"
kind = "lemma"
title = "Weight decomposition for a central torus"
order = 2845
uses = ["def-wf-algebraic-character", "def-wf-algebraic-representations", "def-wf-algebraic-torus"]
+++
Let $T\subseteq Z(H)$ be a central torus and let $M$ be an
algebraic $H$-module. Then

$$
M=\bigoplus_{\lambda\in X^*(T)}M_\lambda,
M_\lambda=\{v:tv=\lambda(t)v\text{ for all }t\in T\},
$$

only finitely many summands are nonzero, and every $M_\lambda$ is
$H$-stable.

## Proof

After identifying $T$ with $\mathbf G_m^d$ as in
[def-wf-algebraic-torus], the algebraic action in
[def-wf-algebraic-representations] makes every matrix coefficient
of the regular map $T\to\operatorname{GL}(M)$ a Laurent polynomial in
$t_1,\ldots,t_d$. Write the action on a basis vector as a finite sum
$t v=\sum_{\mathbf n}t_1^{n_1}\cdots t_d^{n_d}v_{\mathbf n}$.
The equality $(tt')v=t(t'v)$, and linear independence of distinct
Laurent monomials, imply
$t v_{\mathbf n}=t_1^{n_1}\cdots t_d^{n_d}v_{\mathbf n}$.
Thus the finitely many vectors $v_{\mathbf n}$ give the displayed
direct-sum decomposition into the character spaces of
[def-wf-algebraic-character]. If $h\in H$, $v\in M_\lambda$,
and $t\in T$, centrality gives
$t(hv)=h(tv)=\lambda(t)hv$; hence every weight space is $H$-stable.
