+++
id = "pqf-def-coherent"
kind = "definition"
title = "Coherent and quasi-coherent modules"
order = 3205
lean = ["AlgebraicGeometry.IsQuasicoherent", "AlgebraicGeometry.IsFiniteType", "AlgebraicGeometry.IsCoherent"]
+++
Let $X$ be a scheme and $\mathcal F$ an $\mathcal O_X$-module.

1. $\mathcal F$ is *quasi-coherent* if every point of $X$ has an affine
   neighbourhood $\operatorname{Spec}A=U$ with
   $\mathcal F|_U=\widetilde M$ for some $A$-module $M$.
2. $\mathcal F$ is *of finite type* if every point has a neighbourhood $U$
   with a surjection
   $\mathcal O_U^{\oplus n}\twoheadrightarrow\mathcal F|_U$.
3. $\mathcal F$ is *coherent* if it is of finite type and for every open
   $U$ and every map $\mathcal O_U^{\oplus n}\to\mathcal F|_U$ the kernel
   is of finite type.

*Recorded classical input.* The notion of quasi-coherent, finite-type and
coherent $\mathcal O_X$-modules is recorded with the standard citation, as
in the reference decomposition of Stacks Section 30.21, and is not
decomposed in this blueprint: Stacks Project, Cohomology of Sheaves,
Chapter 20, [Tag 01DW](https://stacks.math.columbia.edu/tag/01DW).
