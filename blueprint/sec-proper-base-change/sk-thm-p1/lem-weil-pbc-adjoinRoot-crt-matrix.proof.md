+++
kind = "proof"
of = "lem-weil-pbc-adjoinRoot-crt-matrix"
+++
Let R=A/I, assumed nonzero. Monicity preserves the degree of f under coefficient reduction. The coordinates of the power basis of AdjoinRoot f reduce to the power basis of AdjoinRoot of fbar. Multiplication matrices reduce entrywise: products of representatives are computed by division by the monic polynomial, and division and remainder commute with coefficient reduction. This follows by uniqueness of remainder and reducing the monic division identity. (`AdjoinRoot.powerBasis'` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdjoinRoot.lean))).

For fbar=g*h, coprimality gives comaximal ideals (g) and (h). Ideal.isCoprime_span_singleton_iff and Ideal.quotientMulEquivQuotientProd give the algebra-compatible CRT isomorphism AdjoinRoot fbar to AdjoinRoot g times AdjoinRoot h. The two components are the quotient maps, so the root maps to the pair of roots and the residue of e maps to (1,0).

Concatenate the power bases of the two factors. Monicity over nonzero R gives deg f=deg g+deg h. Hence their sum index type is equivalent to Fin deg f. Reindex the reduced basis along this equivalence d. The coordinate isomorphism to the concatenated basis is invertible; its matrix is a unit U. Its inverse is the inverse coordinate map, and their matrix products are identities by LinearMap.toMatrix_comp. (`AdjoinRoot.powerBasis'` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdjoinRoot.lean))).

The CRT algebra equivalence intertwines multiplication. Multiplication by the pair of roots is block diagonal with the respective root matrices. Multiplication by (1,0) is the first projection with blocks 1,0,0,0. Applying the matrix-of-composition identity gives both conjugation identities with the same U. Degree-zero factors have the empty power basis, so no nontriviality assumption on either factor algebra is needed.
