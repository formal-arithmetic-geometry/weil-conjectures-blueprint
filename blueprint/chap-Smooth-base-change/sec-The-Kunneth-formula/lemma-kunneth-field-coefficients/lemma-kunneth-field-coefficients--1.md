+++
id = "lemma-kunneth-field-coefficients--1"
kind = "lemma"
title = "Dévissage from finite direct images"
name_showing = false
order = 714001
aliases = ["bp-r215-1"]
lean = ["AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_singleFunctor_of_flat_of_lowerStar"]
uses = ["definition-derived-base-change-map", "definition-projection-formula-map"]
+++
The field-coefficient argument is part of the following dévissage over a
finite ring in Lean.

Let $A$ be a finite commutative ring, let $X$ be a scheme of finite type
over a field $k$, and consider morphisms of schemes

$$
p:X'\to X,\qquad f':X'\to S',\qquad
h:Y\to X',\qquad e:Y\to T,\qquad g:T\to S'
$$

with $f'h=ge$ and $h$ quasi-compact and quasi-separated. For sheaves
$E$ on $X_{\acute{e}t}$ and $F$ on $T_{\acute{e}t}$ of $A$-modules,
placed in degree zero, write

$$
\tau_{E,F}:Lp^*E\otimes_A^{\mathrm L}Lf'^*Rg_*F
\longrightarrow
Rh_*\bigl(Lh^*Lp^*E\otimes_A^{\mathrm L}Le^*F\bigr)
$$

for the tensor base change map. It is the adjoint, under
$Lh^*\dashv Rh_*$, of the map obtained from
$Lh^*Lf'^*\simeq Le^*Lg^*$ and the counit $Lg^*Rg_*F\to F$.

Suppose that $\tau_{\pi_*A_{X_i},F}$ is an isomorphism for every finite
morphism $\pi:X_i\to X$ and every sheaf $F$ of $A$-modules on
$T_{\acute{e}t}$. Then $\tau_{E,F}$ is an isomorphism for every flat
sheaf $E$ of $A$-modules on $X_{\acute{e}t}$ and every sheaf $F$ of
$A$-modules on $T_{\acute{e}t}$.
