+++
id = "sk-prop-br-inj"
kind = "proposition"
title = "Generic-point injection for the Brauer group"
order = 906
uses = ["sk-def-br", "sk-prop-hilbert90"]
lean = ["AlgebraicGeometry.Scheme.injective_cohomologyMap_gmSheaf_two"]
tags = ["sketch"]
+++
Let $X$ be an integral regular noetherian scheme (as in
[sk-prop-divisor-gen]) with function field $k(X)$ and generic point
$\eta=\Spec k(X)\to X$. Then (Grothendieck's residue sequence) the
pullback map along $\eta$ is injective:

$$
\Br(X)=H^2(X,\mathbb G_m)\hookrightarrow
H^2(\eta,\mathbb G_m)=\Br(k(X)).
$$

In particular this holds for $C$ a smooth curve.
