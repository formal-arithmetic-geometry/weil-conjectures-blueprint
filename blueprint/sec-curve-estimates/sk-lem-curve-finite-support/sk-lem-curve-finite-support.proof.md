+++
kind = "proof"
of = "sk-lem-curve-finite-support"
uses = ["sk-prop-sf-comparison", "sk-lem-pbc-finite"]
+++
Work first on the étale sites. Over a strict localization of $C$, a finite
scheme is a finite disjoint union of strictly henselian local schemes. Every
étale cover of such a local scheme has a section over its closed geometric
point, so global sections are exact there. This gives vanishing of the higher
direct images under $h$ and the usual stalk formula, which in turn gives
finite base change. This is the calculation of [sk-lem-pbc-finite]. A finite
set of algebraically closed points has exact sections, which gives the first
assertion. Comparison of classical direct images and [sk-prop-sf-comparison]
transport these statements to the pro-étale site. See (Stacks, Tags 03QP,
0959).
