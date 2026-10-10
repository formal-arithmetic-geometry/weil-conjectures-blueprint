+++
kind  = "proof"
of    = "lem-weil-pbc-proper-open-section"
+++
The projection $b:V\to T_1$ is the base change of the open immersion
$j_2$ along $u$; a base change of an open immersion is an open
immersion, and its image is $u^{-1}(j_2(X))$, so $b$ identifies
$V$ with the open subscheme $u^{-1}(j_2(X))$ of $T_1$. Since
$u j_1=j_2$, the morphism $j_1$ maps $X$ into
$u^{-1}(j_2(X))=b(V)$, so the pair $(j_1,\operatorname{id}_X)$
factors through the fibre product $V=T_1\times_{T_2}X$: there is a
morphism $s:X\to V$ with $bs=j_1$ and $ps=\operatorname{id}_X$,
the one named in [def-weil-pbc-proper-open-comparison]. Being
the restriction of the open immersion $j_1$ to the open subscheme
$b(V)$, the morphism $s$ is an open immersion, and it identifies
$X$ with the open subscheme $j_1(X)$ of $V$. By
[lem-weil-pbc-proper-open-p-proper] the morphism $p$ is proper,
hence separated, and $s$ is an open immersion with
$ps=\operatorname{id}_X$; the criterion of
[lem-weil-pbc-open-section-clopen] therefore makes the image of
$s$ open and closed in $V$, with
$V=s(X)\amalg(V\setminus s(X))$ a decomposition into open
subschemes. All schemes and morphisms here are those of
[def-weil-pbc-scheme-conventions].
