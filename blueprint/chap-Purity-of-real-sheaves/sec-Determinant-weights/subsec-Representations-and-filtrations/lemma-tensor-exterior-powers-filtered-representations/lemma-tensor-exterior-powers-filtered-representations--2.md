+++
id = "lemma-tensor-exterior-powers-filtered-representations--2"
kind = "lemma"
title = "Tensor and exterior powers of filtered representations (2)"
name_showing = false
order = 1124002
aliases = ["bp-r345-2"]
lean = []
uses = ["definition-weil-representation"]
+++
The exterior filtration below is bypassed by Lean; it has no declaration
in the mainline source.

Suppose the Weil representation $V$ has composition factors
$A_1,\ldots,A_t$. There is a $W(U_0)$-stable filtration of
$\bigwedge^rV$ with graded pieces

$$
\bigotimes_{a=1}^t\bigwedge^{n_a}A_a,
\qquad 0\le n_a\le\dim A_a,\qquad\sum_an_a=r.
$$

For the purity argument, Lean forms $V^{\mathrm{ss}}=\bigoplus_a A_a$
and proves that each group element has the same characteristic polynomial
on $V$ and $V^{\mathrm{ss}}$. It then applies the exterior-power weight
theorem directly to the semisimple representation $V^{\mathrm{ss}}$.
This route does not require a filtration of $\bigwedge^rV$ or a comparison
of its simple factors with those of $\bigwedge^rV^{\mathrm{ss}}$.
