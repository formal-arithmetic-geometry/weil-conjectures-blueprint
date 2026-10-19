+++
id = "def-weil-algebraic-closure"
kind = "definition"
title = "Algebraic closure of a field"
lean = ["IsAlgClosed", "IsAlgClosure", "AlgebraicClosure"]
tags = ["mathlib", "stacks-09GS"]
+++
Let $K$ be a field. A field $\Omega$ is *algebraically closed* if every nonconstant polynomial in $\Omega[X ]$ has a root in $\Omega$. An *algebraic closure* of $K$ is an algebraically closed field $\overline K$ together with a field homomorphism $\iota:K\to\overline K$ such that $\overline K$ is algebraic over $K$ (every element of $\overline K$ is a root of a nonzero polynomial with coefficients in $\iota(K)$). Every field has an algebraic closure, and any two algebraic closures of $K$ are isomorphic over $K$; 'a fixed algebraic closure' means one chosen once and for all.
