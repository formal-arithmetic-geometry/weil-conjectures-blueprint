+++
kind = "proof"
of = "det-pe-classical-sheaves-unit"
+++
Let $V\to X$ be affine and étale. Then $V$ is an object of both sites, and
$(\nu_{X,*}\nu_X^*F)(V)=(\nu_X^*F)(V)$ since $\nu_{X,*}$ is restriction to the
étale subsite ([def-weil-pbc-site-comparison-morphism]). The inverse image
$\nu_X^*F$ is the sheafification of the presheaf inverse image $P$, the left
Kan extension along the inclusion of sites; since the inclusion is fully
faithful, $P(V)=F(V)$, and the unit of the presheaf adjunction is the identity
there. By [lem-weil-pbc-comparison-sections], applied to the constant system at
$V$, the sheafification map $P(V)\to(\nu_X^*F)(V)$ is an isomorphism. Hence
$\eta_F(V)$ is an isomorphism for every affine étale $V$, and as affine étale
objects form a basis of $X_{\Et}$, $\eta_F$ is an isomorphism of sheaves.

For full faithfulness, the adjunction gives a bijection
$\Hom(\nu_X^*F,\nu_X^*F')\cong\Hom(F,\nu_{X,*}\nu_X^*F')$, and the composite
$\Hom(F,F')\to\Hom(\nu_X^*F,\nu_X^*F')\cong\Hom(F,\nu_{X,*}\nu_X^*F')$ is
$\varphi\mapsto\eta_{F'}\circ\varphi$. Since $\eta_{F'}$ is an isomorphism, this
composite is bijective, hence so is $\varphi\mapsto\nu_X^*\varphi$.
