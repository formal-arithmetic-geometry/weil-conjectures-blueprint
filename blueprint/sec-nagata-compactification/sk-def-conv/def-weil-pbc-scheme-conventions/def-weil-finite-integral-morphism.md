+++
id = "def-weil-finite-integral-morphism"
kind = "definition"
title = "Finite and integral morphisms of schemes"
uses = ["def-pc-scheme", "pqf-def-affine-morphism", "def-weil-affine-spectrum"]
refines = "def-weil-pbc-scheme-conventions"
lean = ["AlgebraicGeometry.IsFinite, AlgebraicGeometry.IsIntegralHom"]
tags = ["sheaf-dag", "mathlib", "stacks-01WH"]
+++
Let $f:X\to Y$ be a morphism of schemes [def-pc-scheme]. The morphism $f$ is *integral* if it is affine [pqf-def-affine-morphism] and for every affine open $V=\operatorname{Spec}R\subseteq Y$ [def-weil-affine-spectrum], with (affine) inverse image $f^{-1}(V)=\operatorname{Spec}A$, the ring map $R\to A$ is integral (every element of $A$ satisfies a monic polynomial with coefficients in the image of $R$). It is *finite* if it is affine and for every such $V$ the ring map $R\to A$ is finite ($A$ is a finitely generated $R$-module). Since a quasi-coherent module $\widetilde M$ on $\operatorname{Spec}R$ is of finite type exactly when $M$ is a finite $R$-module (Stacks Lemma 01PB), $f$ is finite exactly when it is affine and $f_*\mathcal O_X$ is a finite (finite type, quasi-coherent) $\mathcal O_Y$-algebra; in the same sense, $f$ is integral when it is affine and $f_*\mathcal O_X$ is integral over $\mathcal O_Y$ on every affine open.
