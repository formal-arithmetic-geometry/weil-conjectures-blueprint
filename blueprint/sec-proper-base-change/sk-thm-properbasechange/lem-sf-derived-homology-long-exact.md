+++
id = "lem-sf-derived-homology-long-exact"
kind = "lemma"
title = "Long exact cohomology sequence of a distinguished triangle in the derived category"
order = 1950
uses = ["def-weil-abstract-derived-category", "def-weil-triangulated-category"]
lean = ["DerivedCategory.HomologySequence.δ", "DerivedCategory.HomologySequence.exact₁", "DerivedCategory.HomologySequence.exact₂", "DerivedCategory.HomologySequence.exact₃"]
tags = ["mathlib", "stacks-05RS"]
+++
Let $\mathcal C$ be an abelian category, $D(\mathcal C)$ its derived category [def-weil-abstract-derived-category] and $H^n:D(\mathcal C)\to\mathcal C$ the $n$-th cohomology functor (the cohomology of a representing complex). For every distinguished triangle $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{w}X[1 ]$ there are connecting morphisms $\delta^n:H^n(Z)\to H^{n+1}(X)$ such that the sequence
$$
\cdots\to H^n(X)\xrightarrow{H^n(u)}H^n(Y)\xrightarrow{H^n(v)}H^n(Z)\xrightarrow{\delta^n}H^{n+1}(X)\to\cdots
$$
is exact.
