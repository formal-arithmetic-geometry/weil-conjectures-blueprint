+++
id = "cor-pc-dense-points-curves-sections"
kind = "theorem"
title = "Consequences of the density of rational points"
order = 760
tags = ["latex:corollary"]
uses = ["def-pc-curve", "def-pc-separably-closed", "def-pc-smooth-projective-curve", "def-sc-invertible-module"]
lean = ["AlgebraicGeometry.Scheme.Hom.denseRange_baseChangeFieldPoint", "AlgebraicGeometry.Scheme.Hom.exists_baseChangeFieldPoint_notMem_support_zeroLocus", "AlgebraicGeometry.Scheme.Hom.exists_fieldPoints_notMem_support_zeroLocus", "AlgebraicGeometry.Scheme.Hom.infinite_fieldPoints"]
+++
Let $k$ be a separably closed field and let $X$ be a scheme over $k$
which is smooth over $k$.

1. For every field extension $K/k$ put $X_K=X\times_{\operatorname{Spec}k}\operatorname{Spec}K$, and for
$x\in X(k)$ let $x_K=\operatorname{Spec}(K)\times_kx$ be the induced $K$-rational point of
$X_K$. Then the set $\{x_K : x\in X(k)\}$ is Zariski dense in $X_K$ (for $K=k$
this is the density of $X(k)$ in $X$).
1. Let $\mathcal{L}$ be an invertible $\mathcal{O}_{X_K}$-module and
$s\in H^0(X_K,\mathcal{L})$ a section which does not vanish identically, i.e.
$s(y)\neq0$ in $\mathcal{L}(y)=\mathcal{L}_y\otimes\kappa(y)$ for some $y\in X_K$.
Then there is an $x\in X(k)$ such that $s$ does not vanish at $x_K$. More
generally, for a morphism $\varphi:\mathcal M\to\mathcal N$ of invertible
$\mathcal O_{X_K}$-modules whose zero scheme $Z(\varphi)$ (cut out locally by the
coefficient $b$ of $\varphi$ in trivializations, $\varphi(e_{\mathcal M})=b\,e_{\mathcal N}$)
is not all of $X_K$, there is an $x\in X(k)$ with $x_K\notin Z(\varphi)$; a section
$s$ is the case $\varphi=s:\mathcal O_{X_K}\to\mathcal L$.
1. If $X$ is smooth of relative dimension $1$, proper and geometrically integral
over $k$ (for instance a geometrically integral smooth projective curve), then
$X(k)$ is infinite. If $X$ is reduced, then every non-zero morphism
$\varphi:\mathcal M\to\mathcal N$ of invertible $\mathcal{O}_X$-modules, for
instance a non-zero $s\in H^0(X,\mathcal{L})$ for $\mathcal{L}$ invertible, does
not vanish identically, so (2) applies with $K=k$: $\varphi$ does not vanish at
some $x\in X(k)$.
