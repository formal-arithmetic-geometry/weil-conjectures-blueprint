+++
id = "lem-weil-pbc-fpqc-descend-finite"
kind = "lemma"
title = "Being finite descends along fpqc coverings (Stacks 02LA)"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.isFinite_of_fpqc_cover"]
order = 1396
+++
Let $f:X\to S$ be a morphism of schemes [def-pc-scheme] and let $\{g_i:S_i\to S\}_{i\in I}$ be an fpqc covering of $S$. For $i\in I$ let $f_i:X\times_SS_i\to S_i$ be the base change of $f$ along $g_i$, the second projection of the fibre product. If $f_i$ is finite for every $i\in I$, then $f$ is finite.
