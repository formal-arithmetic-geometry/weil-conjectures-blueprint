+++
kind = "proof"
of = "proposition-cohomology-smooth-affine-curve--4"
order = 1579007
uses = ["proposition-cohomology-smooth-affine-curve--2", "proposition-cohomology-smooth-affine-curve--3", "lemma-proper-smooth-model", "corollary-serre-duality-field-extension", "theorem-bounded-below-cohomology-comparison"]
+++
The pullback map is injective by
`AlgebraicGeometry.injective_cohomologyMap_pullback_fst_of_isAlgClosed`.
Indeed, a class which dies after extension to $k'$ dies after extension
to a finitely generated $k$-subalgebra of $k'$, by continuity of étale
cohomology. A $k$-point of its spectrum supplies a section, so the
original class is zero.

Choose a smooth proper connected compactification
$U\hookrightarrow\overline C$ as in [lemma-proper-smooth-model]. Its base
change is a smooth proper connected compactification of $U_{k'}$.
The genus is unchanged by [corollary-serre-duality-field-extension].
Each boundary point is $k$-rational, so the boundary has the same number
of points after extension; this is
`AlgebraicGeometry.Compactification.natCard_compl_baseChangeField`.

For $q=0$, both groups have order $n$ by
[proposition-cohomology-smooth-affine-curve--2]. For $q=1$, apply
[proposition-cohomology-smooth-affine-curve--3] to the two
compactifications and cancel the positive factor $n$. The two finite
groups have the same order, so the injective pullback is bijective.
For $q>1$, both groups vanish by
[proposition-cohomology-smooth-affine-curve--2]. The constant coefficient
sheaf pulls back to the constant coefficient sheaf, and
[theorem-bounded-below-cohomology-comparison] transports the calculation
to the chapter's cohomology convention.
