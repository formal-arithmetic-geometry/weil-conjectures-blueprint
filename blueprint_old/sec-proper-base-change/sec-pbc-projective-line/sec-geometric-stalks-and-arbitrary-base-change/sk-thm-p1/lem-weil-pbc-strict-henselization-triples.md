+++
id = "lem-weil-pbc-strict-henselization-triples"
kind = "lemma"
title = "The colimit over etale algebras with a point and a residue embedding is strictly henselian"
lean = ["AlgebraicGeometry.Scheme.strictHenselization_triples"]
order = 2034
uses = ["def-pc-separably-closed", "def-weil-etale-morphism", "def-weil-pbc-category-colimit", "def-weil-pbc-henselian-terminology"]
tags = ["stacks-04GW"]
+++
Let $R$ be a commutative ring, $\mathfrak p\subset R$ a prime ideal with residue field $\kappa(\mathfrak p)$, and $K$ a separable closure of $\kappa(\mathfrak p)$: a field with a $\kappa(\mathfrak p)$-embedding $\kappa(\mathfrak p)\to K$ such that $K$ is separably closed [def-pc-separably-closed] and every element of $K$ is separable algebraic over $\kappa(\mathfrak p)$. Let $\mathcal T$ be the category of triples $(S,\mathfrak q,\phi)$ with $R\to S$ a ring map such that $\operatorname{Spec}S\to\operatorname{Spec}R$ is etale [def-weil-etale-morphism], $\mathfrak q\subset S$ a prime lying over $\mathfrak p$, and $\phi:\kappa(\mathfrak q)\to K$ a $\kappa(\mathfrak p)$-algebra map; a morphism $(S,\mathfrak q,\phi)\to(S',\mathfrak q',\phi')$ is an $R$-algebra map $\beta:S\to S'$ with $\beta^{-1}(\mathfrak q')=\mathfrak q$ and $\phi'\circ\kappa(\beta)=\phi$. Then:

1. $\mathcal T$ is filtered; let $C=\varinjlim_{(S,\mathfrak q,\phi)\in\mathcal T}S$ [def-weil-pbc-category-colimit], an $R$-algebra which is a filtered colimit of etale $R$-algebras.
2. The maps $S\to S/\mathfrak q\to\kappa(\mathfrak q)\xrightarrow{\phi}K$ are compatible and define a surjective ring map $\psi:C\to K$; $C$ is a local ring with maximal ideal $\mathfrak m_C=\ker\psi=\mathfrak pC$, so $\psi$ induces an isomorphism of $\kappa(\mathfrak p)$-algebras $C/\mathfrak m_C\cong K$; and the preimage of $\mathfrak m_C$ in $R$ is $\mathfrak p$.
3. $C$ is strictly henselian [def-weil-pbc-henselian-terminology]: henselian, with separably closed residue field $C/\mathfrak m_C\cong K$.

($C$ is the strict henselization $(R_{\mathfrak p})^{sh}$ of $R_{\mathfrak p}$ with respect to $\kappa(\mathfrak p)\subset K$.)
