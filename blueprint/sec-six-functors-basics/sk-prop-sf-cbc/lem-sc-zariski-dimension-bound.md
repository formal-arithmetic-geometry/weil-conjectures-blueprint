+++
id = "lem-sc-zariski-dimension-bound"
kind = "lemma"
title = "The Zariski dimension bound"
lean = ["TopCat.Sheaf.subsingleton_H_of_topologicalKrullDim_lt", "AlgebraicGeometry.Scheme.subsingleton_zariskiH_of_topologicalKrullDim_lt"]
order = 1910
uses = ["def-sc-zariski-cohomology", "def-sc-zariski-flasque", "def-sc-zariski-site", "def-weil-pbc-scheme-conventions", "lem-sc-zariski-filtered-cohomology", "lem-sc-zariski-flasque-acyclic"]
+++
Let $X$ be a Noetherian
scheme of finite dimension $d$.
For every abelian sheaf $F$ on [def-sc-zariski-site],

$$
H^q(X_{\rm Zar},F)=0\quad(q>d),
$$

with cohomology as in [def-sc-zariski-cohomology].
