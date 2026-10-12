+++
id = "lem-weil-pbc-map-into-henselian-colimit"
kind = "lemma"
title = "Maps from an ind-etale algebra into a henselian local ring are determined by the residue map"
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-category-colimit", "def-weil-etale-morphism", "def-weil-residue-field"]
tags = ["stacks-08HQ"]
+++
Let $R\to S$ be a ring homomorphism with $S$ a henselian local ring [def-weil-pbc-henselian-terminology] with maximal ideal $\mathfrak m_S$, and put $\mathfrak p=$ the preimage of $\mathfrak m_S$ in $R$. Let $A$ be an $R$-algebra which is a filtered colimit [def-weil-pbc-category-colimit] of $R$-algebras $A_i$ with $\operatorname{Spec}A_i\to\operatorname{Spec}R$ etale [def-weil-etale-morphism] (in particular $A$ may be a single etale $R$-algebra), let $\mathfrak q\subset A$ be a prime lying over $\mathfrak p$, and let $\tau:\kappa(\mathfrak q)\to S/\mathfrak m_S$ be a homomorphism of $\kappa(\mathfrak p)$-algebras. Then there is exactly one homomorphism of $R$-algebras $f:A\to S$ with $f^{-1}(\mathfrak m_S)=\mathfrak q$ and inducing $\tau$ on residue fields (that is, $A\to S\to S/\mathfrak m_S$ equals $A\to A/\mathfrak q\to\kappa(\mathfrak q)\xrightarrow{\tau}S/\mathfrak m_S$).
