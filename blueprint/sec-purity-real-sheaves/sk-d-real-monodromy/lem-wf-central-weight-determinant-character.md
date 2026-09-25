+++
id = "lem-wf-central-weight-determinant-character"
kind = "lemma"
title = "A determinant character detected by a central weight"
order = 2802
uses = ["def-wf-algebraic-character", "def-wf-algebraic-representations", "def-wf-algebraic-torus", "lem-wf-central-torus-weight-decomposition"]
+++
Let $H\subseteq\operatorname{GL}(V)$ be connected, let
$T=Z(H)^\circ\ne1$ be a torus, and let $\zeta\in \operatorname{GL}(V)$ normalize $H$. If conjugation by
$\zeta^m$ is the identity on $T$, then there is a non-trivial
algebraic character $\chi:H\to\mathbf G_m$ such that

$$
\chi(\zeta^m h\zeta^{-m})=\chi(h)\qquad(h\in H).
$$

## Proof

Use the weight-space decomposition

$$
V=\bigoplus_{\lambda\in\Lambda}V_\lambda
$$

of [lem-wf-central-torus-weight-decomposition]. At least one
weight $\lambda$ is non-trivial: otherwise every element of $T$
would act as the identity on the faithful space $V$, forcing
$T=1$. Fix such a $\lambda$ and put $U=V_\lambda$.

The space $U$ is $H$-stable. Indeed, for $h\in H$, $t\in T$
and $u\in U$, centrality of $T$ gives

$$
t(hu)=h(tu)=\lambda(t)hu.
$$

It is also $\zeta^m$-stable: the calculation in
[lem-wf-central-torus-weight-decomposition] gives
$\zeta^mV_\lambda=V_{\lambda\circ \operatorname{Int}(\zeta^{-m})}=V_\lambda$.
Consequently

$$
\chi(h):=\det(h|_U)
$$

is an algebraic character in the sense of
[def-wf-algebraic-character], and restriction of conjugate
operators to the $\zeta^m$-stable space $U$ gives

$$
\chi(\zeta^mh\zeta^{-m})
=\det(\zeta^m|_U)\det(h|_U)\det(\zeta^{-m}|_U)=\chi(h).
$$

Finally $t|_U=\lambda(t)\operatorname{id}_U$, so
$\chi|_T=\lambda^{\dim U}$. Since
$X^*(T)\cong\mathbf Z^{\dim T}$ is torsion-free by
[def-wf-algebraic-torus], a positive power of the non-trivial
character $\lambda$ is still non-trivial. Thus $\chi\ne1$.
