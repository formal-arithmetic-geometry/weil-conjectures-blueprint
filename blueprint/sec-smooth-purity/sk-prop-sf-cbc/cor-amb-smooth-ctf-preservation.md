+++
id = "cor-amb-smooth-ctf-preservation"
kind = "theorem"
title = "Smooth preservation on the ordinary etale site"
order = 1609
tags = ["latex:corollary"]
uses = ["def-sbc-smooth-morphisms", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "thm-asd-smooth-tensor"]
+++
For the smooth morphism of
[thm-asd-smooth-tensor], the ambient right
adjoint preserves bounded constructible complexes of finite
Tor amplitude.

## Proof

Pull back a finite constructible stratification for each
cohomology sheaf of $K$; inverse image is exact and
preserves finite locally constant sheaves. The rank-one
lisse tensor factor in [thm-asd-smooth-tensor]
therefore preserves constructibility. Its shift gives a
finite cohomological interval. On each trivializing etale
neighbourhood, tensoring this factor and shifting changes
only the endpoints of the Tor interval of
[def-weil-finite-tor-amplitude]. Thus the Tor interval
is still finite. This proves the assertion for the actual
ambient right adjoint, with constructibility understood as
in [def-weil-finite-torsion-constructibility].
