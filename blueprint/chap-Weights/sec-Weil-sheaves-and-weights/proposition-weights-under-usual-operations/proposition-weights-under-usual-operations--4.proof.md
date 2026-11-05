+++
kind = "proof"
of = "proposition-weights-under-usual-operations--4"
order = 1070005
uses = ["proposition-weights-under-usual-operations--5"]
+++
Choose bounds $a$ and $b$ for the two outer terms and replace them by
$\max(a,b)$, using
`AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.mono_weight`.
Apply [proposition-weights-under-usual-operations--5]. Mixedness is the
existence of an upper bound; Lean's extension lemma retains that bound
explicitly, rather than stating a separate unbounded extension lemma.
