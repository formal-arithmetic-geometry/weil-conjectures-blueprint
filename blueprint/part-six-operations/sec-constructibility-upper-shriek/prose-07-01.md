+++
id = "prose-07-01"
kind = "hidden"
title = "Constructibility of $f^!$"
order = 320
+++
The right adjoint $f^!$ of Theorem [sk-prop-sf-existence] is a functor
between the localizing categories $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$, and Brown
representability gives no information on its values. Duality and the
trace formula need $f^!$ on constructible complexes. Verdier duality
(Section [sec-poincare-duality]) is the statement that
$\mathbb D_X=\cHom(-,a_X^!\Lambda)$ is an involution of $D^b_{\mathrm{ctf}}(X,\Lambda)$,
and this already requires the dualizing complex $a_X^!\Lambda$ to be
constructible; the local terms of the trace formula are traces on
complexes built from $f^!$ of the projections of a correspondence. So we have to prove part (4) of
Theorem [sk-thm-existence]: for a separated morphism $f:X\to Y$ of finite
type and an admissible $\Lambda$, the functor $f^!$ maps
$D^b_{\mathrm{ctf}}(Y,\Lambda)$ into $D^b_{\mathrm{ctf}}(X,\Lambda)$. Unlike parts (1)–(3), this
is not formal, and we have to compute $f^!$.

Since $f^!$ is compatible with composition, equals $j^*$ for an open
immersion $j$, and is local on $X$ and on $Y$
(Proposition [sk-lem-sf-mate]), we may assume that $Y$
is affine and that $f$ is a closed immersion into some $\mathbf A^n_Y$
followed by the projection to $Y$. Now $\mathbf A^n_Y$ is open in
$(\mathbf P^1_Y)^n$, and $(\mathbf P^1_Y)^n\to Y$ is a composite of $n$
morphisms of the form $\mathbf P^1_T\to T$. Hence it suffices to treat two
cases.

- For the projection $p:\mathbf P^1_T\to T$, the trace map on
  $\mathbf P^1$ gives an explicit adjunction, and

$$
p^!=p^*(1)[2].
$$

The counit is the trace $Rp_*\Lambda(1)[2]\to\Lambda$, which on a
geometric fibre is the projection of
$R\Gamma(\mathbf P^1,\Lambda(1)[2])=\Lambda(1)[2]\oplus\Lambda$ onto
$\Lambda=H^2(\mathbf P^1,\Lambda(1))$. The unit is the cycle class of the
diagonal in $\mathbf P^1_T\times_T\mathbf P^1_T$, and the triangle
identities reduce to the fact that the diagonal meets each fibre of
either projection in a single point
(Proposition [sk-prop-geo-p1-adjunction]).
- For a closed immersion $i:Z\hookrightarrow X$ with open complement
  $j:U\hookrightarrow X$, the functor $i^!$ is sections with support in
  $Z$, and the localization triangle $i_*i^!K\to K\to Rj_*j^*K\to$
  expresses $i^!$ through $Rj_*$.

The first case is a calculation. The second shows where the geometry
lies: we must know that direct image along an open immersion preserves
bounded constructible complexes, and, with finite coefficients, finite Tor
amplitude. A small example shows what is involved. For the origin
$i:0\hookrightarrow\mathbf A^1$ over an algebraically closed field, with
complement $j:\mathbf G_m\hookrightarrow\mathbf A^1$, the Kummer covers
$t\mapsto t^{\ell^n}$ give $R^1j_*\Lambda=i_*\Lambda(-1)$, and the triangle
yields $i^!\Lambda\simeq\Lambda(-1)[-2]$, the value that smooth purity
predicts (Example [sk-rem-closed-support]). Thus $i^!$ is not $i^*$: it
records the cohomology of a punctured neighbourhood of $Z$.

