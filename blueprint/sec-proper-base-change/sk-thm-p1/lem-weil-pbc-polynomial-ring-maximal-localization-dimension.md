+++
id = "lem-weil-pbc-polynomial-ring-maximal-localization-dimension"
kind = "lemma"
title = "Localizations of a polynomial ring over a field at maximal ideals have dimension n"
lean = ["MvPolynomial.ringKrullDim_localizationAtMaximal"]
+++
Let $k$ be a field, $n\ge0$ an integer, $P=k[x_1,\dots,x_n]$ the polynomial ring `MvPolynomial, MvPolynomial.aeval, MvPolynomial.algHom_ext` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/MvPolynomial/Basic.lean)) and $\mathfrak M\subset P$ a maximal ideal. Then the localization $P_{\mathfrak M}$ `Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean)) has Krull dimension `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)) $\dim(P_{\mathfrak M})=n$.
