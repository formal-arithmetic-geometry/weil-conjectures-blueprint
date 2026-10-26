+++
id = "sk-thm-sfb-qlbar-two-colimit"
kind = "lemma"
title = "Descent to a finite coefficient field; $\\Dctf(X,\\Qlb)$ as a $2$-colimit"
order = 2138
lean = ["AlgebraicGeometry.ProEtale.coefficientMap_comp", "AlgebraicGeometry.ProEtale.padicSubfieldRingObjToPadicAlgCl", "AlgebraicGeometry.ProEtale.padicSubfieldRingObjMap_comp_toPadicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteLimits_extendScalars_padicSubfieldRingObjToPadicAlgCl", "AlgebraicGeometry.ProEtale.derivedExtendScalarsSubfield", "AlgebraicGeometry.ProEtale.derivedExtendScalarsToPadicAlgCl", "CategoryTheory.Mod.extendScalarsIsoOfEq", "AlgebraicGeometry.ProEtale.derivedExtendScalarsCompIso", "AlgebraicGeometry.ProEtale.PadicSubfieldConstructible", "AlgebraicGeometry.ProEtale.PadicAlgClConstructible", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsSubfield_obj", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsToPadicAlgCl_obj", "AlgebraicGeometry.ProEtale.constructibleExtendScalars", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgCl", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgClCompIso", "AlgebraicGeometry.ProEtale.constructibleCocone", "AlgebraicGeometry.ProEtale.constructibleCocone_homSurj", "AlgebraicGeometry.ProEtale.constructibleCocone_homInj", "AlgebraicGeometry.ProEtale.constructibleCocone_essSurjObj", "AlgebraicGeometry.ProEtale.constructibleCocone_isFilteredTwoColimit"]
uses = ["sk-prop-sf-open-closed-triangle", "sk-def-sfb-filtered-two-colimit", "sk-prop-sfb-cartesian-coefficients", "sk-lem-constructible-ext-continuity", "sk-prop-sfb-qlbar-colimit-x", "sk-lem-coefficient-heart"]
tags = ["sketch"]
+++
The coefficient ring $\Qlb$ is a filtered union of the fields $E$, but integral lattices exist
only over a single $E$. We therefore show that every object and every morphism of
$\Dbc(X,\Qlb)$ is defined over some finite $E$. For $C\in D(X_{\mathrm{proét}},E)$ and a finite
extension $F/E$ we write $C_F=F_X\otimes_{E_X}C$ and $C_{\Qlb}=\QbarX\otimes_{E_X}C$ for the
extensions of scalars, given by functors $D(X_{\mathrm{proét}},E)\to D(X_{\mathrm{proét}},F)$ and
$D(X_{\mathrm{proét}},E)\to D(X_{\mathrm{proét}},\Qlb)$; since $F_X$ and $\QbarX$ are flat over
$E_X$ ([lem-sfb-subfield-flat], [lem-sfb-qlbar-flat]), these need no deriving.

Let $X$ be a standing scheme.

1. Every lisse $\QbarX$-module is isomorphic to $L_{\Qlb}$ for a lisse $E_X$-module $L$ and
   some finite $E/\mathbf Q_\ell$.
2. For $C,D\in\Dbc(X,E)$ and every integer $r$, extension of scalars induces an isomorphism
   $$
   \varinjlim_{F\supset E}\Hom_{D(X_{\mathrm{proét}},F)}(C_F,D_F[r])\xrightarrow{\ \sim\ }
   \Hom_{D(X_{\mathrm{proét}},\Qlb)}(C_{\Qlb},D_{\Qlb}[r]),
   $$
   the colimit running over finite extensions $F$ of $E$ in $\Qlb$.
3. Every object of $\Dbc(X,\Qlb)$ is isomorphic to $K_{\Qlb}$ for some $K\in\Dbc(X,E)$ and
   some finite $E/\mathbf Q_\ell$.

4. For rational coefficients $\Dctf=\Dbc$; these are the bounded constructible categories
   $D_{\mathrm{cons}}$ of [det-def-sfb-bounded-constructible]. By (2) with $r=0$ and (3), extension
   of scalars identifies
   $$
   \Dctf(X,\Qlb)\simeq\mathop{\text{2-colim}}_{E\subset\Qlb}\Dctf(X,E)
   $$
   as ordinary categories (in the sense of [sk-def-sfb-filtered-two-colimit]): every object of
   $\Dctf(X,\Qlb)$ is isomorphic to $K_{\Qlb}$ for some finite $E$ and some $K\in\Dctf(X,E)$, and
   for $K,L\in\Dctf(X,E)$ extension of scalars induces a bijection
   $$
   \varinjlim_{F\supset E}\Hom_{\Dctf(X,F)}(K_F,L_F)\xrightarrow{\ \sim\ }\Hom_{\Dctf(X,\Qlb)}(K_{\Qlb},L_{\Qlb}),
   $$
   the colimit running over finite extensions $F$ of $E$ in $\Qlb$.
