+++
id = "def-sc-zariski-flasque"
kind = "definition"
title = "Flasque sheaves on the Zariski site"
order = 4914
lean = ["TopCat.Sheaf.IsFlasque"]
+++
An abelian sheaf $F$ on a topological space $X$ is *flasque* if
$F(V)\to F(U)$ is surjective for every inclusion of open subsets
$U\subset V\subset X$.

*Note.* The source marks this declaration as already available in Mathlib,
as `TopCat.Sheaf.IsFlasque`; the `lean` field records that name verbatim.
