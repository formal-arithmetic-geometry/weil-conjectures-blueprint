+++
kind = "proof"
of = "lem-weil-pbc-fpqc-descend-finite"
+++
Use the already proved source declaration AlgebraicGeometry.IsFinite.descendsAlong_surjective_inf_flat_inf_quasicompact (WeilConjectures.Mathlib.AlgebraicGeometry.Morphisms.FlatDescent, Tag 02LA) to install descent of finiteness along surjective flat quasi-compact morphisms. Its proof combines descent of affineness with universal closedness and local finite type; no unfinished Sheaf lemma is needed.

The given fpqc precover generates a covering sieve, by Precoverage.generate_mem_toGrothendieck. Specialize the already proved source declaration AlgebraicGeometry.Scheme.of_isPullback_of_ofArrows_mem_fpqcTopology (WeilConjectures.Mathlib.AlgebraicGeometry.Sites.Fpqc) to the property IsFinite, the two canonical pullback projections, and IsPullback.of_hasPullback. Finiteness is Zariski local at the target and stable under base change by Mathlib. The hypotheses give finiteness of every second projection, and covering-family descent gives finiteness of f.
