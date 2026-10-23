+++
id = "prop-wf-open-curve-h1-no-frobenius-fixed"
kind = "theorem"
title = "No Frobenius-fixed compatible class on an open normal curve"
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.exists_section_of_isIsomorphic_mapIso"]
order = 3837
tags = ["latex:proposition"]
uses = ["def-tw-frobenius-action", "def-weil-pbc-scheme-conventions", "lem-wf-curve-normal-smooth-compactification", "lem-wf-open-curve-residue-sequence", "lem-wf-proper-curve-compatible-h1-no-fixed"]
+++
Let $U_0/\mathbf F_q$ be normal, geometrically connected,
separated and of finite type,
pure of dimension one, and put
$U=U_0\times_{\mathbf F_q}\overline{\mathbf F}_q$. If
$\ell\nmid q$, then for the
geometric Frobenius

$$
\left(\varprojlim_nH^1_{\mathrm{\acute et}}
(U,\mathbf Z/\ell^n\mathbf Z)\right)^{\Phi_q=1}=0.
\tag{5.4}
$$

The scheme and Frobenius conventions are those of
[def-weil-pbc-scheme-conventions], [def-tw-frobenius-action].
