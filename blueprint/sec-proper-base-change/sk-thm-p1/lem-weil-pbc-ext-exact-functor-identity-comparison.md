+++
id = "lem-weil-pbc-ext-exact-functor-identity-comparison"
kind = "lemma"
title = "ExtExactFunctorIdentityComparison"
uses = ["def-pc-ext", "def-sp-abelian"]
lean = ["CategoryTheory.Abelian.Ext.exactFunctorIdentityComparison"]
source = "literature/stacks-project/derived.tex, Lemma Tag 015F (lemma-right-derived-exact-functor), parts (3)-(4), and Definition Tag 06XQ (definition-ext); argument by naturality on localized complexes, written by K1"
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian] with small Ext groups [def-pc-ext], $F:\mathcal A\to\mathcal A$ an additive functor preserving finite limits and finite colimits, and $e:F\xrightarrow{\sim}\mathrm{id}_{\mathcal A}$ a natural isomorphism. For objects $A,B\in\mathcal A$, $n\geq0$, and $x\in\operatorname{Ext}^n_{\mathcal A}(A,B)$, use the termwise exact functor on derived categories `CategoryTheory.Functor.mapDerivedCategoryFactors` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/DerivedCategory/ExactFunctor.lean)) to define $F_*x$. Write $\operatorname{mk}_0(a)$ for the degree-zero Ext class of a morphism $a$. Then
$$\operatorname{mk}_0(e_B)\circ F_*x=x\circ\operatorname{mk}_0(e_A).$$
