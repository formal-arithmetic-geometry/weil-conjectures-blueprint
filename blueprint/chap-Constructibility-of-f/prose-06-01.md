+++
id = "prose-06-01"
kind = "hidden"
title = "Constructibility of $f^!$"
order = 534
+++
Brown representability gave us $f^!$
(Theorem [theorem-existence-exceptional-inverse-image]), but only as a
functor

$$
f^!:\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))\longrightarrow\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))
$$

for $f:X\to Y$ separated of finite type and $\Lambda$ an admissible coefficient
ring. It tells us nothing about the values of $f^!$. A priori, $f^!$ of a
constructible complex is just some object of the large category on the right,
possibly unbounded and with cohomology sheaves that are not constructible.

The rest of the notes needs more than this. For example, Verdier duality (Chapter [chap-Verdier-and-Poincare-duality]) says that
$\mathbb D_X=\cHom(-,a_X^!\Lambda)$ is an involution of $D^b_{\mathrm{ctf}}(X,\Lambda)$,
and this makes sense only if the dualizing complex $a_X^!\Lambda$ lies in
$D^b_{\mathrm{ctf}}(X,\Lambda)$. Similarly, the local terms of the trace formula are defined through the isomorphism
$\cHom(c_2^*K,c_1^!K)\simeq c^!(K\boxtimes\mathbb D_XK)$ for a
correspondence $c=(c_1,c_2)$
(Lemma [lemma-external-duality-trace-morphism]), which also needs $f^!$
to preserve constructible complexes. In this chapter we prove what both need
(part (4) of Theorem [theorem-exceptional-inverse-image]): $f^!$ maps
$D^b_{\mathrm{ctf}}(Y,\Lambda)$ into $D^b_{\mathrm{ctf}}(X,\Lambda)$. A universal property cannot give this, so we have to compute $f^!$, and the computation is local.

By
Proposition [proposition-composition-open-restriction-compactifications-f],
the functor $f^!$ is compatible with composition, equals $j^*$ for an open
immersion $j$, and is local on $X$ and on $Y$. We may therefore assume that
$Y$ is affine and that $f$ is a closed immersion into some $\mathbf A^n_Y$
followed by the projection to $Y$. Since $\mathbf A^n_Y$ is open in
$(\mathbf P^1_Y)^n$, and $(\mathbf P^1_Y)^n\to Y$ is a composite of $n$
projections $\mathbf P^1_T\to T$, two cases remain.

For the projection $p:\mathbf P^1_T\to T$ we can write the adjunction
down, and we find $p^!=p^*(1)[2]$
(Proposition [proposition-adjunction-projective-line]). Here the counit is the trace $Rp_*\Lambda(1)[2]\to\Lambda$, and the unit is the cycle class of the diagonal in $\mathbf P^1_T\times_T\mathbf P^1_T$. The triangle identities then hold because the diagonal meets each fibre of either projection
in a single point. For a closed immersion $i:Z\hookrightarrow X$ with open complement $j:U\hookrightarrow X$, on the other hand, the functor $i^!$ takes sections with support in
$Z$, and it sits in the localization triangle

$$
i_*i^!K\longrightarrow K\longrightarrow Rj_*j^*K\longrightarrow .
$$

Let $K$ be constructible. Then $j^*K$ is constructible, and since $i^*i_*\simeq\mathrm{id}$ and
$i_*$ preserves constructibility, $i^!K$ is constructible exactly when the
third term $Rj_*j^*K$ is. So the constructibility of $f^!$ comes down to one
question: does direct image along an open immersion preserve bounded
constructible complexes and, with finite coefficients, finite Tor
amplitude? Proper base change does not help here, since $j$ is not
proper.

The answer is not formal, because $Rj_*$, and with it $i^!$, sees more
than the stalks of $K$ on $Z$: it sees the cohomology of $K$ on a punctured
neighbourhood of $Z$. For the origin $i:0\hookrightarrow\mathbf A^1$ over
an algebraically closed field, the stalk of $Rj_*\Lambda$ at $0$ is the
cohomology of a punctured disc, which the Kummer covers of $\mathbf G_m$
compute to be $\Lambda\oplus\Lambda(-1)[-1]$, and the triangle gives
$i^!\Lambda\simeq\Lambda(-1)[-2]$, whereas $i^*\Lambda=\Lambda$
(Example [example-closed-support] below).

Over a field the answer is Deligne's finiteness theorem in
SGA 4$\tfrac12$ [sga4-5], and we follow his proof. Its induction on dimension leads to fibrations over bases of positive dimension, so
Deligne proves a statement in families over a base $S$. In families,
however, the formation of $Rj_*$ need not commute with base change. Let
$S=\mathbf A^1$ with coordinate $t$, let $Y=\mathbf A^2$ with coordinates
$(t,x)$, viewed over $S$, and let $j$ be the inclusion of
$X=Y\setminus\{(0,0)\}$. By purity
(Theorem [theorem-smooth-purity-all-admissible-coefficients], proved in
Chapter [chap-Smooth-purity] below), the punctured strict henselization of
$Y$ at the origin has cohomology $\Lambda$ in degree $0$ and
$\Lambda(-2)$ in degree $3$ only. Hence $R^1j_*\Lambda=0$. On the fibre
over $t=0$, however, $j$ becomes $\mathbf G_m\hookrightarrow\mathbf A^1$,
whose $R^1j_*\Lambda$ is $\Lambda(-1)$ at the origin. Since over $t\neq0$ the map $j$ is an isomorphism, base change fails only at $t=0$.

Deligne's generic base change theorem says that this is the general
picture. Let $j:X\hookrightarrow Y$ be an open immersion of schemes of
finite type over an integral base $S$ of finite type over $k$, and let $F$
be a constructible $\Fell$-sheaf on $X$. Then there is a nonempty open
$S_0\subset S$ over which $Rj_*F$ is bounded constructible and its
formation commutes with base change along every $T\to S_0$ of finite type
(Theorem [theorem-generic-constructibility-base-change-rj]; Deligne
proves more). Over $S=\operatorname{Spec}k$ the only nonempty open is $S$
itself, so we obtain the finiteness and base change of $Rj_*$
over a field (Corollary [corollary-open-direct-image-over-field]).

The projective line returns in the proof of the generic theorem. There we
must control $Rf_*L$ for smooth $f$ and locally constant $L$, and we do so
through the formula for $f^!$ of a smooth morphism (Section [sec-Smooth-morphisms]).

For finite coefficients
(Theorem [theorem-f-shriek-finite-coefficients]) we also bound the Tor
amplitude of $Rj_*K$: it grows by at most $\operatorname{cd}_\ell(j)$
(Proposition [proposition-open-direct-image-preserves-finite]). For
integral and rational coefficients we have $D^b_{\mathrm{ctf}}=\Dbc$, and we reduce
modulo a uniformizer. This works because an integral complex is
constructible if it is derived complete with constructible reduction
(Proposition [proposition-integral-constructibility-criterion]). Only the
adjunction for the projective line resists this reduction. Its unit and
counit must be constructed as single morphisms with
$\mathcal O_E$-coefficients
(Proposition [proposition-ell-adic-cycle-class-diagonal]). The result is
Theorem [theorem-f-shriek-ell-adic-coefficients].
