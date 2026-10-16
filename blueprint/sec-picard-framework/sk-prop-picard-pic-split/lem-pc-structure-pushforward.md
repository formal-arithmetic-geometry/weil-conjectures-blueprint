+++
id = "lem-pc-structure-pushforward"
kind = "lemma"
title = "The open locus of $H^0$ of the structure sheaf"
lean = ["AlgebraicGeometry.isIso_pushforwardUnitMap_pullback_snd"]
order = 819
uses = ["def-pc-base-change", "def-pc-morphism-conventions", "def-pc-picard-presheaf", "lem-pc-finite-support-hi", "lem-sc-flat-base-change-coherent"]
+++
Let $k$ be a field, $X$ a
smooth projective curve over
$k$ with $H^0(X,\mathcal{O}_X)=k$ and $T$ a scheme over $k$. Then
$f_{T,*}\mathcal{O}_{X_T}\cong\mathcal{O}_T$, where $f_T:X_T\to T$ is the structure
morphism of the base change.
