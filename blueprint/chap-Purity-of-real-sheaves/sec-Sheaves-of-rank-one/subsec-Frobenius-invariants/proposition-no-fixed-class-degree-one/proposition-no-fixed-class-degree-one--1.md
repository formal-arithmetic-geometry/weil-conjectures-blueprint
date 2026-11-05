+++
id = "proposition-no-fixed-class-degree-one--1"
kind = "proposition"
title = "Frobenius-fixed compatible torsors"
name_showing = false
order = 1097001
aliases = ["bp-r336-1"]
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.exists_section_of_isIsomorphic_mapIso"]
uses = []
+++
Let $U_0/k_0$ be a smooth geometrically connected curve over the finite
field $k_0=\Fq$, let $k$ be an algebraic closure of $k_0$, and put
$U=U_0\times_{k_0}k$. Let $\ell\ne\operatorname{char}k_0$ be prime,
choose a geometric point $\bar u$ of $U$, and write
$G=\pi_1(U,\bar u)$ and $A_n=\mathbf Z/\ell^n$.

For every $n\geq0$, let $\pi_n:T_n\to U$ be a finite étale
$A_n$-torsor, with monodromy character $\rho_n:G\to A_n$. Suppose
that the characters are compatible under reduction:

$$
\rho_{n+1}(g)\bmod\ell^n=\rho_n(g)
\qquad(n\geq0,\ g\in G).
$$

Let $g_U$ be the geometric Galois Frobenius automorphism of $U$.
Suppose also that each $T_n$ is isomorphic, as an $A_n$-torsor, to
its transport along $g_U$: this is the same total space and action,
with structure map $g_U\circ\pi_n$. Then for every $n$ there is a
section $\sigma_n:U\to T_n$ with
$\pi_n\circ\sigma_n=\operatorname{id}_U$. Thus every class in this
compatible system is zero in the torsor description of $H^1(U,A_n)$.
