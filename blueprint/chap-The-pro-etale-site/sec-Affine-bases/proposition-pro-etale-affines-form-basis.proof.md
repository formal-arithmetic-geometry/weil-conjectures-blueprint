+++
kind = "proof"
of = "proposition-pro-etale-affines-form-basis"
order = 67
uses = ["lemma-stability", "theorem-pro-etale-refinements-weakly-etale", "proposition-etale-implications", "proposition-pro-etale-coverings--2", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2"]
+++
The first assertion is the refinement theorem applied chart by chart, and
the second is then formal.

Given an object $U$ of $X_{\mathrm{pro}\acute{e}t}$, cover $X$ by affine opens and cover their inverse images in $U$ by
affine opens. These Zariski coverings are pro-étale coverings, so it
suffices to cover each chart. On such a chart the map is a weakly
étale ring map $R\to B$.
By Theorem [theorem-pro-etale-refinements-weakly-etale] there is a single faithfully flat
cover $\operatorname{Spec}(B')\to\operatorname{Spec}(B)$ such that
$\operatorname{Spec}(B')$ is a limit of
affine schemes étale over $\operatorname{Spec}(R)$, hence over
$X$. The equivalence of categories of sheaves follows from the comparison
lemma for sites; see [bhatt-scholze15, Lemma 4.2.4].
