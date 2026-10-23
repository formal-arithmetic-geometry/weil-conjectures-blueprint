+++
id = "sk-thm-pe-indetale-refinement"
kind = "theorem"
title = "Pro-étale refinements of weakly étale maps"
order = 947
lean = ["Algebra.WeaklyEtale.exists_indEtale", "RingHom.WeaklyEtale.exists_indEtale_comp"]
uses = ["sk-def-pe-morphisms", "sk-lem-pe-weakly-etale-stability", "sk-thm-pe-wc-cover"]
tags = ["sketch"]
+++
If $R\to B$ is weakly étale [sk-def-pe-morphisms], there is a faithfully flat ind-étale map
$B\to B'$ such that $R\to B'$ is ind-étale.

Objects of $X_{\mathrm{proét}}$ are weakly étale, while the covers of [sk-thm-pe-wc-cover]
are ind-étale. This theorem bridges the two: it is the reason a site defined by weakly étale
morphisms can be computed with inverse limits of étale affines.
