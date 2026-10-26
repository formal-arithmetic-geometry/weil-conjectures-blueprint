+++
id = "lem-weil-pbc-filtered-colimit-localization-at-prime"
kind = "lemma"
title = "Localization at a prime commutes with filtered colimits of rings"
lean = ["AlgebraicGeometry.filteredColimitLocalizationAtPrime", "AlgebraicGeometry.filteredColimitLocalizationAtPrime_data"]
order = 1742
+++
Let $I$ be a small filtered category and $i\mapsto R_i$ a functor from $I$ to the category of commutative rings, with colimit $R=\varinjlim_IR_i$ in that category and coprojections $\iota_i:R_i\to R$. Let $\mathfrak p\subset R$ be a prime ideal and put $\mathfrak p_i=\iota_i^{-1}(\mathfrak p)$, a prime ideal of $R_i$. Then: (1) for every morphism $a:i\to j$ of $I$ one has $R(a)^{-1}(\mathfrak p_j)=\mathfrak p_i$, so $R(a)$ induces a ring map $(R_i)_{\mathfrak p_i}\to(R_j)_{\mathfrak p_j}$, $x/s\mapsto R(a)(x)/R(a)(s)$, between the localizations, and these maps form a functor $i\mapsto(R_i)_{\mathfrak p_i}$ from $I$ to commutative rings; (2) the ring maps $\kappa_i:(R_i)_{\mathfrak p_i}\to R_{\mathfrak p}$, $x/s\mapsto\iota_i(x)/\iota_i(s)$, are well defined and make $R_{\mathfrak p}$ a colimit of this functor in the category of commutative rings: $R_{\mathfrak p}=\varinjlim_I(R_i)_{\mathfrak p_i}$.
