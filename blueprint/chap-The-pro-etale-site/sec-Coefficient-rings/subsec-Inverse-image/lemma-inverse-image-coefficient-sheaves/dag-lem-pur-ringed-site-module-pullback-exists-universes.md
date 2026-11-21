+++
id = "dag-lem-pur-ringed-site-module-pullback-exists-universes"
kind = "dag-lemma"
title = "Module pullback exists in a universe containing both sites"
name_showing = false
order = 187522
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-ringed-site-module-pullback-exists-universes"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.module_pushforward_isRightAdjoint_of_universes", "SheafOfModules.coefficientSheafification"]
+++
Let $\mathcal C,\mathcal D$ be categories whose objects and morphisms belong to a universe $W$ `def-weil-size-convention`, with Grothendieck topologies $J,K$ `def-weil-pbc-sites-and-cohomology`. Let $U:\mathcal C\to\mathcal D$ be continuous. Let $R$ be a sheaf of rings on $(\mathcal C,J)$ and $S$ a sheaf of rings on $(\mathcal D,K)$, with section rings in $W$, and let $a:R\to U_*S$ be a ring-sheaf morphism. On categories of module sheaves with section modules in $W$ `def-weil-sheaf-of-modules-category`, the direct-image functor defined by restriction along $U$ and scalar restriction along $a$ has a left adjoint. The site-object and site-morphism universes may be strictly smaller than $W$. Neither preservation of finite limits nor preservation of coverings by $U$ is required.

(SHEAF DAG node `lem-pur-ringed-site-module-pullback-exists-universes`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`.
