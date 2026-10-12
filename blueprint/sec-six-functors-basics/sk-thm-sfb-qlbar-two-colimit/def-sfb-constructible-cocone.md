+++
id = "def-sfb-constructible-cocone"
kind = "definition"
title = "The cocone $E\\mapsto D_{\\mathrm{cons}}(X,E)$"
order = 1765
uses = ["sk-def-sfb-filtered-two-colimit", "def-sfb-dcons-subfield", "def-sfb-dcons-qlbar", "def-sfb-constructible-extend-subfield", "def-sfb-constructible-extend-to-qlbar", "def-sfb-constructible-extend-comp-iso"]
lean = ["AlgebraicGeometry.ProEtale.constructibleCocone"]
+++
Let $\ell$ be a prime and $X$ a scheme. The *constructible cocone* is the cocone of categories
([sk-def-sfb-filtered-two-colimit]) indexed by the set of finite extensions $E$ of
$\mathbf Q_\ell$ inside $\Qlb$, ordered by inclusion, with

- categories $D_{\mathrm{cons}}(X,E)$ ([def-sfb-dcons-subfield]),
- transition functors $T_{E,F}$ for $E\le F$ ([def-sfb-constructible-extend-subfield]),
- vertex $D_{\mathrm{cons}}(X,\Qlb)$ ([def-sfb-dcons-qlbar]) and functors $T_{E,\Qlb}$
  ([def-sfb-constructible-extend-to-qlbar]),
- isomorphisms $T_{F,\Qlb}\circ T_{E,F}\cong T_{E,\Qlb}$
  ([def-sfb-constructible-extend-comp-iso]).
