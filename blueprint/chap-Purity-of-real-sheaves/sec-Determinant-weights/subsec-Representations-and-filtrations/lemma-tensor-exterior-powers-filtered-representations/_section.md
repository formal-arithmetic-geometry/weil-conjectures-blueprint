+++
id = "lemma-tensor-exterior-powers-filtered-representations"
kind = "lemma"
title = "Tensor and exterior powers of filtered representations"
order = 1124
lean = ["Representation.CompositionSeries.hasGradedPieces_tprod", "Representation.CompositionSeries.hasGradedPieces_exteriorPower", "Representation.CompositionSeries.constituentsLE_exteriorPower_semisimplification", "Representation.CompositionSeries.constituentsLE_exteriorPower_semisimplification'", "Subrepresentation.exists_subquotient_tprod_equiv", "Representation.nontrivial_piTensorProduct_exteriorPower_iff"]
+++
Suppose $V$ and $V'$ have composition factors $A_1,\ldots,A_t$ and
$B_1,\ldots,B_u$. There is a $W(U_0)$-stable filtration of $V\otimes V'$
with graded pieces $A_a\otimes B_b$, one for each pair $(a,b)$.
There is a $W(U_0)$-stable filtration of $\bigwedge^rV$ with graded pieces

$$
\bigotimes_{a=1}^t\bigwedge^{n_a}A_a,
\qquad 0\le n_a\le\dim A_a,\qquad\sum_an_a=r.
$$

The simple factors of $V\otimes V'$ and $\bigwedge^rV$, counted with
multiplicity, are those of the respective graded pieces. Every graded
piece of $\bigwedge^rV$ displayed above is nonzero.
