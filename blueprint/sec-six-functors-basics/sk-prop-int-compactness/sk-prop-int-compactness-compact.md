+++
id = "det-prop-int-compactness-compact"
kind = "lemma"
title = "Integral constructible complexes are compact"
order = 2467
uses = ["sk-lem-int-integral-heart", "sk-lem-int-ext", "sk-prop-ind-heart", "sk-cor-ind-heart-ii", "sk-lem-finite-window", "sk-prop-pe-products", "sk-prop-pe-left-complete"]
+++
1. $\IndCons(X,\mathcal O_E)=\operatorname{Ind}(\Cons(X,\mathcal O_E))$ admits an
   exact fully faithful realization in $\Mod(X_{\mathrm{proét}},\mathcal O_E)$,
   closed under extensions and under kernels and cokernels of its own
   morphisms, and for $C\in\Cons(X,\mathcal O_E)$ one has $\Ext^q(C,B)=0$ in
   $\Mod(X_{\mathrm{proét}},\mathcal O_E)$ for $q>d_C$ (the integer of
   [sk-lem-int-ext](2)) and all $B\in\IndCons(X,\mathcal O_E)$.
2. Let $\Dic(X,\mathcal O_E)$ be the full subcategory of complexes with
   cohomology in $\IndCons(X,\mathcal O_E)$. It is closed under direct sums and
   truncations and contains $\Loc(\Dbc(X,\mathcal O_E))$. For
   $C\in\Cons(X,\mathcal O_E)$ and $K\in\Dic(X,\mathcal O_E)$, $\Hom(C,K[m])$
   depends only on $\tau_{[m-d_C,m]}K$.
3. Every $C\in\Dbc(X,\mathcal O_E)$ is compact in $\Loc(\Dbc(X,\mathcal O_E))$:
   $\Hom(C,-)$ commutes with direct sums.
