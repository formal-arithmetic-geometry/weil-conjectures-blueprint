+++
id = "lem-weil-pbc-retract-supplied"
kind = "lemma"
title = "Retract supplied by a proper surjection"
lean = ["AlgebraicGeometry.Etale.mono_homEquiv_of_surjective"]
order = 1925
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $f:X\to Y$ be surjective, let $\Lambda$ be a commutative ring, let $I$ be a
sheaf of $\Lambda$-modules on $Y_{\Et}$ and let $\iota:f^{-1}I\hookrightarrow J$ be
a monomorphism into a sheaf of $\Lambda$-modules $J$ on $X_{\Et}$. Then the
adjoint map

$$
 I\longrightarrow f_*J
$$

of the direct image adjunction [def-weil-pbc-direct-image] is a monomorphism. In
particular, if $I$ is injective, this monomorphism has a retraction
$f_*J\to I$, so $I$ is a direct summand of $f_*J$.
