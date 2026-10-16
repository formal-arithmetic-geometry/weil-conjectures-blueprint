+++
id = "lem-sc-pic-affine"
kind = "lemma"
title = "Pic of an affine curve: quotient description, divisibility, finiteness"
lean = ["AlgebraicGeometry.IsConnectedCurve.exists_units_pic_presentation", "AlgebraicGeometry.IsConnectedCurve.exists_addEquiv_pic_quotient", "AlgebraicGeometry.IsConnectedCurve.surjective_zsmul_pic_and_finite_torsionBy"]
order = 1020
uses = ["def-sc-curves", "def-sc-jacobian", "def-sc-mult-n", "def-sc-pic0", "lem-sc-compactification", "lem-sc-dim0-finite", "lem-sc-divisible-quotient-torsion", "lem-sc-divisor-class-curve", "lem-sc-pic-proper-decomposition", "lem-sc-proper-affine-finite", "thm-av-final", "thm-sc-jacobian-representability"]
+++
Let $C$ be a smooth affine connected curve over
algebraically closed $k$, and let $n$ be prime to
$\operatorname{char}k$. Let $\overline C$ be the
compactification ([lem-sc-compactification]) and
$S=\overline C\setminus C$ its (nonempty finite) complement; fix
$P_0\in S$. Then

$$
\operatorname{Pic}(C)\cong J_{\overline C}(k)/\Lambda,
\qquad
\Lambda:=\langle[P]-[P_0]:P\in S\rangle\subseteq J_{\overline C}(k),
$$

where $J_{\overline C}(k)=\operatorname{Pic}^0(\overline C)$ is
the canonical identification of the
Jacobian of $\overline C$
([def-sc-jacobian], [thm-sc-jacobian-representability]), so $\operatorname{Pic}(C)$ is a quotient
of the divisible group $J_{\overline C}(k)$ (there is
no degree map on $\operatorname{Pic}(C)$ itself). In particular
$\operatorname{Pic}(C)$ is $n$-divisible and
$\operatorname{Pic}(C)[n]$ is finite.
