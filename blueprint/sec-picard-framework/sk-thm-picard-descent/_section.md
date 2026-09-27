+++
id = "sk-thm-picard-descent"
kind = "section"
title = "Descent"
order = 762
uses = ["sk-def-av-pic"]
lean = ["AlgebraicGeometry.isStack_fpqc_quasicoherent", "AlgebraicGeometry.isSheaf_fpqc_finiteLocallyFreeSubscheme"]
+++
*Theorem (sketch).*

Let $\{T_i\to T\}_{i\in I}$ be an fpqc covering.

1. ****(D1)**** *Descending modules.* Descent data for
quasi-coherent $\cO$-modules on the covering are effectively
represented by quasi-coherent $\cO_T$-modules; the equivalence
preserves flatness, finite presentability and local freeness. In
particular: *descent of invertible modules* — cartesian
isomorphisms $\cL_i$'s satisfying the cocycle condition glue to an
invertible $\cL$ on $X_T$ with $\cL|_{X_{T_i}}\cong\cL_i$.
1. ****(D2)**** *Effective closed immersions.* Closed
subschemes $Z_i\subseteq X_{T_i}$, finite flat of degree $d$ over
$T_i$, with cocycle-compatible cartesian identifications, glue to a
closed subscheme $Z\subseteq X_T$, finite flat of degree $d$ over
$T$, with $Z\times_TT_i\cong Z_i$.

## Proof

(D1): the fpqc sheaf sequence for $\cO$ and the functor
$\cM\mapsto\ker(\prod f_{i,*}\cM\rightrightarrows\cdots)$; flatness
and local freeness are fpqc-local. (D2): the ideals
$\cI_{Z_i}$ form a descent datum for quotient modules of $\cO_X$ by
(D1).
