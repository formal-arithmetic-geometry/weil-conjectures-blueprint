+++
id = "prop-compactification-refinement"
kind = "theorem"
title = "Existence and common refinement"
order = 608
tags = ["latex:proposition"]
uses = ["def-weil-compactifications-refinements", "def-weil-scheme-morphism-properties", "thm-nagata-compactification"]
+++
Let $K$ be a field, let $X,Y$ be finite-type $K$-schemes, and let
$f:X\to Y$ be a separated finite-type $K$-morphism. Let
$\operatorname{Comp}(f)$ be the compactification category
([def-weil-compactifications-refinements]) whose objects are factorizations
$X\xrightarrow{j}\overline X\xrightarrow{\bar f}Y$ with $j$ an open
immersion, $\bar f$ proper, and $\bar f j=f$, and whose morphisms are proper
$Y$-morphisms $u:\overline X_1\to\overline X_2$ with $u j_1=j_2$. This
category is nonempty (Nagata's theorem, [thm-nagata-compactification]) and
cofiltered: finitely many objects admit a common refinement, and any two
parallel refinements become equal after a further refinement.

## Proof

The category $\operatorname{Comp}(f)$ of
[def-weil-compactifications-refinements] is nonempty by the
compactification clause of [thm-nagata-compactification]: every
separated finite-type morphism of finite-type schemes over a field
admits a compactification $X\xrightarrow{j}\overline X
\xrightarrow{\bar f}Y$ with $j$ an open immersion and $\bar f$
proper, exactly the objects of $\operatorname{Comp}(f)$. That the
category is cofiltered is the remaining clauses of
[thm-nagata-compactification]: any two compactifications admit a
common proper refinement, so by induction any finite family does, and any
two parallel refinements become equal after a further refinement; the
base-change clause of [thm-nagata-compactification] states the
functoriality up to refinement used in
[def-weil-compactifications-refinements].
