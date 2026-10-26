+++
id = "sk-r-linear-library"
kind = "lemma"
title = "Tensor and exterior powers of filtered representations"
lean = ["CompositionSeries.jordan_holder", "Representation.IsIrreducible.bijective_or_eq_zero", "Representation.IsIrreducible.algebraMap_intertwiningMap_bijective_of_isAlgClosed", "Subrepresentation.exists_subquotient_tprod_equiv"]
order = 3733
uses = ["sk-i-restriction"]
tags = ["sketch"]
+++
Suppose $V$ and $V'$ have composition factors $A_1,\ldots,A_t$ and
$B_1,\ldots,B_u$. There is a $W$-stable filtration of $V\otimes V'$ with
graded pieces $A_a\otimes B_b$, one for each pair $(a,b)$. There is a
$W$-stable filtration of $\bigwedge^rV$ with graded pieces

$$
\bigotimes_{a=1}^t\bigwedge\nolimits^{n_a}A_a,
\qquad 0\le n_a\le\dim A_a,\qquad\sum_an_a=r.
$$

The simple factors of $V\otimes V'$ and $\bigwedge^rV$, counted with
multiplicity, are those of the respective graded pieces. Every displayed
exterior-power piece is nonzero.

*Complement.* Composition series exist, and the multiset of their simple
factors does not depend on the series (Jordan–Hölder); in particular these
multisets do not change when $V$ and $V'$ are replaced by their
semisimplifications. The dual of a filtered representation carries the
dual filtration, with the duals of the graded pieces. Schur's lemma: an
endomorphism of a simple representation commuting with the action is zero
or invertible, and over $\overline{\mathbf Q}_\ell$ it is a scalar; in
particular an invertible central element acts on a simple representation
by a nonzero scalar.
