+++
id = "cor-wf-unramified-boundary-purity"
kind = "theorem"
title = "Purity at an unramified boundary point"
lean = ["AlgebraicGeometry.WeilSheaf.IsLisse.isPunctuallyPureOfWeight_of_upperStar", "AlgebraicGeometry.WeilGroup.isPunctuallyPure_of_forall_mem_range"]
order = 4120
tags = ["latex:corollary"]
uses = ["d-real-setup", "def-weil-frobenius-module-weights", "def-weil-punctual-weights", "lem-a1-lisse-middle-extension", "lem-wf-boundary-semicontinuity", "lem-wf-boundary-stalk-invariants"]
+++
Let $\mathcal F$ be lisse and $\iota$-pure of weight $w$ on a
punctured smooth curve, and let $x$ be the missing point. If the
local inertia action at $x$ is trivial, then the extended stalk
$(j_*\mathcal F)_{\bar x}$ is pure of weight $w$.

Consequently, if $j:U_0\hookrightarrow C_0$ is a dense open in a curve
in the sense of [d-real-setup] and $\mathcal G$ is a lisse Weil sheaf
on $C_0$ whose restriction $j^*\mathcal G$ is punctually $\iota$-pure
of weight $w$ on $U_0$, then $\mathcal G$ is punctually $\iota$-pure
of weight $w$ on all of $C_0$.
