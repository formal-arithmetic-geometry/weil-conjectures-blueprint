+++
kind  = "proof"
of    = "sk-thm-nagata-sketch-two-open"
uses = ["sk-lem-nagata-sketch-graph", "sk-lem-nagata-sketch-boundary", "sk-lem-nagata-sketch-near-closure", "sk-lem-nagata-sketch-common", "lemma-nagata-dense-source-valuative", "lemma-nagata-key-boundary-disjointness", "sk-lem-nagata-sketch-closure"]
+++
*Preparing the two sides* ([lemma-nagata-key-boundary-disjointness]). Choose dense
compactifications $M_i\subseteq X_i$. By [sk-lem-nagata-sketch-graph], after
admissible blow-ups there are opens $M_i\subseteq V_i\subseteq X_i$ and
proper maps $\psi_i:V_i\to M$ which are isomorphisms above $M_i$. Put, for
$\{i,j\}=\{1,2\}$,

$$
Z_i=M\setminus M_j,\qquad
Z_{i,r}=\psi_i^{-1}(Z_r),\qquad
B_{i,r}=\overline{Z_{i,r}}\subseteq X_i .
$$

The subsets $Z_{i,1},Z_{i,2}$ are disjoint and closed in $V_i$.
[sk-lem-nagata-sketch-boundary] lets us arrange
$B_{i,1}\cap B_{i,2}=\varnothing$. Subsequent $V_i$-admissible blow-ups
preserve this disjointness.

*Key disjointness* ([lemma-nagata-key-boundary-disjointness]). Let $X_{12}$
be the schematic closure of $V_1\times_MV_2$ in $X_1\times_SX_2$, with proper
projections $p_i$. Above $V_1$ the first projection is the base change of
$\psi_2$, and is an isomorphism near $Z_{1,2}$.
[sk-lem-nagata-sketch-near-closure] makes it an isomorphism near $B_{1,2}$.
Replace $X_{12}$ by its strict transform, equivalently by the new graph
closure. Since $Z_{1,2}$ is dense in $B_{1,2}$, its inverse image is dense
in $p_1^{-1}(B_{1,2})$. The second projection maps that inverse image into
$Z_{2,2}$, and therefore maps all of $p_1^{-1}(B_{1,2})$ into $B_{2,2}$.
Consequently

$$
X_{12}\cap(B_{1,2}\times_SB_{2,1})=\varnothing. \qquad(\text{KD})
$$

This disjointness (KD) is what makes the valuative criterion work below.

*The two separated candidates.* Glue

$$
W_i=M\coprod_{M_i}(X_i\setminus B_{i,j}).
$$

These schemes are separated over $S$. To check the mixed diagonal, suppose a
point of the graph of $M_i$ specializes in
$M\times_S(X_i\setminus B_{i,j})$. Properness of $\psi_i$ lifts this
specialization to $V_i$. If its image in $M$ lay in $M\setminus M_i=Z_j$,
the lifted point would lie in $Z_{i,j}\subseteq B_{i,j}$, contradicting the
second coordinate. The specialization therefore remains in the graph. That
graph is an immersion with constructible image; in the Noetherian situation
specialization-closed constructible subsets are closed. The graph is thus a
closed immersion, proving separatedness.

*Valuative lifts.* For a valuation ring $R$ with fraction field $K$, an
$S$-map $\operatorname{Spec}(K)\to D$ extends to both proper $X_i$. The pair
of extensions factors through $X_{12}$: the graph closure contains its
generic point, and $\operatorname{Spec}(K)$ is schematically dense in
$\operatorname{Spec}(R)$. By (KD), the closed point cannot land in both
forbidden boundaries $B_{1,2}$ and $B_{2,1}$. For some $i$ the extension
therefore factors through $X_i\setminus B_{i,j}\subseteq W_i$; an open
containing the closed point of a local scheme contains the whole scheme.

*Gluing and properness.* Apply [sk-lem-nagata-sketch-common] to
$M\subseteq W_i$. It gives a separated finite-type $W$, covered by
admissible modifications $W_i'$. The valuation lift into $W_i$ lifts into
$W_i'$ by properness of the modification, hence into $W$. The open $D$ is
dense in $W$, and separatedness supplies uniqueness of valuation lifts. The
dense-source valuative criterion (Stacks 0894;
[lemma-nagata-dense-source-valuative]) now says $W\to S$ is universally
closed. Together with finite type and separatedness, this makes $W$ proper.
Its open $M$ yields the desired compactification; taking the schematic
closure of $M$ makes it dense ([sk-lem-nagata-sketch-closure]). The
construction is also recorded in Stacks 0F40.
