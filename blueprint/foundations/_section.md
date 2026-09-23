+++
id = "foundations"
kind = "section"
title = "Shared language and cohomological foundations"
order = 1100
+++
Part I of `weil_conjectures_detailed.tex`: the common language of the whole
blueprint. Nothing here is a geometric input to the Weil conjectures; it is
the vocabulary in which the later parts are written, collected in one place so
that no statement downstream rests on an unstated convention.

Four chapters, in the order in which they are used:

- [conventions-coefficient-categories-and-basic-operations] fixes the
arithmetic and geometric conventions, builds the coefficient tower through
its four stages ($A_{E,n}$, $\mathcal O_E$, $E$, $\Qlb$), and defines the six
operations in triangulated form.
- [weil-structures-frobenius-and-weight-conventions] fixes the arithmetic
vocabulary the conjectures are stated in: local Frobenius and its trace, the
zeta-series normalization, the Poincare trace and cup product, and the three
notions of weight.
- [spectral-sequence-machinery] builds the exact-couple and hypercohomology
formalism from scratch, up to the Grothendieck spectral sequence and its
base-change naturality.
- [ambient-categories-sites-and-the-comparison-framework] sets up the small
etale and pro-etale sites, direct and inverse image with the named exchange
morphisms, the strict henselization as a limit, hypercover descent, the
predicates $\mathrm{PBC}$ and $\mathrm{IA}$, and derived completion.

The part is self-contained: every `uses` edge recorded inside it resolves
inside it, so this section cites nothing beyond itself and carries no `uses`
list. The references that point outside it — to the six-functor interfaces, to
coefficient biduality, to smooth purity, and to the later proper-base-change
statements — are consumed, not proved, here; they are listed at the end of the
body of the object that names them, under *Unresolved dependencies*, and will
become edges when the corresponding parts are imported.

Fifteen identifiers of this part already name objects imported earlier from
the sketch sources, which read the same notions at a coarser grain. Those
carry the suffix `-detailed` here so that the two readings coexist:
[def-weil-frobenius-detailed], [def-weil-small-proetale-site-detailed],
[def-weil-derived-complete-integral-detailed],
[def-coefficient-twists-detailed],
[def-compact-support-direct-image-detailed],
[def-weil-pbc-cartesian-square-detailed],
[def-weil-pbc-underived-exchange-detailed],
[def-weil-pbc-derived-exchange-detailed],
[def-weil-pbc-pointed-etale-neighbourhoods-detailed],
[def-weil-pbc-strict-henselization-limit-detailed],
[def-weil-pbc-property-detailed],
[prop-weil-pbc-strict-henselization-stalk-formula-detailed],
[def-weil-pbc-finite-section-pullback-detailed],
[def-weil-pbc-completed-pullback-detailed], and the section
[triangulated-coefficient-categories-detailed].

Nothing in this part is formalised yet, so no object carries a `lean`
attribute.
