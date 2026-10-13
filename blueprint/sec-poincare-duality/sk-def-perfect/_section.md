+++
id = "sk-def-perfect"
kind = "definition"
title = "Perfectness at the point and on $X$"
order = 2756
uses = ["sk-def-ops"]
lean = ["CategoryTheory.IsDualizable"]
tags = ["sketch"]
+++
In the setting of [sk-def-ops], an object $K$ of a symmetric monoidal
category $(\mathcal C,\otimes,\mathbf 1)$ is *dualizable* if it has a
right dual: an object $K^\vee$ with an evaluation
$K^\vee\otimes K\to\mathbf 1$ and a coevaluation
$\mathbf 1\to K\otimes K^\vee$ satisfying the two triangle identities.
A *perfect point complex* is a dualizable object of the derived category
of $\Lambda$-modules for $\otimes^L_\Lambda$, and an object
$K\in D(X_{\mathrm{proet}},\Lambda)$ is *perfect over $\Lambda_X$* if
it is dualizable in $D(X_{\mathrm{proet}},\Lambda)$ for
$\otimes^L_{\Lambda_X}$, with unit $\Lambda_X$.

Equivalently, a perfect point complex is a complex of $\Lambda$-modules
quasi-isomorphic to a bounded complex of finite projective
$\Lambda$-modules (over a field: a bounded complex with
finite-dimensional cohomology), and $K$ is perfect over $\Lambda_X$ if
and only if it is locally quasi-isomorphic to a bounded complex of
finite projective $\Lambda_X$-modules.
