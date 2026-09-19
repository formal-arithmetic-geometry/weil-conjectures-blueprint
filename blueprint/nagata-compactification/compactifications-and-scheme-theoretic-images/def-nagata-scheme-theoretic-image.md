+++
id = "def-nagata-scheme-theoretic-image"
kind = "definition"
title = "Scheme-theoretic image"
order = 140
lean = ["AlgebraicGeometry.Scheme.Hom.image"]
uses = ["lemma-nagata-scheme-image-ideal-qc"]
+++
Let $g\colon T\to Y$ be a morphism. Define
$\operatorname{SIm}(g)$ to mean the Mathlib scheme-theoretic image
`Scheme.Hom.image g`, with inclusion $g_{\mathrm{im}}$ and factor map
$g^{\mathrm{im}}$ supplied by
[lemma-nagata-scheme-image-ideal-qc]. Whenever a later argument needs
quasi-compactness, it must state that hypothesis explicitly.
