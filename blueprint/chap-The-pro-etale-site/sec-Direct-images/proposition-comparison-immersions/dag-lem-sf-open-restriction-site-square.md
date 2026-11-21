+++
id = "dag-lem-sf-open-restriction-site-square"
kind = "dag-lemma"
title = "Scalar restriction respects the exact open-extension site boundary"
name_showing = false
order = 139502
tags = ["sheaf-dag"]
split_from = "proposition-comparison-immersions--1"
dag_id = "lem-sf-open-restriction-site-square"
dag_kind = "statement"
dag_status = "split"
serial = false
uses = ["dag-lem-cbc-proetale-extension-zero-comparison"]
+++
Let $A,B$ be finite discrete commutative rings, $a:A\to B$ a unital homomorphism, and $j:X\hookrightarrow Y$ an open immersion of schemes `def-weil-open-immersion`. Regard $R=A,B$ as discrete condensed rings $\underline R$ and put $R_T=p_T^*\underline R$ for $T=X,Y$ `det-def-sfb-pulled-back-coefficients`. These are canonically constant ring sheaves; the identification is natural in $R$ [lem-weil-pbc-finite-discrete-scheme-ring-constant, def-sfb-constant-sheaf-scheme-pullback-comparison]. Work in a common sufficiently large site and module universe. Write $D(T_{\mathrm{proet}},R)=D(\operatorname{Mod}_{R_T})$ `det-def-sfb-derived-categories`, and use constant-$R$ module sheaves on $T_{\mathrm{et}}$ `def-weil-pbc-derived-categories`.

Let $U_T^e,U_T^p$ be exact scalar restriction along $a$ on the etale site and along $p_T^*\underline a$ on the pro-etale site [def-pc-sheaf-restrict-scalars, def-sfb-modobj-restriction]. Let $C_T^R=\nu_T^*$ be exact site comparison, followed by the canonical coefficient identification above `lem-sf-comparison-pullback-exact`. Write $J_R^e=j_{!,R}^e$ and $J_R^p=j_{!,R}^p$ for exact extension by zero; the latter is the module-object functor over $p_T^*\underline R$ [def-weil-pbc-extension-by-zero, det-def-sfb-module-lower-shriek]. All these functors on derived categories are induced termwise.

Use the following specified sheaf comparisons and their termwise derived images: $\delta_T:C_T^AU_T^e\xrightarrow{\sim}U_T^pC_T^B$, the identity on underlying comparison inverse images, with scalar actions identified by naturality of the constant-ring comparisons `def-sfb-comap-mapmod-square`; $b_R:J_R^pC_X^R\xrightarrow{\sim}C_Y^RJ_R^e$, the inverse canonical adjunction comparison [dag-lem-cbc-proetale-extension-zero-comparison]; and $c^s:J_A^sU_X^s\xrightarrow{\sim}U_Y^sJ_B^s$ ($s=e,p$), the identity on underlying abelian extensions by zero [lem-cbc-ringed-open-scalar-adjunction, def-sfb-comap-open-immersion-shriek-iso]. The $c^s$ have the normalization characterized by the open-adjunction unit equation, not an arbitrary endpoint isomorphism.

For every $L\in D^+(X_{\mathrm{et}},B)$, viewed in the unbounded category by its canonical inclusion, the following equality holds in $D(Y_{\mathrm{proet}},A)$:
$$
J_A^p(\delta_{X,L});c^p_{C_X^BL};U_Y^p(b_{B,L})
=b_{A,U_X^eL};C_Y^A(c^e_L);\delta_{Y,J_B^eL}.
$$
Here $v;w$ means first $v$, then $w$. Both sides go from $J_A^pC_X^AU_X^eL$ to $U_Y^pC_Y^BJ_B^eL$, with canonical exact-functor composition and $D^+$-inclusion isomorphisms inserted. No boundedness above, constructibility, finite Tor amplitude, properness or flatness assumption is imposed.

(SHEAF DAG node `lem-sf-open-restriction-site-square`; machine-alignment layer.) Split from [proposition-comparison-immersions--1]. DAG kind: statement. Placed through `lem-cbc-proetale-extension-zero-comparison` (ancestor-1). DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.EtaleModules`, `AlgebraicGeometry.ProEtale.CondensedModules`, `AlgebraicGeometry.ProEtale.SiteComparison`, `AlgebraicGeometry.ProEtale.EtalePlus`, `AlgebraicGeometry.ProEtale.canonicalCoeffMap`, `AlgebraicGeometry.ProEtale.isMonHom_canonicalCoeffMap`, `AlgebraicGeometry.ProEtale.EtaleScalarRestriction`, `AlgebraicGeometry.ProEtale.CondensedScalarRestriction`, `AlgebraicGeometry.ProEtale.EtaleOpenExtension`, `AlgebraicGeometry.ProEtale.CondensedOpenExtension`, `AlgebraicGeometry.ProEtale.EtaleForget`, `AlgebraicGeometry.ProEtale.CondensedForget`, `AlgebraicGeometry.ProEtale.finiteInverseForgetIso`, `AlgebraicGeometry.ProEtale.siteComparisonForgetIso`, `AlgebraicGeometry.ProEtale.etaleOpenForgetIso`, `AlgebraicGeometry.ProEtale.OpenRestrictionSiteComparisons`, `AlgebraicGeometry.ProEtale.canonicalOpenScalarProetale`, `AlgebraicGeometry.ProEtale.openRestriction_site_square_condensed`. Statement dependencies not drawn: `def-weil-open-immersion`, `det-def-sfb-pulled-back-coefficients`, `lem-weil-pbc-finite-discrete-scheme-ring-constant`, `def-sfb-constant-sheaf-scheme-pullback-comparison`, `det-def-sfb-derived-categories`, `def-weil-pbc-derived-categories`, `def-pc-sheaf-restrict-scalars`, `def-sfb-modobj-restriction`, `lem-sf-comparison-pullback-exact`, `def-weil-pbc-extension-by-zero`, `det-def-sfb-module-lower-shriek`, `def-sfb-comap-mapmod-square`, `lem-cbc-ringed-open-scalar-adjunction`, `def-sfb-comap-open-immersion-shriek-iso`.
