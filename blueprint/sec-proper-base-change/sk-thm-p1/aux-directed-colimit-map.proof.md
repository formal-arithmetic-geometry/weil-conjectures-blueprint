+++
kind = "proof"
of = "aux-directed-colimit-map"
+++
For each open U, evaluate the sheaf colimit cocone at U. Its point is (colimit D)(U), and its legs are the component maps of colimit.ι D i. Apply colimit.desc to this cocone of sets. The coprojection equation colimit.ι_desc gives the required formula for every section. No sheafification or directedness argument is needed. (`CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean))).
