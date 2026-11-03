+++
kind  = "proof"
of    = "lem-wft-as-comparison"
+++
*(1).* The map $a\mapsto\Psi(\operatorname{Tr}(a\,\cdot))$ is a homomorphism
from $k_0$ to the group of characters of $k_0$. It is injective: if
$\Psi(\operatorname{Tr}(az))=1$ for all $z$, then $\operatorname{Tr}(az)=0$
for all $z$, because $\Psi$ is a nontrivial character of the group
$\mathbf F_p$ of prime order and hence injective; the trace
$k_0\to\mathbf F_p$ is surjective (the extension is separable), so $a=0$.
A character of the elementary abelian group $k_0\cong\mathbf F_p^m$ takes
values in the group $\mu_p(\Lambda)$, cyclic of order $p$ because $\Lambda$
is a field containing $\mu_p$, so there are exactly $p^m=q$ characters, and
the injection is a bijection. The character attached to $a$ is trivial
exactly when $a=0$.

*(2).* Put $u=\sum_{0\le i<m}(ay)^{p^i}$ in $\mathcal O(Y_q)$. Then

$$
u^p-u=(ay)^{p^m}-ay=a^qy^q-ay=a(y^q-y)=af,
$$

because $a^q=a$. Hence $u$ defines an $X_0$-morphism $h_a:Y_q\to Y_p$. For
$c\in k_0$, $\sigma_c^*u=\sum_i(a(y+c))^{p^i}=u+\operatorname{Tr}(ac)$, which
is the relation $h_a\circ\sigma_c=\sigma_{\operatorname{Tr}(ac)}\circ h_a$.
Pullback of functions along $h_a$ is a map
$h_a^*:\pi_{p*}\Lambda\to\pi_{q*}\Lambda$, and if
$\sigma_b^*\varphi=\Psi(b)\varphi$ for all $b\in\mathbf F_p$, then
$\sigma_c^*h_a^*\varphi=h_a^*\sigma_{\operatorname{Tr}(ac)}^*\varphi
=\Psi(\operatorname{Tr}(ac))\,h_a^*\varphi=\psi(c)\,h_a^*\varphi$. So $h_a^*$
maps $e_\Psi\pi_{p*}\Lambda$ into $e_\psi\pi_{q*}\Lambda$. To see that this is
an isomorphism, look at a geometric point $\bar x$: the fibres $T_q$ and $T_p$
are torsors under $k_0$ and $\mathbf F_p$ ([lem-fd-as-cover] and the same
argument for $\mathrm{AS}_q$), and the stalks are the functions on them. Fix
$y_0\in T_q$ and $u_0=h_a(y_0)$. The $\Psi$-isotypic functions on $T_p$ are
the multiples of $\varphi_0(u_0+b)=\Psi(b)$, and the $\psi$-isotypic functions
on $T_q$ are the multiples of $\varphi'_0(y_0+c)=\psi(c)$; both are free of
rank one. Since $(h_a^*\varphi_0)(y_0+c)=\varphi_0(u_0+\operatorname{Tr}(ac))
=\psi(c)$, the map $h_a^*$ sends the generator to the generator, so it is an
isomorphism on every stalk, hence an isomorphism of sheaves.

*(3).* For $x=0$ and $y=0$ one gets $u=0$. The trivialization at zero is
evaluation of an isotypic function at the chosen root, and
$(h_a^*\varphi)(0)=\varphi(h_a(0))=\varphi(0)$.
