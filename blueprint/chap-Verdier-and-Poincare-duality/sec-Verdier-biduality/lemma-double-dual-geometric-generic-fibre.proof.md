+++
kind = "proof"
of = "lemma-double-dual-geometric-generic-fibre"
order = 843
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "lemma-inverse-image-coefficient-sheaves", "lemma-flat-models-generators", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "proposition-six-operations-change-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-kunneth-field-coefficients", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Replacing $X$ by an affine open we may assume $X$ affine. The twist $(1)[2]$ appears because $X$ has one more dimension than its
generic fibre, and we see it by embedding both in affine spaces whose
dimensions differ by one. To do this, choose a closed immersion $i$ over $\mathbf A^1_k$ of $X$ into $\mathbf A^r_{\mathbf A^1_k}$.
Since $\mathbf A^r_{\mathbf A^1_k}$ is smooth of dimension $r+1$ over
$k$, by composition of exceptional inverse images and Theorem [theorem-smooth-purity-all-admissible-coefficients] we get
$\omega_X\simeq i^!A(r+1)[2r+2]$. In the same way, the geometric
generic fibre is a closed subscheme of $\mathbf A^r_{\bar\eta}$, so
$\omega_{X_{\bar\eta}}\simeq i_{\bar\eta}^!A(r)[2r]$. By the second
comparison,
$g_X^*i^!A(r+1)[2r+2]\simeq i_{\bar\eta}^!A(r+1)[2r+2]$, which is
$\omega_{X_{\bar\eta}}(1)[2]$.

For the double-dual maps, note that the comparison for internal
Hom is adjoint to the pullback of the evaluation
$K\otimes^{\mathbf L}\cHom_X(K,M)\to M$, so it carries evaluation to
evaluation. Together with the twist it gives
$g_X^*\mathbb D_XK\simeq\mathbb D_{X_{\bar\eta}}(g_X^*K)(1)[2]$. This twist does no harm, because the double-dual map does not change if the dualizing
complex is replaced by an isomorphic object $\omega'$: an isomorphism
$\omega\simeq\omega'$ is used once in each of the two duals, and the two
uses cancel in $\delta$. We apply this to
$\omega'=\omega_{X_{\bar\eta}}(1)[2]$, using that
$\cHom(\cHom(N,\omega(1)[2]),\omega(1)[2])\simeq\cHom(\cHom(N,\omega),\omega)$
compatibly with evaluation. It follows that the isomorphism
$g_X^*\mathbb D_X\mathbb D_XK\simeq\mathbb D_{X_{\bar\eta}}
\mathbb D_{X_{\bar\eta}}g_X^*K$ obtained by applying the comparison twice
carries $g_X^*\delta_K$ to $\delta_{g_X^*K}$.
