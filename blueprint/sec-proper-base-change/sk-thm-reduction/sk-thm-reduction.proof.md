+++
kind = "proof"
of = "sk-thm-reduction"
uses = ["sk-thm-chow", "sk-lem-pbc-finite", "sk-lem-pbc-symmetric-product", "sk-lem-pbc-composition-cancellation"]
+++
The assertion is local on the target. Indeed, higher direct images restrict
to the corresponding higher direct images over an étale open of the target,
compatibly with the canonical exchange. For an arbitrary base change
$Y'\to Y$, the inverse images of an affine open cover of $Y$ cover $Y'$, and
geometric stalks detect an isomorphism in $D^+(Y'_{\Et},\mathbf Z)$. We may
therefore suppose $Y$ affine.

Apply [sk-thm-chow]. The two maps $\pi$ and $f\pi$ factor as closed
immersions $i_X$ and $i_Y$ followed by projective-space projections. Closed
immersions are finite, so they satisfy PBC by [sk-lem-pbc-finite].
Projective-space projections satisfy PBC by [sk-lem-pbc-symmetric-product].
Composition ([sk-lem-pbc-composition-cancellation], part (1)) therefore
gives PBC for both $\pi$ and $f\pi$. As $\pi$ is surjective, cancellation
([sk-lem-pbc-composition-cancellation], part (2)) gives PBC for $f$.
