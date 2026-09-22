+++
id = "lem-sc-pic-proper-ntorsion"
kind = "lemma"
title = "Pic of a proper curve: divisibility, $n$-torsion, cokernel"
order = 4510
lean = ["AlgebraicGeometry.Curve.picardGroup_torsion_of_proper"]
uses = ["def-sc-jacobian", "thm-sc-jacobian-representability"]
+++
Let $C$ be a proper smooth curve of genus $g$ over algebraically closed $k$,
and let $n$ be prime to $\operatorname{char}k$. Then
$$
\operatorname{Pic}(C)[n]\cong(\mathbf Z/n\mathbf Z)^{2g},
\qquad
\operatorname{coker}\bigl(n:\operatorname{Pic}(C)\to\operatorname{Pic}(C)\bigr)\cong\mathbf Z/n\mathbf Z,
$$
and $\operatorname{Pic}^0(C)$ is $n$-divisible.

## Proof

By the decomposition lemma for the Picard group of a proper curve,
$\operatorname{Pic}(C)=\mathbf Z\oplus\operatorname{Pic}^0(C)$ with
$\operatorname{Pic}^0(C)=J_C(k)$ ([def-sc-jacobian],
[thm-sc-jacobian-representability]). The group $J_C(k)$ is $n$-divisible
because an isogeny is surjective on points, and its $n$-torsion is
$J_C[n](k)\cong(\mathbf Z/n\mathbf Z)^{2g}$ by the étale-ness of the
$n$-torsion subgroup scheme (with $J_C(k)[n]=J_C[n](k)$ by the definition of
the kernel). Hence
$$
\operatorname{Pic}(C)[n]=\operatorname{Pic}^0(C)[n]\cong(\mathbf Z/n\mathbf Z)^{2g},
$$
and
$$
\operatorname{coker}(n:\operatorname{Pic}(C)\to\operatorname{Pic}(C))
=\mathbf Z/n\mathbf Z\oplus\operatorname{coker}\bigl(n:\operatorname{Pic}^0(C)\to\operatorname{Pic}^0(C)\bigr)
=\mathbf Z/n\mathbf Z,
$$
the second summand being zero by divisibility.

Unresolved dependencies: def:sc-curves, def:sc-pic0, lem:sc-pic-proper-decomposition, lem:sc-isogeny-surjective, lem:sc-ntorsion-etale, def:sc-mult-n
