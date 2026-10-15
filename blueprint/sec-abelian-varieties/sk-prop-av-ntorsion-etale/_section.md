+++
id = "sk-prop-av-ntorsion-etale"
kind = "corollary"
title = "Jacobian torsion and geometric extension"
lean = ["AlgebraicGeometry.etale_torsionSubgroupScheme"]
order = 428
uses = ["sk-def-av", "sk-def-av-mult-n", "sk-prop-av-connected-order", "sk-prop-av-divisible", "sk-prop-av-divisible-structure", "sk-prop-av-finite-etale-points", "sk-prop-av-isogeny", "sk-thm-picard-main", "sk-cor-picard-degree"]
tags = ["sketch"]
+++
Let $k$ be algebraically closed, let $C/k$ be a smooth proper connected
curve of genus $g$, and let $n>0$ be invertible in $k$. Then

$$
J(C)[n](k)\simeq(\Z/n\Z)^{2g}.
$$

This isomorphism is not canonical. For every algebraically closed
extension $K/k$, the natural map

$$
J(C)[n](k)\longrightarrow J(C_K)[n](K)
$$

is a canonical isomorphism. Multiplication by $n$ on $J(C)(k)$ is
surjective, and consequently

$$
\operatorname{Pic}(C)[n]=J(C)[n](k),
\qquad
\operatorname{Pic}(C)/n\operatorname{Pic}(C)\xrightarrow[\ \deg\ ]{\sim}\Z/n\Z.
$$

*Complement* (the same proof, for any abelian variety). Let $A$ be an
abelian variety of dimension $g$ over a field $k$ and let $n\ge1$ be
prime to $\operatorname{char}k$. Then $A[n]$ is a finite étale group
scheme over $k$. If moreover $k$ is algebraically closed, the canonical
base change map $A[n](k)\to A[n](k')$ is a bijection for every extension
$k\subseteq k'$ of algebraically closed fields, and
$A[n](k)=A(k)[n]\cong(\Z/n\Z)^{2g}$.
