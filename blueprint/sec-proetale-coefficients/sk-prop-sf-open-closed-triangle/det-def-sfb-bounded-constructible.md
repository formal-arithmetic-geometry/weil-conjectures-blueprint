+++
id = "det-def-sfb-bounded-constructible"
kind = "definition"
title = "Bounded constructible derived category"
order = 1196
uses = ["det-def-sfb-derived-categories", "def-sfb-constructible-module", "def-weil-abstract-derived-category"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible", "AlgebraicGeometry.ProEtale.BoundedConstructible", "AlgebraicGeometry.ProEtale.mem_boundedConstructible_iff", "AlgebraicGeometry.ProEtale.isTriangulated_boundedConstructible"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive, let $X$ be a scheme, and let $\mathcal R$ be a commutative ring
object of $\Sh(X_{\mathrm{proét}},\mathcal A)$. The *bounded constructible derived
category*
$$
D_{\mathrm{cons}}(X_{\mathrm{proét}},\mathcal R)\subseteq D(\Mod_{\mathcal R})
$$
is the full subcategory of the derived category [det-def-sfb-derived-categories] of the
complexes $K$ that are bounded, i.e. $H^i(K)=0$ for $i$ outside a finite interval, and
all of whose cohomology sheaves $H^i(K)$ are constructible [def-sfb-constructible-module].
Morphisms are computed in $D(\Mod_{\mathcal R})$. No derived completeness condition is
imposed. On a topologically Noetherian $X$ and for $\mathcal R=\Lambda_X$ pulled back from
one of the condensed rings $\underline E$, $\underline{\cO}_E$, $\underline{\Qlb}$ ($E$ a
finite extension of $\mathbf Q_\ell$) or $\underline T$ ($T$ a finite ring killed by a
power of $\ell$), $D_{\mathrm{cons}}(X_{\mathrm{proét}},\Lambda_X)$ is a triangulated
subcategory; for a general $\mathcal R$ it need not be closed under cones.
