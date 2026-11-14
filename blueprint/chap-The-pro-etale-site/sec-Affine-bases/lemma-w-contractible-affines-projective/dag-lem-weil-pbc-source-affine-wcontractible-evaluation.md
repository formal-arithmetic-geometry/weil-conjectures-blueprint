+++
id = "dag-lem-weil-pbc-source-affine-wcontractible-evaluation"
kind = "dag-lemma"
title = "Closed full-site evaluation at a geometrically w-contractible affine object"
name_showing = false
order = 69502
tags = ["sheaf-dag"]
split_from = "lemma-w-contractible-affines-projective--1"
dag_id = "lem-weil-pbc-source-affine-wcontractible-evaluation"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.ProEt.isWeaklyContractible_of_iso"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-det-pe-wlocal-strict-contractible", "dag-sk-def-pe-weak-contractible", "dag-sk-def-pe-wlocal"]
+++
Let T be a scheme `def-pc-scheme`, W an object of the small pro-etale site of T [dag-def-weil-pbc-proetale-site], and R a commutative ring. Suppose W.left is isomorphic to Spec R `def-weil-affine-spectrum` and R is geometrically w-contractible: Spec R is w-local, every maximal localization is strictly henselian, and its connected-component space is extremally disconnected (the source class IsWContractibleRing R). Then for any universe w, every locally surjective morphism F to G of sheaves valued in Type w is surjective on W-sections. Equivalently W satisfies the source predicate (ProEt.topology T).IsWeaklyContractible. In the section universe u+1 this applies to every epimorphism, by the site sheaf-sets epi/local-surjectivity equivalence `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`. No nonempty or nontrivial hypothesis is imposed.

(SHEAF DAG node `lem-weil-pbc-source-affine-wcontractible-evaluation`; machine-alignment layer.) Split from [lemma-w-contractible-affines-projective--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-affine-spectrum`, `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`.
