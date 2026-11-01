+++
kind  = "proof"
of    = "lem-weil-derived-tensor-resolution-independent"
+++
Over a ring, a quasi-isomorphism $\alpha:P\to Q$ between K-flat complexes
induces a quasi-isomorphism
$\operatorname{id}_L\otimes\alpha:\operatorname{Tot}(L\otimes P)\to
\operatorname{Tot}(L\otimes Q)$ for every complex $L$: this is Lemma 15.60.12
of the Stacks Project, Tag
[064L](https://stacks.math.columbia.edu/tag/064L), whose proof uses only the
K-flatness [def-weil-derived-tensor] of the two complexes, the existence of
K-flat resolutions (Tag
[06Y4](https://stacks.math.columbia.edu/tag/06Y4)) and the behaviour of
K-flatness under tensoring (Tag
[06Y0](https://stacks.math.columbia.edu/tag/06Y0)). For complexes of
$A_Y$-modules on the small pro-etale site
[def-weil-pbc-proetale-site] the same argument applies: tensor
products, total complexes and truncations are formed termwise in the abelian
category of sheaves of $A_Y$-modules, in which filtered colimits are exact,
and K-flat resolutions exist by the functorial flat-resolution construction.
A morphism $u:P\to P'$ over $K_1$ is a quasi-isomorphism between K-flat
complexes (two out of three), so $u\otimes\operatorname{id}$ is a
quasi-isomorphism by the first part. For the independence, the K-flat
resolutions of $K_1$ form a cofiltered category (Stacks Project,
Definition 15.60.13, Tag
[064M](https://stacks.math.columbia.edu/tag/064M)): any two of them,
$P$ and $P'$, are connected by a roof $P\leftarrow P''\rightarrow P'$ of
K-flat resolutions over $K_1$, and two parallel morphisms of resolutions
are equalized after composing with a further resolution. By the first part
(Tag [064L](https://stacks.math.columbia.edu/tag/064L)) both legs of a roof
become quasi-isomorphisms after $-\otimes_AK_2$, which gives an
isomorphism $P\otimes_AK_2\cong P'\otimes_AK_2$ in $D(Y_{\mathrm{proet}},A)$,
independent of the roof by cofilteredness.
