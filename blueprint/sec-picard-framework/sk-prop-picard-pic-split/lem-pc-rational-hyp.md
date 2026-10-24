+++
id = "lem-pc-rational-hyp"
kind = "lemma"
title = "Curves with a rational point satisfy the hypotheses"
lean = ["AlgebraicGeometry.Scheme.GlobalSectionsBijective.of_section", "AlgebraicGeometry.isIso_pushforwardUnitMap_pullback_snd_of_geometricallyIntegral", "AlgebraicGeometry.isIso_pushforwardUnitMap_pullback_snd_of_section"]
order = 673
uses = ["def-pc-rational-point", "def-pc-smooth-projective-curve", "lem-pc-h0-proper-variety", "lem-pc-structure-pushforward", "thm-pc-pic-split"]
+++
Let $k$ be a field and let $X$ be a
smooth projective curve over
$k$ (more generally, an integral proper scheme over $k$) which has a
$k$-rational point $\sigma$. Then the hypotheses of
[thm-pc-pic-split] (with $S=\operatorname{Spec}(k)$, $f:X\to\operatorname{Spec}(k)$) are
satisfied: $f$ has the section $\sigma$, and
$\mathcal{O}_T\to f_{T,*}\mathcal{O}_{X_T}$ is an isomorphism for every
$T\in\operatorname{Ob}((\mathit{Sch}/k)_{fppf})$. The second condition also holds,
without a rational point, whenever $X$ is smooth of relative dimension $1$,
proper and geometrically integral over $k$.
