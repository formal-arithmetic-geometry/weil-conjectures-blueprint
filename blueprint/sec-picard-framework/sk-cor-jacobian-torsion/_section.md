+++
id = "sk-cor-jacobian-torsion"
kind = "corollary"
title = "Jacobian torsion and geometric extension"
order = 613
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
