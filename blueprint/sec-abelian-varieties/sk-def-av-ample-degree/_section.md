+++
id = "sk-def-av-ample-degree"
kind = "definition"
title = "Ample modules and the Hilbert degree"
lean = ["AlgebraicGeometry.IsAmple", "AlgebraicGeometry.Scheme.Hom.degree"]
order = 435
tags = ["sketch"]
+++
Let $X$ be a scheme over a field $k$. An $\cO_X$-module $\cM$ is
*very ample* if it is the pullback of $\cO(1)$ along a closed immersion
$X\hookrightarrow\mathbf P^N_k$ over $k$, and *ample* if
$\cM^{\otimes m}$ is very ample for some $m\ge1$. Let $g$ be the Krull
dimension of $X$ ($g=0$ if $X$ is empty or infinite-dimensional). The
*degree of $X$ with respect to $\cM$* is the $g$-th forward difference
at $0$ of the Hilbert function $m\mapsto \chi(X,\cM^{\otimes m})$:

$$
\deg_{\cM}(X):=\sum_{i=0}^{g}(-1)^{g-i}\binom gi\,
\chi(X,\cM^{\otimes i}).
$$

For $X$ proper and $\cM$ ample invertible the Hilbert function is a
numerical polynomial of degree at most $g$ (the Hilbert polynomial), and
$\deg_{\cM}(X)$ is $g!$ times its coefficient of $m^g$.
