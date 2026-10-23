+++
id = "lem-sfb-constructible-cocone-hom-inj"
kind = "lemma"
title = "(Hom-inj) for the constructible cocone"
order = 2177
uses = ["def-sfb-constructible-cocone", "sk-def-sfb-filtered-two-colimit"]
lean = ["AlgebraicGeometry.ProEtale.constructibleCocone_homInj"]
+++
Let $\ell$ be a prime and $X$ a scheme whose underlying topological space is Noetherian. The
constructible cocone ([def-sfb-constructible-cocone]) satisfies (Hom-inj) of
[sk-def-sfb-filtered-two-colimit]: if two morphisms $g,g'\colon K\to L$ in
$D_{\mathrm{cons}}(X,H)$ satisfy $T_{H,\Qlb}(g)=T_{H,\Qlb}(g')$, then
$T_{H,H'}(g)=T_{H,H'}(g')$ for some finite extension $H'\supseteq H$.
