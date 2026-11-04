+++
kind = "proof"
of = "lemma-invariant-additive-characters"
order = 1096
+++
After scaling, the coordinates of $a$ reduce modulo $\ell^n$ to a
compatible system of Frobenius-fixed classes in
$H^1(U,\mathbf Z/\ell^n)$, which vanish by
Proposition [proposition-no-fixed-class-degree-one]. This needs $H^1$ to be
identified with homomorphisms.

Recall that for a finite abelian
group $G$ the group $H^1(U,G)$ classifies $G$-torsors. By
[Stacks, [0DV5](https://stacks.math.columbia.edu/tag/0DV5)], finite locally constant sheaves on the connected scheme
$U$ correspond to finite continuous $\pi_1(U)$-sets. Under this
correspondence a $G$-torsor becomes a finite $\pi_1(U)$-set with a commuting
simply transitive action of $G$, that is, a continuous homomorphism
$\pi_1(U)\to G$. Hence $H^1(U,G)=\Hom_{\mathrm{cont}}(\pi_1(U),G)$.
Frobenius acts on $H^1(U,G)$ through the action of
$s$ on $\pi_1(U)$ by conjugation. The Frobenius-fixed classes are therefore
the homomorphisms $b$ with $b(s^{-1}gs)=b(g)$.

Choose a $\mathbf Q_\ell$-basis of $E$, with coordinate maps $t_i$.  Since
$\pi_1(U)$ is compact, each $t_i a(\pi_1(U))$ is bounded, and after multiplying all
coordinates by one power of $\ell$ we may assume that they take values
in $\mathbf Z_\ell$.  Each coordinate is then a continuous homomorphism
$\pi_1(U)\to\mathbf Z_\ell$ invariant under conjugation by $s$. Its reductions
modulo $\ell^n$ are compatible classes in $H^1(U,\mathbf Z/\ell^n)$
fixed by Frobenius. By the proposition they vanish, and hence every
coordinate of $a$ is zero.
