+++
id = "def-weil-affine-spectrum"
kind = "definition"
title = "The spectrum of a commutative ring as a scheme"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Spec"]
tags = ["mathlib", "stacks-00DZ"]
+++
Let $A$ be a commutative ring. The *spectrum* $\operatorname{Spec}A$ is the affine scheme whose underlying topological space is the set of prime ideals of $A$ with the Zariski topology and whose structure sheaf has ring of global sections $A$. A ring homomorphism $\varphi:A\to B$ induces a morphism of schemes $\operatorname{Spec}\varphi:\operatorname{Spec}B\to\operatorname{Spec}A$, contravariantly and functorially in $\varphi$, and every morphism of schemes $\operatorname{Spec}B\to\operatorname{Spec}A$ is $\operatorname{Spec}\varphi$ for exactly one $\varphi$. For a field $K$, $\operatorname{Spec}K$ is a scheme with one point, whose residue field is $K$.
