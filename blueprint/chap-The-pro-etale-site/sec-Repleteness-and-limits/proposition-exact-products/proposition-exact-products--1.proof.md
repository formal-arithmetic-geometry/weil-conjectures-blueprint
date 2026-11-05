+++
kind = "proof"
of = "proposition-exact-products--1"
order = 88003
uses = ["corollary-evaluation-weakly-contractible-objects"]
+++
The product functor is additive and preserves finite limits. To prove
that it also preserves finite colimits, it suffices to show that it
takes exact short complexes of families to exact short complexes.

By Corollary [corollary-evaluation-weakly-contractible-objects](3), this
can be checked on sections over affine weakly contractible objects $W$.
By part (2) of that corollary, evaluation at $W$ is exact and commutes
with products. The evaluated family is therefore exact, and its product
is exact in the category of $\mathcal R(W)$-modules. Here exactness is
coordinatewise, with the axiom of choice supplying simultaneous lifts.
The comparison between evaluation of a product and the product of the
evaluations identifies this exact short complex with the evaluation of
the original product. Part (3) now detects its exactness.
