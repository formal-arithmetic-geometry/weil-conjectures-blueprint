+++
id = "def-sfb-constructible-extend-to-qlbar"
kind = "definition"
title = "$T_{E,\\Qlb}$ on bounded constructible complexes"
order = 1767
uses = ["def-sfb-derived-extend-to-qlbar", "def-sfb-dcons-subfield", "def-sfb-dcons-qlbar", "lem-sfb-extend-to-qlbar-constructible"]
lean = ["AlgebraicGeometry.ProEtale.constructibleToPadicAlgCl"]
+++
For a prime $\ell$, a scheme $X$ and a finite extension $E$ of $\mathbf Q_\ell$ inside $\Qlb$, the
functor

$$
T_{E,\Qlb}\colon D_{\mathrm{cons}}(X,E)\longrightarrow D_{\mathrm{cons}}(X,\Qlb)
$$

between the categories of [def-sfb-dcons-subfield] and [def-sfb-dcons-qlbar] is the restriction
of the derived extension of scalars of [def-sfb-derived-extend-to-qlbar], which preserves
bounded constructible complexes by [lem-sfb-extend-to-qlbar-constructible].