Over a field, $Rj_*$ preserves constructibility; this is Deligne's
finiteness theorem in SGA 4$\tfrac12$ (SGA4.5). His proof, which we
follow, is indirect: it proves a statement in families over a base $S$,
because an induction on dimension leads to fibrations over bases of
positive dimension. In families, however, the formation of $Rj_*$ does
not commute with base change. Let $S=\mathbf A^1$ with coordinate $t$, let $Y=\mathbf A^2$ with
coordinates $(t,x)$, viewed over $S$, and let $j$ be the inclusion of
$X=Y\setminus\{(0,0)\}$. The punctured strict henselization of $Y$ at the
origin has, by purity, cohomology $\Lambda$ in degree $0$ and
$\Lambda(-2)$ in degree $3$ only, so $R^1j_*\Lambda=0$. On the fibre over
$t=0$, however, $j$ becomes $\mathbf G_m\hookrightarrow\mathbf A^1$, whose
$R^1j_*\Lambda$ is $\Lambda(-1)$ at the origin. Over $t\neq0$ the map $j$
is an isomorphism, so base change fails only at $t=0$. Deligne's generic
base change theorem says that this is the general picture: for an open
immersion $j:X\hookrightarrow Y$ of schemes of finite type over an
integral base $S$ of finite type over $k$ and a constructible
$\Fell$-sheaf $F$ on $X$, there is a nonempty open $S_0\subset S$ over
which $Rj_*F$ is bounded constructible and its formation commutes with
base change along every $T\to S_0$ of finite type
(Theorem [sk-thm-geo-generic-open]; Deligne proves more). Over $S=\operatorname{Spec}k$ the
only nonempty open is $S$ itself, and we obtain the finiteness and base
change of $Rj_*$ over a field (Corollary [sk-cor-geo-open-finiteness]).

The generic statement is proved by induction on the dimension of the
generic fibre of $X\to S$, and its proof uses the first case. For smooth
$f$ of relative dimension $d$, the functor $f^!$ is $f^*$ tensored with an
invertible complex, locally $\Lambda(d)[2d]$
(Proposition [sk-prop-cohsm]). Hence, for a locally
constant sheaf $L$, the complex $Rf_*L$ is, up to twist and shift, the
dual of $Rf_!$ applied to the dual of $L$. Since $Rf_!$ preserves
constructibility and commutes with base change, $Rf_*L$ is generically
constructible and commutes with base change
(Lemma [sk-lem-geo-smooth-generic]); this is the analogue of Poincaré
duality turning compactly supported cohomology into ordinary cohomology.
For the general case one compactifies $Y$ projectively over $S$ and uses
the coordinate functions as maps to $\mathbf A^1_S$. Each lowers the
dimension of the generic fibre, so the induction hypothesis applies over
the base $\mathbf A^1_S$, and together they cover $Y$ up to a closed
subset finite over $S$ (Lemma [sk-lem-geo-coordinates]). Along a
subset finite over the base, constructibility can be read off from a
proper direct image (Lemma [sk-lem-geo-finite-boundary]). When $X$ is
smooth over $S$ and $F$ is locally constant, the smooth case supplies that
direct image, and the general case reduces to this one by shrinking $X$ to
a dense open on which these conditions hold, after a finite universal
homeomorphism of the base, and applying the induction hypothesis to the
complement.

With torsion coefficients we then obtain
Theorem [sk-prop-sf-rf-shriek-preservation]; the Tor amplitude of $Rj_*K$ is
controlled by a projection formula and grows by at most
$\operatorname{cd}_\ell(j)$ (Proposition [sk-cor-sf-direct-image-ctf]). We pass to
integral and rational coefficients, where $D^b_{\mathrm{ctf}}=\Dbc$, by reduction
modulo a uniformizer: an integral complex is constructible when it is
derived complete with constructible reduction
(Proposition [sk-prop-integral-criterion]). The only point that does not
reduce in this way is the adjunction for the projective line, whose unit
and counit must be constructed as single morphisms with
$\mathcal O_E$-coefficients (Proposition [sk-prop-diagonal-tower]). The
result is Theorem [sk-thm-restriction], and on the way we prove the
compactness of integral constructible complexes that
Section [sec-six-functors-basics] needed (Proposition [sk-prop-int-compactness]).
