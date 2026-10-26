+++
id = "thm-pd-spreading-out"
kind = "theorem"
title = "Descent of finitely presented data at a filtered limit"
lean = ["AlgebraicGeometry.Scheme.exists_isPullback_of_finitePresentation", "AlgebraicGeometry.Scheme.exists_pullback_hom_of_isLimit", "AlgebraicGeometry.Scheme.exists_pullback_fst_comp_eq_of_isLimit"]
order = 856
uses = ["def-pc-base-change", "def-pc-morphism-conventions"]
+++
Let $(S_i)_{i\in I}$ be a cofiltered inverse system of schemes (for instance
indexed by a directed set $I$) with affine transition morphisms
$f_{i'i}\colon S_{i'}\to S_i$ and $S_i$ quasi-compact and quasi-separated, and
let $S=\varprojlim_iS_i$. Then:

1. for every morphism of finite presentation $V\to S$ there are $i\in I$ and
a morphism of finite presentation $V_i\to S_i$ with
$V\cong V_i\times_{S_i}S$ over $S$;
1. given $i$, schemes $V_i,W_i$ of finite presentation over $S_i$ and a
morphism $\psi:V_i\times_{S_i}S\to W_i$ over $S_i$, there are $i'\to i$
and a morphism $\psi_{i'}:V_i\times_{S_i}S_{i'}\to W_i$ over $S_i$
whose composite with the canonical map
$V_i\times_{S_i}S\to V_i\times_{S_i}S_{i'}$ is $\psi$;
1. given $i$, schemes $V_i,W_i$ of finite presentation over $S_i$ and two
morphisms $\psi_i,\chi_i:V_i\to W_i$ over $S_i$ whose composites with the
projection $V_i\times_{S_i}S\to V_i$ agree, there is $i'\to i$ such that
their composites with the projection $V_i\times_{S_i}S_{i'}\to V_i$ agree.

By the universal property of $W_i\times_{S_i}S$, (2) and (3) say equivalently
that $S$-morphisms $V_i\times_{S_i}S\to W_i\times_{S_i}S$ descend to
$S_{i'}$-morphisms $V_i\times_{S_i}S_{i'}\to W_i\times_{S_i}S_{i'}$, and that
two $S_i$-morphisms $V_i\to W_i$ whose base changes to $S$ agree have equal
base changes to some $S_{i'}$.
