+++
id = "def-weil-pbc-ambient-ringed-exchange"
kind = "definition"
title = "Ambient ringed exchange"
order = 1963
lean = ["AlgebraicGeometry.ProEtale.derivedBaseChangeMap"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-proetale-operations"]
+++
For a cartesian square [def-weil-pbc-cartesian-square] with its chosen
identification, and a coefficient sheaf $R$, define the ambient pro-etale
exchange transformation

$$
 \Ex^R_{\square}:Lg^*Rf_*\longrightarrow Rf'_*Lg'^*
$$

to be the mate, under $Lf'^*\dashv Rf'_*$, of

$$
 Lf'^*Lg^*Rf_*\xrightarrow{\sim}
 Lg'^*Lf^*Rf_*\xrightarrow{Lg'^*\varepsilon_f}Lg'^*,
$$

using the derived operations on ringed pro-etale topoi.

The transformation is defined before, and independently of, any completeness
or constructibility condition.
