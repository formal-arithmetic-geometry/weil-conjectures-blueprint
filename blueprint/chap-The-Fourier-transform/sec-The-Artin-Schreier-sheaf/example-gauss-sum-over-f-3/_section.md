+++
id = "example-gauss-sum-over-f-3"
kind = "example"
title = "A Gauss sum over $\\mathbf F_3$"
order = 1220
uses = ["lemma-extreme-degrees-affine-curve"]
+++
Take $q=3$, a primitive cube root of unity $\omega\in\overline{\mathbf Q}_\ell$ and
$\psi(x)=\omega^x$ on $\mathbf F_3$. Pull $\mathcal L_\psi$ back along
$h:\mathbf A^1\to\mathbf A^1$, $x\mapsto x^2$. By the lemma, the trace
of Frobenius on the stalk of $h^*\mathcal L_\psi$ at $x\in\mathbf F_3$ is
$\psi(x^2)$, so the trace formula gives

$$
\sum_r(-1)^r\operatorname{Tr}\bigl(F\mid H^r_c(\mathbf A^1_k,h^*\mathcal L_\psi)\bigr)
=\sum_{x\in\mathbf F_3}\omega^{x^2}=1+2\omega ,
$$

and $(1+2\omega)^2=-3$.
The sheaf $h^*\mathcal L_\psi$ is lisse of rank one. It is geometrically
nontrivial, since the cover $u^3-u=x^2$ is geometrically irreducible.
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
at infinity, and it has dimension $2$. Since the first summand on the right is
zero, it remains to see that the last two summands have the same
dimension. For this, note that the automorphism $(u,x)\mapsto(-u,ix)$ of $Y$, with $i^2=-1$ in
$\mathbf F_9$, conjugates the translation by $c$ into the translation by
$-c$. It therefore exchanges the last two summands, and each of them is a
line. This automorphism is defined only over $\mathbf F_9$, but we use it
only to count dimensions. The decomposition itself is stable under
Frobenius, because the translations are defined over $\mathbf F_3$.

Thus Frobenius acts on the line $H^1_c(\mathbf A^1,h^*\mathcal L_\psi)$
by $-(1+2\omega)$. This is a square root of $-3$, and it is one of the two
reciprocal roots $\pm i\sqrt3$ of $P_1(T)=1+3T^2$ found in the
introduction. Moreover, the number $1+2\omega=\omega-\omega^2$ is the Gauss sum $g$
of the quadratic character of $\mathbf F_3$. The classical fact $|g|=\sqrt q$ is
thus the statement that this $H^1_c$ is pure of weight one.
Section [chap-The-Deligne-Laumon-theorem-for-curves] proves the analogue for every such
sheaf.
