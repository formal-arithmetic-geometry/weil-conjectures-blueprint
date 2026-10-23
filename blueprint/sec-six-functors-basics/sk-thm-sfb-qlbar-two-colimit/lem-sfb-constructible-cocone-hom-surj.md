+++
id = "lem-sfb-constructible-cocone-hom-surj"
kind = "lemma"
title = "(Hom-surj) for the constructible cocone"
order = 2176
uses = ["def-sfb-constructible-cocone", "sk-def-sfb-filtered-two-colimit"]
lean = ["AlgebraicGeometry.ProEtale.constructibleCocone_homSurj"]
+++
Let $\ell$ be a prime and $X$ a scheme whose underlying topological space is Noetherian. The
constructible cocone ([def-sfb-constructible-cocone]) satisfies (Hom-surj) of
[sk-def-sfb-filtered-two-colimit]: for finite extensions $E,F$ of $\mathbf Q_\ell$ in $\Qlb$,
$K_E\in D_{\mathrm{cons}}(X,E)$, $L_F\in D_{\mathrm{cons}}(X,F)$ and every morphism
$\varphi\colon T_{E,\Qlb}K_E\to T_{F,\Qlb}L_F$, there are a finite extension $H\supseteq E,F$ and
a morphism $g\colon T_{E,H}K_E\to T_{F,H}L_F$ in $D_{\mathrm{cons}}(X,H)$ with
$\varphi=T_{H,\Qlb}(g)$ up to the transitivity isomorphisms.
