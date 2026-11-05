+++
id = "lemma-base-change-along-product-projection--1"
kind = "lemma"
title = "Tensor base change for unbounded complexes"
name_showing = false
order = 706001
aliases = ["bp-r212-1"]
lean = ["AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap"]
uses = ["definition-derived-base-change-map"]
+++
Let $k$ be a field and $A$ a finite commutative ring whose exponent is
invertible in $k$. Consider a diagram with both squares cartesian,

$$
\begin{CD}
X @<{p}<< X' @<{h}<< Y\\
@V{a}VV @V{f'}VV @V{e}VV\\
\operatorname{Spec}k @<{b}<< S' @<{g}<< T,
\end{CD}
$$

where $X$, $S'$ and $T$ are of finite type over $k$, and the structure
morphism of $T$ is $b\circ g$. For arbitrary complexes
$E\in D(X_{\acute{e}t},A)$ and $F\in D(T_{\acute{e}t},A)$, the tensor base
change map

$$
Lp^*E\otimes_A^{\mathbf L}Lf'^*Rg_*F
\longrightarrow
Rh_*\bigl(Lh^*Lp^*E\otimes_A^{\mathbf L}Le^*F\bigr)
$$

is an isomorphism. No separatedness, boundedness, constructibility or
finite Tor amplitude hypothesis is imposed.

The map is the adjoint transpose under $Lh^*\dashv Rh_*$ of

$$
Lh^*\bigl(Lp^*E\otimes_A^{\mathbf L}Lf'^*Rg_*F\bigr)
\simeq Lh^*Lp^*E\otimes_A^{\mathbf L}Le^*Lg^*Rg_*F
\xrightarrow{\,1\otimes Le^*\varepsilon_g\,}
Lh^*Lp^*E\otimes_A^{\mathbf L}Le^*F.
$$
