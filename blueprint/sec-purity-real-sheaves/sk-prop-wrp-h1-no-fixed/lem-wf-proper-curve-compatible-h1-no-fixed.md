+++
id = "lem-wf-proper-curve-compatible-h1-no-fixed"
kind = "lemma"
title = "No fixed compatible $H^1$-system on a proper curve"
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.exists_section_of_isIsomorphic_mapIso_of_isProper"]
order = 4005
uses = ["def-tw-frobenius-action", "def-weil-pbc-etale-cohomology", "lem-wf-curve-h1-dual-tate-module", "lem-wf-finite-field-tate-no-fixed", "lem-wf-geometric-jacobian-galois-action", "thm-pod-equivariance-of-the-twisted-pairing"]
+++
Let $C_0/\mathbf F_Q$ be a smooth projective geometrically connected
curve, put $C=C_0\times_{\mathbf F_Q}\overline{\mathbf F}_Q$, and put
$A_n=\mathbf Z/\ell^n\mathbf Z$, where $\ell\nmid Q$. Then

$$
\left(\varprojlim_nH^1_{\mathrm{\acute et}}(C,A_n)\right)^{\Phi_Q=1}=0,
\tag{4.4}
$$

where $\Phi_Q$ is the geometric
Frobenius. The finite-level cohomology is that of
[def-weil-pbc-etale-cohomology].
