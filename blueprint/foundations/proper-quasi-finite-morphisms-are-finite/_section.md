+++
id = "proper-quasi-finite-morphisms-are-finite"
kind = "section"
title = "Proper quasi-finite morphisms are finite"
order = 1964
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-proper", "lem-weil-pbc-proper-base-change", "lem-weil-pbc-proper-closed-image", "lem-weil-pbc-proper-to-separated", "lem-weil-pbc-surjective-nonempty-fibres", "thm-sp-grothendieck"]
+++
Chapter 8 of `weil_conjectures_detailed.tex`: a proper quasi-finite morphism
is finite. The chapter decomposes Stacks Project, Cohomology of Schemes,
Section 30.21 (Tags 02OG and 02OH), and closes a citation the curve
calculations quote as an input.

- [affine-morphisms-quasi-finite-morphisms-and-coherent-modules] and
[properness-integral-extensions-and-quasi-finite-morphisms] fix the
vocabulary and the properties of proper, integral and quasi-finite morphisms.
- [affineness-criteria-formal-functions-and-the-leray-spectral-sequence]
collects the cohomological tools: affineness criteria, the theorem on formal
functions, and the Leray spectral sequence.
- [the-inputs-of-the-descent-of-the-immersion] and
[the-finite-fibre-criteria-and-zariski-s-main-theorem] prove the main
results: a morphism is finite iff it is proper with finite fibres
[thm-pqf-finite-iff-proper-finite-fibres], hence
[cor-pqf-proper-quasifinite-finite]; finiteness spreads out from one finite
fibre [thm-pqf-finiteness-spreads]; and Zariski's main theorem in its
quasi-finite form [thm-pqf-zmt-factorization].
- [the-finite-presentation-stage-of-the-descent] upgrades the factorization to
finite presentation [pqf-thm-zmt-fp].

Six classical inputs are recorded rather than proved, each stated with its
Stacks tag and the note "No separate proof is given": upper semicontinuity of
fibre dimension, integral = affine + universally closed, affineness local on
the target, Serre's affineness criterion, vanishing of quasi-coherent
cohomology on affines, and openness of the quasi-finite locus. The source
keeps them as the ledger OBL-PQF-01..06.
