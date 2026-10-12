+++
id = "lem-weil-pbc-constant-module-sheaf-underlying"
kind = "lemma"
title = "The underlying abelian sheaf of a constant sheaf of modules"
uses = ["def-weil-pbc-etale-site", "def-weil-presheaf-modules-sheafification", "def-weil-sheaf-of-modules-category", "def-weil-pbc-etale-sheaves", "def-weil-pbc-constant-sheaf"]
lean = ["CategoryTheory.constantCommuteCompose"]
tags = ["mathlib", "stacks-03CY"]
+++
Let $T$ be a scheme, $T_{\Et}$ its small etale site [def-weil-pbc-etale-site], $R$ a commutative ring and $M$ an $R$-module. Let $\underline M^{R}$ be the constant sheaf of $R$-modules with value $M$ on $T_{\Et}$, i.e. the sheafification in sheaves of $R$-modules [def-weil-presheaf-modules-sheafification] of the constant presheaf $U\mapsto M$ (an object of the category of sheaves of $\underline R$-modules [def-weil-sheaf-of-modules-category], [def-weil-pbc-etale-sheaves]), and let $\underline M$ be the constant abelian sheaf [def-weil-pbc-constant-sheaf] on $T_{\Et}$ with value the underlying abelian group of $M$. Then the underlying abelian sheaf of $\underline M^{R}$ is canonically isomorphic to $\underline M$, the isomorphism being compatible with the canonical maps from the constant presheaf $U\mapsto M$; the isomorphism is natural in $M$. (Equivalently: the forgetful functor from sheaves of $R$-modules to abelian sheaves commutes with the constant-sheaf functors.)
