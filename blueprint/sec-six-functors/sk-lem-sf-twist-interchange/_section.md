+++
id = "sk-lem-sf-twist-interchange"
kind = "lemma"
title = "Internal Hom with an invertible twist"
order = 2515
uses = ["sk-lem-sf-determination", "sk-prop-sf-dualizable-biduality"]
lean = ["AlgebraicGeometry.Etale.DerivedCategory.nonempty_iso_derivedHom_tensor"]
tags = ["sketch"]
+++
Let $K\in D(X,\Lambda)$ be perfect over $\Lambda_X$, that is, dualizable for
$\otimes^L_{\Lambda_X}$, let $T\in D(X,\Lambda)$ be invertible for
$\otimes^L_{\Lambda_X}$ (for instance a Tate twist $\Lambda(m)_X$, $m\in\Z$), and
let $M\in D(X,\Lambda)$. Then the canonical map

$$
\RHom_X\bigl(K,M\otimes^L_{\Lambda_X}T\bigr)\to
\RHom_X(K,M)\otimes^L_{\Lambda_X}T
$$

is an isomorphism; in particular
$\RHom_X(K,\Lambda_X(m)[n])\cong K^\vee(m)[n]$.
