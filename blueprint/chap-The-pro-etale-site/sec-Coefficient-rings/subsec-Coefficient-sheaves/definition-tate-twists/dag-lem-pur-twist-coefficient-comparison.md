+++
id = "dag-lem-pur-twist-coefficient-comparison"
kind = "dag-lemma"
title = "The canonical coefficient pushout comparison is invertible"
name_showing = false
order = 184523
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-twist-coefficient-comparison"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.purTwistCoefficientComparison_isIso"]
uses = ["dag-def-pur-twist-coefficient-rings"]
+++
For the actual four coefficient sheaves and specified scalar maps [dag-def-pur-twist-coefficient-rings], the canonical morphism purTwistCoefficientComparison from their pushout to the completed coefficient sheaf is an isomorphism. No hypothesis on invertibility of l on the scheme is needed.

theorem purTwistCoefficientComparison_isIso (S : Scheme.{t}) (l : ℕ) [Fact l.Prime]
    (E : Type u) [Field E] [Algebra ℚ_$[l]$ E] [FiniteDimensional ℚ_$[l]$ E] :
    IsIso (purTwistCoefficientComparison S l E)

(SHEAF DAG node `lem-pur-twist-coefficient-comparison`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `lem-weil-l-adic-extension-integers-dvr`.
