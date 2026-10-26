+++
id = "lem-weil-pbc-proper-open-section"
kind = "lemma"
title = "The section of the comparison square and the open it fixes"
order = 2256
lean = ["AlgebraicGeometry.ProperOpenDatum.section_spec"]
uses = ["def-weil-pbc-proper-open-comparison", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-open-section-clopen", "lem-weil-pbc-proper-open-p-proper"]
+++
Let $u:T_1\to T_2$ be
proper and let
$j_i:X\hookrightarrow T_i$ be
open immersions with
$u j_1=j_2$. For $V=T_1\times_{T_2}X$, with projections
$b:V\to T_1$, $p:V\to X$ and the morphism $s:X\to V$ induced by
$j_1$ of [def-weil-pbc-proper-open-comparison], the morphism
$s$ is an
open immersion with
$p\circ s=\operatorname{id}_X$ whose image is open and closed in
$V$, and $s$ identifies $X$ with the open subscheme $j_1(X)$
of $V$, the projection $b$ identifying $V$ with the open
subscheme $u^{-1}(j_2(X))$ of $T_1$.
