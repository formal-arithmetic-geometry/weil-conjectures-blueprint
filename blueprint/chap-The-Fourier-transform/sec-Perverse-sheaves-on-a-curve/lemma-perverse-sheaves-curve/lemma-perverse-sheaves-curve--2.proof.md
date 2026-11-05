+++
kind = "proof"
of = "lemma-perverse-sheaves-curve--2"
order = 1249004
uses = ["lemma-largest-punctual-subsheaf"]
+++
For $G$ placed in degree zero, the only nonzero cohomology sheaf is
$\mathcal H^0=G$. Finite support gives the upper-class condition, and
$\mathcal H^{-1}=0$ gives the lower-class condition. For $G[1]$, the
only nonzero cohomology sheaf is $\mathcal H^{-1}=G$, so the two
conditions follow from the hypothesis on finite-support subsheaves.

For $(j_*M)[1]$, the same cohomology calculation reduces the assertion
to the absence of nonzero finite-support subsheaves of $j_*M$.
The affine-line result
`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.eq_zero_of_support_finite`,
associated with [lemma-largest-punctual-subsheaf], says that every map
from a finite-support Weil sheaf to $j_*M$ is zero. An inclusion of such
a sheaf must therefore have zero source, which proves the claim.
