+++
id = "the-karoubi-envelope-and-bounded-t-structures"
kind = "section"
title = "The Karoubi envelope and bounded t-structures"
order = 1321
uses = ["def-weil-pbc-derived-categories"]
+++
The subsection of the source that shows the coefficient categories need no
formal completion. The Karoubi envelope [def-weil-karoubi-envelope] is
constructed, shown to receive its category fully faithfully
[lem-weil-karoubi-envelope-fully-faithful], to be idempotent complete
[lem-weil-karoubi-envelope-idempotent-complete], and to be triangulated when
its input is [lem-weil-karoubi-envelope-triangulated]; a t-structure
[def-weil-t-structure] has abelian heart [prop-weil-heart-abelian] and is
inherited by the envelope [lem-weil-envelope-tstructure].

The point of all of it is [thm-weil-karoubian-bounded-t]: a triangulated
category carrying a bounded t-structure is already idempotent complete. That
is what lets the rationalized category
[def-weil-rationalization-karoubi] and the common-stage category
[def-weil-algebraically-closed-coefficients] be defined without formally
adjoining idempotents, which is how
[lem-weil-rationalization-idempotent-complete],
[lem-weil-qbar-idempotent-complete] and
[lem-weil-weil-complex-qbar-idempotent-complete] are proved in the
conventions chapter.

In the source this subsection heading is not closed before the pro-etale
block that follows it, which was moved in from part 2 and has nothing to do
with Karoubi envelopes. That block is classified here as direct content of
[complete-rational-and-algebraically-closed-coefficients] instead.

Several statements here carry long *Source note* paragraphs recording that no
Stacks Project entry states the form proved, together with the nearest entry
and what the blueprint adds. They are kept verbatim: they say what is and is
not discharged.
