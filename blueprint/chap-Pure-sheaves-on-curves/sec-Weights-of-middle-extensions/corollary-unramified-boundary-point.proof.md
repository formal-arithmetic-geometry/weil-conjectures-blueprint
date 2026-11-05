+++
kind = "proof"
of = "corollary-unramified-boundary-point"
order = 1184
uses = ["proposition-sp-unique-adjoint", "theorem-trace-formula-euler-product", "lemma-filtrations-spectra", "proposition-lattices-representations-normal-scheme", "lemma-degree-zero-top-cohomology", "lemma-boundary-stalk", "lemma-point-count-bound", "proposition-weights-j-boundary-points", "lemma-cohomological-range-curve", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Purity follows from the upper bounds for the sheaf and for its dual,
provided the stalk of the dual is the dual of the stalk, and trivial
inertia guarantees this. So we apply
Proposition [proposition-weights-j-boundary-points] to the sheaf and to its
dual, which is pure of weight $-a$.  Since the inertia acts trivially,
the stalk of the extended dual is the dual of the stalk of the
extension, and so every eigenvalue $\alpha$ satisfies
$|\iota\alpha|^2\le q_z^a$ and $|\iota\alpha^{-1}|^2\le q_z^{-a}$, and
equality holds.

For a sheaf that is already lisse on the curve, the inertia is trivial, and
Lemma [lemma-boundary-stalk] identifies the stalk of $j_*$ with the
original stalk. The first assertion, applied at each of the finitely many
points outside the dense open, then gives the second.
