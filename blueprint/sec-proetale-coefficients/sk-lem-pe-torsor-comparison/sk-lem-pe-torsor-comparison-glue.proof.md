+++
kind = "proof"
of = "det-pe-torsor-comparison-glue"
+++
Cover $X$ by affine opens $X_a$. The inverse image $\nu_X^*$ commutes with
restriction to open subschemes, so $T|_{X_a}$ is a torsor under
$\nu_{X_a}^*(G_0|_{X_a})$, and [det-pe-torsor-comparison-affine] gives
$G_0|_{X_a}$-torsors $T_{0,a}$ with isomorphisms
$\alpha_a\colon\nu_{X_a}^*T_{0,a}\cong T|_{X_a}$.

On $X_{ab}=X_a\cap X_b$ the isomorphism
$\alpha_b^{-1}\alpha_a\colon\nu^*T_{0,a}|_{X_{ab}}\to\nu^*T_{0,b}|_{X_{ab}}$ is
$\nu^*\varphi_{ab}$ for a unique map of sheaves
$\varphi_{ab}\colon T_{0,a}|_{X_{ab}}\to T_{0,b}|_{X_{ab}}$, by full faithfulness
([det-pe-classical-sheaves-unit] on the scheme $X_{ab}$). By faithfulness
$\varphi_{ab}$ is an isomorphism, is $G_0$-equivariant, and satisfies
$\varphi_{bc}\varphi_{ab}=\varphi_{ac}$ on triple overlaps, since the corresponding
identities hold after $\nu^*$. Étale sheaves glue along Zariski coverings, so the
$T_{0,a}$ glue to a $G_0$-torsor $T_0$ with $T_0|_{X_a}\cong T_{0,a}$, and the
isomorphisms $\alpha_a$ agree on overlaps by construction, hence glue to
$\nu_X^*T_0\cong T$. Uniqueness follows from full faithfulness of $\nu_X^*$.

The étale coverings of the $X_a$ trivializing $T_{0,a}$ together form an étale
covering of $X$ trivializing $T_0$, hence $T$; and $T\cong\nu_X^*T_0$ is classical
by [det-pe-classical-sheaves-image].
