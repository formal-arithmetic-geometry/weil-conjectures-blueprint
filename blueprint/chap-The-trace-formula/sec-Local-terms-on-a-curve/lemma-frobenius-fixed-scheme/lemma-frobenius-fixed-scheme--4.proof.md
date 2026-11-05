+++
kind = "proof"
of = "lemma-frobenius-fixed-scheme--4"
order = 959009
uses = ["lemma-frobenius-fixed-scheme--2"]
+++
The structure morphism is finite by [lemma-frobenius-fixed-scheme--2],
hence proper. In `IsModelFrobenius.graphFixedLocus`, the fixed locus is
chosen to be the coproduct of the fixed rational points, and
`WeilBoundedConstructible.trace_globalOperator_graph_eq_sum` obtains its
properness from the finite structure morphism by instance inference.
