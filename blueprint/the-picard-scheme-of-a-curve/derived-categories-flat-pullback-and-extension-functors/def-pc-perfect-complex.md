+++
id = "def-pc-perfect-complex"
kind = "definition"
title = "Perfect complexes"
order = 4243
lean = ["AlgebraicGeometry.IsPerfect"]
uses = ["def-pc-derived-category", "lem-pc-invertible-perfect"]
+++
Let $X$ be a scheme and $E\in D(\mathcal{O}_X)$. $E$ is *perfect* if it is
locally (on an affine open cover of $X$) isomorphic to a bounded complex of
finite projective modules (Derived Categories of Schemes, Section 36.31,
[Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)); the subcategory is
$D_{\mathrm{perf}}(\mathcal{O}_X)$.

*Import note.* The source's sentence breaks off after the subcategory is
named and the definition then closes; the property deferred there — that an
invertible module placed in degree zero is perfect — is
[lem-pc-invertible-perfect], as [rem-ptr-pc-perfect-complex-9] records.

Unresolved dependencies: def:sc-invertible-module
