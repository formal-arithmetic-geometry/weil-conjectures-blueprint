+++
kind = "proof"
of = "lemma-cohomology-multiplicative-group--8"
order = 1576017
uses = ["definition-small-pro-etale-site--1"]
+++
The divisor sequence is a short exact sequence

$$
0\longrightarrow\mathbf G_m\longrightarrow i_*i^*\mathbf G_m
\longrightarrow\bigoplus_{x\in X^{(1)}}i_{x,*}\mathbf Z\longrightarrow0,
$$

where $X^{(1)}$ denotes the points of codimension one and
$i_x:\operatorname{Spec}(\kappa(x))\to X$.
Each point sheaf $i_{x,*}\mathbf Z$ has vanishing $H^1$, by the
injective degree-one Leray edge map and the vanishing of
$H^1(\operatorname{Spec}(\kappa(x)),\mathbf Z)$. The same vanishing holds
for their direct sum: by quasi-compactness, the differences of local
lifts involve only finitely many of the point sheaves. Hence the long
exact sequence makes
$H^2(X,\mathbf G_m)\to H^2(X,i_*i^*\mathbf G_m)$ injective.

The degree-two Leray edge map from the latter group to
$H^2(\operatorname{Spec}(k(X)),i^*\mathbf G_m)$ is injective as well.
Indeed, embed $i^*\mathbf G_m$ in an injective sheaf. On the generic
fibres of affine étale $X$-schemes, Hilbert 90 lifts sections of its
cokernel to the injective sheaf. Thus $i_*$ takes the cokernel map to
an epimorphism. The composite of the two injections is the asserted
pullback map.
