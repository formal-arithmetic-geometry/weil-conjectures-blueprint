+++
id = "lem-weil-pbc-ext-exact-functor-composition-comparison"
kind = "lemma"
title = "ExtExactFunctorCompositionComparison"
uses = ["def-pc-ext", "def-sp-abelian"]
lean = ["CategoryTheory.Abelian.Ext.exactFunctorCompositionComparison"]
source = "literature/stacks-project/derived.tex, Lemma Tag 015F (lemma-right-derived-exact-functor), parts (3)-(4), and Definition Tag 06XQ (definition-ext); argument by naturality on localized complexes, written by K1"
+++
Let $\mathcal A,\mathcal B,\mathcal C$ be abelian categories [def-sp-abelian] with small Ext groups [def-pc-ext]. Let $F:\mathcal A\to\mathcal B$, $G:\mathcal B\to\mathcal C$, $H:\mathcal A\to\mathcal C$ be additive functors preserving finite limits and finite colimits, and let $e:H\xrightarrow{\sim}G\circ F$ be a natural isomorphism. For objects $A,B\in\mathcal A$, $n\geq0$, and $x\in\operatorname{Ext}^n_{\mathcal A}(A,B)$, let $F_*x$ denote its image under the termwise exact functor on derived categories `CategoryTheory.Functor.mapDerivedCategoryFactors` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/DerivedCategory/ExactFunctor.lean)), using the canonical identifications of the single complexes and shifts. For a morphism $a$ write $\operatorname{mk}_0(a)$ for its degree-zero Ext class. Then
$$\operatorname{mk}_0(e_B)\circ H_*x=G_*F_*x\circ\operatorname{mk}_0(e_A).$$
