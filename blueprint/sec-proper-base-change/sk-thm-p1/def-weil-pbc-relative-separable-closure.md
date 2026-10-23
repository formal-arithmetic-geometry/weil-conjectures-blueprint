+++
id = "def-weil-pbc-relative-separable-closure"
kind = "definition"
title = "Separable algebraic closure of a field inside an extension"
uses = ["def-pc-separably-closed"]
lean = ["separableClosure", "separableClosure.isSepClosure"]
order = 1657
tags = ["mathlib", "stacks-09HC"]
+++
Let $F\to E$ be a homomorphism of fields, making $E$ an extension of $F$. The *separable algebraic closure of $F$ in $E$* is the set of elements of $E$ that are separable algebraic over $F$ (roots of a separable polynomial with coefficients in $F$); it is a subfield of $E$ containing the image of $F$, and it is algebraic and separable over $F$. If $E$ is separably closed [def-pc-separably-closed] (for instance algebraically closed), then the separable algebraic closure of $F$ in $E$ is separably closed, hence a separable closure of $F$ (a separably closed field, separable algebraic over $F$).
