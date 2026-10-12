+++
id = "def-pur-proetale-structure-sheaf"
kind = "definition"
title = "The structure sheaf of rings on the small pro-etale site"
uses = ["def-weil-pbc-small-proetale-site"]
tags = ["stacks-03P4"]
+++
Let $S$ be a scheme and $S_{\mathrm{proet}}$ its small pro-etale site
[def-weil-pbc-small-proetale-site]. The *structure sheaf* $\mathcal O_S$ on
$S_{\mathrm{proet}}$ is the presheaf of commutative rings

$$
 \mathcal O_S(U)=\Gamma(U,\mathcal O_U)\qquad(U\to S\text{ weakly etale}),
$$

whose restriction map along a morphism $h:V\to U$ over $S$ is the ring map
$h^\sharp:\Gamma(U,\mathcal O_U)\to\Gamma(V,\mathcal O_V)$ on global sections. It is a
sheaf of rings on $S_{\mathrm{proet}}$: as a presheaf of sets it is isomorphic to
$U\mapsto\operatorname{Mor}(U,\operatorname{Spec}\mathbf Z[t ])$ (a morphism to
$\operatorname{Spec}\mathbf Z[t ]$ is a ring map $\mathbf Z[t ]\to\Gamma(U,\mathcal O_U)$,
i.e. a global section), hence it is representable on schemes and satisfies the sheaf
condition for fpqc coverings; the coverings of $S_{\mathrm{proet}}$ are fpqc coverings,
and the sheaf condition for a presheaf of rings is that of its underlying presheaf of
sets.
