+++
id = "def-weil-pbc-abelian-etale-sheaves"
kind = "definition"
title = "The category of abelian sheaves on the small etale site"
order = 1364
uses = ["def-weil-pbc-etale-site"]
lean = ["CategoryTheory.Sheaf", "AlgebraicGeometry.Scheme.smallEtaleTopology", "CategoryTheory.sheafIsAbelian"]
tags = ["mathlib", "stacks-095S"]
+++
Let $T$ be a scheme and $T_{\Et}$ its small etale site [def-weil-pbc-etale-site]. A *sheaf of abelian groups* (abelian sheaf) on $T_{\Et}$ is a contravariant functor $F$ from $T_{\Et}$ to abelian groups such that for every object $U$ and every covering $\{U_i\to U\}_i$ of $T_{\Et}$ the sequence $F(U)\to\prod_iF(U_i)\rightrightarrows\prod_{i,j}F(U_i\times_UU_j)$ is an equalizer. Abelian sheaves on $T_{\Et}$, with natural transformations as morphisms, form a full subcategory $\Ab(T_{\Et})$ of the category of presheaves of abelian groups; it is an abelian category, and it has all small colimits.
