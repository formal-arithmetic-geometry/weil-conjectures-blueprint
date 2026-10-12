+++
id = "def-sfb-constructible-extend-comp-iso"
kind = "definition"
title = "Transitivity on bounded constructible complexes"
order = 1764
uses = ["def-sfb-constructible-extend-subfield", "def-sfb-constructible-extend-to-qlbar", "def-sfb-derived-extend-comp-iso"]
lean = ["AlgebraicGeometry.ProEtale.constructibleToPadicAlgClCompIso"]
+++
For a prime $\ell$, a scheme $X$ and finite extensions $E\le F$ of $\mathbf Q_\ell$ inside
$\Qlb$, the natural isomorphism

$$
T_{F,\Qlb}\circ T_{E,F}\;\cong\;T_{E,\Qlb}\colon D_{\mathrm{cons}}(X,E)\longrightarrow
D_{\mathrm{cons}}(X,\Qlb)
$$

of functors between bounded constructible categories
([def-sfb-constructible-extend-subfield], [def-sfb-constructible-extend-to-qlbar]) is the
restriction of the isomorphism of [def-sfb-derived-extend-comp-iso].
