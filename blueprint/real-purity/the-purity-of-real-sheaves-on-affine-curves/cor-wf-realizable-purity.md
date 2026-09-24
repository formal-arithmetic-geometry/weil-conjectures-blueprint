+++
id = "cor-wf-realizable-purity"
kind = "theorem"
title = "Purity of an irreducible realizable sheaf"
order = 4188
tags = ["latex:corollary"]
uses = ["def-sc-curves", "def-weil-punctual-weights", "def-wf-determinantal-weight", "def-wf-iota-real", "lem-wf-real-semisimplification", "thm-rp-real-lisse-purity-affine"]
+++
An irreducible lisse $\iota$-realizable Weil sheaf on a
smooth geometrically connected affine curve
is punctually $\iota$-pure of
its determinantal weight.

## Proof

By [def-wf-iota-real], the sheaf $\mathcal F$ is an irreducible
direct summand of an $\iota$-real lisse Weil sheaf. Pass to the
semisimplification of the ambient sheaf using
[lem-wf-real-semisimplification]; the result is semisimple and
$\iota$-real, and $\mathcal F$ is one of its irreducible
constituents. The affine purity of
[thm-rp-real-lisse-purity-affine] applies to the ambient sheaf
and hence to $\mathcal F$: it is punctually $\iota$-pure of weight
$\dw_\iota(\mathcal F)$, as defined in
[def-wf-determinantal-weight].
