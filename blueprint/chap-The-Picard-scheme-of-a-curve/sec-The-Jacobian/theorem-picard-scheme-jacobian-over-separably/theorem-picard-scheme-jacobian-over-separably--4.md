+++
id = "theorem-picard-scheme-jacobian-over-separably--4"
kind = "theorem"
title = "The tangent-space identification"
name_showing = false
order = 1549004
aliases = ["bp-r483-4"]
lean = []
uses = ["theorem-picard-scheme-jacobian-over-separably--3", "lemma-tangent-space-picard-functor"]
+++
The Lean proof of the main theorem bypasses this tangent-space
identification; the supplied source contains no declaration proving it.

For the Jacobian of [theorem-picard-scheme-jacobian-over-separably--3],
the classical identification is

$$
T_0J(C)\simeq H^1(C,\mathcal O_C).
$$

The human argument uses [lemma-tangent-space-picard-functor]. The
name `AlgebraicGeometry.nonempty_tangentSpaceAt_linearEquiv_H_one`
occurs only in comments in the supplied source, so it is not a Lean
tag for this statement.
