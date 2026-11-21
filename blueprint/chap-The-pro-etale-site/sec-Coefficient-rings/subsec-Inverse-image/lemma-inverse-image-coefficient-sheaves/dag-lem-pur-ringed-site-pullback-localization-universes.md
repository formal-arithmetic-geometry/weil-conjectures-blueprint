+++
id = "dag-lem-pur-ringed-site-pullback-localization-universes"
kind = "dag-lemma"
title = "Module pullback commutes with localization in a containing universe"
name_showing = false
order = 187524
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-ringed-site-pullback-localization-universes"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.RingedSitePullback.locMap", "SheafOfModules.RingedSitePullback.localComparison", "SheafOfModules.RingedSitePullback.localComparison_eq", "SheafOfModules.RingedSitePullback.localComparison_isIso", "SheafOfModules.RingedSitePullback.localHomEquiv", "SheafOfModules.RingedSitePullback.localHomEquiv_apply", "SheafOfModules.RingedSitePullback.local_hom_ext", "SheafOfModules.RingedSitePullback.local_continuous"]
uses = ["dag-def-pur-localized-ringed-site"]
+++
Let C and D be sites small relative to the coefficient universe W [def-weil-size-convention, def-weil-pbc-sites-and-cohomology], with finite limits. Let U:C → D be continuous and preserve finite limits. Let R and S be sheaves of rings and a:R → U_*S a ring-sheaf morphism. For V in C assume Over.post U is continuous on the slice sites. Write a_V for the restricted coefficient map and assume the global and slice module pushforwards `def-weil-sheaf-of-modules-category` have left adjoints F and F_V. The canonical comparison F_V(L|V) → (FL)|U(V), whose adjunct is the restricted global adjunction unit, is invertible. Its composite with the slice unit equals the restricted global unit. Thus maps from (FL)|U(V) to a module N correspond bijectively to maps L|V → U_V* N, with the correspondence given by composition with the restricted unit. Restriction and localized rings are as in [dag-def-pur-localized-ringed-site]. If U preserves covering sieves, the slice continuity assumption holds.

(SHEAF DAG node `lem-pur-ringed-site-pullback-localization-universes`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`.
