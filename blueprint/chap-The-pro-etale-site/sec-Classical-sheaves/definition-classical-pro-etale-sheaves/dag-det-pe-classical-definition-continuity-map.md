+++
id = "dag-det-pe-classical-definition-continuity-map"
kind = "dag-definition"
title = "The continuity map and classical sheaves, in detail"
name_showing = false
order = 111501
tags = ["sheaf-dag"]
split_from = "definition-classical-pro-etale-sheaves--1"
dag_id = "det-pe-classical-definition-continuity-map"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.AffinePresentation", "AlgebraicGeometry.ProEtale.sectionDiagram", "AlgebraicGeometry.ProEtale.sectionCocone", "AlgebraicGeometry.ProEtale.continuityMap", "AlgebraicGeometry.ProEtale.continuityMap_natural", "AlgebraicGeometry.ProEtale.IsClassical", "AlgebraicGeometry.ProEtale.isClassical_iso_iff", "AlgebraicGeometry.ProEtale.moduleSectionPresheaf", "AlgebraicGeometry.ProEtale.moduleContinuityMap", "AlgebraicGeometry.ProEtale.IsClassicalModule", "AlgebraicGeometry.ProEtale.isClassicalModule_iff", "AlgebraicGeometry.ProEtale.IsClassicalComplex"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $X$ be a scheme and $F$ a sheaf of sets on $X_{\Proet}$ [dag-def-weil-pbc-proetale-site]. Use the universes of `def-weil-size-convention`; all index categories below are small in the universe in which the colimits are formed `def-weil-pbc-category-colimit`. For module coefficients, fix a discrete commutative ring $\Lambda$ and its constant sheaf $\Lambda_X$, as in [dag-def-weil-pbc-proetale-site]; module sheaves have the meaning of `def-weil-sheaf-of-modules-category`.

1. **Presentations.** A *pro-étale affine presentation* is an affine object $U$ of $X_{\Proet}$, a small cofiltered category $I$, a diagram $i\mapsto U_i$ of affine schemes étale over $X$, and a specified isomorphism $U\cong\varprojlim_{i\in I}U_i$ of $X$-schemes, as in [dag-sk-def-pe-morphisms]. For an arrow $a:j\to i$ write $u_a:U_j\to U_i$, and write $u_i:U\to U_i$ for the projections. The $U_i$ are objects of $X_{\Proet}$ because étale morphisms are weakly étale `det-pe-morphisms-etale-comparison`; the $u_a$ and $u_i$ are morphisms of that site.
2. **The continuity map.** The restriction maps $F(u_a):F(U_i)\to F(U_j)$ form a filtered diagram indexed by $I^{\mathrm{op}}$. The compatible maps $F(u_i)$ induce the unique map
$$c_{F,(U_i)}:\varinjlim_{i\in I^{\mathrm{op}}}F(U_i)\longrightarrow F(U),\qquad [i,s]\longmapsto F(u_i)(s).$$
It is natural in $F$. The notation retains the presentation, since the source of the map depends on that presentation.
3. **Classical sheaves.** $F$ is *classical* if $c_{F,(U_i)}$ is bijective for every such presentation. For a sheaf of $\Lambda_X$-modules, take the colimit in $\Lambda$-modules, with the $\Lambda$-actions on sections induced by the canonical maps $\Lambda\to\Lambda_X(V)$. The resulting map is $\Lambda$-linear. Such a module sheaf is *classical* if every resulting continuity map is an isomorphism of $\Lambda$-modules; equivalently its underlying sheaf of sets is classical.
4. **Complexes.** A cochain complex of $\Lambda_X$-module sheaves, or an object $K$ of $D(X_{\Proet},\Lambda)$ `def-weil-abstract-derived-category`, is *classical* if every cohomology sheaf $H^q(K)$ is classical. This depends only on the isomorphism class in the derived category.

When $X$ is affine, the objects $U$ admitting these presentations are exactly the affine ind-étale objects of [dag-def-weil-pbc-ind-etale-basis], with ind-étale understood as in [dag-def-weil-pbc-ind-etale-algebra]. For general $X$ the inverse-limit formulation of [dag-sk-def-pe-morphisms] is the definition used here.

(SHEAF DAG node `det-pe-classical-definition-continuity-map`; machine-alignment layer.) Split from [definition-classical-pro-etale-sheaves--1]. DAG kind: definition. DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.continuityMap_ι`, `AlgebraicGeometry.ProEtale.IsClassicalCochainComplex`, `AlgebraicGeometry.ProEtale.isClassicalComplex_Q_iff`, `AlgebraicGeometry.ProEtale.isClassicalComplex_iso_iff`, `AlgebraicGeometry.ProEtale.affinePresentation_iff`. Statement dependencies not drawn: `def-weil-abstract-derived-category`, `def-weil-pbc-category-colimit`, `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`.
