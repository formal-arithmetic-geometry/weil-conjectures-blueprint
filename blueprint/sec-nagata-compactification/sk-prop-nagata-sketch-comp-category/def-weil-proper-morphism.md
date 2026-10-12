+++
id = "def-weil-proper-morphism"
kind = "definition"
title = "Separated, universally closed and proper morphisms"
uses = ["def-pc-base-change", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.IsProper"]
tags = ["sheaf-dag", "mathlib", "stacks-01W1"]
+++
Let $f:X\to S$ be a morphism of schemes. $f$ is *separated* if its diagonal $\Delta_f:X\to X\times_SX$ (the morphism to the fibre product [def-pc-base-change] with both components the identity) is a closed immersion, i.e. identifies $X$ with a closed subscheme of $X\times_SX$. $f$ is *universally closed* if for every morphism $S'\to S$ the base change $X\times_SS'\to S'$ is a closed map of the underlying topological spaces. $f$ is *proper* if it is separated, of finite type [def-weil-finite-type-morphism], and universally closed. A scheme over a field $K$ is *proper over $K$* if its structure morphism to $\operatorname{Spec}K$ is proper.
