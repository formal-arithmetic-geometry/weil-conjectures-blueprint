+++
id = "sk-prop-wrp-h1-no-fixed"
kind = "proposition"
title = "No fixed class in degree one"
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.exists_section_of_isIsomorphic_mapIso"]
order = 3815
uses = ["sk-cor-pe-bounded-continuity", "sk-d-real-jacobian", "sk-i-real-compactification", "sk-p-tate", "sk-prop-pe-continuous-cohomology", "sk-prop-sf-open-closed-triangle", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-sf-identification"]
tags = ["sketch"]
+++
For a smooth geometrically connected curve $U_0/k_0$, geometric
Frobenius has no fixed vector on $H^1(U,E)$ for every finite
$E/\Ql$. More precisely,

$$
 \left(\varprojlim_nH^1(U,\mathbf Z/\ell^n)\right)^{F=1}=0.
$$

*Complement.* Here $H^1(U,E)$ is the cohomology of [d-real-cohom]: the
rationalization of the derived inverse limit of the finite levels of a
lattice, extended to $E$.
