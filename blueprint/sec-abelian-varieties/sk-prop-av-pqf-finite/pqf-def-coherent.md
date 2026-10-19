+++
id = "pqf-def-coherent"
kind = "definition"
title = "Coherent and quasi-coherent modules"
lean = ["AlgebraicGeometry.Scheme.Modules.IsFiniteTypeWithFiniteTypeKernels", "SheafOfModules.IsQuasicoherent", "SheafOfModules.IsFiniteType"]
order = 532
+++
Let $X$ be a scheme and $\mathcal F$ an $\mathcal O_X$-module.

1. $\mathcal F$ is *quasi-coherent* if every point of $X$ has an
affine neighbourhood $\operatorname{Spec}A=U$ with
$\mathcal F|_U=\widetilde M$ for some $A$-module $M$.
1. $\mathcal F$ is *of finite type* if every point has a
neighbourhood $U$ with a surjection
$\mathcal O_U^{\oplus n}\twoheadrightarrow\mathcal F|_U$.
1. $\mathcal F$ is *coherent* if it is of finite type and for
every open $U$ and every map
$\mathcal O_U^{\oplus n}\to\mathcal F|_U$ the kernel is of finite
type.
