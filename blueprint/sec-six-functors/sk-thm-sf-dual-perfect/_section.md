+++
id = "sk-thm-sf-dual-perfect"
kind = "section"
title = "The dual of a perfect complex"
order = 2294
uses = ["sk-def-sf-orientation", "sk-lem-sf-twist-interchange", "sk-prop-sf-dualizable-biduality"]
+++
*Theorem (sketch).*

Let $X$ be separated of finite type with admissible structure morphism and let
$K\in\Dctf(X,\Lambda)$ be perfect over $\Lambda_X$. Under the orientation of
[sk-def-sf-orientation] (which is [sk-thm-smooth-purity]) one has
$\mathbb D_XK\cong K^\vee(d)[2d]$, so that $\mathbb D_X$ restricts to an
anti-equivalence on the perfect objects, with $K\to\mathbb D_X\mathbb D_XK$ the
coefficient-dual biduality of [sk-prop-sf-dualizable-biduality].

## Proof

Substitute the orientation $\omega_X\cong\Lambda_X(d)[2d]$ into
$\mathbb D_XK=\RHom_X(K,\omega_X)$ and apply
[sk-lem-sf-twist-interchange] with $m=d$ together with the shift of the
second variable.

Uses: `\Cref{def:sf-orientation}`, `\Cref{lem:sf-twist-interchange}`, `\Cref{prop:sf-dualizable-biduality}`
