+++
id = "lem-weil-pbc-hom-into-triangle-exact"
kind = "lemma"
title = "Hom(W,-) applied to a distinguished triangle: zero composite and exactness at the middle and at X[1]"
uses = ["def-weil-triangulated-category"]
lean = ["CategoryTheory.Pretriangulated.comp_distTriang_mor_zero₁₂", "CategoryTheory.Pretriangulated.Triangle.coyoneda_exact₂", "CategoryTheory.Pretriangulated.Triangle.coyoneda_exact₁"]
order = 1994
tags = ["mathlib", "stacks-0146"]
+++
Let $\mathcal T$ be a pre-triangulated category [def-weil-triangulated-category], $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{d}X[1 ]$ a distinguished triangle and $W$ an object of $\mathcal T$. (i) $v\circ u=0$. (ii) If $a:W\to Y$ satisfies $v\circ a=0$, there is $b:W\to X$ with $a=u\circ b$ (exactness of $\Hom(W,X)\to\Hom(W,Y)\to\Hom(W,Z)$). (iii) If $c:W\to X[1 ]$ satisfies $u[1 ]\circ c=0$, there is $k:W\to Z$ with $c=d\circ k$ (exactness of $\Hom(W,Z)\to\Hom(W,X[1 ])\to\Hom(W,Y[1 ])$).
