+++
id = "thm-sf-dual-perfect"
kind = "theorem"
title = "The dual of a perfect complex"
order = 2279
uses = ["def-sf-datum", "def-sf-orientation", "def-sf-pf", "lem-sf-twist-interchange", "prop-sf-dualizable-biduality"]
+++
In the setting of [def-sf-datum], let $X$ be separated of finite type
with exceptional-adjoint admissible structure morphism and let
$K\in D^b_{ctf}(X,\Lambda)$ be perfect over $\Lambda_X$. If the
orientation of [def-sf-orientation] holds, then
$D_XK\cong K^\vee(d)[2d]$, so that
$D_X$ restricts to an anti-equivalence on the perfect objects, where the
biduality $K\to D_XD_XK$ is the coefficient-dual biduality of
[prop-sf-dualizable-biduality].

## Proof

Substitute the
orientation $\omega_X\cong\Lambda_X(d)[2d]$ of [def-sf-orientation]
into the Verdier dual $D_XK=R\mathcal H om_X(K,\omega_X)$ of
[def-sf-pf] and apply
[lem-sf-twist-interchange] with $m=d$ together with the shift of the
second variable:
$D_XK\cong R\mathcal H om_X(K,\Lambda_X(d)[2d])\cong \bigl(R\mathcal H om_X(K,\Lambda_X(d))\bigr)[2d]\cong K^\vee(d)[2d]$. The
restriction to the perfect objects is then
[prop-sf-dualizable-biduality] transported along this
identification.
