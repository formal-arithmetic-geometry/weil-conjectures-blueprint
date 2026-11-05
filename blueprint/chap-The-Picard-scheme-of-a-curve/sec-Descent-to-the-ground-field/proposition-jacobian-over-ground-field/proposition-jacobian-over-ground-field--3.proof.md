+++
kind = "proof"
of = "proposition-jacobian-over-ground-field--3"
order = 1562009
uses = ["proposition-jacobian-over-ground-field--1", "proposition-jacobian-over-ground-field--2"]
+++
Apply [proposition-jacobian-over-ground-field--2] to $k'=\bar k$ and
the representation $r$ of [proposition-jacobian-over-ground-field--1].
In `AlgebraicGeometry.exists_jacobian_descent`, this representation is
constructed by `CategoryTheory.Functor.RepresentableBy.ofAdjunction`
followed by the canonical Picard base-change isomorphism. Evaluating
this composite on $T$ gives the stated compatibility with $r$.
