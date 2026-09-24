+++
id = "prop-weil-proper-base-change-coherence"
kind = "theorem"
title = "Coherence of the proper base-change exchange"
order = 3156
tags = ["latex:proposition"]
uses = ["def-exchange-projection", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "def-weil-small-proetale-site-detailed", "prop-weil-finite-proper-base-change-exchange"]
+++
In the setting of [prop-weil-finite-proper-base-change-exchange], the
exchange transformation
$\operatorname{Ex}_*(K)$ of
[prop-weil-finite-proper-base-change-exchange] is compatible with
composition of Cartesian squares, and its specialization at a
geometric point $\bar y$
is the canonical proper-base-change comparison on the corresponding
geometric fiber.

## Proof

Compatibility with composition of Cartesian squares is the horizontal
and vertical pasting law recorded for the exchange transformation in
[def-exchange-projection], the exchange maps of
[prop-weil-finite-proper-base-change-exchange] being the
corresponding instances. The specialization at $\bar y$ is the
evaluation of the exchange map for the base change
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y,\bar y}\to Y$ by the
(generically) pro-etale point: by
[def-exchange-projection] the exchange transformation is natural
in the Cartesian square, so applying the stalk functor
$\bar y^*$ identifies the displayed map with the canonical
comparison $H^*(X_{\bar y},K)\to H^*(X_{\bar y'},g'^*K)$ on the
geometric fibers.
