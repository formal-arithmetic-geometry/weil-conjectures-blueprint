+++
id = "sk-thm-sfb-qlbar-two-colimit"
kind = "theorem"
title = "$D_{\\mathrm{cons}}(X,\\Qlb)$ is the 2-colimit of the $D_{\\mathrm{cons}}(X,E)$"
order = 1740
uses = ["sk-def-sfb-bounded-constructible", "sk-def-sfb-filtered-two-colimit", "sk-prop-sfb-finite-extension-compatibility"]
lean = ["AlgebraicGeometry.ProEtale.derivedExtendScalarsSubfield", "AlgebraicGeometry.ProEtale.derivedExtendScalarsToPadicAlgCl", "CategoryTheory.Mod.extendScalarsIsoOfEq", "AlgebraicGeometry.ProEtale.derivedExtendScalarsCompIso", "AlgebraicGeometry.ProEtale.PadicSubfieldConstructible", "AlgebraicGeometry.ProEtale.PadicAlgClConstructible", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsSubfield_obj", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsToPadicAlgCl_obj", "AlgebraicGeometry.ProEtale.constructibleExtendScalars", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgCl", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgClCompIso", "AlgebraicGeometry.ProEtale.constructibleCocone", "AlgebraicGeometry.ProEtale.constructibleCocone_homSurj", "AlgebraicGeometry.ProEtale.constructibleCocone_homInj", "AlgebraicGeometry.ProEtale.constructibleCocone_essSurjObj", "AlgebraicGeometry.ProEtale.constructibleCocone_isFilteredTwoColimit"]
tags = ["sketch"]
+++
Let $\ell$ be a prime and $X$ a scheme. For finite extensions $E\le F$ of $\mathbf Q_\ell$ inside
$\Qlb$, let $T_{E,F}=F_X\otimes^{\mathrm L}_{E_X}-$ and
$T_{E,\Qlb}=\overline{\mathbf Q}_{\ell,X}\otimes^{\mathrm L}_{E_X}-$ be the derived extensions of scalars of
[sk-prop-sfb-finite-extension-compatibility] ([sk-def-sfb-derived-extension-of-scalars]), and
$D_{\mathrm{cons}}(X,E)$, $D_{\mathrm{cons}}(X,\Qlb)$ the bounded constructible derived
categories of $E_X$- resp. $\overline{\mathbf Q}_{\ell,X}$-modules ([sk-def-sfb-bounded-constructible]).

1. $T_{E,F}$ and $T_{E,\Qlb}$ preserve bounded constructible complexes, and their restrictions
   form a cocone of categories, in the sense of [sk-def-sfb-filtered-two-colimit],

   $$
   E\longmapsto D_{\mathrm{cons}}(X,E)\xrightarrow{\ T_{E,\Qlb}\ }D_{\mathrm{cons}}(X,\Qlb),
   $$

   indexed by the directed set of finite extensions of $\mathbf Q_\ell$ in $\Qlb$, with
   transition functors $T_{E,F}$ and the transitivity isomorphisms
   $T_{F,\Qlb}\circ T_{E,F}\cong T_{E,\Qlb}$.
2. If the underlying topological space of $X$ is Noetherian, this cocone is a filtered
   2-colimit:

   $$
   D_{\mathrm{cons}}(X,\Qlb)=2\text{-}\colim_E\,D_{\mathrm{cons}}(X,E).
   $$

   Explicitly: every bounded constructible $\overline{\mathbf Q}_{\ell,X}$-complex is isomorphic to
   $T_{E,\Qlb}K_E$ for some $E$ and some $K_E\in D_{\mathrm{cons}}(X,E)$; every morphism
   $T_{E,\Qlb}K_E\to T_{F,\Qlb}L_F$ is the extension of scalars of a morphism
   $T_{E,H}K_E\to T_{F,H}L_F$ for some finite $H\supseteq E,F$; and two morphisms of
   $D_{\mathrm{cons}}(X,H)$ with the same extension of scalars to $\Qlb$ have the same extension
   of scalars to some finite $H'\supseteq H$.
