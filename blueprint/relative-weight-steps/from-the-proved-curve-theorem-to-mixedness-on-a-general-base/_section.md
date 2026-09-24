+++
id = "from-the-proved-curve-theorem-to-mixedness-on-a-general-base"
kind = "section"
title = "From the proved curve theorem to mixedness on a general base"
order = 4302
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "def-weil-scheme-morphism-properties", "def-wf-fundamental-representation", "def-wf-iota-real", "def-wf-weil-group", "lem-a1-mixed-direct-summand", "lem-mg-normal-restriction-semisimple", "lem-wf-finite-index-restriction-semisimple", "lem-wf-schur-scalar", "lem-wf-weil-group-constant-extension", "lem-zl-finite-pushforward", "thm-rp-real-lisse-purity-affine"]
+++
The curve estimates are established before this section. The final Weil
statements need only absolute cohomology bounds for the constant sheaf;
the general direct-image theorem below is a stronger intermediate result.
In the chosen reduction, however, successive projections
$\mathbf A^d\to\mathbf A^{d-1}\to\cdots\to\operatorname{Spec}k_0$
produce cohomology sheaves on bases of dimension greater than one.
The next projection needs their finite mixed filtrations. A bound on their individual
Frobenius stalks does not by itself provide the finite filtration required
by [def-weil-punctual-weights]. We obtain that filtration by testing
geometrically irreducible constituents on curves. This is the geometric
reduction underlying Kiehl–Weissauer, I.4.3, pp. 36–38, and its use in
I.7, pp. 52–54; it is placed here after the curve proof of I.6's type.
The rank-one and monodromy arguments already proved for curves are retained.
This bridge belongs to this successive-projection proof; it is not asserted
to be a logically necessary step in every proof of the Weil conjectures.
The supplied August note, *Deligne's Weight Estimate*, gives another
implementation of the relative-curve step in Propositions 5.8–5.9,
pp. 13–14: its explicit TAME and MON inputs provide a controlled smooth
projective family and a boundary filtration, and projective-curve purity
then supplies the relative filtration directly. That route does not use
the general real-sheaf lemma proved here. The present chapter implements
the Kiehl–Weissauer route instead; the shared requirement is a proved
relative-curve estimate, not this particular mixedness lemma.
