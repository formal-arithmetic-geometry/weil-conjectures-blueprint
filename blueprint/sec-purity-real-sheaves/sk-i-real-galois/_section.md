+++
id = "sk-i-real-galois"
kind = "proposition"
title = "Galois correspondence for finite local systems"
order = 2924
uses = ["sk-d-real-setup"]
lean = ["AlgebraicGeometry.Scheme.exists_equivalence_isFiniteLocallyConstantSheaf", "Rep.IsFiniteContinuous"]
tags = ["sketch"]
+++
Let $Y$ be a connected scheme with geometric point $\bar y$ and let
$\Lambda$ be a finite ring. Write $\mathrm{F\acute Et}(Y)$ for the category
of finite etale covers of $Y$, $F_{\bar y}$ for the fiber functor sending a
cover to its finite fiber at $\bar y$, and
$\pi_1(Y,\bar y)=\operatorname{Aut}(F_{\bar y})$ with its profinite topology.
A sheaf of finite $\Lambda$-modules on $Y_\Et$ is locally constant if it
becomes constant on an etale covering.

The geometric-stalk functor is an exact tensor equivalence between locally
constant sheaves of finite $\Lambda$-modules on $Y_\Et$ and finite
$\Lambda$-modules carrying a continuous action of $\pi_1(Y,\bar y)$
(every stabilizer open); the underlying $\Lambda$-module of the
representation attached to a sheaf is its stalk at $\bar y$.
