+++
kind  = "proof"
of    = "sk-r-linear-library"
+++
For the tensor product, we first filter by the filtration on $V$, and then
filter each quotient $A_a\otimes V'$ by the filtration on $V'$. Since
tensoring over a field is exact, the quotients are as asserted.

For the exterior power, lift bases of the $A_a$ to a basis of $V$ adapted
to its filtration. A wedge of basis vectors determines a tuple $(n_a)$, by
counting how many vectors it uses from each lifted basis. The action is
block upper triangular, in the sense that each term of the image of a
basis wedge either has the same tuple or has one index replaced by a
smaller one. Choose a total order on the tuples compatible with these
moves. Then the spans of the initial segments of basis wedges form a
stable filtration, and on the quotient indexed by $(n_a)$ the diagonal
blocks act as on $\bigotimes_a\bigwedge^{n_a}A_a$. This space has dimension
$\prod_a\binom{\dim A_a}{n_a}>0$.

Composition series exist by induction on dimension, and their multisets of
simple factors do not depend on the series. To see this, let $V_i$ and
$W_j$ be two filtrations, and refine the first by $V_{i-1}+(V_i\cap W_j)$
and the second by $W_{j-1}+(W_j\cap V_i)$. The two quotients indexed by
$(i,j)$ are both naturally isomorphic to

$$
\frac{V_i\cap W_j}{(V_{i-1}\cap W_j)+(V_i\cap W_{j-1})}
$$

by the isomorphism $(U+V)/V\simeq U/(U\cap V)$. Applied to two composition
series, this refinement proves the Jordan–Hölder assertion. Applied to a
composition series and to the tensor or exterior filtration, it proves the
statement about simple factors. In particular, these multisets do not
change when $V$ and $V'$ are replaced by their Weil semisimplifications.

The dual filtration is handled by the inverse transpose of a
block-triangular matrix. For Schur's lemma, kernel and image of a
commuting endomorphism are stable, hence trivial or everything; over the
algebraically closed field an eigenvalue $c$ of such an endomorphism gives
a nonzero stable eigenspace, which is the whole space.
