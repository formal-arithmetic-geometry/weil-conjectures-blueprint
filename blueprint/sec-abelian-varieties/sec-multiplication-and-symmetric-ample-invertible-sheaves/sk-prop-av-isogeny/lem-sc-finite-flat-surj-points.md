+++
id = "lem-sc-finite-flat-surj-points"
kind = "lemma"
title = "Finite surjections are surjective on $k$-points"
lean = ["AlgebraicGeometry.exists_comp_eq_of_isFinite_of_surjective"]
order = 553
uses = ["lem-sc-finite-nonempty-point"]
+++
Let $k$ be algebraically closed and $f:X\to Y$ a finite surjective
morphism of schemes. Then every morphism $y:\Spec k\to Y$ lifts to a
morphism $x:\Spec k\to X$ with $f\circ x=y$. In particular, if $f$ is
a morphism of $k$-schemes, then $f(X(k))=Y(k)$.
