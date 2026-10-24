+++
id = "def-weil-pbc-ind-etale-basis"
kind = "definition"
title = "The affine ind-etale subsite"
order = 957
lean = ["AlgebraicGeometry.Scheme.AffineProEt", "AlgebraicGeometry.Scheme.AffineProEt.toProEt", "AlgebraicGeometry.Scheme.AffineProEt.topology", "AlgebraicGeometry.proAffineEtale_Spec_iff"]
uses = ["def-weil-pbc-ind-etale-algebra", "def-weil-pbc-proetale-site"]
+++
For a scheme $X$, let $\mathcal B_X$ be the full subcategory of $X_{\Proet}$
consisting of the pro-etale affines over $X$: the objects $U\to X$ with $U$
affine and $U$ a cofiltered limit of affine schemes etale over $X$. For
affine $X=\operatorname{Spec}R$ these are the objects
$\operatorname{Spec}B\to X$ with $R\to B$ ind-etale
[def-weil-pbc-ind-etale-algebra]. Give $\mathcal B_X$ the coverings induced
from the small pro-etale site.
