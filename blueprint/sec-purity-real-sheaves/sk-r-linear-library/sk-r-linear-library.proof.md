+++
kind  = "proof"
of    = "sk-r-linear-library"
+++
We construct the two filtrations and then compare simple factors by the
Jordan–Hölder argument. For the tensor product, we first filter by the
filtration on $V$, and then filter each quotient $A_a\otimes V'$ by the
filtration on $V'$. Since tensoring over a field is exact, the quotients
are as asserted.

For the exterior power, lift bases of the $A_a$ to a basis of $V$ adapted
to its filtration. A wedge of basis vectors determines a tuple $(n_a)$, by
counting how many vectors it uses from each lifted basis. The action is
block upper triangular, in the sense that each term of the image of a
basis wedge either has the same tuple or has a tuple obtained from it by
moving some of its vectors to smaller indices $a$, because $W(U_0)$
carries a lifted basis vector of $A_a$ into the span of the lifted bases
of $A_1,\ldots,A_a$. Choose a total order on the tuples compatible with
these moves. Then the spans of the initial segments of basis wedges form a
stable filtration, and on the quotient indexed by $(n_a)$ the diagonal
blocks act as on $\bigotimes_a\bigwedge^{n_a}A_a$. This space has dimension
$\prod_a\binom{\dim A_a}{n_a}>0$.

It remains to compare simple factors. By the Schreier refinement theorem,
any two finite filtrations have refinements with isomorphic graded pieces,
matched by the Zassenhaus isomorphism

$$
\frac{V_{i-1}+V_i\cap W_j}{V_{i-1}+V_i\cap W_{j-1}}\simeq
\frac{W_{j-1}+W_j\cap V_i}{W_{j-1}+W_j\cap V_{i-1}};
$$

applied to two composition series this is the Jordan–Hölder theorem.
Applied to a composition series and to the tensor or exterior filtration,
the same refinement proves the statement about simple factors. In
particular, these multisets do not change when $V$ and $V'$ are replaced
by their semisimplifications.

For the complement, composition series exist by induction on dimension.
The dual filtration is handled by the inverse transpose of a
block-triangular matrix. For Schur's lemma, kernel and image of a
commuting endomorphism are stable, hence trivial or everything; over the
algebraically closed field an eigenvalue $c$ of such an endomorphism gives
a nonzero stable eigenspace, which is the whole space.
