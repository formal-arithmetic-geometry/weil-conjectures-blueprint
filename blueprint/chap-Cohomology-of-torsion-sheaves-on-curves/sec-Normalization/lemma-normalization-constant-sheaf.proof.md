+++
kind = "proof"
of = "lemma-normalization-constant-sheaf"
order = 1604
uses = ["definition-underived-base-change-map", "lemma-finite-morphisms", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
The map is computed on stalks by the formula for stalks of finite direct
images, and the cokernel has finite support because $\pi$ is an
isomorphism away from finitely many points. Compatibility with field
extension holds because normalization commutes with algebraically
closed extension.

Normalization is finite for reduced schemes of finite type over a
field.  On each one-dimensional component, its normal model is regular,
hence smooth over the perfect field, while the isolated components of
dimension zero are reduced points, that is, copies of the spectrum of the
ground field.  Since the normalization is an
isomorphism over a dense open of each component, the locus
where it is not an isomorphism is finite.

By the calculation of stalks in Lemma [lemma-finite-morphisms], the
displayed map at a geometric point is the diagonal $M\to M^b$, with
$b\geq1$, so its kernel is zero and its cokernel has the asserted
form.  Where $\pi$ is an isomorphism we have $b=1$ and the cokernel
vanishes; hence the cokernel is supported on the finite locus found above.

After algebraically closed extension, the normalization remains smooth
and is a finite birational normal model of the reduced base change,
so it is the normalization of the base change.  Base change for
finite morphisms identifies the fibres and their sets of branches, and
therefore the diagonal maps and their cokernels are obtained by
extension of scalars.
