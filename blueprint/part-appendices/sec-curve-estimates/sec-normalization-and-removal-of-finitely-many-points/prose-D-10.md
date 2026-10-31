+++
id = "prose-D-10"
kind = "hidden"
title = "Normalization and removal of finitely many points (3)"
order = 931
+++
In the proof of Theorem [sk-thm-curve-package] the lemma is applied
only to sheaves killed by a single prime $\ell$, after a constructible
torsion sheaf has been split into primary parts and filtered.

If $j$ is dense, it follows from Lemma [sk-lem-curve-dense-open] and
the calculation for constant $\mathbf F_\ell$ on $C$ via
Lemma [sk-lem-curve-normalization] that $j_!\underline{\mathbf F_\ell}$
satisfies the assertions of Theorem [sk-thm-curve-package].
An arbitrary open is dense in the reduced union of the components it
meets, which is a closed subscheme of $C$. We apply the dense case
there and pass back to $C$, using that direct image along a finite
morphism is exact [Stacks, Tag 0A3Q](https://stacks.math.columbia.edu/tag/0A3Q) and does not change cohomology
(Lemma [sk-lem-curve-finite-support]).
