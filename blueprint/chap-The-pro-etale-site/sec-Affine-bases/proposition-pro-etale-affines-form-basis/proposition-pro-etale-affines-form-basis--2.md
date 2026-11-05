+++
id = "proposition-pro-etale-affines-form-basis--2"
kind = "proposition"
title = "Pro-étale affines form a basis (2)"
name_showing = false
order = 66002
aliases = ["bp-r015-2"]
lean = ["AlgebraicGeometry.Scheme.AffineProEt", "AlgebraicGeometry.Scheme.AffineProEt.toProEt", "AlgebraicGeometry.Scheme.AffineProEt.instFullProEtToProEt", "AlgebraicGeometry.Scheme.AffineProEt.instFaithfulProEtToProEt", "AlgebraicGeometry.Scheme.AffineProEt.topology", "AlgebraicGeometry.Scheme.AffineProEt.isEquivalence_sheafPushforwardContinuous_toProEt"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site"]
+++
The pro-étale affines over $X$, with all $X$-morphisms, form a full
subcategory $\affproet{X}$ of $X_{\mathrm{pro}\acute{e}t}$. Equip it
with the topology restricted from $X_{\mathrm{pro}\acute{e}t}$.

Let $X$ be a scheme in universe $u$, and let $\mathcal A$ be a category
admitting limits indexed by categories whose objects lie in universe
$u+1$ and whose morphisms lie in universe $u$. Restriction induces an
equivalence between $\mathcal A$-valued sheaves on
$X_{\mathrm{pro}\acute{e}t}$ and $\mathcal A$-valued sheaves on
$\affproet{X}$. In particular, this applies to sets and abelian groups
in universe $u+1$.
