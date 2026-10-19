+++
id = "thm-av-final"
kind = "theorem"
title = "Abelian-variety estimate"
lean = ["AlgebraicGeometry.abelianVariety_estimate", "AlgebraicGeometry.abelianVariety_estimate_of_isAlgClosed", "AlgebraicGeometry.IsIsogeny.isFinite", "AlgebraicGeometry.IsIsogeny.flat"]
order = 599
uses = ["def-sc-abelian-variety", "def-sc-isogeny", "def-sc-mult-n", "def-wf-abelian-tate-module", "lem-sc-connected-finite-order", "lem-sc-divisible-group-structure", "lem-sc-fg-order-prime-etale", "lem-sc-finite-flat-surj-points", "lem-sc-finite-nonempty-point", "lem-sc-abelian-variety-characterization", "lem-sc-isogeny-degree"]
+++
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
