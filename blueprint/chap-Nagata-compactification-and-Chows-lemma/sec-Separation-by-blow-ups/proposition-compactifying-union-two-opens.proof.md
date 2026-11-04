+++
kind = "proof"
of = "proposition-compactifying-union-two-opens"
order = 1453
uses = ["lemma-schematic-closure-uniqueness", "definition-admissible-blow-up", "lemma-making-open-schematically-dense", "definition-strict-transform", "lemma-extending-graph-from-compactification", "lemma-separation-closures", "lemma-extending-isomorphism-over-closure-closed", "lemma-gluing-after-admissible-blow-ups"]
+++
The idea is to glue $M$ to each compactification $X_i$ of $M_i$ after
removing from $X_i$ the closure of the part lying over $M\setminus M_i$.
This gives separated schemes $W_i$ containing $M$, and a common
modification combines them into one separated $W$. We check that $W$ is
proper by the valuative criterion. Separating the closures of the
boundaries, we obtain
(A.1), and from it we deduce that every
valuation of $D$ extends into one of the $W_i$.

*Separating the boundaries.* Since the subsets to be removed from $X_i$ are defined by points of
$M$ outside $M_i$, we must relate each $X_i$ to $M$ itself. Choose dense compactifications $M_i\subseteq X_i$. By
Lemma [lemma-extending-graph-from-compactification], after admissible blow-ups
there are opens $M_i\subseteq V_i\subseteq X_i$ and proper maps
$\psi_i:V_i\to M$ that are isomorphisms above $M_i$.
Put, for $\{i,j\}=\{1,2\}$,

$$
Z_i=M\setminus M_j,\qquad
Z_{i,r}=\psi_i^{-1}(Z_r),\qquad
B_{i,r}=\overline{Z_{i,r}}\subseteq X_i.
$$

The subsets $Z_{i,1},Z_{i,2}$ are disjoint and closed in $V_i$.
By Lemma [lemma-separation-closures], after a further
$V_i$-admissible blow-up we may assume that
$B_{i,1}\cap B_{i,2}=\varnothing$, and subsequent $V_i$-admissible
blow-ups preserve this disjointness.

Let $X_{12}$ be the schematic closure of
$V_1\times_MV_2$ in $X_1\times_SX_2$, with proper projections
$p_i$. Above $V_1$, the first projection is the base change of
$\psi_2$, so it is an isomorphism near $Z_{1,2}$. By
Lemma [lemma-extending-isomorphism-over-closure-closed] it becomes
an isomorphism near $B_{1,2}$ after a blow-up. We replace $X_{12}$ by its strict transform, or
equivalently by the closure of the new graph. Since $p_1$ is now an
isomorphism over a neighbourhood of $B_{1,2}$ and $Z_{1,2}$ is dense in
$B_{1,2}$, the inverse image of $Z_{1,2}$ is dense in $p_1^{-1}(B_{1,2})$. The second
projection maps that inverse image into $Z_{2,2}$. By density it
maps all of $p_1^{-1}(B_{1,2})$ into $B_{2,2}$, which is disjoint
from $B_{2,1}$. This gives the disjointness used in the valuative
argument below:

$$
X_{12}\cap(B_{1,2}\times_SB_{2,1})=\varnothing.
\tag{A.1}
$$

*The separated schemes $W_i$.* We glue

$$
W_i=M\coprod_{M_i}(X_i\setminus B_{i,j}).
$$

We claim that these schemes are separated over $S$. The scheme $W_i$
is covered by $M$ and $X_i\setminus B_{i,j}$, both separated, and they
are glued along $M_i$. It therefore suffices to show that the graph of
the inclusion $M_i\to X_i\setminus B_{i,j}$, which is the mixed part of
the diagonal, is closed in $M\times_S(X_i\setminus B_{i,j})$.

Suppose that a point of the graph of $M_i$ specializes in
$M\times_S(X_i\setminus B_{i,j})$. Since $\psi_i$ is proper, its graph
is closed in $M\times_SX_i$. Hence the specialized point lies in the
graph of $\psi_i$, over a point of $V_i$. If its image in $M$ lay in
$M\setminus M_i=Z_j$, the lifted point would lie in
$Z_{i,j}\subseteq B_{i,j}$, contradicting the second coordinate. So
the specialization remains in the graph. The graph is an immersion with
constructible image, and in the Noetherian situation a constructible
subset that is closed under specialization is closed. Therefore the
graph is a closed immersion, which proves separatedness.

*Valuations of $D$.* For properness we use the valuative criterion, and we show first that
every valuation of $D$ extends into one of the $W_i$.
Let $R$ be a valuation ring with fraction field $K$, and let
$\operatorname{Spec}(K)\to D$ be an $S$-map over a given
$\operatorname{Spec}(R)\to S$. It extends to both $X_i$, since they are
proper. The pair of extensions factors through $X_{12}$, because the
closure of the graph contains its generic point and
$\operatorname{Spec}(K)$ is schematically dense in
$\operatorname{Spec}(R)$. By
(A.1), the closed point cannot map into
both of the removed closed subsets $B_{1,2}$ and $B_{2,1}$.
Choose $i$ such that the closed point does not map into $B_{i,j}$. An open containing
the closed point of a local scheme contains the whole scheme, so the
extension factors through $X_i\setminus B_{i,j}\subseteq W_i$.

*Gluing and properness.*
Lemma [lemma-gluing-after-admissible-blow-ups], applied to
$M\subseteq W_i$, gives a separated $W$ of finite type, covered by
admissible modifications $W_i'$. Since the modification is proper, the
lift of the valuation into $W_i$ lifts further into $W_i'$, hence
into $W$. Such lifts are unique because $W$ is separated. The valuative
criterion [Stacks, [0894](https://stacks.math.columbia.edu/tag/0894)], in the form that only requires lifts of maps
from $\operatorname{Spec}(K)$ into the dense open $D$, then shows that
$W\to S$ is universally closed. As $W$ is also of finite type and
separated, it is proper over $S$. Its open $M$ yields the desired
compactification, which becomes dense after we take the schematic
closure of $M$. This is [Stacks, [0F40](https://stacks.math.columbia.edu/tag/0F40)].
