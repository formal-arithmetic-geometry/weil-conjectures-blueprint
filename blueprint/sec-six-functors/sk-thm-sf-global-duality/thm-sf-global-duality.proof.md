+++
kind  = "proof"
of    = "thm-sf-global-duality"
+++
Apply [thm-sf-verdier-exchange] with $Y=s$, $f=a_X$ and $M=K$:
$D_s(Ra_{X!}K)\cong Ra_{X*}D_XK$. Apply $\Fib_s$ and the point
identifications of [lem-sf-point]: the left-hand side becomes
$R\operatorname{Hom}_\Lambda(R\Gamma_c(X,K),\Lambda)=R\Gamma_c(X,K)^\vee$
and the right-hand side becomes
$\Fib_s(Ra_{X*}D_XK)=R\Gamma(X,\mathbb D_XK)$. Since $\Fib_s$ is an
equivalence onto the point category by [lem-sf-point], the resulting
composite is an isomorphism in $D^b_c(s,\Lambda)$, and it is the displayed
isomorphism; naturality and the compatibilities are those of
the two ingredients. The argument uses only the exceptional adjunction for $a_X$ (so that
[thm-sf-verdier-exchange] applies to $f=a_X$, $Y=s$), which is available
for every separated finite-type morphism, never that $a_X$ is proper: the compact-support image
$Ra_{X!}$ and the ordinary image $Ra_{X*}$ enter as two different
functors, and no comparison $Ra_{X!}\cong Ra_{X*}$ is invoked. Hence the
same proof covers both cases of the hypothesis, the proper one and the
nonproper one $X=X_0\times_{k_0}k$. The constant case is
$\mathbb D_X\Lambda_X=R\mathcal H om_X(\Lambda_X,Ra_X^!\Lambda)=\omega_X$
by [def-sf-pf].
