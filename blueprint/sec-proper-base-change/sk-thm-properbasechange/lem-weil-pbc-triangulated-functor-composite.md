+++
id = "lem-weil-pbc-triangulated-functor-composite"
kind = "lemma"
title = "A composite of triangulated functors, with the composite shift isomorphism, is triangulated"
uses = ["def-weil-triangulated-category"]
lean = ["CategoryTheory.Functor.IsTriangulated", "CategoryTheory.Functor.CommShift.comp", "CategoryTheory.Functor.mapTriangleCompIso"]
order = 2024
tags = ["mathlib", "stacks-014Y"]
+++
Let $\mathcal D,\mathcal D',\mathcal D''$ be pre-triangulated categories [def-weil-triangulated-category] with shifts $[1 ]$, and let $(F,\varphi):\mathcal D\to\mathcal D'$ and $(G,\psi):\mathcal D'\to\mathcal D''$ be triangulated (exact) functors, $\varphi_X:F(X[1 ])\xrightarrow{\sim}F(X)[1 ]$ and $\psi_Y:G(Y[1 ])\xrightarrow{\sim}G(Y)[1 ]$ their natural shift-commutation isomorphisms. Equip $G\circ F$ with the composite isomorphism
$$
 \chi_X=\psi_{F X}\circ G(\varphi_X):\ GF(X[1 ])\xrightarrow{\sim}GF(X)[1 ],
$$
natural in $X$. Then $(G\circ F,\chi)$ is triangulated: for every distinguished triangle $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{w}X[1 ]$ of $\mathcal D$, the triangle $GFX\xrightarrow{GFu}GFY\xrightarrow{GFv}GFZ\xrightarrow{\chi_X\circ GF(w)}GF(X)[1 ]$ is distinguished in $\mathcal D''$.
