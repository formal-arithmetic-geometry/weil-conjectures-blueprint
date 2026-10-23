+++
id = "the-dense-source-valuative-criterion--remark-1"
kind = "remark"
title = "Formalization route"
order = 382
uses = ["lemma-nagata-composite-valuation-ring", "lemma-nagata-dense-flat-pullback", "lemma-nagata-dense-valuation-probe", "lemma-nagata-reduced-dense-image-schematic", "lemma-nagata-valuation-intersection", "lemma-nagata-valuation-ring-extension"]
+++
The formal proof splits the two conclusions into a universal-closedness
statement and a separatedness statement. It deviates from the Stacks
Project text in two reductions: instead of replacing $U,X,S$ by their
reductions, the morphism $h$ is factored through its scheme-theoretic
image — the factor map is scheme-theoretically dominant with no
reducedness hypothesis, and the valuative data factors through the image
because $\operatorname{Spec}$ of a valuation ring or of a field is
reduced; and the polynomial presentation of a field-valued point is
inlined. The extension lemma (Tag 00IA) is obtained from Chevalley's
extension theorem rather than from the Zorn argument. The flat-pullback and
reduced-density inputs ([lemma-nagata-dense-flat-pullback],
[lemma-nagata-reduced-dense-image-schematic]) enter through the general
theory of scheme-theoretically dominant morphisms.
