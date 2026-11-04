+++
id = "example-gauss-sum-over-f-3--3"
kind = "example"
title = "A Gauss sum over $\\mathbf F_3$ (3)"
name_showing = false
order = 1214003
aliases = ["bp-r376-3"]
+++
Hence its geometric coinvariants vanish, and $H^0_c=H^2_c=0$
(Lemma [lemma-extreme-degrees-affine-curve]). The sum is therefore
$-\operatorname{Tr}(F\mid H^1_c)$.

To see that $H^1_c$ is a line, we use the running example. The cover
$u^3-u=x^2$ is the affine part $Y_0$ of the elliptic curve
$C_0\colon y^2=x^3-x$ of the introduction, with the coordinates renamed
($x^2=u^3-u$). It lies over $\mathbf A^1$ by $\pi(u,x)=x$. Since $\pi$ is
the pullback along $h$ of the Artin–Schreier cover, $\pi_*E$ is the direct sum
of $h^*\mathcal L_{\psi'}$ over the three characters $\psi'$ of $\mathbf F_3$.
Over $k=\overline{\mathbf F}_3$ we obtain

$$
H^1_c(Y,E)=H^1_c(\mathbf A^1,E)\oplus H^1_c(\mathbf A^1,h^*\mathcal L_\psi)
\oplus H^1_c(\mathbf A^1,h^*\mathcal L_{\psi^{-1}}).
$$

The left side is $H^1(C,E)$, because $C$ minus $Y$ is the single point
at infinity, and it has dimension $2$. The first summand on the right is
zero. The automorphism $(u,x)\mapsto(-u,ix)$ of $Y$, with $i^2=-1$ in
$\mathbf F_9$, conjugates the translation by $c$ into the translation by
$-c$. It therefore exchanges the last two summands, and each of them is a
line. This automorphism is defined only over $\mathbf F_9$, but we use it
only to count dimensions. The translations are defined over
$\mathbf F_3$, so the decomposition is stable under Frobenius.
