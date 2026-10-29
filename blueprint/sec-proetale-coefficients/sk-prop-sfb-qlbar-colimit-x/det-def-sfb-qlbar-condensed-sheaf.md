+++
id = "det-def-sfb-qlbar-condensed-sheaf"
kind = "lemma"
title = "$\\underline{\\overline{\\mathbf Q}}_\\ell$ is a condensed ring"
lean = ["Profinite.isSheaf_padicAlgClSubfunctor", "Profinite.isSheaf_padicAlgClRingPresheaf", "Profinite.padicAlgClCondensedRing", "Profinite.padicAlgClRingObj", "Profinite.isCommMonObj_padicAlgClRingObj"]
order = 1239
uses = ["det-def-sfb-qlbar-condensed-definition", "def-sfb-continuous-map-condensed-ring", "det-def-sfb-ring-object-sheaf", "det-def-sfb-condensed-ring", "det-def-sfb-qlbar-condensed-subextensions"]
+++
The presheaf of rings $\underline{\Qlb}$ of [det-def-sfb-qlbar-condensed-definition] is a sheaf on
$*_{\mathrm{proét}}$, i.e. a condensed ring ([det-def-sfb-condensed-ring]); no sheafification is
needed. Equivalently, its underlying presheaf of sets, a subpresheaf of the sheaf $C(-,\Qlb)$, is
a sheaf. Its underlying abelian sheaf is a commutative ring object of $\Sh(*_{\mathrm{proét}},\Ab)$
([det-def-sfb-ring-object-sheaf]).
