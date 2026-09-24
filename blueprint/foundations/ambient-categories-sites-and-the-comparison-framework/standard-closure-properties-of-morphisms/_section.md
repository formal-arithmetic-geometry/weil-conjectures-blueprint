+++
id = "standard-closure-properties-of-morphisms"
kind = "section"
title = "Standard closure properties of morphisms"
order = 1180
uses = ["def-weil-pbc-scheme-conventions"]
+++
The morphism-theoretic facts the rest of the blueprint uses without comment,
proved from the conventions of [def-weil-pbc-scheme-conventions]: finite
implies proper [lem-weil-pbc-finite-proper]; properness is stable under
composition [lem-weil-pbc-proper-composition] and base change
[lem-weil-pbc-proper-base-change] and has closed image
[lem-weil-pbc-proper-closed-image]; closed immersions are proper
[lem-weil-pbc-closed-immersion-proper] and a proper immersion is a closed
immersion [lem-weil-pbc-proper-immersion-closed]; a morphism from a proper
scheme to a separated one is proper [lem-weil-pbc-proper-to-separated]. The
last is what makes the graph constructions of the Chow chapter work.

Two further scheme-theoretic facts stand here that the source states only where
it first needs them, in the proper-base-change chapter: a flat morphism locally
of finite presentation is open [lem-weil-pbc-flat-lfp-open], and a Noetherian
scheme has finitely many irreducible components
[lem-weil-pbc-noetherian-finite-components]. Neither depends on anything, both
are used from four different chapters, and leaving them in the
proper-base-change chapter would make this part depend on it.
