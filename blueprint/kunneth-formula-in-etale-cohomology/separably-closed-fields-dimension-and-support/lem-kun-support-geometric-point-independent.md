+++
id = "lem-kun-support-geometric-point-independent"
kind = "lemma"
title = "The support does not depend on the chosen geometric point"
order = 6013
lean = ["AlgebraicGeometry.Etale.support_indep_geometricPoint"]
uses = ["lem-kun-stalk-as-pullback", "def-kun-support"]
+++
Let $X$ be a scheme, $x\in X$, and let $\bar x,\bar x'$ be geometric points
of $X$ with image $x$. For every étale sheaf $F$ on $X_{\Et}$ one has
$F_{\bar x}=0$ if and only if $F_{\bar x'}=0$; consequently the support
[def-kun-support] of $F$ is independent of the chosen geometric point over
each of its points.

## Proof

Write $i:\Spec\kappa(x)\to X$ for the canonical point of $x$. Both $\bar x$
and $\bar x'$ factor through $i$, say $\bar x=a\circ i$ and
$\bar x'=a'\circ i$, where $a$ and $a'$ are the structure maps of the
separably closed extensions $\Omega/\kappa(x)$ and $\Omega'/\kappa(x)$.

The stalks are the inverse images along $\bar x$ and $\bar x'$, and inverse
images compose, so $F_{\bar x}=a^{-1}(i^{-1}F)$ and
$F_{\bar x'}=(a')^{-1}(i^{-1}F)$. Both are filtered colimits of the sections
of $i^{-1}F$ over the pointed étale neighbourhoods of the respective
geometric point, that is, over the finite separable extensions of
$\kappa(x)$ that embed into $\Omega$, respectively into $\Omega'$; and every
finite separable extension of $\kappa(x)$ embeds into either field, both
being separably closed. The two colimits therefore have the same index
category up to cofinality and vanish simultaneously, which gives the first
assertion, and with it the independence of the support of the choice of
geometric point.

Unresolved dependencies: def:weil-pbc-geometric-stalks, def:weil-pbc-inverse-image
