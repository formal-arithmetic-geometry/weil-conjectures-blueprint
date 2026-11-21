+++
id = "dag-def-pe-etale-constructible-module"
kind = "dag-definition"
title = "Constructible etale modules for discrete Noetherian coefficients"
name_showing = false
order = 149502
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "def-pe-etale-constructible-module"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.coefficientModelFixedScalars", "CategoryTheory.IsCoefficientModelLocallyConstantFinite", "AlgebraicGeometry.Scheme.coefficientEtaleBaseChange", "AlgebraicGeometry.Scheme.coefficientEtaleBaseChange_isContinuous", "AlgebraicGeometry.Scheme.coefficientEtaleFixedPullback", "AlgebraicGeometry.Scheme.IsCoefficientConstructibleEtaleModule", "AlgebraicGeometry.Scheme.IsCoefficientBoundedConstructibleEtale", "AlgebraicGeometry.Scheme.CoefficientConstructibleEtaleModuleCategory", "AlgebraicGeometry.Scheme.CoefficientBoundedConstructibleEtaleCategory"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
Let $X$ be a scheme `def-pc-scheme` and $\Lambda$ a discrete commutative Noetherian ring `def-weil-pbc-noetherian-ring`. Use the universes and small skeletons of `def-weil-size-convention`. On its small etale site $X_{\mathrm{et}}$ `def-weil-pbc-etale-site`, write $\underline\Lambda_X$ for the constant sheaf of rings [dag-def-weil-pbc-constant-sheaf], and use sheaves of $\underline\Lambda_X$-modules and their linear morphisms `def-weil-sheaf-of-modules-category`. Such a module sheaf $F$ is constructible if, for every affine open $U\subseteq X$, there is a finite partition $U=\coprod_{a=1}^n Z_a$ into constructible locally closed subschemes (a scheme stratification `def-constructible-stratification`, including its schemes and immersion maps): their underlying subsets are constructible in $U$ `def-weil-constructible-subset`, locally closed `def-weil-locally-closed-subset`, pairwise disjoint, and cover $U$. For each inclusion $i_a:Z_a\to X$, the inverse-image restriction $i_a^{-1}F$ `def-weil-pbc-inverse-image` must admit an etale covering $\{V_{ab}\to Z_a\}_b$ and isomorphisms $(i_a^{-1}F)|_{V_{ab}}\cong\underline{M_{ab}}_{V_{ab}}$ of module sheaves, where $M_{ab}$ are finitely generated $\Lambda$-modules `def-weil-finitely-generated-module` and the right side is the sheafification of the constant presheaf with value $M_{ab}$ [dag-def-weil-pbc-constant-sheaf], with its induced $\underline\Lambda_{V_{ab}}$-module structure. Finite generation refers to modules, and does not require their underlying sets to be finite. The constructible etale module category has these sheaves as objects and all module-sheaf morphisms between them as morphisms, with identities and composition inherited from the ambient module-sheaf category (the full subcategory).

Write $D^b_c(X_{\mathrm{et}},\Lambda)$ for the full subcategory of the derived category of the ambient abelian category of all sheaves of $\underline\Lambda_X$-modules on $X_{\mathrm{et}}$ `def-weil-abstract-derived-category` whose objects $K$ have constructible cohomology sheaves $H^q(K)$ for every integer $q$ and $H^q(K)=0$ outside some finite interval. Here full subcategory again means that all ambient derived morphisms between the specified objects are retained, with inherited identities and composition. No completeness condition is imposed.

(SHEAF DAG node `def-pe-etale-constructible-module`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: definition. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-size-convention`, `def-pc-scheme`, `def-weil-pbc-noetherian-ring`, `def-weil-pbc-etale-site`, `def-weil-sheaf-of-modules-category`, `def-weil-constructible-subset`, `def-weil-locally-closed-subset`, `def-weil-pbc-inverse-image`, `def-weil-finitely-generated-module`, `def-weil-abstract-derived-category`, `def-constructible-stratification`, `lem-weil-pbc-etale-constant-ring-module-equivalence`.
