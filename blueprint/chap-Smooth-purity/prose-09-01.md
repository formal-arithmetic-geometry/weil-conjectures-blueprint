+++
id = "prose-09-01"
kind = "hidden"
title = "Smooth purity"
order = 717
+++
Poincaré duality for a smooth variety $X$ of dimension $d$ pairs
$H^i_c(X,\Lambda)$ with $H^{2d-i}(X,\Lambda(d))$ through the cup product and a
trace map $H^{2d}_c(X,\Lambda(d))\to\Lambda$. Such a
trace map is the counit of $Ra_!\dashv a^!$ for the structure map $a$ of $X$,
once we know that $a^!\Lambda\simeq\Lambda_X(d)[2d]$. But
Part I produces $f^!$
(Theorem [theorem-exceptional-inverse-image]) as a right adjoint by Brown
representability, with no formula. On charts we can compute it. Let
$f:X\to Y$ be smooth of pure relative dimension $d$, and let $U\subset X$ be
an open subscheme on which $f$ factors as an étale map
$e:U\to\mathbf A^d_Y$ followed by the projection $p_d$. Then with finite
coefficients $f^!K|_U\simeq e^*p_d^*K(d)[2d]$
(Proposition [proposition-exceptional-inverse-image-smooth-morphism]).
Under this isomorphism the counit is integration along $d$ affine lines. It
comes from the trace map of $\mathbf P^1$
(Proposition [proposition-adjunction-projective-line]), which sends the
class of a point to $1$. The question is whether these chart descriptions
agree on overlaps.

In topology they need not. For a submersion $f:X\to Y$ of manifolds with fibres
of real dimension $m$, Verdier's theory gives
$f^!K\simeq f^*K\otimes\mathrm{or}_{X/Y}[m]$. Here the relative orientation
sheaf $\mathrm{or}_{X/Y}$ is locally constant of rank one, and it is trivial
exactly when $f$ can be oriented. A linear change of coordinates $g$ acts on
$H^m_c(\mathbf R^m)$ by the sign of $\det g$. Since
$\operatorname{GL}_m(\mathbf R)$ has two components, the local
identifications need not glue. For complex manifolds
$\operatorname{GL}_d(\mathbf C)$ is connected and the orientation is canonical.

The same argument works for us on a chart. A linear change of coordinates
multiplies the trace map of $\mathbf A^d$ by a locally constant unit on
$\operatorname{GL}_d$. This unit is $1$ at the identity, hence everywhere,
since $\operatorname{GL}_d$ has connected geometric fibres. So every vector
bundle has a canonical trace map
(Proposition [proposition-purity-vector-bundles]). The orientation sheaf
is replaced by the Tate twist $\Lambda(d)$. Over an algebraically closed
field a compatible system of roots of unity trivializes $\Lambda(d)$, but
not canonically, and over $\mathbf F_q$ the twist is visible. Over $\mathbf F_q$ geometric
Frobenius acts on $\Lambda(1)$ by $q^{-1}$ (Section [sec-Weil-complexes]),
and this is where the factor $q^d$ in Weil's Poincaré duality comes from.

Connectedness of $\operatorname{GL}_d$ does not settle the gluing, because two
étale charts $U\to\mathbf A^d_Y$ differ by a map that need not be linear. We
therefore construct the isomorphism without charts, from the diagonal, in the
way a tubular neighbourhood linearizes a submanifold
(Section [sec-Finite-coefficients-3]).

The outcome, Theorem [theorem-smooth-purity-all-admissible-coefficients], is a
canonical isomorphism

$$
\gamma_f:f^*K(d)[2d]\xrightarrow{\sim}f^!K,
$$

natural in $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$ for every admissible $\Lambda$. It is
compatible with base change, composition and change of coefficients, and it
is normalized by the trace map of the affine line. The
statement is Deligne's [sga4, XVIII], where it is called Poincaré
duality.
