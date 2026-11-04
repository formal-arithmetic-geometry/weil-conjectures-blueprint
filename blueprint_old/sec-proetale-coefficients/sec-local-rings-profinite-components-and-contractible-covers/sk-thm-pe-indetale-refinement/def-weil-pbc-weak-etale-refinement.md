+++
id = "def-weil-pbc-weak-etale-refinement"
kind = "definition"
title = "An affine refinement of a weakly etale algebra"
order = 958
lean = ["Algebra.WeaklyEtale.refinement", "Algebra.WeaklyEtale.refinementIdeal"]
uses = ["def-weil-pbc-ind-etale-algebra", "def-weil-pbc-retained-localization", "def-weil-pbc-strict-w-cover", "lem-weil-pbc-strict-w-cover"]
+++
For an $A$-algebra $B$ (we use it for $A\to B$ weakly etale
[def-weil-pbc-ind-etale-algebra]), take $C=C_A$ from
[def-weil-pbc-strict-w-cover], and let $J\subset C$ be the ideal cutting out
its closed points, supplied by [lem-weil-pbc-strict-w-cover]. Define

$$
 D_0=C\otimes_AB,\qquad
 B'= (D_0)_{[JD_0]}
$$

using [def-weil-pbc-retained-localization].
