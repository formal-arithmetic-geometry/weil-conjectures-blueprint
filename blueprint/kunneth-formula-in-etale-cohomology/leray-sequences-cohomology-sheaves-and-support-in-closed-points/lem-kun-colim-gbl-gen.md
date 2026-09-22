+++
id = "lem-kun-colim-gbl-gen"
kind = "lemma"
title = "Filtered colimits of globally generated sheaves"
order = 6067
lean = ["AlgebraicGeometry.Etale.isGloballyGenerated_of_filteredColimit"]
uses = ["def-kun-global-generated", "lem-kun-global-generated-stalkwise", "lem-kun-stalks-commute-colimits"]
+++
A filtered colimit of globally generated sheaves of abelian groups on a site
is globally generated.

## Proof

Let $F=\varinjlim_iF_i$. By exactness of the stalk functors and the
commutativity of stalks with filtered colimits
([lem-kun-stalks-commute-colimits]),
$F_{\bar x}=\varinjlim_i(F_i)_{\bar x}$, each $(F_i)_{\bar x}$ being mapped
onto by $H^0(T_{\Et},F_i)$; filtered colimits of abelian groups preserve
surjections, so the evaluation map of [def-kun-global-generated] is
surjective on every stalk, and stalkwise surjectivity is global generation
by [lem-kun-global-generated-stalkwise].

Unresolved dependencies: def:weil-pbc-geometric-stalks, prop:weil-pbc-geometric-stalks-exact
