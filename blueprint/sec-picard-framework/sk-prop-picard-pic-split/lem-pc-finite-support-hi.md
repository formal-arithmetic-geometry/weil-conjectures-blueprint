+++
id = "lem-pc-finite-support-hi"
kind = "lemma"
title = "Finite support of higher direct images"
lean = ["AlgebraicGeometry.Scheme.Modules.isQuasicoherent_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.exists_isZero_higherDirectImage_of_isPullback"]
order = 655
uses = ["def-pc-morphism-conventions", "def-pc-scheme", "pqf-lem-affine-vanishing", "lem-pc-cech-computes"]
+++
Let $f:X\to S$ be a quasi-compact, quasi-separated morphism of schemes.
For every quasi-coherent $\mathcal{O}_X$-module $\mathcal{F}$:

1. the $R^if_*\mathcal{F}$ are quasi-coherent;
1. if $S$ is quasi-compact, there is an integer $n=n(X,S,f)$ such
that $R^pf_*\mathcal{F}=0$ for all $p\ge n$ and all quasi-coherent $\mathcal{F}$; the
same integer works for every base change
$S'\to S$ (i.e. $R^p(f')_*\mathcal{F}'=0$ for $p\ge n$ and quasi-coherent
$\mathcal{F}'$ on $X'=S'\times_SX$).
