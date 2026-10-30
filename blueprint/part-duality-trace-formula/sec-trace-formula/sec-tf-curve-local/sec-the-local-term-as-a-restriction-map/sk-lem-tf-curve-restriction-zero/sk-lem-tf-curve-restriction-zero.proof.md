+++
kind = "proof"
of = "sk-lem-tf-curve-restriction-zero"
uses = ["sk-lem-curve-sylow-trace", "sk-lem-sf-flat-model", "sk-lem-tf-blowup-restriction"]
+++
When $K_{\bar y}=0$, the cohomology of $T$ and of the diagonal of $T$
without supports vanishes, so by localization
the restriction map $\rho$ becomes an ordinary restriction to the
punctured diagonal. After passing to a cover of degree prime to $\ell$, the
monodromy is an $\ell$-group and the curves are in the position of
Lemma [sk-lem-tf-blowup-restriction], which shows that the restriction
vanishes on the cover. Since the degree is invertible in $A$, the
vanishing descends by the finite étale trace.

We compute on the étale model. This is legitimate because the classical
comparison identifies tensor products, duality,
exceptional adjunctions and the pairing between graph and diagonal
with their versions there. Let $X_1$ and $X_2$ be two copies of
the strict localization of $X$ at $y$, and let $T$ be the
strict localization of $X_1\times X_2$ at $(y,y)$. Write

$$
H=X_1\times\{y\},\qquad V=\{y\}\times X_2,
$$

and keep $\Gamma$ and $\Delta$ for the transposed Frobenius graph and the
diagonal in $T$. The graph $\Gamma$ is tangent to $V$, the diagonal has slope one
and $H$ is horizontal, so the tangent cone of $\Gamma\cup V$ meets those of
$\Delta$ and of $H$ only at the origin. We verify this below in coordinates,
on the cover where it is used.

Let $N=(\mathbb D_XK)|_{X_1-y}$, the dual of $K|_{X_1-y}$ with respect to the restriction
of $\omega_X$, and let $Q=K|_{X_2-y}$. Write $j_1:X_1-y\hookrightarrow X_1$ and
$j_2:X_2-y\hookrightarrow X_2$ for the inclusions. Since $K_{\bar y}=0$,
localization gives $K|_{X_2}=j_{2!}Q$, and by duality
$(\mathbb D_XK)|_{X_1}=Rj_{1*}N$, since the dual of an extension by zero is the direct image of the dual. The ordinary external Künneth comparison identifies
$P=(\mathbb D_XK\boxtimes K)|_T$ with $Rj_*j'_!(N\boxtimes Q)$, where

$$
j:T-V\hookrightarrow T,\qquad
j':T-(H\cup V)\hookrightarrow T-V.
$$

Both $R\Gamma(T,P)$ and $R\Gamma(\Delta,\delta^*P)$ are
zero, because the schemes are strictly local and the stalk at the closed point is
$(\mathbb D_XK)_{\bar y}\otimes^{\mathbf L} K_{\bar y}=0$. Therefore the localization triangles
identify $\rho$, shifted by one, with the
ordinary restriction

$$
R\Gamma(T-\Gamma,P)\longrightarrow
R\Gamma(\Delta-y,\delta^*P),
$$

which under the Künneth identification above is

