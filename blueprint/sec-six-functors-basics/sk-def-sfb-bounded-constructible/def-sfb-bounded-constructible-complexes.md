+++
id = "def-sfb-bounded-constructible-complexes"
kind = "definition"
title = "Bounded constructible complexes"
order = 1638
uses = ["sk-def-sfb-derived-categories", "sk-def-sfb-constructible", "def-weil-abstract-derived-category"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible", "AlgebraicGeometry.ProEtale.BoundedConstructible"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive, let $X$ be a scheme, and let $\mathcal R$ be a commutative ring
object of $\Sh(X_{\mathrm{proét}},\mathcal A)$. A complex
$K\in D(\Mod_{\mathcal R})$ [sk-def-sfb-derived-categories] is *bounded constructible* if
it is bounded for the canonical t-structure and every cohomology sheaf $H^n(K)$,
$n\in\mathbf Z$, is constructible [sk-def-sfb-constructible]. The *bounded constructible
derived category* $D_{\mathrm{cons}}(X_{\mathrm{proét}},\mathcal R)$ is the full
subcategory of $D(\Mod_{\mathcal R})$ on the bounded constructible complexes.
