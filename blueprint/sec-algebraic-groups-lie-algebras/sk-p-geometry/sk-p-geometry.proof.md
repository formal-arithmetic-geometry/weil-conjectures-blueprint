+++
kind  = "proof"
of    = "sk-p-geometry"
+++
Since $G$ is Noetherian, it has finitely many irreducible components. By
[sk-i-cartier], the scheme $G$ is smooth, and since a regular local ring is
a domain, distinct irreducible components of $G$ do not meet. Hence the
irreducible components are open and closed, and they are exactly the
connected components. Multiplication and inversion map the component
containing $1$ to itself, so it is a subgroup, and conjugation preserves
it. Translations identify the other components with its cosets.

Let $f\colon G\to G'$ be a homomorphism. By continuity of multiplication
and inversion, the closure $J$ of its image is a subgroup. Chevalley's
theorem ([Stacks 054K](https://stacks.math.columbia.edu/tag/054K)) says
that $f(G)$ is constructible, and a dense constructible subset contains a
nonempty open subset of its closure. Thus the subgroup $f(G)(L)$ contains
the $L$-points of a nonempty open $U\subseteq J$. Translating $U$ by the
inverse of one of its points in the image, we obtain an open neighbourhood
of $1$ contained in the image, and translating further by points of the
image, we see that the image is open in $J$. Its complement is a union of
cosets of this open subgroup, hence open as well. Therefore the image is
closed, and since it is dense in $J$, it is equal to $J$. For closed
subgroups $G\subseteq\GL(V)$ and $G'\subseteq\GL(W)$, take $J$ with its
reduced structure: since $J\times J$ is reduced and multiplication and
inversion preserve $J(L)$, they restrict to $J$, so $J$ is a closed
subgroup of $G'$, and $f(G(L))=J(L)$.

Next, let $J\subseteq G$ be as in the dimension criterion, with $G$
connected. By the first part, $G$ is irreducible. Since a proper closed
subset of the irreducible variety $G$ has smaller dimension, $J$ and $G$
have the same underlying closed subset. Both are reduced by
[sk-i-cartier], and hence they are equal as schemes.

Finally, let $K\subseteq G\subseteq\GL(V)$ be as in the last assertion.
By Cartier's theorem [sk-i-cartier],
$\dim K=\dim\Lie(K)=\dim\Lie(G)=\dim G$, so $K=G$ by the dimension
criterion.
