+++
kind = "proof"
of = "det-cd-etale-comparison"
+++
*(1).* If $F$ is $\ell$-power torsion, so is $F_0\cong\nu_{S,*}F$, whose sections
are sections of $F$ on étale objects. Conversely, if $F_0$ is $\ell$-power
torsion, then on an affine presentation $U=\varprojlim_iU_i$ every section of
$\nu_S^*F_0$ comes from some $F_0(U_i)$ ([sk-prop-pe-comparison-morphism]) and is
killed by a power of $\ell$; affine objects cover every object, so $F$ is
$\ell$-power torsion.

*(2).* By (1) and [det-pe-classical-sheaves-modules] (with $\Lambda=\mathbf Z$),
the classical $\ell$-power torsion sheaves on $S_{\Proet}$ are, up to isomorphism,
exactly the $\nu_S^*F_0$ with $F_0$ an $\ell$-power torsion étale sheaf. The
cohomology comparison of [sk-prop-sf-comparison] gives
$H^q(S_{\Proet},\nu_S^*F_0)\cong H^q(S_{\Et},F_0)$, so the two sets of degrees
coincide.

*(3).* For $F=\nu_X^*F_0$ the direct-image comparison
([prop-weil-pbc-comparison-direct-image]) gives
$R^qg_{\Proet,*}F\cong\nu_Y^*R^qg_{\Et,*}F_0$, using exactness of $\nu_Y^*$. Since
$\nu_Y^*$ is faithful and exact, $\nu_Y^*G=0$ if and only if $G=0$. Hence the two
sets of degrees coincide.

*(4).* An $\ell$-power torsion sheaf is a torsion sheaf, so (2) bounds
$\operatorname{cd}_\ell(S)$ by $\operatorname{cd}_{\rm tor}(S)$.
