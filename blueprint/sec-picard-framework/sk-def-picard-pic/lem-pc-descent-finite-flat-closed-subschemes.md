+++
id = "lem-pc-descent-finite-flat-closed-subschemes"
kind = "lemma"
title = "Effective descent of finite flat closed subschemes"
order = 592
uses = ["def-pc-finite-locally-free", "lem-pc-fpqc-descent"]
lean = ["AlgebraicGeometry.isSheaf_fpqc_finiteLocallyFreeSubscheme"]
+++
Let $X\to S$ be a
morphism of schemes, $T$ an $S$-scheme, $\{g_i:T_i\to T\}_{i\in I}$ an
fpqc covering of $S$-schemes, and $d\geq0$; write
$X_T:=X\times_ST$, $X_{T_i}:=X\times_ST_i$ and $T_{ii'}:=T_i\times_TT_{i'}$.
Let $Z_i\subseteq X_{T_i}$ be closed subschemes such that each
$Z_i\to T_i$ is finite locally free of degree $d$
([def-pc-finite-locally-free]), and such that for all $i,i'$ the two
pullbacks $Z_i\times_{T_i}T_{ii'}$ and $Z_{i'}\times_{T_{i'}}T_{ii'}$ are
the same closed subscheme of $X_{T_{ii'}}$ (the cartesian identifications;
as a closed subscheme has no nontrivial automorphisms over the ambient
scheme, the cocycle condition is then automatic). Then there is a
unique closed subscheme $Z\subseteq X_T$ with $Z\times_TT_i=Z_i$ as closed
subschemes of $X_{T_i}$ for every $i$, and $Z\to T$ is finite locally
free of degree $d$.
