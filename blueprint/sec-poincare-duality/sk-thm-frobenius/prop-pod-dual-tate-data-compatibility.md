+++
id = "prop-pod-dual-tate-data-compatibility"
kind = "theorem"
title = "Compatibility of the dual and Tate data"
order = 3413
tags = ["latex:proposition"]
uses = ["def-pod-dual-tate-datum", "def-pur-tate-datum", "def-trf-scheme-frobenius", "def-trf-strict-weil-complex", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes", "sk-prop-scalar-six", "sk-thm-transport", "lem-fix-weil-operations", "lem-pod-coefficient-dual-perfect", "thm-pur-weil-equivariance-of-purity-and-trace", "thm-sf-dual-perfect"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), let $(K,\varphi_K)$ be a strict Weil complex with $K$ perfect. The datum $\varphi _{K^\vee }$ of [def-pod-dual-tate-datum] defines a strict Weil complex $(K^\vee ,\varphi _{K^\vee })$, the coefficient evaluation

$$
K\otimes ^L_{A_X}K^\vee \xrightarrow {\  \operatorname {ev}_K\  }A_X
$$

is a morphism of Weil objects, the twisted object $(K^\vee (r),\varphi _{K^\vee (r)})$ is a strict Weil complex, and the canonical identification $\mathbb D_XK\cong K^\vee (d)[2d]$ of [thm-sf-dual-perfect] is an isomorphism of Weil objects (the compatibility of the purity isomorphism with the geometric-Frobenius data is the Weil equivariance of purity and trace, [thm-pur-weil-equivariance-of-purity-and-trace], and the duality isomorphisms are morphisms of Weil complexes by [lem-fix-weil-operations]). Here Weil complexes are the pairs of [sk-def-sf-weil-complexes]. All these objects and morphisms are compatible with the coefficient comparisons of [sk-prop-scalar-six] (reduction modulo $\pi_E^n$, inverting $\ell$, and finite and algebraic extension of the coefficient field), as in [sk-thm-transport].
