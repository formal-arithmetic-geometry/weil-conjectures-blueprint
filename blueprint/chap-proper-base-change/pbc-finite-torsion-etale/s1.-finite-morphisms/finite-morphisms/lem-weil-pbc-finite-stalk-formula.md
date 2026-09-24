+++
id = "lem-weil-pbc-finite-stalk-formula"
kind = "lemma"
title = "Geometric stalk formula"
order = 1557
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions"]
+++
Let $f:X\to Y$ be finite, let $F$ be an etale sheaf of abelian groups on $X$,
and let $\bar y:\operatorname{Spec}\Omega\to Y$ be a geometric point. If
$\{\bar x\}$ is the finite set of geometric points of $X_{\bar y}$, then

$$
 (f_*F)_{\bar y}\xrightarrow{\sim}
 \prod_{\bar x\in|X_{\bar y}|}F_{\bar x}.
$$

For a finite set, this product is also the direct sum.

## Proof

After base change to the strict henselization at $\bar y$, the finite scheme
$X_{\bar y}$ is the spectrum of a finite algebra over a strictly henselian
local ring, hence a finite disjoint union of strictly henselian local schemes
indexed by the geometric points $\bar x$. Sections over a disjoint union are
the corresponding product of stalks, as computed by the stalk description of
the geometric-stalk convention and the definition of the direct image; for a
finite index set this product is the direct sum.
