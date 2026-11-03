+++
id = "sk-thm-sfb-qlbar-two-colimit"
kind = "lemma"
title = "Descent to a finite coefficient field"
order = 249
lean = ["AlgebraicGeometry.ProEtale.coefficientMap_comp", "AlgebraicGeometry.ProEtale.padicSubfieldRingObjToPadicAlgCl", "AlgebraicGeometry.ProEtale.padicSubfieldRingObjMap_comp_toPadicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteLimits_extendScalars_padicSubfieldRingObjToPadicAlgCl", "AlgebraicGeometry.ProEtale.derivedExtendScalarsSubfield", "AlgebraicGeometry.ProEtale.derivedExtendScalarsToPadicAlgCl", "CategoryTheory.Mod.extendScalarsIsoOfEq", "AlgebraicGeometry.ProEtale.derivedExtendScalarsCompIso", "AlgebraicGeometry.ProEtale.PadicSubfieldConstructible", "AlgebraicGeometry.ProEtale.PadicAlgClConstructible", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsSubfield_obj", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsToPadicAlgCl_obj", "AlgebraicGeometry.ProEtale.constructibleExtendScalars", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgCl", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgClCompIso"]
uses = ["sk-def-sfb-constructible"]
tags = ["sketch"]
+++
1. For $C,D\in\Dbc(X,E)$ and every integer $r$, extension of scalars
   induces an isomorphism

$$
\varinjlim_{E'\supset E}
\Hom_{D(X_{\mathrm{pro}\acute{e}t},E')}(C_{E'},D_{E'}[r])
\;\xrightarrow{\ \sim\ }\;
\Hom_{D(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)}(C_{\overline{\mathbf Q}_\ell},D_{\overline{\mathbf Q}_\ell}[r]),
$$

the colimit running over finite extensions $E'$ of $E$ in $\overline{\mathbf Q}_\ell$.
2. Every object of $\Dbc(X,\overline{\mathbf Q}_\ell)$ is isomorphic to $K_{\overline{\mathbf Q}_\ell}$ for
   some $K\in\Dbc(X,E)$ and some finite $E/\Ql$.
