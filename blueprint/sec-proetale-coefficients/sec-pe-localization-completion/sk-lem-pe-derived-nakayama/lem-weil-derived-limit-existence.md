+++
id = "lem-weil-derived-limit-existence"
kind = "lemma"
title = "Existence and computation of derived limits"
lean = ["CategoryTheory.exists_isDerivedLimit_and_iso", "CategoryTheory.derivedCategory_countableProducts_and_towerLimit"]
order = 1223
uses = ["def-weil-derived-limit"]
+++
Let $\mathcal D$ be a triangulated category and let $(K_n,f_n)$ be an inverse
system of objects of $\mathcal D$.

1. If $\prod_nK_n$ exists in $\mathcal D$, then a derived limit
   [def-weil-derived-limit] $R\varprojlim_nK_n$ exists, and any two derived
   limits of the system are isomorphic, although not canonically so.
2. Let $\mathcal A$ be an abelian category with exact countable products and
   let $\mathcal D=D(\mathcal A)$. Then countable products exist in $\mathcal
   D$, are represented by termwise products of any representatives, and
   satisfy $H^p\bigl(\prod_iK_i\bigr)\cong\prod_iH^p(K_i)$ for all $p$.
3. In the situation of (2), assume in addition that $\mathcal A$ has enough
   injectives. If $I_\bullet$ is a K-injective representative, in the abelian
   category of towers in $\mathcal A$, of the system $(K_n,f_n)$, then
   $\varprojlim_nI_n$ represents $R\varprojlim_nK_n$. Consequently "choosing
   a K-injective replacement of the tower" and "taking the first term of the
   Roos triangle" [def-weil-derived-limit] produce isomorphic objects.
