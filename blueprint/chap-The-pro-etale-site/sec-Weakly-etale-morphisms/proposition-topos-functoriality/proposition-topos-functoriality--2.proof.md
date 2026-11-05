+++
kind = "proof"
of = "proposition-topos-functoriality--2"
order = 39004
+++
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

*Source:* the proof of Proposition [proposition-topos-functoriality].
