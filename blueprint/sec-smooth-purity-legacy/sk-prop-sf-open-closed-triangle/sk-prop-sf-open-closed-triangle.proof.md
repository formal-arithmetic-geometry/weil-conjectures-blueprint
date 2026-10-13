+++
kind  = "proof"
of    = "sk-prop-sf-open-closed-triangle"
uses = ["sk-def-sf-operations"]
+++
*The sequence is a complex, naturally in $F$.* Both maps are components of
natural transformations (the counit of $j_!\dashv j^*$ and the unit of
$i^*\dashv i_*$), so the sequence is natural in $F$. For the composite to
vanish only the disjointness of the images of $j$ and $i$ is needed: $j^*i_*G=0$
for every sheaf $G$ on $Z_{\Et}$, since an étale $V\to U$ has
$V\times_XZ=\emptyset$. By adjunction
$\operatorname{Hom}(j_!j^*F,i_*i^*F)\cong\operatorname{Hom}(j^*F,j^*i_*i^*F)=0$,
so the composite $j_!j^*F\to F\to i_*i^*F$ is zero.

*Short exactness.* The functors $j^*$ and $i^*$ are exact, and because the
images of $j$ and $i$ cover $X$ they jointly reflect isomorphisms: every
geometric point of $X$ factors through $U$ or through $Z$, and geometric stalks
are conservative for sheaves with values in $\mathcal A$ (this is where the
concreteness of $\mathcal A$, compatibly with filtered colimits and
sheafification, is used). Hence a complex of sheaves on $X_{\Et}$ is short exact
as soon as its images under $j^*$ and under $i^*$ are, and it suffices to check
the two restrictions.

Over $U$: the third term $j^*i_*i^*F$ vanishes as above, and the first map
$j^*j_!j^*F\to j^*F$ is an isomorphism, since the unit
$\mathrm{id}\to j^*j_!$ is an isomorphism ($j$ is an open immersion) and the
triangle identity exhibits $j^*$ of the counit as its inverse. So the
restricted sequence is $0\to j^*F\xrightarrow{\sim}j^*F\to0\to0$, which is
short exact.

Over $Z$: the first term $i^*j_!j^*F$ vanishes, since the stalks of $j_!G$ at
geometric points outside the image of $j$ are zero. The map
$i^*F\to i^*i_*i^*F$ is $i^*$ of the unit; by the triangle identity it is a
section of the counit $i^*i_*i^*F\to i^*F$, which is an isomorphism because
$i_*$ is fully faithful for a closed immersion (on geometric stalks,
$(i_*G)_{\bar z}=G_{\bar z}$ for $\bar z$ over $Z$). So the restricted sequence is
$0\to0\to i^*F\xrightarrow{\sim}i^*i_*i^*F\to0$, which is short exact.

Hence the sequence is short exact. For $F=\Lambda_X$ it reads
$0\to j_!\Lambda_U\to\Lambda_X\to i_*\Lambda_Z\to0$, since
$j^*\Lambda_X=\Lambda_U$ and $i^*\Lambda_X=\Lambda_Z$.
This is the elementary sheaf sequence used in SGA 5, III, proof of 1.7.4.
