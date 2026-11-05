+++
kind = "proof"
of = "lemma-tensor-exterior-powers-filtered-representations"
order = 1128
+++
We construct the two filtrations and then compare simple factors by
the Jordan–Hölder argument. The tensor product is filtered
by the filtration on $V$, and each quotient
$A_a\otimes V'$ by the filtration on $V'$; since tensoring over a
field is exact, the quotients are as asserted.

For the exterior power we cannot simply filter factor by factor,
because a wedge product may use several vectors from the same
composition factor. Instead we sort wedges of basis vectors by how many
vectors they take from each factor, after lifting bases of the
$A_a$ to a basis of $V$ adapted to its filtration. Thus a wedge of basis vectors determines a tuple
$(n_a)$, by counting how many vectors it uses from each lifted basis.
Since the basis is adapted, the group $W(U_0)$ carries a lifted basis vector of $A_a$ into the span of the
lifted bases of $A_1,\ldots,A_a$. Hence the action is block upper triangular:
each term of the image of a basis wedge either has the same tuple or has a
tuple obtained from it by moving some of its vectors to smaller indices $a$.
Choose a total order on the tuples
compatible with these moves. Then the spans of the initial segments of
basis wedges form a stable filtration, and on the quotient indexed by
$(n_a)$ the diagonal blocks act as on
$\bigotimes_a\bigwedge^{n_a}A_a$, a space of dimension
$\prod_a\binom{\dim A_a}{n_a}>0$. For example, for $V$ an extension of $A_2$ by
$A_1$, both of dimension one, and $r=1$, the tuples are $(1,0)$ and
$(0,1)$, and the filtration is the given one. For $r=2$ there is the
single tuple $(1,1)$, and $\bigwedge^2V=A_1\otimes A_2$.

The graded pieces of the filtrations just built need not be simple, so to
compare simple factors we refine. By the Schreier refinement
theorem, any two finite filtrations have refinements with isomorphic
graded pieces, matched by the Zassenhaus isomorphism
$(V_{i-1}+V_i\cap W_j)/(V_{i-1}+V_i\cap W_{j-1})\simeq
(W_{j-1}+W_j\cap V_i)/(W_{j-1}+W_j\cap V_{i-1})$; for two
composition series this is the Jordan–Hölder theorem. Applying the same refinement to a composition series and to the tensor or
exterior filtration, we obtain the statement about simple factors. In
particular, these multisets do not change when $V$ and $V'$ are
replaced by their semisimplifications.
