+++
id = "def-sc-picard-functor"
kind = "definition"
title = "The Picard functor of a proper curve"
lean = ["AlgebraicGeometry.algPicardFunctor", "AlgebraicGeometry.picardSubfunctorDegree", "AlgebraicGeometry.picardFunctorDegree"]
order = 562
uses = ["def-sc-curves", "def-sc-invertible-module", "def-sc-pic0", "def-sc-picard-group"]
+++
Let $C$ be a proper smooth connected curve over a
field $k$. The *Picard functor*

$$
\operatorname{Pic}_{C/k}:(k\text{-algebras})\longrightarrow\mathbf{Sets},
\qquad \operatorname{Pic}_{C/k}:=
\bigl(R\longmapsto\operatorname{Pic}(C\times_k\operatorname{Spec}R)\bigr)^{\#}_{\mathrm{fppf}},
$$

is the fppf sheafification of the presheaf of isomorphism classes of
invertible modules. For
$d\in\mathbf Z$, $\operatorname{Pic}^d_{C/k}$ is the fppf sheafification,
on the category of $k$-schemes $T$, of the subpresheaf of
$T\mapsto\operatorname{Pic}(C\times_kT)$ of the classes $[\mathcal L]$ of
fibrewise degree $d$: for every field $K$ over $k$ and every $k$-morphism
$t:\operatorname{Spec}K\to T$, the pullback of $\mathcal L$ to
$C_K$ has degree $d$.
