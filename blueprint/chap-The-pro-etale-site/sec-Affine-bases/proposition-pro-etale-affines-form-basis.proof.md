+++
kind = "proof"
of = "proposition-pro-etale-affines-form-basis"
order = 67
uses = ["proposition-etale-implications", "lemma-stability", "theorem-pro-etale-refinements-weakly-etale"]
+++
The first assertion is the [refinement theorem](@theorem-pro-etale-refinements-weakly-etale) applied chart by chart, and
the second is then formal.

Given an object $U$ of [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site), cover $X$ by affine opens and cover their inverse images in $U$ by
affine opens. These Zariski coverings are [pro-étale coverings](@definition-small-pro-etale-site), so it
suffices to cover each chart. On such a chart the map is a [weakly
étale](@definition-ind-etale-pro-etale-weakly) ring map $R\to B$.
By Theorem [theorem-pro-etale-refinements-weakly-etale] there is a single faithfully flat
cover $\operatorname{Spec}(B')\to\operatorname{Spec}(B)$ such that
$\operatorname{Spec}(B')$ is a limit of
affine schemes étale over $\operatorname{Spec}(R)$, hence over
$X$. The equivalence of categories of sheaves follows from the comparison
lemma for sites; see [bhatt-scholze15, Lemma 4.2.4].
