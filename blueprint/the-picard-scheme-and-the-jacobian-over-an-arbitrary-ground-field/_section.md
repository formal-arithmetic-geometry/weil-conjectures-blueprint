+++
id = "the-picard-scheme-and-the-jacobian-over-an-arbitrary-ground-field"
kind = "section"
title = "The Picard scheme and the Jacobian over an arbitrary ground field"
order = 4700
+++
This chapter supplies what the Jacobian chapter's scope remark declares to be
outside its scope: the representability of $\operatorname{Pic}_{C/k}$, and
the existence of the Jacobian, for a geometrically integral smooth
projective curve over an *arbitrary* ground field.

*The route (descent).* The separably closed case is the Picard chapter
(Stacks Proposition 44.6.6, [Tag
0B9Z](https://stacks.math.columbia.edu/tag/0B9Z)) together with the theorem
of the base of the Jacobian chapter (Stacks Lemma 44.6.7, [Tag
0BA0](https://stacks.math.columbia.edu/tag/0BA0)). The Picard functor itself
is defined over the ground field $k$, so its representing object over a
separable closure $k_s$ carries a *canonical* descent datum relative to
$k_s/k$: the datum is produced by Yoneda from the identification of
functors, and no Galois action has to be chosen. Effectivity is reduced to a
finite level: the finitely presented data (the scheme, a projective
embedding, the descent isomorphism, the cocycle equation) spread out to a
finite separable subextension $K/k$ by Stacks Lemma 32.10.1 ([Tag
01ZM](https://stacks.math.columbia.edu/tag/01ZM)), and along the resulting
finite locally free cover the descent datum is effective by Stacks Lemma
39.25.3 ([Tag 0CCJ](https://stacks.math.columbia.edu/tag/0CCJ)). The group
law descends because pullback to the cover is fully faithful on descent
data, and the geometric properties descend because they are local in the
fpqc topology on the target.

*No $k$-rational point of $C$ is used anywhere in this chapter.* This is the
point of the route: the step "choose a separably closed point so that the
curve acquires a rational point" is not needed.

Unresolved dependencies: thm:pc-picard-representable, thm:sc-theorem-of-the-base, thm:sc-jacobian-representability, def:sc-jacobian, lem:sc-jacobian-unique, rem:sc-jacobian-scope
