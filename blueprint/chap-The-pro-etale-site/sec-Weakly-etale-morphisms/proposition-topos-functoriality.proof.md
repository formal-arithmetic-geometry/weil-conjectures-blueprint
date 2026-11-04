+++
kind = "proof"
of = "proposition-topos-functoriality"
order = 40
uses = ["lemma-stability"]
+++
There are two things to check: that the coverings form a subcanonical
topology, and that base change of objects is a morphism of sites.

Identity covers, composites of covers, and base changes of covers are
again covers. For the underlying morphisms this is
Lemma [lemma-stability], and for the finite refinement
condition it is part of the fpqc covering axioms. Representable presheaves
satisfy descent for these covers by fpqc descent for morphisms of
schemes, so they are sheaves, and the topology is subcanonical.

For $f:X\to Y$, the functor $V\mapsto V\times_YX$ sends weakly étale
$Y$-schemes to weakly étale $X$-schemes by
Lemma [lemma-stability]. It preserves fibre products and
the final object, hence finite limits, and it carries covering families
to covering families because fpqc coverings are stable under base change.
Such a functor defines a geometric morphism, whose inverse image $f^{-1}$
is left exact and, as a left adjoint, preserves all colimits. Exactness
on abelian sheaves follows, and compatibility with composition holds
because $(V\times_ZY)\times_YX\simeq V\times_ZX$ canonically. This is the
small-site version of the constructions in [Stacks, [0988](https://stacks.math.columbia.edu/tag/0988)].
