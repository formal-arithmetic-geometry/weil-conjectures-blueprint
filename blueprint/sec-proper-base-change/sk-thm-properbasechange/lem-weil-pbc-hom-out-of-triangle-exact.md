+++
id = "lem-weil-pbc-hom-out-of-triangle-exact"
kind = "lemma"
title = "Hom(-,W) applied to a distinguished triangle: exactness at Y and at Z"
uses = ["def-weil-triangulated-category"]
lean = ["CategoryTheory.Pretriangulated.Triangle.yoneda_exact₂"]
tags = ["sheaf-dag", "mathlib", "stacks-0149"]
+++
Let $\mathcal T$ be a pre-triangulated category [def-weil-triangulated-category], $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{d}X[1 ]$ a distinguished triangle and $W$ an object of $\mathcal T$. (i) If $a:Y\to W$ satisfies $a\circ u=0$, there is $b:Z\to W$ with $a=b\circ v$ (exactness of $\Hom(Z,W)\to\Hom(Y,W)\to\Hom(X,W)$). (ii) If $c:Z\to W$ satisfies $c\circ v=0$, there is $k:X[1 ]\to W$ with $c=k\circ d$ (exactness of $\Hom(X[1 ],W)\to\Hom(Z,W)\to\Hom(Y,W)$).
