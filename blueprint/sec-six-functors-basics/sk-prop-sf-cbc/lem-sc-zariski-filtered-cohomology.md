+++
id = "lem-sc-zariski-filtered-cohomology"
kind = "lemma"
title = "Filtered colimits on a Noetherian Zariski site"
lean = ["TopCat.Sheaf.preservesColimitsOfShape_functorH"]
order = 2690
uses = ["def-sc-zariski-cohomology", "def-sc-zariski-site", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-cohomology-filtered-colimit", "thm-weil-pbc-hypercover-cohomology"]
+++
Let $X$ be a Noetherian
scheme and $(F_i)$ a filtered system of abelian sheaves on
[def-sc-zariski-site]. Then

$$
\varinjlim_i H^q(X_{\rm Zar},F_i)
\simeq H^q(X_{\rm Zar},\varinjlim_i F_i)
\quad(q\geq0),
$$

with cohomology as in [def-sc-zariski-cohomology].
