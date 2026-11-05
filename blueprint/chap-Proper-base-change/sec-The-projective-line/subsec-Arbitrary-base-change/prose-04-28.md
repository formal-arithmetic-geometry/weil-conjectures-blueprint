+++
id = "prose-04-28"
kind = "hidden"
title = "Arbitrary base change"
order = 379
+++
Let $\pi:\mathbf P^1_S\to S$ be the projection and $\bar s$ a geometric
point of $S$. The stalk of $R^q\pi_*F$ at $\bar s$ is the cohomology of
$\mathbf P^1$ over the strict localization at $\bar s$, by
(4.12) below. By
Proposition [proposition-cohomology-p-1-over-henselian] it is therefore
the cohomology of $\mathbf P^1_{k_s}$, where $k_s$ is the separably
closed residue field. Along a base change $g:T\to S$ the residue field
grows from $k_s$ to $k_t$, so on stalks the base change map becomes the
pullback from $\mathbf P^1_{k_s}$ to $\mathbf P^1_{k_t}$, which is an
isomorphism by Lemma [lemma-extension-separably-closed-ground-field].
This is the second place where properness enters: for $\mathbf A^1$ and
$p$-torsion coefficients the corresponding map is not surjective.

The stalk formula holds for every
quasi-compact quasi-separated morphism $f:Z\to S$. For a geometric point $\bar s$ of $S$ and an abelian sheaf
$G$ on $Z_{\acute{e}t}$ we have

$$
(R^qf_*G)_{\bar s}
\simeq H^q(Z\times_SS_{(\bar s)},G|),\qquad
S_{(\bar s)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}.
\tag{4.12}
$$

Indeed, the stalk is the filtered
colimit of $H^q(Z\times_SV,G|)$ over pointed étale neighbourhoods
$(V,\bar v)$ of $\bar s$, and by continuity of étale cohomology this
colimit is the cohomology of the indicated limit scheme
[Stacks, [03Q9](https://stacks.math.columbia.edu/tag/03Q9)].
