+++
id = "lem-fin-finite-type-pushforward-embedding"
kind = "lemma"
title = "Finite-pushforward embeddings over a field"
lean = ["AlgebraicGeometry.Etale.exists_mono_biproduct_lowerStar_of_locallyOfFiniteType"]
order = 1954
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lem-fin-normal-generic-constant", "lem-fin-normalization-extension-finite", "lem-weil-pbc-constructible-noetherian-finite-selection"]
+++
Let $X$ be of finite type
over a field, and let $F$ be a
constructible
sheaf of $\mathbf Z/N$-modules. There are finitely many finite maps
$h_i:Y_i\to X$, finite groups $M_i$ killed by $N$, and an
injective map

$$
F\longrightarrow\bigoplus_i(h_i)_*\underline M_i .
$$

Direct images have the meaning of [def-weil-pbc-direct-image].
