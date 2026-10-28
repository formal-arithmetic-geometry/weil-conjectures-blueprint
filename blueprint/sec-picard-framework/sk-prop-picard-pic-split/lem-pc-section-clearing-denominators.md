+++
id = "lem-pc-section-clearing-denominators"
kind = "lemma"
title = "Clearing denominators for a section of an invertible module"
lean = ["AlgebraicGeometry.Scheme.Modules.exists_tensorPowSection_eq_restrict"]
order = 632
uses = ["def-pc-morphism-conventions", "def-pc-zero-scheme", "def-sc-invertible-module", "pqf-def-coherent"]
+++
Let $X$ be a quasi-compact scheme
separated over an affine scheme,
let $\mathcal L$ be an
invertible module, and let
$s\in\Gamma(X,\mathcal L)$. Put
$X_s=X\setminus Z(s)$, the complement of its
zero scheme.
For every quasi-coherent module
$\mathcal F$ and $t\in\Gamma(X_s,\mathcal F)$, there exist $m\ge0$
and $u\in\Gamma(X,\mathcal F\otimes\mathcal L^{\otimes m})$ such that
$u|_{X_s}=t\otimes s^m$.
