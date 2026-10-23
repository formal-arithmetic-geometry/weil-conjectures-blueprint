+++
kind = "proof"
of = "sk-thm-reduction"
uses = ["sk-def-pbc", "sk-thm-chow", "sk-lem-pbc-finite", "sk-lem-pbc-symmetric-product", "sk-lem-pbc-composition-cancellation"]
+++
*Reduction to torsion coefficients.* Composition and cancellation
([sk-lem-pbc-composition-cancellation]) need a coefficient ring which is torsion
as an abelian group. For a prime $p$, $\mathrm{PBC}_\Lambda(g)$ implies
$\mathrm{PBC}_{\Lambda/p\Lambda}(g)$ for every morphism $g$, since restriction of
scalars along $\Lambda\to\Lambda/p\Lambda$ is exact, conservative and commutes
with inverse and derived direct images. Conversely $\mathrm{PBC}_\Lambda(f)$
follows from $\mathrm{PBC}_{\Lambda/p\Lambda}(f)$ for all primes $p$: a torsion
sheaf is the filtered union of its subsheaves killed by integers, and a sheaf
killed by an integer is a finite extension of sheaves killed by primes, i.e. of
sheaves of $\Lambda/p\Lambda$-modules ([sk-def-pbc]). So we may assume that
$\Lambda$ is torsion.

The assertion is local on the target. Indeed, higher direct images restrict
to the corresponding higher direct images over an étale open of the target,
compatibly with the canonical exchange. For an arbitrary base change
$Y'\to Y$, the inverse images of an affine open cover of $Y$ cover $Y'$, and
geometric stalks detect an isomorphism in $D^+(Y'_{\Et},\Lambda)$. We may
therefore suppose $Y$ affine.

Apply [sk-thm-chow]. The two maps $\pi$ and $f\pi$ factor as closed
immersions $i_X$ and $i_Y$ followed by projective-space projections. Closed
immersions are finite, so they satisfy PBC by [sk-lem-pbc-finite].
Projective-space projections satisfy PBC by [sk-lem-pbc-symmetric-product].
Composition ([sk-lem-pbc-composition-cancellation], part (1)) therefore
gives PBC for both $\pi$ and $f\pi$. As $\pi$ is surjective, cancellation
([sk-lem-pbc-composition-cancellation], part (2)) gives PBC for $f$.
