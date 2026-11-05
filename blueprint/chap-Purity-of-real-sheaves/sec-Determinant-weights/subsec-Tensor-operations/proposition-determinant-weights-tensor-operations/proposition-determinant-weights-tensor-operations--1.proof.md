+++
kind = "proof"
of = "proposition-determinant-weights-tensor-operations--1"
order = 1145005
uses = ["lemma-tensor-exterior-powers-filtered-representations", "proposition-central-element-arithmetic-monodromy-group", "lemma-determinant-weight-from-central-scalar", "corollary-determinant-weights"]
+++
By the tensor subquotient assertion of
[lemma-tensor-exterior-powers-filtered-representations], implemented by
`Subrepresentation.exists_subquotient_tprod_equiv`, $Q$ is equivalent to a
subquotient of $A\otimes B$ for irreducible subquotients $A$ of $V$ and $B$
of $V'$. Intersecting the denominator with the numerator gives a quotient
by a proper subrepresentation. Determinant weights and finiteness of the
geometric determinant are preserved by this equivalence.

Apply `Representation.detWeight_subquotient_tprod_eq_add`. If $\deg=0$,
finite geometric determinant makes all three weights zero. Otherwise divide
the image of $\deg$ by its positive generator to obtain a surjective degree
map with the same kernel, and write $\gamma=u\delta^m$ with $u\in\ker\deg$
and $\delta$ of degree one for the new map. The weights at $\gamma$ are $m$
times the weights at $\delta$.

For this degree datum, $A\oplus B$ is semisimple, so
[proposition-central-element-arithmetic-monodromy-group] supplies a positive
central pair $(N,z)$. Its scalars on $A$ and $B$ are $c$ and $d$. Transport
the pair to $(A\oplus B)\otimes(A\oplus B)$ and use its surjection onto
$A\otimes B$; the induced scalar is $cd$. Applying
[lemma-determinant-weight-from-central-scalar] to the preimage of the
subquotient gives

$$
\operatorname{dw}_{\chi,\delta}(Q)
=\frac{\chi(cd)}{N}
=\frac{\chi(c)}{N}+\frac{\chi(d)}{N}.
$$

Scale by $m$ and transport back to $Q$. In the Weil setting,
[corollary-determinant-weights] supplies the finite geometric determinants
of the lisse subquotients, giving the displayed inclusion.
