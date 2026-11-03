+++
kind = "proof"
of = "sk-lem-curve-normalization"
uses = ["sk-lem-curve-finite-support", "sk-thm-curveestimate", "sk-prop-curve-affine-kummer", "sk-prop-curve-artin-schreier", "sk-lem-curve-affine-artin-schreier", "thm-sc-main", "sk-def-exchange", "sk-lem-pbc-finite", "sk-thm-br"]
+++
Normalization is finite for reduced schemes of finite type over a
field. On each one-dimensional component, its normal model is regular,
and hence smooth over the perfect field, and the isolated components of
dimension zero are reduced points, hence copies of the spectrum of the
ground field. The normalization is an
isomorphism over a dense open of each component, and hence the locus
where it is not an isomorphism is finite.

By the calculation of stalks in Lemma [sk-lem-curve-finite-support], the
displayed map at a geometric point is the diagonal $M\to M^b$, with
$b\geq1$. Thus its kernel is zero and its cokernel has the asserted
form. Where $a$ is an isomorphism, $b=1$ and the cokernel vanishes, so
the cokernel is supported on the finite locus found above.

After algebraically closed extension, the normalization remains smooth
and is a finite birational normal model of the reduced base change,
and hence it is the normalization of the base change. Base change for
finite morphisms identifies the fibres and their sets of branches, and
therefore the diagonal maps and their cokernels are obtained by
extension of scalars.
