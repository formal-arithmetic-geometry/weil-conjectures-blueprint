+++
id = "dag-lem-pur-twist-root-transitions"
kind = "dag-lemma"
title = "Prime-power roots have epimorphic power transitions"
name_showing = false
order = 184528
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-twist-root-transitions"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.purTwistRootTransitions_epi"]
uses = ["dag-def-pur-roots-of-unity-sheaf"]
+++
For any scheme S on which l is invertible in every residue field, the canonical l-th-power transition from the roots of order l^(n+2) to the roots of order l^(n+1) [dag-def-pur-roots-of-unity-sheaf] is an epimorphism for every natural n.

theorem purTwistRootTransitions_epi (S : Scheme.{u}) (l : ℕ) [Fact l.Prime]
    [∀ x : S, Invertible (l : S.residueField x)] (n : ℕ) :
    Epi (proEtaleRootsOfUnityTransition S (l ^ (n + 1)) (l ^ (n + 2))
      (pow_pos (Fact.out : l.Prime).pos _) (pow_pos (Fact.out : l.Prime).pos _)
      (pow_dvd_pow l (Nat.le_succ (n + 1))))

(SHEAF DAG node `lem-pur-twist-root-transitions`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split.
