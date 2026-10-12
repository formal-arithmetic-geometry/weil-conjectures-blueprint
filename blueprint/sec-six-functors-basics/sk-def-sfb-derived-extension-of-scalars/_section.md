+++
id = "sk-def-sfb-derived-extension-of-scalars"
kind = "definition"
title = "Derived extension of scalars"
order = 1621
uses = ["sk-def-sfb-derived-categories", "sk-def-sfb-change-of-scalars"]
lean = ["CategoryTheory.Mod.preservesKFlatQuasiIso", "CategoryTheory.Mod.derivedExtendRestrictAdjunction", "CategoryTheory.Mod.rightDerivedComapIsoMapDerivedCategory", "CategoryTheory.Mod.derivedExtendMapDerivedCategoryAdjunction"]
tags = ["sketch"]
+++
Let $\mathcal C$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive and which has functorial flat resolutions. Let
$\varphi\colon\mathcal R\to\mathcal S$ be a morphism of commutative ring objects of
$\mathcal C$, with extension of scalars $\operatorname{Ext}_\varphi=\mathcal S\otimes_{\mathcal R}-$
and restriction of scalars $\operatorname{Res}_\varphi$ [sk-def-sfb-change-of-scalars]. The
*derived extension of scalars* is the left derived functor
[sk-def-sfb-derived-categories]
$$
\mathcal S\otimes^{\mathrm L}_{\mathcal R}-:=L(\operatorname{Ext}_\varphi)\colon D(\Mod_{\mathcal R})\to D(\Mod_{\mathcal S}).
$$
It is computed by applying $\mathcal S\otimes_{\mathcal R}-$ to a K-flat resolution. It is
left adjoint to the termwise restriction of scalars $D(\operatorname{Res}_\varphi)$, which
is the right derived functor of the exact functor $\operatorname{Res}_\varphi$:
$$
\mathcal S\otimes^{\mathrm L}_{\mathcal R}-\dashv D(\operatorname{Res}_\varphi).
$$
