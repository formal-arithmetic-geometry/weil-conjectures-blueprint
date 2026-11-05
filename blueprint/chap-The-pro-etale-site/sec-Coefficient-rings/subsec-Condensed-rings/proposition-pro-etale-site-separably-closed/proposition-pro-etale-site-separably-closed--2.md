+++
id = "proposition-pro-etale-site-separably-closed--2"
kind = "proposition"
title = "The pro-étale site of a separably closed field (2)"
name_showing = false
order = 173002
aliases = ["bp-r050-2"]
lean = ["AlgebraicGeometry.ProEtale.isEquivalence_upperStarFromPoint", "AlgebraicGeometry.ProEtale.geometric_field_proetale_evaluation"]
uses = ["definition-small-pro-etale-site"]
+++
Let $\Omega$ be a separably closed field in a fixed universe, and let
$*_{\mathrm{pro}\acute{e}t}$ be the site of profinite sets in that
universe with finite jointly surjective families as covers. Sheaves take
values in the next universe. The inverse image

$$
p_\Omega^*:\Sh(*_{\mathrm{pro}\acute{e}t},\Ab)
\longrightarrow
\Sh((\operatorname{Spec}\Omega)_{\mathrm{pro}\acute{e}t},\Ab)
$$

is an equivalence. Here $p_\Omega^*$ is the composite of inverse image
along $S\mapsto\operatorname{Spec}LC(S,\mathbf Z)$ and inverse image
along $\operatorname{Spec}\Omega\to\operatorname{Spec}\mathbf Z$.

If $\Omega$ is algebraically closed, restriction along
$S\mapsto(\operatorname{Spec}\Omega)[S]$ gives equivalences for sheaves
of sets, abelian groups and rings. The units and counits of the specified
point adjunctions for sets and abelian groups are isomorphisms, and the
canonical map from the singleton test object to the final object
$\operatorname{Spec}\Omega$ is an isomorphism. For every sheaf of rings
$R$ on $(\operatorname{Spec}\Omega)_{\mathrm{pro}\acute{e}t}$,
restriction also gives an equivalence from sheaves of $R$-modules to
modules over the restricted ring sheaf on $*_{\mathrm{pro}\acute{e}t}$.
