+++
id = "sk-d-central"
kind = "definition"
title = "Positive central pairs"
order = 2862
uses = ["sk-d-geometry", "sk-d-monodromy"]
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.IsPositiveCentralPair"]
tags = ["sketch"]
+++
For data $(G,H,F)$, a positive central pair is
$(N,z)$ with $N\in\mathbf Z_{>0}$ and
$z\in\hyperref[sk-d-geometry]{Z(G)}(k)\cap H(k)F^N$, a $k$-point of
$\GL_n$.
The coset condition does not assert that $G/H$ is infinite cyclic or
that the cosets $HF^N$ for different $N$ are distinct.
