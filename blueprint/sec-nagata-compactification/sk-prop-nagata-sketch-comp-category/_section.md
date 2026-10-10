+++
id = "sk-prop-nagata-sketch-comp-category"
kind = "proposition"
title = "The compactification category and common refinements"
order = 408
uses = ["sk-def-nagata-sketch-data", "sk-thm-nagata-compactification"]
lean = ["AlgebraicGeometry.Compactification.category", "AlgebraicGeometry.Compactification.isCofiltered", "AlgebraicGeometry.Compactification.exists_common_refinement", "AlgebraicGeometry.Compactification.baseChange"]
tags = ["sketch"]
+++
Let $f:X\to S$ be quasi-compact. Let
$\operatorname{Comp}(f)$ be the category whose objects are the
compactifications $c=(j,\bar f)$ of [sk-def-nagata-sketch-data] and whose
morphisms $u:c_1\to c_2$ — the *refinements* — are the proper
$S$-morphisms $u:\overline X_1\to\overline X_2$ with $u\circ j_1=j_2$.
If $f$ admits a compactification (for instance when $S$ is qcqs and $f$ is
separated of finite type, by [sk-thm-nagata-compactification]), the
category is nonempty and cofiltered. In general it has the following
refinement properties:

1. **(i)** any two objects admit a common refinement, hence so does every
finite family;
1. **(ii)** any two parallel refinements $u,v:c_1\to c_2$ are equalized by a
further refinement $c'\to c_1$.

Moreover the construction is compatible with base change: for any $g:S'\to S$
(and any $f$) the base change of a compactification of $f$ is a
compactification of $f'=f\times_SS'$, a refinement base-changes to a refinement, and these base
changes carry common refinements to common refinements.
