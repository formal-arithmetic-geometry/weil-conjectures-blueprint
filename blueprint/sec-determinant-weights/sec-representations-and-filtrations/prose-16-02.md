+++
id = "prose-16-02"
kind = "hidden"
title = "Representations and filtrations"
order = 660
+++
In this section lisse sheaves are treated as representations of the
Weil group, and the geometry of the curve enters through a single fact
from Section [sec-rank-one-curves]: the geometric fundamental group acts
through a finite group on every determinant. Everything else is linear
algebra and the structure of algebraic groups, and we begin by fixing
the language.

Throughout this section $U_0$ is a geometrically connected smooth curve
over $k_0$, with Weil group $W(U_0)$ and geometric fundamental group
$\pi_1(U)$ as in Convention [sk-d-real-weil], and $s\in W(U_0)$ is a lift of
geometric Frobenius, so that $\deg(s)=1$ and
$W(U_0)=\pi_1(U)\rtimes\langle s\rangle$. A *Weil representation* is
a finite-dimensional $\overline{\mathbf Q}_\ell$-representation of $W(U_0)$ whose
restriction to $\pi_1(U)$ is continuous; by Convention [sk-d-real-weil]
these are the lisse Weil $\overline{\mathbf Q}_\ell$-sheaves on $U_0$. By
Corollary [sk-d-real-detweights], $\pi_1(U)$ acts through a finite group on
the determinant of every Weil representation. A Weil representation $V$ is
semisimple if it is a direct sum of simple representations. The semisimplification $V^{\mathrm{ss}}$ of $V$ is the
direct sum of its composition factors.

We need two elementary facts. Semisimplicity is preserved by
restriction to a normal subgroup, which lets us apply Lie theory to the
identity component of the monodromy group below. The composition
factors of tensor and exterior powers are computed from those of the
given representations, which reduces the formulas to semisimple
representations.
