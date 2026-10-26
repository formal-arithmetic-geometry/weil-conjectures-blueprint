+++
id = "det-cor-picard-hilb-sheaf"
kind = "corollary"
title = "Hilbert functor is the fppf sheaf"
order = 760
uses = ["det-thm-picard-descent"]
lean = ["AlgebraicGeometry.isSheaf_hilbertPresheaf", "AlgebraicGeometry.isSheaf_zariskiTopology_hilbertPresheaf"]
+++
Let $X\to S$ be a morphism of schemes and $d\geq0$. By
[det-thm-picard-descent] (D2), $\Hilb^d_{X/S}$ is an fppf (hence
Zariski) sheaf.
