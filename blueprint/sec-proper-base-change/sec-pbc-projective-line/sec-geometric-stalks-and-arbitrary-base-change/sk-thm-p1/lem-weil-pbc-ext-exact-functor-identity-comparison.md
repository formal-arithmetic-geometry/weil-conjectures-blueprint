+++
id = "lem-weil-pbc-ext-exact-functor-identity-comparison"
kind = "lemma"
title = "Pushing Ext classes along an exact functor isomorphic to the identity"
uses = ["def-pc-ext", "def-sp-abelian"]
lean = ["CategoryTheory.Abelian.Ext.exactFunctorIdentityComparison"]
order = 1854
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian] with small Ext groups [def-pc-ext], $F:\mathcal A\to\mathcal A$ an additive functor preserving finite limits and finite colimits, and $e:F\xrightarrow{\sim}\mathrm{id}_{\mathcal A}$ a natural isomorphism. For objects $A,B\in\mathcal A$, $n\geq0$, and $x\in\operatorname{Ext}^n_{\mathcal A}(A,B)$, use the termwise exact functor on derived categories to define $F_*x$. Write $\operatorname{mk}_0(a)$ for the degree-zero Ext class of a morphism $a$. Then
$$\operatorname{mk}_0(e_B)\circ F_*x=x\circ\operatorname{mk}_0(e_A).$$
