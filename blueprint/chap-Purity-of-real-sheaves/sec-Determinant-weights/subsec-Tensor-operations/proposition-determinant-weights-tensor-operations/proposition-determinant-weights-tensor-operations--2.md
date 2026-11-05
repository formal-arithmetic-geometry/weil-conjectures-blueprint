+++
id = "proposition-determinant-weights-tensor-operations--2"
kind = "proposition"
title = "Weights of constituents of a semisimple exterior power"
name_showing = false
order = 1145003
aliases = ["bp-r352-2"]
lean = ["Representation.exists_multiset_le_and_detWeight_eq_sum_of_exteriorPower"]
uses = ["definition-determinant-weight", "definition-weil-representation"]
+++
Let $k$ be an algebraically closed field of characteristic zero, $W$ a group,
$\deg:W\to\mathbf Z$ a homomorphism, $\chi:k^\times\to(\mathbf R,+)$ a
homomorphism, and $\gamma\in W$. Let $V\ne0$ be a finite-dimensional
representation with an internal direct-sum decomposition
$V=\bigoplus_{a=1}^t A_a$ into irreducible subrepresentations. Assume that
each $A_a$ has finite geometric determinant, that is, its determinant
character has finite image on $\ker\deg$. Put

$$
\gamma_a=\operatorname{dw}_{\chi,\gamma}(A_a)
=\frac{\chi(\det(\gamma\mid A_a))}{\dim A_a},
$$

and let $L$ be the multiset in which $\gamma_a$ occurs $\dim A_a$ times.
For any $r\ge0$ and any irreducible subquotient $Q=S/U$, with $U<S$, of
$\bigwedge^rV$ having finite geometric determinant, there is a submultiset
$T\le L$ of cardinality $r$ such that

$$
\operatorname{dw}_{\chi,\gamma}(Q)
=\frac{\chi(\det(\gamma\mid Q))}{\dim Q}
=\sum_{x\in T}x.
$$

The degree map need not be surjective, and $\gamma$ need not have degree one.
For a nonzero semisimple Weil representation, with $\chi=\lambda_\iota$
and $\gamma$ of degree one, this gives

$$
\operatorname{DW}(\bigwedge^rV)\subseteq
\bigl\{\sum_an_a\gamma_a:
0\le n_a\le\dim A_a,\ \sum_an_a=r\bigr\}.
$$

The converse and the extension of this identity to a nonsemisimple $V$
are bypassed by the Lean route: the purity proof applies this inclusion
directly to the semisimplification.
