+++
id = "rem-pur-assembly-status"
kind = "remark"
title = "Status of the assembly"
order = 2693
uses = ["def-exc-direct-image-input", "def-exc-open-complement-bound", "lem-exc-open-complement-known", "thm-dg-finite-type-constructibility", "thm-exc-direct-image-input-holds", "thm-sc-finite-type-torsion-cd"]
+++
The only hypothesis of [thm-pur-general-admissibility] is the
open-complement condition
([def-exc-open-complement-bound]) for the finitely many complements of
the affine charts inside affine space; the ambient exceptional right adjoint
datum, which is false in general, is not one, the right adjoints the
assembly forms on the coefficients it quantifies over being those relative
to the bounded-below objects of étale origin of
[thm-sf-ambient-adjoint-class]. The open-complement condition is a theorem of this
blueprint, not an assumption: [lem-exc-open-complement-known] derives
it with $c=2d$ from the two clauses of the direct-image finiteness input
[def-exc-direct-image-input], which are
[thm-dg-finite-type-constructibility] of the constructibility chapter and
[thm-sc-finite-type-torsion-cd] of the Jacobian chapter,
assembled as [thm-exc-direct-image-input-holds], and
[thm-pur-open-complement-unconditional] records the same two clauses with
a constant independent of the coefficient ring and hence of the coefficient
stage. Consequently
[thm-pur-general-admissibility] and
[cor-pur-general-admissibility-datum] prove the two preservation
clauses for an arbitrary separated finite-type morphism without further
hypotheses, on the coefficients of the blueprint's class. No
affineness of the base is needed: the passage from the affine opens of
$Y$ to $Y$ itself uses the base-change compatibility of the right
adjoint along an open immersion, which is proved in the chapter on
exceptional right adjoints
([cor-exc-base-change-open-immersion-general]) and is read here in its
class form, for the right adjoints relative to the bounded-below objects
of étale origin, where it holds without the ambient datum.
