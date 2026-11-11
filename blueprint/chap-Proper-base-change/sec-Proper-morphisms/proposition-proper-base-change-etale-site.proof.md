+++
kind = "proof"
of = "proposition-proper-base-change-etale-site"
order = 399
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "lemma-finite-morphisms", "lemma-composition-cancellation", "lemma-pbc-projective-space", "definition-compactification-refinement", "theorem-chow-s-lemma-projective-form", "lemma-finite-direct-images"]
+++
Let $f:X\to Y$ be proper. We first reduce to the case that $Y$ is affine,
as Chow's lemma requires. Let $Y=\bigcup U$ be an affine open cover, and
assume $\mathrm{PBC}_\Lambda$ for each restriction $f^{-1}(U)\to U$. Given a base change
$Y'\to Y$, the inverse images $U'$ of the sets $U$ then cover $Y'$. Since higher
direct images commute with restriction to open subschemes, the restriction
of the base change map to $U'$ is the base change map of $f^{-1}(U)\to U$
along $U'\to U$, hence an isomorphism. As isomorphisms can be checked on
geometric stalks, the base change map over $Y'$ is an isomorphism.

Now $Y$ is affine, hence quasi-compact and quasi-separated, so
Theorem [theorem-chow-s-lemma-projective-form] with $S=Y$ gives a proper surjection
$\pi:\widetilde X\to X$ and closed immersions
$i_Y:\widetilde X\hookrightarrow\mathbf P^n_Y$ and
$i_X=(\pi,i_Y):\widetilde X\hookrightarrow\mathbf P^n_X$ with $f\pi$ equal to
$i_Y$ followed by the projection. Here we need Chow's lemma over a base
that is affine but need not be Noetherian; we prove this form
in Appendix [chap-Nagata-compactification-and-Chows-lemma]. The two maps $\pi$ and $f\pi$ factor as
closed immersions $i_X$ and $i_Y$ followed by projections of projective
spaces. Closed immersions are finite, so they satisfy $\mathrm{PBC}_\Lambda$ by
Lemma [lemma-finite-morphisms], and projections of projective spaces satisfy
$\mathrm{PBC}_\Lambda$ by the hypothesis and
Lemma [lemma-pbc-projective-space]. By stability under
composition (Lemma [lemma-composition-cancellation](i)), both $\pi$ and
$f\pi$ therefore satisfy $\mathrm{PBC}_\Lambda$. As $\pi$ is surjective, we may cancel it by
Lemma [lemma-composition-cancellation](ii), and this gives
$\mathrm{PBC}_\Lambda$ for $f$.
