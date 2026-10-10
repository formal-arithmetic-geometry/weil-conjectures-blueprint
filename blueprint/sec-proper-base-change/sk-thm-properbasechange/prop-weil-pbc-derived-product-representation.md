+++
id = "prop-weil-pbc-derived-product-representation"
kind = "theorem"
title = "Representation of the derived product of a tower"
order = 1244
uses = ["def-weil-derived-limit", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-kinjective-resolutions", "lem-weil-derived-limit-existence"]
tags = ["latex:proposition"]
+++
Let $\operatorname{Tow}_{A}(T)$ be the tower category of
[def-weil-pbc-adic-coefficient-datum] and let $M_\bullet\in
D(\operatorname{Tow}_{A}(T))$ with a K-injective resolution
[def-weil-pbc-kinjective-resolutions] $M_\bullet\to I_\bullet$ in the abelian
category of towers. Then the derived product $R\!\prod_nM_n$ of
[def-weil-pbc-derived-inverse-limit] is represented by
$\prod_n\operatorname{ev}_n(I_\bullet)$.

## Proof

By [def-weil-pbc-derived-inverse-limit] the derived product $R\!\prod_nM_n$
is the product of the system $(\operatorname{ev}_nM_\bullet)$ in the
triangulated category $D(T_{\Proet},A)$ attached to the tower category of
[def-weil-pbc-adic-coefficient-datum]. Clause (2) of the derived-limit
existence lemma of the conventions chapter states that in the derived
category of an abelian category with exact countable products the countable
products exist and are represented by termwise products of any
representatives, and clause (3) of the same lemma exhibits
$\prod_n\operatorname{ev}_n(I_\bullet)$ as the termwise product of the
K-injective representatives $\operatorname{ev}_n(I_\bullet)$ of the objects
$\operatorname{ev}_nM_\bullet$; hence that product represents
$R\!\prod_nM_n$.
