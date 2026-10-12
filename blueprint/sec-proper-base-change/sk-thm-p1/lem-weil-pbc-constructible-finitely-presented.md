+++
id = "lem-weil-pbc-constructible-finitely-presented"
kind = "lemma"
title = "Constructible sheaves are finitely presented in the category of sheaves"
order = 1167
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-etale-sheaves"]
+++
Let $X$ be a quasi-compact and quasi-separated scheme, let $\Lambda$ be a
Noetherian ring, let $F$ be a constructible sheaf of $\Lambda$-modules on
$X_{\Et}$, and let $G=\varinjlim_iG_i$ be a filtered colimit of sheaves of
$\Lambda$-modules. Then the canonical map

$$
 \varinjlim_i\operatorname{Mor}(F,G_i)\longrightarrow
 \operatorname{Mor}(F,G)
$$

is a bijection; equivalently, every morphism $F\to G$ factors through one of
the $G_i$, and any two such factorizations agree after passing to a common
refinement of the index.
