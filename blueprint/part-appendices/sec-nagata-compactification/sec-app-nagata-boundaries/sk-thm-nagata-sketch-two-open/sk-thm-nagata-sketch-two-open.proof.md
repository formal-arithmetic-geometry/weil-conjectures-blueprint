+++
kind = "proof"
of = "sk-thm-nagata-sketch-two-open"
uses = ["sk-lem-nagata-sketch-graph", "sk-lem-nagata-sketch-boundary", "sk-lem-nagata-sketch-near-closure", "sk-lem-nagata-sketch-common", "lemma-nagata-dense-source-valuative", "lemma-nagata-key-boundary-disjointness", "sk-lem-nagata-sketch-closure"]
+++
The idea is to glue $M$ to each compactification $X_i$ of $M_i$ after
removing from $X_i$ the closure of the part lying over $M\setminus M_i$.
This gives separated schemes $W_i$ containing $M$, and a common
modification combines them into one separated $W$. We check that $W$ is
proper by the valuative criterion. Separating the closures of the
boundaries yields
(A.1), and this implies that every valuation of
$D$ extends into one of the $W_i$.

Choose dense compactifications $M_i\subseteq X_i$. By
Lemma [sk-lem-nagata-sketch-graph], after admissible blow-ups
there are opens $M_i\subseteq V_i\subseteq X_i$ and proper maps
$\psi_i:V_i\to M$ that are isomorphisms above $M_i$.
Put, for $\{i,j\}=\{1,2\}$,

$$
Z_i=M\setminus M_j,\qquad
Z_{i,r}=\psi_i^{-1}(Z_r),\qquad
B_{i,r}=\overline{Z_{i,r}}\subseteq X_i.
$$

The subsets $Z_{i,1},Z_{i,2}$ are disjoint and closed in $V_i$.
Lemma [sk-lem-nagata-sketch-boundary] lets us arrange
$B_{i,1}\cap B_{i,2}=\varnothing$. Subsequent $V_i$-admissible
blow-ups preserve this disjointness.

Let $X_{12}$ be the schematic closure of
$V_1\times_MV_2$ in $X_1\times_SX_2$, with proper projections
$p_i$. Above $V_1$, the first projection is the base change of
$\psi_2$, and hence it is an isomorphism near $Z_{1,2}$. By
Lemma [sk-lem-nagata-sketch-near-closure], after a blow-up it becomes an isomorphism
near $B_{1,2}$. We replace $X_{12}$ by its strict transform, or
equivalently by the closure of the new graph. Since $p_1$ is now an
isomorphism over a neighbourhood of $B_{1,2}$ and $Z_{1,2}$ is dense in
$B_{1,2}$, the inverse image of $Z_{1,2}$ is dense in $p_1^{-1}(B_{1,2})$. The second
projection maps that inverse image into $Z_{2,2}$, and therefore
maps all of $p_1^{-1}(B_{1,2})$ into $B_{2,2}$, which is disjoint
from $B_{2,1}$. Consequently

$$
X_{12}\cap(B_{1,2}\times_SB_{2,1})=\varnothing.
\tag{A.1}
$$

The valuative criterion below relies on this disjointness.

Now we glue

$$
W_i=M\coprod_{M_i}(X_i\setminus B_{i,j}).
$$

We claim that these schemes are separated over $S$. To check this on the
mixed part of the diagonal, suppose that a point of the graph of $M_i$
specializes in $M\times_S(X_i\setminus B_{i,j})$. Since $\psi_i$ is
proper, its graph is closed in $M\times_SX_i$, and so the specialized
point lies in the graph of $\psi_i$, over a point of $V_i$. If its image in $M$ lay in
$M\setminus M_i=Z_j$, the lifted point would lie in
$Z_{i,j}\subseteq B_{i,j}$, contradicting the second coordinate.
Hence the specialization remains in the graph. Since the graph is
an immersion with constructible image, and in the Noetherian situation
a constructible subset that is closed under specialization is closed,
the graph is a closed immersion. This proves separatedness.

Let $R$ be a valuation ring with fraction field $K$, and let
$\operatorname{Spec}(K)\to D$ be an $S$-map over a given
$\operatorname{Spec}(R)\to S$. It extends to both $X_i$, since they are
proper. The pair of extensions factors through $X_{12}$, because the
closure of the graph contains its generic point and
$\operatorname{Spec}(K)$ is schematically dense in
$\operatorname{Spec}(R)$. By
(A.1), the closed point cannot map into
both of the removed closed subsets $B_{1,2}$ and $B_{2,1}$.
Hence, for some $i$, the extension factors through
$X_i\setminus B_{i,j}\subseteq W_i$, because an open containing the
closed point of a local scheme contains the whole scheme.

Next we apply Lemma [sk-lem-nagata-sketch-common] to
$M\subseteq W_i$. This gives a separated $W$ of finite type, covered by
admissible modifications $W_i'$. Since the modification is proper, the
lift of the valuation into $W_i$ lifts further into $W_i'$, and hence
into $W$. Such lifts are unique because $W$ is separated. We now apply the valuative criterion
[Stacks, Tag 0894](https://stacks.math.columbia.edu/tag/0894) in the form that only requires lifts of maps from
$\operatorname{Spec}(K)$ into the dense open $D$, and we conclude that
$W\to S$ is universally closed. Since $W$ is also of finite type and
separated, it is proper over $S$. Its open $M$ yields the desired
compactification, and after taking the schematic closure of $M$ the
compactification is dense. This is [Stacks, Tag 0F40](https://stacks.math.columbia.edu/tag/0F40).
