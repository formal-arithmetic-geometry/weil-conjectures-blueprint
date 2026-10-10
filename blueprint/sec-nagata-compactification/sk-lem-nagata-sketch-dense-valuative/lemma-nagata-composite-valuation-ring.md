+++
id = "lemma-nagata-composite-valuation-ring"
kind = "lemma"
title = "Composite of two valuation rings"
order = 274
lean = ["ValuationSubring.comapResidue"]
+++
Let $A'$ be a valuation ring with maximal ideal $\mathfrak m'$, and let
$A''$ be a valuation subring of the residue field
$k'=A'/\mathfrak m'$. The inverse image

$$
C=\{a\in A'\mid a\bmod\mathfrak m'\in A''\}
$$

is a valuation ring. Its fraction field is the fraction field of $A'$,
$\mathfrak m'\subseteq C$, and $C/\mathfrak m'\cong A''$.