$$
R\Gamma(T-(V\cup\Gamma),j'_!(N\boxtimes Q))
\longrightarrow R\Gamma(\Delta-y,(N\boxtimes Q)|_{\Delta-y}).
$$

It remains to show that this restriction map is zero.

Choose bounded finite projective lisse models of $N$ and $Q$ by
Lemma [sk-lem-sf-flat-model]. Since a punctured strictly local trait is
its generic point, the constructible terms of these models are lisse. Choose
finite Galois covers trivializing all their terms and take quotients
by $\ell$-Sylow subgroups as in Lemma [sk-lem-curve-sylow-trace].
Their normalizations are covers $X_1'\to X_1$ and $X_2'\to X_2$ of degrees
$d_1,d_2$ prime to $\ell$, over which the monodromy of each term factors
through a finite $\ell$-group. After further generically
étale totally ramified extensions, followed by normalization, we may
assume that both degrees are equal to
$d=\operatorname{lcm}(d_1,d_2)$: over a trait with uniformizer $t$,
the Eisenstein polynomial $z^e+tz-t$ has derivative $ez^{e-1}+t\neq0$,
so for every $e>1$, also when $p\mid e$, it defines a totally ramified,
generically étale extension of degree $e$.

The two covers are finite flat of rank $d$, and their product,
localized at the unique closed point $y'$ over $(y,y)$, is a strictly
local smooth surface $T'$, finite flat of rank $d^2$ over $T$. To see
smoothness, note that the covers descend to normal covers of étale
neighbourhoods of $y$, which are curves, and that normal curves over the
perfect field $k$ are smooth. Write $\Gamma',V',\Delta',H'$ for the inverse
images of $\Gamma,V,\Delta,H$ in $T'$.

We now compute the tangent cones of these four curves at $y'$. Let $u$ and
$v$ be the pullbacks to the two factors $X_1$ and $X_2$ of the same uniformizer
of $X$ at $y$, so that $\Delta$ has equation $u-v=0$, while $V$ and $H$
have equations $u=0$ and $v=0$. Choose uniformizers $\xi$ of $X_1'$ and
$\eta$ of $X_2'$; the completed local ring of $T'$ at $y'$ is $k[[\xi,\eta]]$.
Since the residue field $k$ is algebraically closed, both covers are totally
ramified, so $u$ is a unit of $k[[\xi]]$ times $\xi^d$, and similarly for
$v$. Multiplying $\xi$ and $\eta$ by suitable $d$th roots of nonzero
constants, we may assume that

$$
u\equiv\xi^d,\qquad v\equiv\eta^d\pmod{(\xi,\eta)^{d+1}}.
$$

Write $\varphi(v)=(\Phi_X^m)^\#u$, a power series in $v$. The graph $\Gamma$ has
equation $u-\varphi(v)=0$. Since $\Phi_X^m$ is purely inseparable of degree
$q^m$ and fixes $y$, we have $\operatorname{ord}_v\varphi=q^m>1$, and hence

$$
\varphi(v)\in(\eta)^{dq^m}\subseteq(\xi,\eta)^{d+1}.
$$

It follows that the pulled-back equations of $\Gamma'$, $V'$, $\Delta'$ and $H'$
have initial forms

$$
\xi^d,\qquad\xi^d,\qquad\xi^d-\eta^d,\qquad\eta^d,
$$

respectively. Thus the tangent cone of $\Gamma'\cup V'$ is supported on the line
$\xi=0$. The tangent cone of $H'$ is supported on $\eta=0$, and that of
$\Delta'$ on the lines $\xi=\zeta\eta$ with $\zeta^d=1$. Away from the origin,
the first support therefore meets neither of the others. When $p\mid d$
the form $\xi^d-\eta^d$ is a $p$th power, but its zero set is still a
union of such lines. Lemma [sk-lem-tf-blowup-restriction] uses only these
zero sets, so we may replace $\Gamma'\cup V'$, $\Delta'$ and $H'$ by their
reductions, since this changes neither the open complements nor the local
cohomology.

Let $N'$ and $Q'$ be the pullbacks of $N$ and $Q$ to the punctured covers
$X_1'-y'$ and $X_2'-y'$. By the choice of the covers, the complex $N'\boxtimes Q'$
has finite $\ell$-group monodromy on the complement of the axes, and hence
also on the smaller open set obtained by removing $\Gamma'$. Therefore Lemma [sk-lem-tf-blowup-restriction], applied with $D=\Gamma'\cup V'$, the regular curve $H'$ and $C=\Delta'$,
shows that the punctured
restriction on the cover is zero.

The finite map $T'\to T$ has degree $d^2$ and is étale away
from $H\cup V$. In particular, $\Delta'-y'\to\Delta-y$ is finite étale
of degree $d^2$. Pullback along $T'\to T$ commutes with restriction
and with extension by zero.
Thus the restriction on $T$, followed by pullback to $\Delta'-y'$, equals
pullback to $T'$ followed by the restriction on $T'$, which is zero.
Composing with the finite étale trace from $\Delta'-y'$ to $\Delta-y$, and using
that the trace after pullback is multiplication by $d^2$, we see that
$d^2$ times the restriction on $T$ is zero. Since $d^2$ is a unit
of $A$, the punctured restriction is zero in $D(A)$, and hence so is
$\rho$. The comparison theorems transport this
identity from the classical strictly local models back to the
pro-étale formulation.

Finally, by Lemma [sk-lem-tf-curve-supported-pairing], $\operatorname{LT}_y(\psi)$
is the image of $[\psi]$ under a composite that begins with
$\rho$, so it is zero.
