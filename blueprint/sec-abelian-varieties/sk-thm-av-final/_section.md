+++
id = "sk-thm-av-final"
kind = "proposition"
title = "Multiplication on an abelian variety"
lean = ["AlgebraicGeometry.abelianVariety_estimate"]
order = 427
uses = ["sk-def-av", "sk-def-av-isogeny", "sk-def-av-mult-n", "sk-def-av-tate", "sk-prop-av-connected-order", "sk-prop-av-divisible", "sk-prop-av-divisible-structure", "sk-prop-av-prime-p-etale", "sk-prop-av-tate-rank", "sk-prop-av-isogeny"]
tags = ["sketch"]
+++
Let $B/k$ be an abelian variety of dimension $g$, and let $n>0$ be
invertible in $k$. Multiplication $[n]:B\to B$ is a finite étale
surjection of degree $n^{2g}$. In particular $B[n]=\ker[n]$ is a finite
étale group scheme of rank $n^{2g}$.

*Complements* (proved in this sketch, and used by the curve estimates).
Let $A$ be an abelian variety of dimension $g$ over a field $k$, let
$p=\operatorname{char}k$ and let $n\ge1$.

- **(a)** $[n]:A\to A$ is a finite flat surjective homomorphism, hence
an isogeny of degree $n^{2g}$; $A[n]=\ker[n]$ is a finite flat group
scheme over $k$ of order $n^{2g}$.
- **(b)** If $p>0$, then $A[p^e]$ is finite flat of order $p^{2ge}$ for
every $e\ge1$. If $n$ is prime to $p$ (in particular if $p=0$), then
$A[n]$ is finite étale of rank $n^{2g}$.
- **(c)** Let $k$ be algebraically closed and $n$ prime to $p$. Then
$A[n](k)\cong(\Z/n\Z)^{2g}$, and for every extension
$k\subseteq k'$ of algebraically closed fields the canonical map
$A[n](k)\to A[n](k')$ is an isomorphism.
- **(d)** Let $k$ be algebraically closed. Then $A(k)$ is a divisible
abelian group, $A(k)[n]\cong(\Z/n\Z)^{2g}$ for every $n$ prime to $p$,
and for every prime $\ell\ne p$
$$
T_\ell A\cong\Z_\ell^{2g},\qquad V_\ell A\cong\Q_\ell^{2g}.
$$
