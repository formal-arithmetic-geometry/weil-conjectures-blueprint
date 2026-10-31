+++
id = "prose-04-18"
kind = "hidden"
title = "Geometric stalks and arbitrary base change"
order = 210
+++
We now have the comparison of $\mathbf P^1_R$ with its closed fibre for
every henselian local ring $R$ (Proposition [sk-prop-pbc-p1-henselian]), and
it remains to turn it into proper base change for
$\pi:\mathbf P^1_S\to S$. The stalk of $R^q\pi_*F$ at a geometric point
$\bar s$ is the cohomology of $\mathbf P^1$ over the strict localization
at $\bar s$, hence, by the proposition, the cohomology of
$\mathbf P^1_{k_s}$ with $k_s$ the separably closed residue field. Along
a base change $g:T\to S$ the residue field grows from $k_s$ to $k_t$,
so the base change map on stalks becomes the pullback from
$\mathbf P^1_{k_s}$ to $\mathbf P^1_{k_t}$, which is an isomorphism by
Lemma [sk-cor-curve-invariance]. Here properness enters a second
time, since for $\mathbf A^1$ and $p$-torsion coefficients the
corresponding map is not surjective.

Proposition [sk-prop-pbc-p1-henselian] enters through the stalks of higher direct
images. For a quasi-compact quasi-separated morphism $f:Z\to S$, a
geometric point $\bar s$ of $S$, and an abelian sheaf $G$ on $Z_{\acute{e}t}$,

$$
(R^qf_*G)_{\bar s}
\simeq H^q(Z\times_SS_{(\bar s)},G|),\qquad
S_{(\bar s)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}.
\tag{4.11}
$$

Indeed, the stalk is the filtered
colimit of $H^q(Z\times_SV,G|)$ over pointed étale neighbourhoods
$(V,\bar v)$ of $\bar s$, and by continuity of étale cohomology this
colimit is the cohomology of the indicated limit scheme
[Stacks, Tag 03Q9](https://stacks.math.columbia.edu/tag/03Q9).
