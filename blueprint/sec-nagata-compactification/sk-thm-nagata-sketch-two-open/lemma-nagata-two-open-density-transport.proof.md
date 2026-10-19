+++
kind  = "proof"
of    = "lemma-nagata-two-open-density-transport"
uses = ["def-nagata-two-open-boundary-loci", "lemma-nagata-boundary-loci", "lemma-nagata-intermediate-separated", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-two-open-final-modification"]
+++
*Density in $W_i$.* The scheme $W_i$ is covered by the opens $U$ and
$X_i^\circ=X_i\setminus\overline Z_{i,j}$. The copy of $U_i$ is dense in
$X_i$ and contained in the open $X_i^\circ$, hence dense in $X_i^\circ$.
Since $U_i\subseteq U$, every nonempty open of $W_i$ meets $U$: either it
meets the open $U$ directly, or it meets $X_i^\circ$ in a nonempty open,
which meets $U_i$.

*Density in $W$.* Let $\pi\colon W'_i\to W_i$ be the $U$-admissible blow-up
with center $V(\mathcal I)$ disjoint from $U$. By
[lemma-nagata-admissible-blowup-preserves-density] the inverse image of
$W_i\setminus V(\mathcal I)$ is dense in $W'_i$, and $\pi$ is an isomorphism
over $W_i\setminus V(\mathcal I)$. As $U$ is dense in the open
$W_i\setminus V(\mathcal I)$, its inverse image is dense in
$\pi^{-1}(W_i\setminus V(\mathcal I))$ and hence in $W'_i$; this inverse
image is the copy of $U$ in $W'_i$. The two opens $W'_1,W'_2$ cover $W$ and
the two copies of $U$ agree in $W$, so every nonempty open of $W$ meets
$U$.

*The final modification.* The intermediate schemes $W_i$ are of finite
type over the Noetherian scheme $S$ by
[lemma-nagata-intermediate-separated], hence Noetherian, and the final
common modification is a common modification of $W_1,W_2$ along $U$ by
[lemma-nagata-two-open-final-modification].
