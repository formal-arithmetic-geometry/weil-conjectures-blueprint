+++
kind = "proof"
of = "lem-weil-pbc-etale-module-sheaf-nonzero-section-universe"
+++
For any type A in the scheme universe, form the disjoint union V of copies of U indexed by A. Its structure map to X is etale by locality at the source. Its summand inclusions form a covering family, with pairwise disjoint images. (`AlgebraicGeometry.instHasColimitsOfShapeDiscreteSchemeOfSmall, AlgebraicGeometry.sigmaOpenCover, AlgebraicGeometry.disjoint_opensRange_sigmaι` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Limits.lean))).

Put E=F(U). For each a in A prescribe maps E to F(U) equal to the identity on summand a and zero on other summands. These maps are compatible: on the same summand use monicity of its inclusion; a common source of distinct summands is empty, whose section module is terminal by the empty covering. Apply the module-valued sheaf condition to obtain t(a): E to F(V).

If t(a)=t(b) with a different from b, restrict to summand a to obtain id_E=0. Evaluation at s contradicts s nonzero. Thus t embeds A in the type of maps E to F(V), a type in the coefficient universe. Mathlib small_of_injective gives Small A. Since A was arbitrary this is UnivLE. Empty A causes no problem; empty U or the zero ring cannot have a nonzero section.
