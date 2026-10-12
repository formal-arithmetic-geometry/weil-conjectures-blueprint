+++
id = "def-sfb-constructible-extend-subfield"
kind = "definition"
title = "$T_{E,F}$ on bounded constructible complexes"
order = 1711
uses = ["def-sfb-derived-extend-subfield", "def-sfb-dcons-subfield", "lem-sfb-extend-subfield-constructible"]
lean = ["AlgebraicGeometry.ProEtale.constructibleExtendScalars"]
+++
For a prime $\ell$, a scheme $X$ and finite extensions $E\le F$ of $\mathbf Q_\ell$ inside
$\Qlb$, the functor

$$
T_{E,F}\colon D_{\mathrm{cons}}(X,E)\longrightarrow D_{\mathrm{cons}}(X,F)
$$

between the categories of [def-sfb-dcons-subfield] is the restriction of the derived extension
of scalars of [def-sfb-derived-extend-subfield], which preserves bounded constructible
complexes by [lem-sfb-extend-subfield-constructible].
