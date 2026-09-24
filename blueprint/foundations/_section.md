+++
id = "foundations"
kind = "section"
title = "Shared language and cohomological foundations"
order = 0
+++
Part I of `weil_conjectures_detailed.tex`: the common language of the whole
blueprint. Nothing here is a geometric input to the Weil conjectures; it is
the vocabulary in which the later parts are written, collected in one place so
that no statement downstream rests on an unstated convention.

Eight chapters, in the order in which they are used — the order is a
topological order of the chapter dependency graph, so every chapter stands
after everything it cites. It is not the source's chapter order: the ambient
site chapter stands before the coefficient chapter, because the coefficient
tower is built on the sites.

- [the-karoubi-envelope-and-bounded-t-structures] is pure category theory:
idempotent completion, t-structures, the fact that a bounded t-structure makes
a triangulated category Karoubian, and derived limits in a triangulated
category. It depends on nothing else in the part. The source files all of it
where first used, which made chapters cite each other in both directions; it
is a chapter of its own here.
- [spectral-sequence-machinery] builds the exact-couple and hypercohomology
formalism from scratch, up to the Grothendieck spectral sequence and its
base-change naturality.
- [ambient-categories-sites-and-the-comparison-framework] sets up the small
etale and pro-etale sites, direct and inverse image with the named exchange
morphisms, the strict henselization as a limit, hypercover descent, the
predicates $\mathrm{PBC}$ and $\mathrm{IA}$, and derived completion.
- [conventions-coefficient-categories-and-basic-operations] fixes the
arithmetic and geometric conventions, builds the coefficient tower through
its four stages ($A_{E,n}$, $\mathcal O_E$, $E$, $\Qlb$), and defines the six
operations in triangulated form.
- [weil-structures-frobenius-and-weight-conventions] fixes the arithmetic
vocabulary the conjectures are stated in: local Frobenius and its trace, the
zeta-series normalization, the Poincare trace and cup product, and the three
notions of weight.
- [finite-etale-covers-the-fibre-functor-and-the-fundamental-group]
(chapter 7 of the source) proves the Galois dictionary for finite etale
covers: the fibre functor, the fundamental group, and the forms of it used
downstream.
- [proper-quasi-finite-morphisms-are-finite] (chapter 8 of the source) proves
that proper quasi-finite morphisms are finite, and Zariski's main theorem in
its quasi-finite form.
- [curves] (the first two chapters of Part 3 of the source) is the language of
curves the algebraic-group, abelian-variety, Picard and curve-estimate
material is written in: curves and their constants, the Kummer sequence,
Tsen's theorem, divisors and the Picard functor, Riemann--Roch, duality on
curves, and the Brauer group of a curve.

The dependency graph of the part is acyclic at chapter level and at section
level: the conventions chapter cites the Karoubi chapter, the Weil-structure
and ambient chapters cite the conventions chapter, and the spectral-sequence
chapter cites nothing outside itself. Objects the source files in a section
that cites them but is cited by them are moved to the section they belong to;
each such move is recorded in the body of both sections.

The coefficient chapter also carries the construction half of chapter 6 of the
source, *The pro-etale comparison and coefficient categories*: the comparison
of sites, the constructible finiteness, the rational and $\Qlb$ stages, and
the ambient open--closed recollement. Those six sections build the categories;
the four theorems of that chapter which carry proper base change up them are
not here but in [chap-proper-base-change], continuing its S0--S10 route. The
split is one-way by construction: no object in this part cites the
base-change half.

Reading order is a topological order of the whole `uses` graph: no object in
the part cites anything that comes after it.

Chapters 7 and 8 cite only the ambient-site and spectral-sequence
chapters; [curves] cites them and the conventions, and nothing in the part
cites [curves], so it stands last. Two
general statements they need were filed in [chap-proper-base-change], where
they were first used, and are moved here to keep the part self-contained:
[def-weil-pbc-finite-torsors] to [etale-site-ambient-categories] and
[lem-weil-pbc-surjective-nonempty-fibres] to
[standard-closure-properties-of-morphisms]. Two more, needed by the curve
estimates, moved to [direct-and-inverse-image-and-the-exchange-morphism]:
[lemma-weil-pbc-finite-stalk-formula] and
[lemma-weil-pbc-finite-direct-image-exact]; and four, from the Künneth chapter
and cited by [cohomological-dimension] as well, moved there too: the torsion
cohomological dimension [def-kun-cd] and its vanishing at a separably closed
point [lem-kun-cd-sep-closed-point], with [def-kun-separably-closed] and
[lem-kun-03qu-sep-closed].

One circular proof in the source was repaired rather than refiled.
[thm-sp-if-e1] and [lem-sp-kinjective-computes] cited each other, because the
chapter used $Rv$ on complexes while defining it only on objects, so each of
the two was the only thing that could say what the other meant. The definition
is now stated once, in [def-sp-kinjective-bridge]; the lemma is proved from
K-injectivity alone, and the theorem from the lemma.

The part is self-contained: every `uses` edge recorded inside it resolves
inside it, so this section cites nothing beyond itself and carries no `uses`
list. Nothing in it cites a later part either. The source files some
statements here that need later results; those moved out to where their inputs
are available:

- the compact-support direct image $Rf_!$, its coefficient stages, the
ambient exceptional adjoint, the exceptional inverse image and the
exchange-projection map, which need the compactification coherence
[prop-compactification-coherence-detailed], together with the Weil-structure
definitions on compactly supported cohomology built on them (local Frobenius
traces, the global geometric Frobenius, the Poincare trace and cup product,
weights), are in [compact-support-operations];
- the smooth-proper cohomological family and its reciprocal roots, which need
[prop-cohomological-finiteness], are in [direct-image-finiteness];
- the remark on how exceptional-adjoint admissibility is discharged, which
cites the results that discharge it, is in [verdier-biduality].

Fifteen identifiers of this part already name objects imported earlier from
the sketch sources, which read the same notions at a coarser grain. Those
carry the suffix `-detailed` here so that the two readings coexist:
[def-weil-frobenius-detailed], [def-weil-pbc-proetale-site],
[def-weil-derived-complete-integral-detailed],
[def-coefficient-twists-detailed],
[def-compact-support-direct-image-detailed],
[def-weil-pbc-cartesian-square],
[def-weil-pbc-underived-exchange],
[def-weil-pbc-derived-exchange],
[def-weil-pbc-pointed-etale-neighbourhoods],
[def-weil-pbc-strict-henselization-limit],
[def-weil-pbc-property],
[prop-weil-pbc-strict-henselization-stalk-formula],
[def-weil-pbc-finite-section-pullback],
[def-weil-pbc-completed-pullback], and the section
[triangulated-coefficient-categories-detailed].

Few objects of this part carry a `lean` attribute: the point-count
definition [def-weil-point-counts-zeta], the étale open--closed lemmas of
[etale-sheaves-along-a-complementary-open-closed-pair], and the formalized
account of constructible étale sheaves [constructible-sheaves-formalized],
which the detailed route does not cite.
