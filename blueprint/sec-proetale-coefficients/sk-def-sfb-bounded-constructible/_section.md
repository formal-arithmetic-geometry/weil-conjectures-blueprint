+++
id = "sk-def-sfb-bounded-constructible"
kind = "definition"
title = "Bounded constructible derived category"
order = 866
uses = ["sk-def-sfb-derived-categories", "sk-def-sfb-constructible", "def-weil-abstract-derived-category"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible", "AlgebraicGeometry.ProEtale.BoundedConstructible", "AlgebraicGeometry.ProEtale.mem_boundedConstructible_iff", "AlgebraicGeometry.ProEtale.isTriangulated_boundedConstructible"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive, let $X$ be a scheme, and let $\mathcal R$ be a commutative ring
object of $\Sh(X_{\mathrm{proét}},\mathcal A)$. The *bounded constructible derived
category*
$$
D_{\mathrm{cons}}(X_{\mathrm{proét}},\mathcal R)\subseteq D(\Mod_{\mathcal R})
$$
is the full subcategory of the derived category [sk-def-sfb-derived-categories] of the
complexes $K$ that are bounded, i.e. $H^i(K)=0$ for $i$ outside a finite interval, and
all of whose cohomology sheaves $H^i(K)$ are constructible [sk-def-sfb-constructible].
Morphisms are computed in $D(\Mod_{\mathcal R})$. No derived completeness condition is
imposed. On a topologically Noetherian $X$, $D_{\mathrm{cons}}(X_{\mathrm{proét}},\mathcal R)$
is a triangulated subcategory.
