+++
id = "lem-sc-arbitrary-curve-cd"
kind = "lemma"
title = "The torsion bound on an arbitrary algebraic curve"
order = 4903
lean = ["AlgebraicGeometry.Curve.torsionCohomologicalDimensionLE"]
uses = ["def-sc-etale-torsion-cd"]
+++
Let $X$ be a separated finite-type scheme of dimension at most one over an
algebraically closed field. Put $e=1$ if $X$ is affine, and $e=2$ otherwise.
Then $\operatorname{cd}_{\rm tor}(X)\leq e$, in the sense of
[def-sc-etale-torsion-cd].

## Proof

Reduction is a universal homeomorphism, so by the invariance of the étale
site under universal homeomorphisms we may assume $X$ reduced. Normalize each
of its finitely many irreducible components in its own function field and
take their disjoint union $h:X'\to X$. This map is finite. It is an
isomorphism off a finite set $S$: on each component, finite generators of the
normalization have a common nonzero denominator; remove its zero locus and
the intersections with the other components. These closed subsets have
dimension zero.

Every one-dimensional component of $X'$ is regular, including its generic
field local ring. Regular finite-type schemes over the perfect ground field
are smooth, by the local algebra criterion [Tag
00TV](https://stacks.math.columbia.edu/tag/00TV). The zero-dimensional
components are spectra of the ground field. If $X$ is affine then $X'$ is
affine, since $h$ is finite.

For any torsion $F$, the kernel and cokernel of $F\to h_*h^*F$ are supported
on $S$. Such sheaves equal their direct images from $S$, by checking stalks,
and are acyclic. The two long exact sequences give
$H^q(X,F)\simeq H^q(X,h_*h^*F)$ for $q\geq2$. Finite direct image gives
$H^q(X,h_*h^*F)=H^q(X',h^*F)$. Apply the smooth-curve cohomological
dimension bounds to its smooth curve components, and zero-dimensional
vanishing to its points.

Unresolved dependencies: def:weil-pbc-scheme-conventions, thm:weil-pbc-universal-homeomorphism-invariance, lem:fin-normalization-extension-finite, lem:sc-normal-dim1-dvr, lem:sc-cohomological-dimension, lem:sc-affine-cohomological-dimension, lem:weil-pbc-finite-direct-image-exact, lem:weil-pbc-zero-dimensional-cohomology
