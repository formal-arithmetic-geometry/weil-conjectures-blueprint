+++
id = "thm-sf-global-duality"
kind = "theorem"
title = "Global Verdier duality"
order = 3403
uses = ["def-sf-datum", "def-sf-pf", "lem-sf-point", "thm-sf-verdier-exchange"]
+++
In the setting of [def-sf-datum], let $X$ be smooth, proper,
geometrically connected of pure dimension $d$ over $k$ with
exceptional-adjoint admissible structure morphism $a_X$, and let
$K\in D^b_{ctf}(X,\Lambda)$. Then there is a canonical isomorphism

$$
R\Gamma_c(X,K)^\vee\xrightarrow{\ \sim\ }R\Gamma\bigl(X,\mathbb D_XK\bigr),
$$

natural in $K$ and compatible with finite reduction, scalar extension, and
shifts. For $K=\Lambda_X$ it specializes to
$R\Gamma_c(X,\Lambda)^\vee\cong R\Gamma(X,\omega_X)$.

## Proof

Apply [thm-sf-verdier-exchange] with $Y=s$, $f=a_X$ and $M=K$:
$D_s(Ra_{X!}K)\cong Ra_{X*}D_XK$. Apply $\Fib_s$ and the point
identifications of [lem-sf-point]: the left-hand side becomes
$R\operatorname{Hom}_\Lambda(R\Gamma_c(X,K),\Lambda)=R\Gamma_c(X,K)^\vee$
and the right-hand side becomes
$\Fib_s(Ra_{X*}D_XK)=R\Gamma(X,\mathbb D_XK)$. The resulting composite is
the displayed isomorphism; naturality and the compatibilities are those of
the two ingredients. The constant case is
$\mathbb D_X\Lambda_X=R\mathcal H om_X(\Lambda_X,Ra_X^!\Lambda)=\omega_X$
by [def-sf-pf].
