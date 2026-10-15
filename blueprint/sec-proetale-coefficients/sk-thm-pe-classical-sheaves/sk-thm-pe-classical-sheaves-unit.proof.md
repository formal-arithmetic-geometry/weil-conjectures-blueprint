+++
kind = "proof"
of = "det-pe-classical-sheaves-unit"
+++
Let $V\to X$ be étale. Then $V$ is an object of both sites, and
$(\nu_{X,*}\nu_X^*F)(V)=(\nu_X^*F)(V)$ since $\nu_{X,*}$ is restriction to the
étale subsite. By the formula of [sk-prop-pe-comparison-morphism] with $h$
étale, $(\nu_X^*F)(V)=\Gamma(V_{\Et},h_{\Et}^*F)=F(V)$, because the étale inverse
image along an étale map is restriction to the slice. Under this identification
the unit $\eta_F(V)$ is the identity of $F(V)$: the unit is the map
$F\to\nu_{X,*}\nu_X^*F$ adjoint to the identity of $\nu_X^*F$, and in the explicit
adjunction of [lem-weil-pbc-comparison-sections] it sends a section on an étale
object to the same section regarded as a section of $\nu_X^*F$. (When $V$ is
affine this is the presentation of $V$ by the constant system; the general case
follows by gluing over an affine open cover of $V$.) Hence $\eta_F$ is bijective
on every étale $V$, so it is an isomorphism of sheaves.

For full faithfulness, the adjunction gives a bijection
$\Hom(\nu_X^*F,\nu_X^*F')\cong\Hom(F,\nu_{X,*}\nu_X^*F')$, and the composite
$\Hom(F,F')\to\Hom(\nu_X^*F,\nu_X^*F')\cong\Hom(F,\nu_{X,*}\nu_X^*F')$ is
$\varphi\mapsto\eta_{F'}\circ\varphi$. Since $\eta_{F'}$ is an isomorphism, this
composite is bijective, hence so is $\varphi\mapsto\nu_X^*\varphi$.
