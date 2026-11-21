+++
id = "dag-lem-poincare-compatible-primitive-roots"
kind = "dag-lemma"
title = "A single pro-etale cover gives compatible bases of the abelian root diagram"
name_showing = false
order = 184534
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "lem-poincare-compatible-primitive-roots"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.tateRootsSystem", "AlgebraicGeometry.ProEtale.exists_compatible_roots_diagram_basis"]
uses = ["dag-def-sfb-finite-upper-star", "dag-lem-poincare-integral-residue-free-comparison"]
+++
Let l be a prime, and let X be a scheme with l invertible in Gamma(X,O_X). Let T_n=rootsOfUnitySheaf X (l^n), the actual abelian sheafification of the presheaf of roots, with the lth-power transitions of [dag-def-pur-condensed-tate-twists]. Let C_n be the constant abelian residue diagram constantTateResidueSystem X l of [dag-lem-poincare-integral-residue-free-comparison]. There is a pro-etale cover (u_i:U_i->X) such that T composed with raw upperStar(u_i) is naturally isomorphic to C composed with raw upperStar(u_i) [dag-def-sfb-finite-upper-star]. The diagrams include n=0. This is a statement of abelian sheaves only: it has no integral-module action, coefficient quotient, inverse limit, rational extension or constructibility conclusion.

(SHEAF DAG node `lem-poincare-compatible-primitive-roots`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split.
