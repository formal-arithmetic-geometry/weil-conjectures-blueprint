+++
id = "dag-lem-sfb-pointwise-kan-colimit"
kind = "dag-lemma"
title = "Pointwise left Kan extension as a colimit, natural in the presheaf"
name_showing = false
order = 39507
tags = ["sheaf-dag"]
split_from = "proposition-topos-functoriality--2"
dag_id = "lem-sfb-pointwise-kan-colimit"
dag_kind = "statement"
dag_status = "mathlib"
serial = false
+++
Fix a universe $\mathcal V$. Let $\mathcal C,\mathcal D$ be $\mathcal V$-small categories, $b:\mathcal C\to\mathcal D$ a functor, and $\mathcal A$ a category with $\mathcal V$-small morphism sets and all $\mathcal V$-small colimits `def-weil-pbc-category-colimit`. A presheaf means a functor $\mathcal C^{\mathrm{op}}\to\mathcal A$, with natural transformations as morphisms. For $W\in\mathcal D$, let $\mathcal I_W$ have objects $(V,\phi:W\to b(V))$ and arrows $(V,\phi)\to(V',\phi')$ given by $a:V\to V'$ satisfying $b(a)\phi=\phi'$. Left Kan extension $\operatorname{Lan}_{b^{\mathrm{op}}}$ means a left adjoint to restriction $G\mapsto G\circ b^{\mathrm{op}}$ from $\operatorname{Fun}(\mathcal D^{\mathrm{op}},\mathcal A)$ to $\operatorname{Fun}(\mathcal C^{\mathrm{op}},\mathcal A)$. It exists and there is an isomorphism of functors in the presheaf $F$,
$$
(\operatorname{Lan}_{b^{\mathrm{op}}}F)(W)\cong\operatorname{colim}_{\mathcal I_W^{\mathrm{op}}} F(V).
$$
Here the diagram on the right sends an arrow opposite to $a:V\to V'$ to $F(a):F(V')\to F(V)$; a natural transformation $F\to F'$ induces the colimit morphism of its components.

(SHEAF DAG node `lem-sfb-pointwise-kan-colimit`; machine-alignment layer.) Split from [proposition-topos-functoriality--2]. DAG kind: statement. Placed through `lem-sfb-finite-upper-star-exact` (ancestor-1). DAG status: mathlib. Statement dependencies not drawn: `def-weil-pbc-category-colimit`.
