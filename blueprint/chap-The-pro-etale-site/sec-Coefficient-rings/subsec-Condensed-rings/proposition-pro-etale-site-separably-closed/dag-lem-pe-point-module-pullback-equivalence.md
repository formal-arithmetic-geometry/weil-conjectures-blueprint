+++
id = "dag-lem-pe-point-module-pullback-equivalence"
kind = "dag-lemma"
title = "Pullback from the point is an equivalence on module objects over a separably closed field"
name_showing = false
order = 173502
tags = ["sheaf-dag"]
split_from = "proposition-pro-etale-site-separably-closed--2"
dag_id = "lem-pe-point-module-pullback-equivalence"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isEquivalence_upperStarFromPointMod", "AlgebraicGeometry.ProEtale.isEquivalence_lowerStar_comp_pointLowerStar", "AlgebraicGeometry.ProEtale.isEquivalence_upperStarFromPoint", "AlgebraicGeometry.ProEtale.isEquivalence_mapMod_upperStarFromPoint"]
+++
Let $\Lambda$ be a commutative condensed ring, that is a commutative monoid object in abelian condensed sheaves on profinite sets `sk-def-sfb-condensed-ring`. For a scheme $X$ let $p_X^*$ be the pullback from the point `sk-def-sfb-pullback-from-point`, $\Lambda_X=p_X^*\Lambda$ `sk-def-sfb-pulled-back-coefficients`, and $p_X^*\colon\operatorname{Mod}_\Lambda\to\operatorname{Mod}_{\Lambda_X}$ the induced functor on module objects `sk-def-sfb-module-objects`. If $\Omega$ is a separably closed field and $X=\operatorname{Spec}\Omega$, then $p_X^*\colon\operatorname{Mod}_\Lambda\to\operatorname{Mod}_{\Lambda_X}$ is an equivalence of categories (the pro-étale site of $\operatorname{Spec}\Omega$ being equivalent to profinite sets through $S\mapsto\operatorname{Spec}LC(S,\Omega)$ `det-pe-condensed-point-basis`).

(SHEAF DAG node `lem-pe-point-module-pullback-equivalence`; machine-alignment layer.) Split from [proposition-pro-etale-site-separably-closed--2]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sfb-modobj-transport`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-pullback-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-transport`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-module-objects`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`, `sk-def-sfb-transport`.
