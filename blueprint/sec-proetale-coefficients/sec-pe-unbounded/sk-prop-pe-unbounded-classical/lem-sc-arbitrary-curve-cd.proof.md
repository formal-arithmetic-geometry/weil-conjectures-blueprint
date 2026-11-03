+++
kind  = "proof"
of    = "lem-sc-arbitrary-curve-cd"
+++
Reduction is a universal homeomorphism, so
[thm-weil-pbc-universal-homeomorphism-invariance] allows us
to assume $X$ reduced. Normalize each of its finitely many
irreducible components in its own function field and take their
disjoint union $h:X'\to X$. This map is finite by
[lem-fin-normalization-extension-finite]. It is an
isomorphism off a finite set $S$: on each component, finite
generators of the normalization have a common nonzero
denominator; remove its zero locus and the intersections with
the other components. These closed subsets have dimension zero.

Every one-dimensional component of $X'$ is regular by
[lem-sc-normal-dim1-dvr], including its generic field
local ring. Regular finite-type schemes over the perfect
ground field are smooth, by the local algebra criterion
[Tag 00TV](https://stacks.math.columbia.edu/tag/00TV).
The zero-dimensional components are spectra of the ground field.
If $X$ is affine then $X'$ is affine, since $h$ is finite.

For any torsion $F$, the kernel and cokernel of
$F\to h_*h^*F$ are supported on $S$.
Such sheaves equal their direct images from $S$, by checking
stalks, and are acyclic by
[lemma-weil-pbc-finite-direct-image-exact], [lem-weil-pbc-zero-dimensional-cohomology].
The two long exact sequences give
$H^q(X,F)\simeq H^q(X,h_*h^*F)$ for $q\geq2$.
Finite direct image gives
$H^q(X,h_*h^*F)=H^q(X',h^*F)$.
Apply [lem-sc-cohomological-dimension], [lem-sc-affine-cohomological-dimension]
to its smooth curve components and
[lem-weil-pbc-zero-dimensional-cohomology] to its points.
