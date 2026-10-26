+++
id = "d-central"
kind = "definition"
title = "Positive central pairs"
order = 3747
uses = ["d-monodromy"]
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.IsPositiveCentralPair"]
+++
For the monodromy data $(G,H,F)$ of a represented degree datum
([d-monodromy]), a positive central pair is
$(N,z)$ with $N\in\mathbf Z_{>0}$ and
$z\in Z(G)(k)\cap H(k)F^N$, a $k$-point of $\operatorname{GL}_n$, where
$Z(G)$ is the centre of $G$.

The coset condition does not assert that $G/H$ is infinite cyclic or
that the cosets $HF^N$ for different $N$ are distinct.
