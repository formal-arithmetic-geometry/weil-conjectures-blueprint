+++
kind = "proof"
of = "sk-thm-reduction"
uses = ["sk-def-pbc", "sk-thm-chow-projective", "sk-thm-chow", "sk-lem-pbc-finite", "sk-lem-pbc-symmetric-product", "sk-lem-pbc-composition-cancellation"]
+++
Let $f:X\to Y$ be proper. We first reduce to the case that $Y$ is affine,
as Chow's lemma requires. Let $Y=\bigcup U$ be an affine open cover, and
assume $\mathrm{PBC}_\Lambda$ for each restriction $f^{-1}(U)\to U$. Given a base change
$Y'\to Y$, the inverse images $U'$ of the sets $U$ cover $Y'$. Since higher
direct images commute with restriction to open subschemes, the restriction
of the base change map to $U'$ is the base change map of $f^{-1}(U)\to U$
along $U'\to U$, hence an isomorphism. As isomorphisms can be checked on
geometric stalks, the base change map over $Y'$ is an isomorphism.

Since $Y$ is affine, it is quasi-compact and quasi-separated, and
Theorem [sk-thm-chow-projective] with $S=Y$ gives a proper surjection
$\pi:\widetilde X\to X$ and closed immersions
$i_Y:\widetilde X\hookrightarrow\mathbf P^n_Y$ and
$i_X=(\pi,i_Y):\widetilde X\hookrightarrow\mathbf P^n_X$ with $f\pi$ equal to
$i_Y$ followed by the projection. We need that theorem over an arbitrary
qcqs base, not only in the Noetherian case of
Appendix [sec-nagata-compactification]. The two maps $\pi$ and $f\pi$ factor as
closed immersions $i_X$ and $i_Y$ followed by projections of projective
spaces. Closed immersions are finite, so they satisfy $\mathrm{PBC}_\Lambda$ by
Lemma [sk-lem-pbc-finite], and projections of projective spaces satisfy
$\mathrm{PBC}_\Lambda$ by the hypothesis and
Lemma [sk-lem-pbc-symmetric-product]. By stability under
composition (Lemma [sk-lem-pbc-composition-cancellation](i)), both $\pi$ and
$f\pi$ satisfy $\mathrm{PBC}_\Lambda$. As $\pi$ is surjective, we may cancel it by
Lemma [sk-lem-pbc-composition-cancellation](ii), and we conclude that
$\mathrm{PBC}_\Lambda$ holds for $f$.
