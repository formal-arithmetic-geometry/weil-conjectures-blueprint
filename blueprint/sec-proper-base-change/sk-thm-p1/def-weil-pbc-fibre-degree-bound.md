+++
id = "def-weil-pbc-fibre-degree-bound"
kind = "definition"
title = "Integers bounding the degrees of the fibres; universally bounded fibres (Stacks 03J4)"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.Hom.HasUniversallyBoundedFibers", "AlgebraicGeometry.Scheme.Hom.BoundsFiberDegrees"]
order = 1751
+++
Let $f:X\to Y$ be a morphism of schemes [def-pc-scheme]. For $y\in Y$ let $\kappa(y)$ be the residue field and $X_y=X\times_Y\operatorname{Spec}\kappa(y)$ the fibre of $f$ at $y$, a scheme over $\kappa(y)$ through its second projection. A scheme $T$ over a field $k$, with structure morphism $t:T\to\operatorname{Spec}k$, is *finite over $k$* if $t$ is finite. For such $T$, $\Gamma(T,\mathcal O_T)$ is a $k$-algebra through the ring map $k=\Gamma(\operatorname{Spec}k,\mathcal O)\to\Gamma(T,\mathcal O_T)$ induced by $t$, of finite dimension as a $k$-vector space, and the *degree* of $T$ over $k$ is the integer $\dim_k\Gamma(T,\mathcal O_T)\ge0$. (1) An integer $n\ge0$ *bounds the degrees of the fibres of $f$* if for every $y\in Y$ the fibre $X_y$ is finite over $\kappa(y)$ and its degree satisfies $\dim_{\kappa(y)}\Gamma(X_y,\mathcal O_{X_y})\le n$. (2) The *fibres of $f$ are universally bounded* if there is an integer $n\ge0$ which bounds the degrees of the fibres of $f$.
