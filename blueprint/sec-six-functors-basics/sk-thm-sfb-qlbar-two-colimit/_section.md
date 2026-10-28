+++
id = "sk-thm-sfb-qlbar-two-colimit"
kind = "lemma"
title = "Descent to a finite coefficient field"
order = 2286
lean = ["AlgebraicGeometry.ProEtale.coefficientMap_comp", "AlgebraicGeometry.ProEtale.padicSubfieldRingObjToPadicAlgCl", "AlgebraicGeometry.ProEtale.padicSubfieldRingObjMap_comp_toPadicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteLimits_extendScalars_padicSubfieldRingObjToPadicAlgCl", "AlgebraicGeometry.ProEtale.derivedExtendScalarsSubfield", "AlgebraicGeometry.ProEtale.derivedExtendScalarsToPadicAlgCl", "CategoryTheory.Mod.extendScalarsIsoOfEq", "AlgebraicGeometry.ProEtale.derivedExtendScalarsCompIso", "AlgebraicGeometry.ProEtale.PadicSubfieldConstructible", "AlgebraicGeometry.ProEtale.PadicAlgClConstructible", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsSubfield_obj", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsToPadicAlgCl_obj", "AlgebraicGeometry.ProEtale.constructibleExtendScalars", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgCl", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgClCompIso"]
uses = ["sk-def-sfb-constructible"]
tags = ["sketch"]
+++
Since $\Qlb$ is the filtered union of the finite extensions $E$ of $\mathbf Q_\ell$, we show that every
object and every morphism of $\Dbc(X,\Qlb)$ ([sk-def-sfb-constructible]) is defined over some
finite $E$. For $C\in D(X_{\mathrm{proét}},E)$ and a finite extension $E'/E$, the extensions of
scalars are the complexes $C_{E'}=E'_X\otimes_{E_X}C$ and $C_{\Qlb}=\QbarX\otimes_{E_X}C$. They
need no deriving, since $E'_X$ and $\QbarX$ are flat over $E_X$.

1. For $C,D\in\Dbc(X,E)$ and every integer $r$, extension of scalars induces an isomorphism
   $$
   \varinjlim_{E'\supset E}\Hom_{D(X_{\mathrm{proét}},E')}(C_{E'},D_{E'}[r])\xrightarrow{\ \sim\ }
   \Hom_{D(X_{\mathrm{proét}},\Qlb)}(C_{\Qlb},D_{\Qlb}[r]),
   $$
   the colimit running over finite extensions $E'$ of $E$ in $\Qlb$.
2. Every object of $\Dbc(X,\Qlb)$ is isomorphic to $K_{\Qlb}$ for some $K\in\Dbc(X,E)$ and
   some finite $E/\mathbf Q_\ell$.
