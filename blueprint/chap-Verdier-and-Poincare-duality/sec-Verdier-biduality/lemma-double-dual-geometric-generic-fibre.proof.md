+++
kind = "proof"
of = "lemma-double-dual-geometric-generic-fibre"
order = 836
uses = ["theorem-smooth-purity-all-admissible-coefficients"]
+++
Replacing $X$ by an affine open we may assume $X$ affine.
The twist $(1)[2]$ appears because $X$ has one more dimension than its
generic fibre, and we see it by embedding both in affine spaces whose
dimensions differ by one. Choose a closed
immersion $i$ over $\mathbf A^1_k$ of $X$ into $\mathbf A^r_{\mathbf A^1_k}$.
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
$g_X^*\mathbb D_XK\simeq\mathbb D_{X_{\bar\eta}}(g_X^*K)(1)[2]$. The
twist does no harm, because the double-dual map does not change if the dualizing
complex is replaced by an isomorphic object $\omega'$: an isomorphism
$\omega\simeq\omega'$ is used once in each of the two duals, and the two
uses cancel in $\delta$. We apply this to
$\omega'=\omega_{X_{\bar\eta}}(1)[2]$, using that
$\cHom(\cHom(N,\omega(1)[2]),\omega(1)[2])\simeq\cHom(\cHom(N,\omega),\omega)$
compatibly with evaluation. It follows that the isomorphism
$g_X^*\mathbb D_X\mathbb D_XK\simeq\mathbb D_{X_{\bar\eta}}
\mathbb D_{X_{\bar\eta}}g_X^*K$ obtained by applying the comparison twice
carries $g_X^*\delta_K$ to $\delta_{g_X^*K}$.
