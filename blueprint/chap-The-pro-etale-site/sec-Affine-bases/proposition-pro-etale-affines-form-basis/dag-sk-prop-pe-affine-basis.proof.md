+++
kind = "proof"
of = "dag-sk-prop-pe-affine-basis"
tags = ["sheaf-dag"]
uses = ["dag-sk-thm-pe-indetale-refinement", "dag-lem-weil-pbc-ind-etale-basis"]
+++
1. Let $U$ be an object of $X_{\mathrm{proét}}$. Cover $X$ by affine opens and cover their inverse images in $U$ by affine opens. On such a
chart the map is $R\to B$ weakly étale. [dag-sk-thm-pe-indetale-refinement] supplies
$\operatorname{Spec}(B')\to\operatorname{Spec}(B)$ as a single faithfully flat cover, with
$\operatorname{Spec}(B')$ a limit of affine schemes étale over $\operatorname{Spec}(R)$,
hence over $X$. The site comparison lemma gives the equivalence of sheaf categories. This
is Bhatt–Scholze, Lemma 4.2.4. In detail: the affine ind-étale subsite is
[dag-def-weil-pbc-ind-etale-basis], and the covering, finite-refinement and fibre-product
properties together with the equivalence of sheaf categories are
[dag-lem-weil-pbc-ind-etale-basis]. (uses [dag-sk-thm-pe-indetale-refinement], [dag-lem-weil-pbc-ind-etale-basis], `def-weil-pbc-ind-etale-basis`)

Proof dependencies not drawn: `def-weil-pbc-ind-etale-basis`.
