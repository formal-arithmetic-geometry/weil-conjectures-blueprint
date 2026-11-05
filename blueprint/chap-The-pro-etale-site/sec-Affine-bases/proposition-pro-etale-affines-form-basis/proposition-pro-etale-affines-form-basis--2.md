+++
id = "proposition-pro-etale-affines-form-basis--2"
kind = "proposition"
title = "Pro-étale affines form a basis (2)"
name_showing = false
order = 66003
aliases = ["bp-r015-2"]
lean = ["AlgebraicGeometry.Scheme.AffineProEt", "AlgebraicGeometry.Scheme.AffineProEt.instFaithfulProEtToProEt", "AlgebraicGeometry.Scheme.AffineProEt.instFullProEtToProEt", "AlgebraicGeometry.Scheme.AffineProEt.isEquivalence_sheafPushforwardContinuous_toProEt", "AlgebraicGeometry.Scheme.AffineProEt.toProEt", "AlgebraicGeometry.Scheme.AffineProEt.topology"]
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "definition-small-pro-etale-site--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "proposition-w-local-components--1", "example-locally-constant-functions-w-local--1"]
+++
The pro-étale affines over $X$, with all $X$-morphisms, form a full
subcategory $X^{\mathrm{aff}}_{\mathrm{pro}\acute{e}t}$ of $X_{\mathrm{pro}\acute{e}t}$. Equip it
with the topology restricted from $X_{\mathrm{pro}\acute{e}t}$.

Let $X$ be a scheme in universe $u$, and let $\mathcal A$ be a category
admitting limits indexed by categories whose objects lie in universe
$u+1$ and whose morphisms lie in universe $u$. Restriction induces an
equivalence between $\mathcal A$-valued sheaves on
$X_{\mathrm{pro}\acute{e}t}$ and $\mathcal A$-valued sheaves on
$X^{\mathrm{aff}}_{\mathrm{pro}\acute{e}t}$. In particular, this applies to sets and abelian groups
in universe $u+1$.
