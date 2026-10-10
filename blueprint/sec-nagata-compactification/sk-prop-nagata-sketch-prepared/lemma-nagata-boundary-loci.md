+++
id = "lemma-nagata-boundary-loci"
kind = "lemma"
title = "Closedness and disjointness of the four boundary loci"
order = 267
lean = ["AlgebraicGeometry.TwoOpenSide.closure_image_preimage_inter"]
uses = ["def-nagata-two-open-boundary-loci", "def-nagata-two-open-graph-extensions", "lemma-nagata-graph-extension"]
+++
The subsets $Z_i$ are closed in $U$ and contained in $U_i$. Each $Z_{i,k}$
is closed in $V_i$; equivalently, its closure $\overline Z_{i,k}$ in $X_i$
satisfies $\overline Z_{i,k}\cap V_i=Z_{i,k}$. The sets $Z_{i,1}$ and
$Z_{i,2}$ are disjoint, and $\psi_i$ is an isomorphism over an open
neighbourhood of $Z_i$.

## Proof

The set $Z_i=U\setminus U_j$ is closed in $U$, and it is contained in $U_i$
because $U=U_i\cup U_j$. Since $\psi_i$ is continuous, each
$Z_{i,k}=\psi_i^{-1}(Z_k)$ is closed in $V_i$. As $V_i$ is open in $X_i$,
write $Z_{i,k}=C\cap V_i$ with $C$ closed in $X_i$; then
$\overline Z_{i,k}\subseteq C$, so
$\overline Z_{i,k}\cap V_i\subseteq C\cap V_i=Z_{i,k}$, and the reverse
inclusion is clear. The sets $Z_i$ and $Z_j$ are disjoint because
$(U\setminus U_j)\cap(U\setminus U_i)=U\setminus(U_i\cup U_j)=\varnothing$;
their inverse images in $V_i$ are consequently disjoint. Finally,
$Z_i\subseteq U_i$, and by [def-nagata-two-open-graph-extensions] the map
$\psi_i^{-1}(U_i)\to U_i$ is an isomorphism. This gives the required
isomorphism on the open neighbourhood $U_i$ of $Z_i$.
