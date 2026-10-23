+++
id = "lem-sc-pic-proper-ntorsion"
kind = "lemma"
title = "Pic of a proper curve: divisibility, n-torsion, cokernel"
lean = ["AlgebraicGeometry.Scheme.nonempty_addEquiv_torsionBy_pic_and_quotient"]
order = 1433
uses = ["def-sc-curves", "def-sc-jacobian", "def-sc-mult-n", "def-sc-pic0", "lem-pc-genus-agrees-sc", "lem-sc-pic-proper-decomposition", "thm-av-final", "thm-sc-jacobian-representability", "def-sc-genus"]
+++
Let $C$ be a proper smooth connected curve of
genus $g$ over algebraically closed $k$, and let $n$ be prime
to $\operatorname{char}k$. Then

$$
\operatorname{Pic}(C)[n]\cong(\mathbf Z/n\mathbf Z)^{2g},
\qquad
\operatorname{coker}\bigl(n:\operatorname{Pic}(C)\to
\operatorname{Pic}(C)\bigr)\cong\mathbf Z/n\mathbf Z,
$$

and $\operatorname{Pic}^0(C)$ is $n$-divisible.
