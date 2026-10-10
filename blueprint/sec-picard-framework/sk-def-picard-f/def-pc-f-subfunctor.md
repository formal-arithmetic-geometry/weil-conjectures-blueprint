+++
id = "def-pc-f-subfunctor"
kind = "definition"
title = "The open subfunctor $F$"
order = 819
uses = ["def-pc-base-change", "def-pc-derived-direct-image", "def-pc-invertible-in-degree-zero", "def-pc-pic-sigma-functor", "def-pc-subfunctor"]
lean = ["AlgebraicGeometry.picardFunctorInvertibleDirectImage"]
+++
Let $k$ be a field, $X$ a scheme over $k$ and $\sigma\in X(k)$. For a
scheme $T$ over $k$, let $F(T)\subseteq\operatorname{Pic}_{X/k,\sigma}(T)$ be the
subset of those $\mathcal{L}$ such that ($f_T:X_T\to T$, $R^qf_{T,*}$ as in
[def-pc-derived-direct-image]) $R^0f_{T,*}\mathcal{L}$ is an invertible
$\mathcal{O}_T$-module and $R^qf_{T,*}\mathcal{L}=0$ for all $q>0$, i.e.
$Rf_{T,*}\mathcal{L}$ is isomorphic in $D(\mathcal{O}_T)$ to an invertible
$\mathcal{O}_T$-module placed in degree $0$.
