+++
id = "dag-lem-pur-twist-integral-basis"
kind = "dag-lemma"
title = "The coefficient extension integers have a finite Z_l basis"
name_showing = false
order = 184525
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-twist-integral-basis"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.purTwistIntegralBasis"]
uses = ["dag-def-pur-twist-coefficient-rings"]
+++
The integral coefficient ring O_E of [dag-def-pur-twist-coefficient-rings], with its specified Z_l action, admits a basis indexed by Fin k for some finite k.

theorem purTwistIntegralBasis (l : ℕ) [Fact l.Prime]
    (E : Type u) [Field E] [Algebra ℚ_$[l]$ E] [FiniteDimensional ℚ_$[l]$ E] :
    ∃ k : ℕ, Nonempty (@Module.Basis (Fin k) ℤ_$[l]$
        (Padic.coefficientExtensionIntegers l E) _ _
        (Module.compHom (Padic.coefficientExtensionIntegers l E) (purTwistIntegersMap l E)))

(SHEAF DAG node `lem-pur-twist-integral-basis`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `lem-weil-l-adic-extension-integers-dvr`.
