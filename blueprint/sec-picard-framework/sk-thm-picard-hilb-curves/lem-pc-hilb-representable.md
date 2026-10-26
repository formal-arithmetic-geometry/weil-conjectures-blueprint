+++
id = "lem-pc-hilb-representable"
kind = "lemma"
title = "Hilbert schemes of points are representable"
order = 769
uses = ["def-pc-finite-locally-free", "def-pc-fppf-site", "def-sc-ample"]
lean = ["AlgebraicGeometry.isRepresentable_hilbertPresheaf"]
+++
Let $X\to S$
be a separated morphism of schemes and $d\geq0$. Assume that for all points
$s\in S$ and $x_1,\dots,x_d\in X_s$ (a finite set of points of a fibre)
there exists an affine open $U\subset X$ containing them
(e.g. if $X\to S$ is quasi-projective, or if there exists an ample
invertible sheaf on $X$). Then $\operatorname{Hilb}^d_{X/S}$ is representable by a
scheme $\underline{\operatorname{Hilb}}^d_{X/S}$. (Separatedness cannot be
dropped: for $d=1$ the affine-open hypothesis is vacuous, but for the
affine line with doubled origin over a field $\operatorname{Hilb}^1$ is not
representable, by Lundkvist–Skjelnes.)
