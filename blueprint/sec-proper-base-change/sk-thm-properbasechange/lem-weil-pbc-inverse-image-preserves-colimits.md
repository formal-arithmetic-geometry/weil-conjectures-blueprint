+++
id = "lem-weil-pbc-inverse-image-preserves-colimits"
kind = "lemma"
title = "Inverse image of etale abelian sheaves commutes with colimits"
uses = ["def-weil-pbc-inverse-image", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-category-colimit"]
tags = ["sheaf-dag", "stacks-0038"]
+++
Let $u:U\to V$ be a morphism of schemes and $u^{-1}:\Ab(V_{\Et})\to\Ab(U_{\Et})$ the inverse image [def-weil-pbc-inverse-image] on the categories of abelian sheaves on the small etale sites [def-weil-pbc-abelian-etale-sheaves]. For every small category $I$ and every diagram $F:I\to\Ab(V_{\Et})$, $i\mapsto F_i$, with colimit $\varinjlim_iF_i$ in $\Ab(V_{\Et})$ [def-weil-pbc-category-colimit], the canonical morphism

$$
\varinjlim_i u^{-1}F_i\longrightarrow u^{-1}\bigl(\varinjlim_iF_i\bigr),
$$

induced by the morphisms $u^{-1}$ of the coprojections $F_i\to\varinjlim F_i$, is an isomorphism; that is, $u^{-1}$ preserves all small colimits.
