+++
id = "the-karoubi-envelope-and-bounded-t-structures"
kind = "section"
title = "Karoubi envelopes, t-structures, and derived limits"
order = 1102
+++
Pure category theory, placed first because the coefficient chapter needs it
and it needs nothing in return. The Karoubi envelope
[def-weil-karoubi-envelope] is constructed over an arbitrary additive
category, shown to receive that category fully faithfully
[lem-weil-karoubi-envelope-fully-faithful], to be idempotent complete
[lem-weil-karoubi-envelope-idempotent-complete], and to be triangulated when
its input is [lem-weil-karoubi-envelope-triangulated]; a t-structure
[def-weil-t-structure] on a triangulated category has abelian heart
[prop-weil-heart-abelian] and is inherited by the envelope
[lem-weil-envelope-tstructure].

The point of all of it is [thm-weil-karoubian-bounded-t]: a triangulated
category carrying a bounded t-structure is already idempotent complete. That
is what lets the rationalized category [def-weil-rationalization-karoubi] and
the common-stage category [def-weil-algebraically-closed-coefficients] be
defined without formally adjoining idempotents, which is how
[lem-weil-rationalization-idempotent-complete],
[lem-weil-qbar-idempotent-complete] and
[lem-weil-weil-complex-qbar-idempotent-complete] are proved in the
conventions chapter.

In the source this is a subsection of chapter 4, and the heading is never
closed before a pro-etale block moved in from part 2, so the block reads as
part of it. Both placements are corrected here. Nothing in the source's
chapter 4 uses this material; only chapter 1 does, and reading it as a
subsection of chapter 4 is what made chapters 1 and 4 depend on each other in
both directions. Read as its own chapter, placed first, it depends on nothing
and the part becomes acyclic at chapter level.

The two `uses` edges the source records here, from
[def-weil-karoubi-envelope] and [def-weil-t-structure] to the etale derived
category [def-weil-pbc-derived-categories], are dropped: both definitions are
stated over an abstract additive or triangulated category and neither mentions
a scheme, a site or a sheaf. They were the citation of the nearest concrete
triangulated category in the source, not a dependence on it.

Several statements here carry long *Source note* paragraphs recording that no
Stacks Project entry states the form proved, together with the nearest entry
and what the blueprint adds. They are kept verbatim: they say what is and is
not discharged.

The derived limit of an inverse system in a triangulated category
[def-weil-derived-limit], and its existence [lem-weil-derived-limit-existence],
stand here too. The source states them in the coefficient chapter, where they
are first used, but they depend on nothing, and leaving them there was the only
thing making the ambient chapter cite the coefficient chapter --- which, once
the pro-etale coefficient tower is filed in the coefficient chapter, would have
made those two chapters cite each other in both directions. The identifier of
this chapter still reads `the-karoubi-envelope-and-bounded-t-structures`; only
the title records the wider contents.
