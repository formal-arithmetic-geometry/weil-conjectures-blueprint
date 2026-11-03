+++
id = "lem-weil-pbc-etale-stratification-local-gluing-core"
kind = "lemma"
title = "Global constructible immersed refinement factoring through local strata"
uses = ["def-constructible-stratification", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.exists_global_stratification_factoring_local"]
order = 1852
+++
Let $X$ be a quasi-compact quasi-separated scheme [def-weil-pbc-scheme-conventions], and let $W_1,\dots,W_n\subseteq X$ be affine open subschemes covering $X$. For each $a$ let $T_a=(T_{a,b},\ \iota_{a,b}:Z_{a,b}\to W_a)_b$ be a stratification of $W_a$ [def-constructible-stratification] (in particular its strata are constructible and $\iota_{a,b}$ are immersions with image $T_{a,b}$). Then there is a stratification $S=(S_i,\ \iota_i:Z_i\to X)_i$ of $X$ such that every stratum immersion of $S$ factors through a local one: for each $i$ there are indices $a,b$ and a morphism of schemes $q:Z_i\to Z_{a,b}$ with $\iota_i=(W_a\hookrightarrow X)\circ\iota_{a,b}\circ q$.
