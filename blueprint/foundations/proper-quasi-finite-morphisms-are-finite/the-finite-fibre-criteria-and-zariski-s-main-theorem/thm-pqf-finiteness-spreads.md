+++
id = "thm-pqf-finiteness-spreads"
kind = "theorem"
title = "Finiteness spreads out from a finite fibre; Stacks Lemma 30.21.2"
order = 2134
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-proper-base-change", "pqf-def-locnoeth", "pqf-def-quasifinite", "pqf-lem-locqf-fibre-discrete", "pqf-lem-locqf-restrict", "pqf-lem-proper-basic", "pqf-lem-proper-closed-map", "pqf-lem-qf-finitefibres", "pqf-lem-qf-locqf-qc", "pqf-lem-qf-locus-open", "thm-pqf-finite-iff-proper-finite-fibres"]
+++
Let $f:X\to S$ be a morphism of schemes and $s\in S$. Assume that $S$
is locally Noetherian, that $f$ is
proper, and that
$f^{-1}(\{s\})$ is a finite set. Then there exists an open
neighbourhood $V\subset S$ of $s$ such that
$f|_{f^{-1}(V)}:f^{-1}(V)\to V$ is finite.
(*Stacks Project, Cohomology of Schemes, Lemma 30.21.2, Tag
[02OH](https://stacks.math.columbia.edu/tag/02OH).*)

## Proof

The morphism $f$ is of finite type by [def-weil-pbc-scheme-conventions],
hence locally of finite type, and $f^{-1}(\{s\})$ is finite, so by
[pqf-lem-locqf-fibre-discrete] the morphism $f$ is quasi-finite at
all points of $f^{-1}(\{s\})$. By [pqf-lem-qf-locus-open] the set
$U\subset X$ of points at which $f$ is quasi-finite is open. Let
$Z=X\setminus U$. Then $s\notin f(Z)$: every point of $f^{-1}(\{s\})$
lies in $U$. Since $f$ is proper, $f$ is a closed map by
[pqf-lem-proper-closed-map], so $f(Z)\subset S$ is closed. Choose an
open neighbourhood $V\subset S$ of $s$ with $f(Z)\cap V=\emptyset$.
Then $f^{-1}(V)\subset U$. The restriction
$f|_{f^{-1}(V)}:f^{-1}(V)\to V$ is proper by
[lem-weil-pbc-proper-base-change] of the ambient-foundations chapter (base change
along the open immersion $V\hookrightarrow S$), and it is locally
quasi-finite: it is the restriction of the locally quasi-finite
morphism $U\to S$ of [pqf-lem-qf-locus-open] to open
subschemes, so [pqf-lem-locqf-restrict] applies. Hence
$f|_{f^{-1}(V)}$ is quasi-finite by [pqf-lem-qf-locqf-qc]
(proper morphisms are quasi-compact by
[pqf-lem-proper-basic]), and consequently has finite fibres by
[pqf-lem-qf-finitefibres]. Since $V$ is an open subscheme of
the locally Noetherian scheme $S$, it is locally Noetherian by
[pqf-def-locnoeth]. Therefore
[thm-pqf-finite-iff-proper-finite-fibres] applies to the proper
morphism $f|_{f^{-1}(V)}$ with finite fibres, so it is finite.
