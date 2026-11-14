+++
id = "dag-sk-def-pbc-conventions"
kind = "dag-definition"
title = "Conventions for proper base change"
name_showing = false
order = 111503
tags = ["sheaf-dag"]
split_from = "definition-classical-pro-etale-sheaves--1"
dag_id = "sk-def-pbc-conventions"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.IsClassicalModuleSheaf", "AlgebraicGeometry.ProEtale.IsClassicalModuleComplex", "CategoryTheory.ringedSiteModules"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
In this section, schemes `def-pc-scheme` are arbitrary unless an additional hypothesis is
stated. The theorem concerns the classical part of
$D^+(T_{\mathrm{proét}},\Lambda)$, for a discrete commutative ring $\Lambda$. Here $T_{\mathrm{proét}}$ is the small pro-étale site `sk-def-pe-site`; its coefficient ring is the constant sheaf $\Lambda_T$ [dag-def-weil-pbc-constant-sheaf], its module sheaves are `def-weil-sheaf-of-modules-category`, and $D^+$ is the bounded below part `def-weil-pbc-bounded-derived-subcategories` of their derived category `def-weil-abstract-derived-category`. Classical means classical cohomology sheaves [dag-sk-def-pe-classical-definition].
The intermediate acyclicity, curve and Chow calculations are made on
$T_{\Et}$, with abelian sheaves or modules over its discrete constant ring `def-weil-pbc-etale-sheaves`. We
write $D^+(T_{\Et},\Lambda)$ for the bounded below derived category `def-weil-pbc-derived-categories`. Inverse
image on these sheaves is denoted by $u^{-1}$; for $u:S\to T$ it is a functor
$\Sh(T_{\Et})\to\Sh(S_{\Et})$, and likewise on module sheaves and
$D^+(T_{\Et},\Lambda)\to D^+(S_{\Et},\Lambda)$. On sheaves of sets, this is the inverse image of `lem-weil-pbc-sets-etale-inverse-image-exact`; on abelian and module sheaves and their bounded below derived categories it is `def-weil-pbc-derived-inverse-image`. It is exact and agrees with
$u^*$ for the constant coefficient rings under consideration `prop-weil-pbc-inverse-image-modules-exact`. The derived
direct image is $Ru_*$ `def-weil-pbc-direct-image`. Torsion always means torsion of the underlying abelian
sheaves `def-weil-pbc-etale-sheaves`.

The proper base change theorem (with proper meaning separated, locally of finite type and universally closed, as in the properness clause of `sk-def-conv`) imposes no invertibility condition on the
torsion coefficients, so a prime $r$ appearing in this section may equal a
residue characteristic. The standing condition on $\ell$ from the introduction
returns with the $\ell$-adic constructible theory.

*Module and abelian cohomology.* Cohomology of a sheaf of $\Lambda$-modules is
canonically the cohomology of its underlying abelian sheaf (Stacks Project,
Tag 03FD), because an injective module sheaf is acyclic for the underlying
section functor on every object of the site. Applying this on the étale
objects over the target gives the same compatibility for $R^qu_*$ and, by
bounded below resolutions, for $Ru_*$. Forgetting the module structure need
not preserve injectives; only acyclicity is used. These cohomology and direct-image comparison assertions are the three clauses of `det-pbc-conventions-module-cohomology`.

(SHEAF DAG node `sk-def-pbc-conventions`; machine-alignment layer.) Split from [definition-classical-pro-etale-sheaves--1]. DAG kind: definition. DAG status: split. Lean names not on master: `AlgebraicGeometry.Scheme`, `AlgebraicGeometry.Scheme.ProEt`, `AlgebraicGeometry.Scheme.ProEt.topology`, `CategoryTheory.constantSheaf`, `DerivedCategory`, `AlgebraicGeometry.IsProper`. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-abstract-derived-category`, `def-weil-pbc-bounded-derived-subcategories`, `def-weil-sheaf-of-modules-category`, `sk-def-conv`, `sk-def-pe-site`.
