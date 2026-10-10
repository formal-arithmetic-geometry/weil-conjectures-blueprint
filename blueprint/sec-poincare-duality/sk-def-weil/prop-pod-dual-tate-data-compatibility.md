+++
id = "prop-pod-dual-tate-data-compatibility"
kind = "theorem"
title = "Compatibility of the dual and Tate data"
order = 2425
tags = ["latex:proposition"]
uses = ["def-pod-dual-tate-datum", "def-pur-tate-datum", "def-trf-scheme-frobenius", "def-trf-strict-weil-complex", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-weil-sheaf-complex", "lem-fix-weil-operations", "lem-pod-coefficient-dual-perfect", "lem-weil-weil-complex-qbar-idempotent-complete", "thm-pur-weil-equivariance-of-purity-and-trace", "thm-sf-dual-perfect"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), let $(K,\varphi_K)$ be a strict Weil complex with $K$ perfect. The datum $\varphi _{K^\vee }$ of [def-pod-dual-tate-datum] defines a strict Weil complex $(K^\vee ,\varphi _{K^\vee })$, the coefficient evaluation

$$
K\otimes ^L_{A_X}K^\vee \xrightarrow {\  \operatorname {ev}_K\  }A_X
$$

is a morphism of Weil objects, the twisted object $(K^\vee (r),\varphi _{K^\vee (r)})$ is a strict Weil complex, and the canonical identification $\mathbb D_XK\cong K^\vee (d)[2d]$ of [thm-sf-dual-perfect] is an isomorphism of Weil objects (the compatibility of the purity isomorphism with the geometric-Frobenius data is the Weil equivariance of purity and trace, [thm-pur-weil-equivariance-of-purity-and-trace], and the duality isomorphisms are morphisms of Weil complexes by [lem-fix-weil-operations]). All these objects and morphisms commute with finite reduction, adic normalization, rationalization, finite coefficient-field extension, and idempotent splitting (which exists for Weil complexes by [lem-weil-weil-complex-qbar-idempotent-complete]).
