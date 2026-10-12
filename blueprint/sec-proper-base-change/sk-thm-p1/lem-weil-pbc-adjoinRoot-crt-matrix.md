+++
id = "lem-weil-pbc-adjoinRoot-crt-matrix"
kind = "lemma"
title = "Simultaneous CRT coordinates for reduced root and idempotent-lift multiplication matrices"
lean = ["Polynomial.adjoinRoot_crt_matrix"]
source = "literature/stacks-project/more-algebra.tex, Tag 09XI, lemma-characterize-henselian-pair, proof of (3) implies (1), B/IB product decomposition; its coordinate and matrix details written out by E2"
+++
Let A be a commutative ring, I an ideal with nonzero R=A/I, f in A[X] monic, and g,h in R[X] monic and coprime with fbar=g*h. Let e in AdjoinRoot f have images 1 and 0 in AdjoinRoot g and AdjoinRoot h under the canonical coefficient-reduction quotient maps. Let T,P be multiplication by the root and by e in the power basis of AdjoinRoot f, and Tg,Th the root multiplication matrices in the power bases of AdjoinRoot g and AdjoinRoot h `AdjoinRoot.powerBasis'` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdjoinRoot.lean)). There exist an index equivalence d: Fin deg f ≃ Fin deg g ⊕ Fin deg h and an invertible matrix U over R on this sum index such that U reindex_d(Tbar) U^-1 = blockdiag(Tg,Th) and U reindex_d(Pbar) U^-1 = blockdiag(1,0).
