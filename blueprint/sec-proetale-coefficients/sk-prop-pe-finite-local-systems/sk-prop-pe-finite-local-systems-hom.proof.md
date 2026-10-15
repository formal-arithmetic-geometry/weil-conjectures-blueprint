+++
kind = "proof"
of = "det-pe-finite-local-systems-hom"
+++
The constant étale sheaf functor $M\mapsto M_{X,\Et}$ is exact and preserves
finite limits (it is the inverse image of the morphism from $X_{\Et}$ to the
point), and $\nu_X^*$ is exact and preserves finite limits
([sk-prop-pe-comparison-morphism]). Hence $M\mapsto\underline M$ is exact,
preserves finite limits, and $\underline{\Lambda^n}=\Lambda_X^n$.

*(1).* Exactness gives the presentation
$\Lambda_X^m\xrightarrow{a}\Lambda_X^n\to\underline M\to0$. For an object $V$ of
$X_{\Proet}$, applying $\Hom_{\Lambda_V}(-,N|_V)$ and using
$\Hom_{\Lambda_V}(\Lambda_V^n,N|_V)=N(V)^n$ gives
$\Hom(\underline M|_V,N|_V)=\ker(N(V)^n\to N(V)^m)$, naturally in $V$, which is
the claimed isomorphism of sheaves.

*(2).* By (1) with $N=\underline{M'}$ and exactness of the constant sheaf
functor, $\mathcal Hom(\underline M,\underline{M'})\cong
\ker(\underline{M'}^n\to\underline{M'}^m)\cong
\underline{\ker(M'^n\to M'^m)}=\underline{\Hom_\Lambda(M,M')}$. On sections over
the constant presentation this sends a module map $M\to M'$ to the induced map of
constant sheaves; composition is compatible because it is so on these sections
and both sides are sheaves generated locally by them.

*(3).* The automorphism sheaf is the finite limit
$\{(f,g)\in\mathcal End(\underline M)^2:fg=1,\ gf=1\}$, mapped isomorphically
to its first factor. By (2) and preservation of finite limits by
$M\mapsto\underline M$, it is
$\underline{\{(f,g)\in\operatorname{End}(M)^2:fg=1=gf\}}=
\nu_X^*\operatorname{Aut}_\Lambda(M)_{X,\Et}$, with the group law induced by
composition. Such a sheaf is classical by [sk-thm-pe-classical-sheaves].
