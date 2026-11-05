+++
kind = "proof"
of = "lemma-cohomology-near-two-transverse-divisors--1"
order = 972003
uses = ["lemma-punctured-surface-punctured-curve", "lemma-cohomology-modules-underlying-abelian", "proposition-extension-zero-restriction-closed-subscheme--8", "proposition-smooth-purity-finite-coefficients"]
+++
For the assertion at the corner, we may extend the separably closed
field of the geometric point to its algebraic closure, since this
pullback detects zero objects. Let $S$ be the strict localization at
the resulting point. For constant $\mathbf F_\ell$ coefficients, the
restriction

$$
R\Gamma(S-D_{2,S},\mathbf F_\ell)
\longrightarrow R\Gamma(D_{1,S}-z,\mathbf F_\ell)
$$

is an isomorphism by [lemma-punctured-surface-punctured-curve]. The
open–closed sequence [proposition-extension-zero-restriction-closed-subscheme--8]
therefore gives $R\Gamma(S-D_{2,S},j'_!\mathbf F_\ell)=0$, where $j'$
now denotes the base change to $S$.

The complement of the two divisors in $S$ is connected. A sheaf with
finite $\ell$-group monodromy on this complement is an iterated extension
of constant sheaves associated to finite $A$-modules killed by $\ell$.
Indeed, after choosing a connected trivializing cover, a nonzero fixed
vector killed by $\ell$ gives a constant submodule, and the quotient has
smaller cardinality. Each such constant module is a finite sum of
$\mathbf F_\ell$ as an abelian group. The comparison with underlying
abelian sheaves [lemma-cohomology-modules-underlying-abelian], the stalk
formula for $Rj_*$, and base change for extension by zero give vanishing
for sheaves. Truncation then gives vanishing for bounded complexes.
This is the argument of
`AlgebraicGeometry.Scheme.TransverseCorner.isZero_leftDerivedUpperStar_boundaryComplex_of_bijective`.

For local constancy, put $W=X-D_1$ and let
$j_W:X-(D_1\cup D_2)\hookrightarrow W$. Open base change and
$j'^*j'_!N\simeq N$ identify $M|_W$ with $Rj_{W*}N$. This comparison
restricts to $D_2-z$, as in
`AlgebraicGeometry.Scheme.TransverseCorner.leftDerivedUpperStarPuncturedYBoundaryComplexIso`.
For constant $\mathbf F_\ell$ coefficients, purity, obtained from
[proposition-smooth-purity-finite-coefficients], computes the direct
images locally along the divisor: they are $\mathbf F_\ell$ in degree
zero, $i_*\mathbf F_\ell(-1)$ in degree one, and zero in higher degrees,
where $i:D_2-z\hookrightarrow W$. In the limit case a local equation
descends to a smooth stage, and étale limit base change transports this
calculation to $X$.

Finite sums and comparison with underlying abelian sheaves give the
same finite local constancy for constant finite $A$-modules killed by
$\ell$. On connected components of $W$, apply the monodromy filtration
and truncation again. Finite local constancy of cohomology is stable
under shifts and extensions, so the result holds for $N$. This is
`AlgebraicGeometry.Etale.hasFiniteLocallyConstantHomology_of_constantSheaf`;
the comparison on $D_2-z$ finishes the proof.
