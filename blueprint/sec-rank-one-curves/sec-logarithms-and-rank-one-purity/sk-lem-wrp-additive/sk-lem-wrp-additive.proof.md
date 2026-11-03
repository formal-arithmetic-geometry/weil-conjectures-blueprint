+++
kind = "proof"
of = "sk-lem-wrp-additive"
+++
After scaling, the coordinates of $a$ reduce modulo $\ell^n$ to a
compatible system of Frobenius-fixed classes in
$H^1(U,\mathbf Z/\ell^n)$, and these vanish by
Proposition [sk-prop-wrp-h1-no-fixed]. Recall that for a finite abelian
group $G$ the group $H^1(U,G)$ classifies $G$-torsors. By
[Stacks, Tag 0DV5](https://stacks.math.columbia.edu/tag/0DV5), finite locally constant sheaves on the connected scheme
$U$ correspond to finite continuous $\pi_1(U)$-sets, so a $G$-torsor
corresponds to a finite $\pi_1(U)$-set with a commuting simply
transitive action of $G$, that is, to a continuous homomorphism
$\pi_1(U)\to G$. Hence $H^1(U,G)=\Hom_{\mathrm{cont}}(\pi_1(U),G)$.
Frobenius acts on $H^1(U,G)$ through the action of
$s$ on $\pi_1(U)$ by conjugation, so the Frobenius-fixed classes are
the homomorphisms $b$ with $b(s^{-1}gs)=b(g)$.

Now choose a $\Ql$-basis of $E$, with coordinate maps $t_i$. Since
$\pi_1(U)$ is compact, each $t_i a(\pi_1(U))$ is bounded, and after multiplying all
coordinates by one power of $\ell$ we may assume that they take values
in $\Zl$. Each coordinate is then a continuous homomorphism
$\pi_1(U)\to\Zl$ invariant under conjugation by $s$, so its reductions
modulo $\ell^n$ are compatible classes in $H^1(U,\mathbf Z/\ell^n)$
fixed by Frobenius. They vanish by the proposition, and therefore all
coordinates of $a$ are zero.
