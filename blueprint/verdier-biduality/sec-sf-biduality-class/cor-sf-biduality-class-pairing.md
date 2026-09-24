+++
id = "cor-sf-biduality-class-pairing"
kind = "theorem"
title = "Naturality and pairings on the coefficient class"
order = 3749
tags = ["latex:corollary"]
uses = ["lem-sf-twist-interchange", "lem-weil-duality-pairing", "thm-pur-adic-reconstruction", "thm-pur-finite-coefficient-smooth-purity", "thm-pur-rational-and-qbar-purity", "thm-sf-biduality-class"]
+++
In the setting of [thm-sf-biduality-class], evaluation and biduality
are natural and compatible with shifts, triangles and twists. On smooth
$X$ of pure dimension $d$, the orientation identifies
$\omega_{X,\Lambda}\cong\Lambda(d)[2d]$.

## Proof

Use [thm-sf-biduality-class] and its evaluation-compatible
coefficient transports for the anti-equivalence and naturality.
The pairing is the evaluation of [lem-weil-duality-pairing],
and twists commute by [lem-sf-twist-interchange].
The orientations at the finite, integral and field stages are
[thm-pur-finite-coefficient-smooth-purity],
[thm-pur-adic-reconstruction] and
[thm-pur-rational-and-qbar-purity], respectively.
