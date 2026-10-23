+++
kind  = "proof"
of    = "lem-pc-higher-direct-image-derived-model"
+++
Take $E=Rf_*(\mathcal F[0])$, computed by an injective resolution of
$\mathcal F$ in degrees $\ge0$. Then $E$ has no cohomology in negative
degrees, and $H^q(E)$ is the $q$-th right derived functor of $f_*$ at
$\mathcal F$, that is $R^qf_*\mathcal F$; this gives (a) and (b).

For (c), let $c$ be the comparison map from $Lg'^*(\mathcal F[0])$ to
$g'^*\mathcal F[0]$. The canonical base-change map
$Lg^*Rf_*(\mathcal F[0])\to Rf'_*(Lg'^*\mathcal F[0])$ followed by
$Rf'_*(c)$ is an isomorphism in $D(\mathcal O_{T'})$ by
[lem-pc-relatively-flat-canonical-module-base-change], since $f$ is proper, hence
quasi-compact and separated, and $\mathcal F$ is flat over $T$ (Stacks,
Tag 0A1D, and Tag 0B91 (2)); here $c$ is itself an isomorphism, by the
same lemma. Taking $H^q$ and applying (b) on $X'$ to the module
$g'^*\mathcal F$ gives $H^q(Lg^*E)\cong R^qf'_*(g'^*\mathcal F)$.
