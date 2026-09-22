+++
id = "rem-pd-scope"
kind = "remark"
title = "What changed relative to the separably closed case"
order = 4726
tags = ["latex:remark"]
uses = ["thm-pd-jacobian-general-field", "thm-pd-geometric-pic0", "thm-pd-effective-descent", "thm-pd-spreading-out"]
+++
[thm-pd-jacobian-general-field] is the statement that the Jacobian chapter's
scope remark declares to lie outside the scope of that chapter. The route
taken here is the descent route: the theorem is proved over a separable
closure by [thm-pd-geometric-pic0] and then descended, so that neither
Grothendieck's existence theorem in the presence of a rational point nor a
choice of a base point enters.

In particular the hypothesis that $k$ be separably closed in the Picard
chapter's representability theorem and in the Jacobian chapter's existence
theorem is used only to manufacture a $k$-rational point, as the proof of the
former records through the density of rational points on a smooth scheme over
a separably closed field; over an arbitrary ground field the rational point is
unnecessary.

## Proof

The comparison of scopes is immediate from the statements: the Jacobian
chapter's scope remark asserts that representability over a general ground
field is not proved there and would require a descent from a finite separable
extension, while [thm-pd-jacobian-general-field] supplies exactly that
descent, with the two ingredients named in that remark replaced by
[thm-pd-effective-descent] (Stacks Project, Lemma 39.25.3, [Tag
0CCJ](https://stacks.math.columbia.edu/tag/0CCJ)) and [thm-pd-spreading-out]
(Stacks Project, Lemma 32.10.1, [Tag
01ZM](https://stacks.math.columbia.edu/tag/01ZM)).

That the separable closedness of the two cited theorems serves only to produce
a rational point is visible in the proof of the Picard chapter's theorem,
which obtains $\sigma$ from the density of rational points and then applies
the hypothesis-checking lemma for curves with a rational point; the rational
point is what [thm-pd-geometric-pic0] supplies geometrically and what the
descent of [thm-pd-jacobian-general-field] replaces.

Unresolved dependencies: rem:sc-jacobian-scope, thm:pc-picard-representable, thm:sc-jacobian-representability, lem:pc-rational-points-dense, lem:pc-rational-hyp
