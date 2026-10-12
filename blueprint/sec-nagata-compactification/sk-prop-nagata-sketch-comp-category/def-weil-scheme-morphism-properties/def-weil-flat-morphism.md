+++
id = "def-weil-flat-morphism"
kind = "definition"
title = "Flat morphism of schemes"
uses = ["def-pc-scheme"]
refines = "def-weil-scheme-morphism-properties"
lean = ["AlgebraicGeometry.Flat"]
tags = ["sheaf-dag", "mathlib", "stacks-01U3"]
+++
Let $f:X\to S$ be a morphism of schemes [def-pc-scheme]. For $x\in X$, $f$ induces a local homomorphism of local rings $\mathcal O_{S,f(x)}\to\mathcal O_{X,x}$. The morphism $f$ is *flat at $x$* if $\mathcal O_{X,x}$ is a flat $\mathcal O_{S,f(x)}$-module, and *flat* if it is flat at every point of $X$.
