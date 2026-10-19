+++
kind = "proof"
of = "sk-lem-tf-curve-restriction-zero"
uses = ["sk-lem-curve-sylow-trace", "sk-lem-sf-flat-model", "sk-lem-tf-blowup-restriction"]
+++
Both full complexes vanish when $K_{\bar y}=0$, so localization turns
the supported restriction into an ordinary restriction to the
punctured diagonal. A cover of degree prime to $\ell$ makes the
monodromy an $\ell$-group and puts the curves in the position of
[sk-lem-tf-blowup-restriction], which kills the restriction
upstairs. The finite étale trace then descends the vanishing,
because the degree is invertible in $A$.

The classical comparison transports tensor products, duality,
exceptional adjunctions and the graph–diagonal pairing to the
étale model, where we compute. Let $X,Y$ now denote two copies of
the strict localization of the given curve at $y$, and $T$ the
strict localization of $X\times Y$ at $(y,y)$. Write

$$
 H=X\times\{y\},\quad V=\{y\}\times Y,\quad
 G=\Gamma_{(\Phi_X^m,\mathrm{id})},\quad B=\Delta.
$$

The Frobenius graph has vertical tangent, the diagonal has slope
one, and $H$ has horizontal tangent. Thus $D=G\cup V$ is in
general position with both $B$ and $H$.

Let $N=(\mathbb D_XK)|_{X-y}$, the dual of $K|_{X-y}$ for the restriction
of $\omega_X$, and let $Q=K|_{Y-y}$. Since $K_{\bar y}=0$, localization and
duality give, for $K$ on the first and on the second factor,

$$
 \mathbb D_XK=Rj_{X*}N,\qquad K=j_{Y!}Q.
$$

The ordinary external Künneth comparison identifies
$P=(\mathbb D_XK\boxtimes K)|_T$ with $Rf_*g_!(N\boxtimes Q)$, where

$$
 f:T-V\hookrightarrow T,\qquad
 g:T-(H\cup V)\hookrightarrow T-V.
$$

The graph–diagonal pairing factors through the supported
restriction

$$
 R\Gamma_G(T,P)\longrightarrow
 R\Gamma_y(B,b^*P).
$$

Indeed, the product of a class supported on $G$ with a class
supported on $B$ is restriction to $B$ followed by the supported
evaluation product. Both $R\Gamma(T,P)$ and $R\Gamma(B,b^*P)$ are
zero: the schemes are strictly local, and their closed stalk is
$(\mathbb D_XK)_{\bar y}\otimes^{\mathbf L} K_{\bar y}=0$. The localization triangles therefore
identify the supported restriction, shifted by one, with the
ordinary restriction

$$
 R\Gamma(T-G,P)\longrightarrow
 R\Gamma(B-y,b^*P),
$$

which under the Künneth identification above is

$$
 R\Gamma(T-(V\cup G),g_!(N\boxtimes Q))
 \longrightarrow R\Gamma(B-y,(N\boxtimes Q)|_{B-y}).
$$

It remains to show that this restriction map is zero.

Choose bounded finite projective lisse models of $N,Q$ by
[sk-lem-sf-flat-model]; a punctured strictly local trait is
its generic point, so its constructible terms are lisse. Choose
finite Galois covers trivializing all their terms and take quotients
by $\ell$-Sylow subgroups as in [sk-lem-curve-sylow-trace].
Their normalizations give $X'\to X$ and $Y'\to Y$ of degrees
$d_1,d_2$ prime to $\ell$, over which the termwise monodromy factors
through finite $\ell$-groups. Normalize after further generically
étale totally ramified extensions to make both degrees equal to
$d=\operatorname{lcm}(d_1,d_2)$. An extension of any degree $e>1$
of a trait with uniformizer $t$ is given by the Eisenstein equation
$z^e+t z-t=0$: its derivative is nonzero, and it defines a regular
trait with uniformizer $z$, generically separable even when $p\mid e$.

The two covers are finite flat of rank $d$, and their product,
localized at the unique closed point, is a strictly local smooth
surface $T'$, finite flat of rank $d^2$ over $T$. The data descend
to curve neighbourhoods, and normalization over the perfect field
gives smooth curves; equivalently, the completed local ring of $T'$
is $k[[\xi,\eta]]$ for independent parameters $\xi,\eta$. Replacing
the inverse-image curves by their reductions does not change the
relevant open sets or local cohomology. For parameters $u,v$ on the
original factors write

$$
 u=\alpha\xi^d+O(\xi^{d+1}),\qquad
 v=\beta\eta^d+O(\eta^{d+1}),\qquad \alpha\beta\ne0.
$$

Write $\varphi(v)=(\Phi_X^m)^\#u$. The graph has equation $u=\varphi(v)$,
with $\operatorname{ord}_v\varphi=q^m$, and the diagonal has
equation $u=v$. Their pulled-back initial forms, up to nonzero
constants, are

$$
 \xi^d,\qquad \alpha\xi^d-\beta\eta^d.
$$

The vertical axis has initial form $\xi^d$, and the horizontal
axis $\eta^d$. Thus the support of the tangent cone of $G'\cup V'$
meets neither that of $B'$ nor the horizontal axis outside zero;
this holds also when $p\mid d$, since only supports of tangent cones
enter. The complex $N'\boxtimes Q'$ has finite $\ell$-group
monodromy on the complement of the axes, and also after removing
$G'$. [sk-lem-tf-blowup-restriction], applied with removed curve
$G'\cup V'$ and regular divisor $H'$, therefore makes the upstairs
punctured restriction zero.

The finite map $T'\to T$ has degree $d^2$ and is étale away
from $H\cup V$; in particular $B'-y'\to B-y$ is finite étale
of degree $d^2$. The square formed by the downstairs and upstairs
restriction maps commutes by functoriality of ordinary pullback and
extension by zero. It is formed after the Künneth rewriting, on
the complement of the axes, where only étale pullbacks occur.
Applying the finite étale trace on the punctured target, and using
that trace after pullback is multiplication by $d^2$, shows that
$d^2$ times the downstairs restriction is zero. Since $d^2$ is a unit
of $A$, the punctured restriction is zero in $D(A)$, and hence so is
the supported restriction. The comparison theorems transport this
identity back to the proétale formulation.
