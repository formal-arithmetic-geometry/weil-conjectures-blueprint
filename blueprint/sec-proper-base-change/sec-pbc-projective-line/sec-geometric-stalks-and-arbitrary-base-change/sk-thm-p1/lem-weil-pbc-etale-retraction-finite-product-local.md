+++
id = "lem-weil-pbc-etale-retraction-finite-product-local"
kind = "lemma"
title = "Over a local ring whose etale algebras retract through rational points, every finite algebra is a finite product of local rings"
uses = ["def-weil-etale-morphism", "def-weil-residue-field"]
lean = ["finite_algebra_is_product_local_rings"]
order = 1845
tags = ["stacks-04GG"]
+++
Let $(R,\mathfrak m,\kappa)$ be a local ring such that for every ring map $R\to R'$ with $\operatorname{Spec}R'\to\operatorname{Spec}R$ etale [def-weil-etale-morphism] and every prime $\mathfrak m'\subset R'$ lying over $\mathfrak m$ with $\kappa\to\kappa(\mathfrak m')$ an isomorphism [def-weil-residue-field] there is an $R$-algebra homomorphism $\tau:R'\to R$ with $\tau^{-1}(\mathfrak m)=\mathfrak m'$. Then every finite $R$-algebra $B$ ($B$ finitely generated as an $R$-module) is isomorphic, as an $R$-algebra, to a finite product $B_1\times\cdots\times B_r$ ($r\ge0$) of local rings.
