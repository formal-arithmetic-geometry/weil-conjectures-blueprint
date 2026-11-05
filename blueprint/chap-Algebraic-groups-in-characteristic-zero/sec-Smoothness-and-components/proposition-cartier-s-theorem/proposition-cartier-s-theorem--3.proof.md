+++
kind = "proof"
of = "proposition-cartier-s-theorem--3"
order = 1717003
uses = []
+++
The inclusion $G^\circ\subseteq G$ gives one inclusion of Lie algebras.
For the reverse, put $B=\Omega[\GL_n]/I$, let $e:B\to\Omega$ be the
counit, and put $\mathfrak m=\ker e$. Cartier's lemma for bialgebras
shows that

$$
P=\bigcap_{r\geq0}\mathfrak m^r
$$

is prime (`Bialgebra.isPrime_iInf_pow_ker_counitAlgHom`). Hence $V(P)$
is an irreducible closed subset of $G$ containing the identity, and is
contained in its identity component. Every function $a$ vanishing on
$G^\circ$ therefore has image in $P$. By Krull's intersection theorem
there is an $s\in B$ with $e(s)=1$ and $sa=0$
(`AlgHom.mem_iInf_pow_ker_iff`).

A tangent vector $1+\varepsilon X$ of $G$ gives an algebra map
$\varphi:B\to\Omega[\varepsilon]/(\varepsilon^2)$ reducing to $e$.
The element $\varphi(s)$ is a unit, since its reduction is $1$.
The equation $\varphi(s)\varphi(a)=0$ implies $\varphi(a)=0$.
Thus the tangent vector satisfies every equation of the reduced
identity component. This is
`AlgebraicGeometry.GeneralLinearGroup.dualUnit_mem_zeroLocus_identityComponent`;
combining it with the first inclusion proves equality.
