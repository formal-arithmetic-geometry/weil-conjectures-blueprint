+++
id = "sk-i-restriction"
kind = "lemma"
title = "Restriction to a normal subgroup"
lean = ["Representation.isSemisimpleRepresentation_comp_subtype"]
order = 4035
uses = ["sk-d-real-weil", "sk-d-real-detweights", "sk-i-cartier", "sec-algebraic-groups-lie-algebras"]
tags = ["sketch"]
+++
Throughout the part on monodromy and determinant weights, $U_0$ is a
geometrically connected smooth curve over $k_0$, with Weil group $W(U_0)$
and geometric fundamental group $\pi_1(U)$ as in [sk-d-real-weil], and
$s\in W(U_0)$ is a lift of geometric Frobenius, so that $\deg(s)=1$ and
$W(U_0)=\pi_1(U)\rtimes\langle s\rangle$. A *Weil representation* is a
finite-dimensional $\overline{\mathbf Q}_\ell$-representation of $W(U_0)$
whose restriction to $\pi_1(U)$ is continuous; by [sk-d-real-weil] these
are the lisse Weil $\overline{\mathbf Q}_\ell$-sheaves on $U_0$. By
[sk-d-real-detweights], $\pi_1(U)$ acts through a finite group on the
determinant of every Weil representation. A Weil representation $V$ is
semisimple if it is a direct sum of simple representations. The
semisimplification $V^{\mathrm{ss}}$ of $V$ is the direct sum of its
composition factors.

Let $N$ be a normal subgroup of a group $\Gamma$. The restriction to $N$ of
a finite-dimensional semisimple $\overline{\mathbf Q}_\ell$-representation
of $\Gamma$ is semisimple.
