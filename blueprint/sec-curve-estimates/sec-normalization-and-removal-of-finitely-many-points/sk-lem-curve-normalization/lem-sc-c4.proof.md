+++
kind = "proof"
of = "lem-sc-c4"
uses = ["def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-sheaves", "lem-sc-affine-open-proper", "lem-sc-affine-unit-quotient", "lem-sc-compactification", "lem-sc-pic-affine", "thm-sc-affine-cohomology", "thm-sc-proper-cohomology"]
+++
The constant sheaf $\mathbf F_r$ is locally constant with finite stalks on $C$, so it is constructible by [def-weil-pbc-etale-sheaves]. This is the sheaf to which the assertion $\mathcal C_4(C,\mathbf F_r)$ applies.

By [lem-sc-compactification] and [lem-sc-affine-open-proper], the smooth separated connected curve $C$ is either proper or affine. These two cases exhaust the proof.

If $C$ is proper, [thm-sc-proper-cohomology] identifies the cohomology groups with $\mathbf Z/r\mathbf Z$ in degrees $0$ and $2$, with $(\mathbf Z/r\mathbf Z)^{2g}$ in degree $1$, and with $0$ in higher degrees. Since $r$ is finite, each of these abelian groups is finite.

If $C$ is affine, [thm-sc-affine-cohomology] gives $H^0(C,\mathbf F_r)=\mathbf Z/r\mathbf Z$ and vanishing in degrees above $1$. In degree $1$ it gives an extension whose subquotient is the finite group $\operatorname{Pic}(C)[r]$ from [lem-sc-pic-affine] and whose complementary unit quotient is finite by [lem-sc-affine-unit-quotient]. An extension of finite abelian groups is finite, so $H^1(C_{\Et},\mathbf F_r)$ is finite.

The proper and affine cases establish finiteness of $H^q(C_{\Et},\mathbf F_r)$ for every $q\geq0$, which is precisely $\mathcal C_4(C,\mathbf F_r)$ in [def-weil-pbc-eight-curve-assertions].
