+++
id = "thm-pd-effective-descent"
kind = "theorem"
title = "Effective descent for projective schemes"
lean = ["CategoryTheory.Over.DescentDatum.isEffective_of_isFinite", "CategoryTheory.Over.DescentDatum.isEffective_of_isClosedImmersion", "AlgebraicGeometry.IsQuasiProjective.exists_isAffineOpen_superset", "CategoryTheory.Over.DescentDatum.exists_isInvariant_isAffineOpen_of_fibre", "CategoryTheory.Over.DescentDatum.exists_isInvariant_isAffineOpen", "CategoryTheory.Over.DescentDatum.isEffective_of_isFinite_of_fibre", "CategoryTheory.Over.DescentDatum.isEffective_of_isHProjective"]
order = 893
uses = ["cor-pd-finite-level", "def-pc-finite-locally-free", "def-pc-morphism-conventions", "def-pc-projective-morphism", "def-pd-descent-datum"]
+++
Let $X\to Y$ be a surjective
finite locally free morphism and let $V$
be a scheme over $X$ such that $V\to X$ is
projective. Then every
descent datum on $V$ over $X/Y$ is effective.
