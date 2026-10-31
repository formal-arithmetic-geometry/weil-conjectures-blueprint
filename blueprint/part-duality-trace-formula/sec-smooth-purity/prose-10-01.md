+++
id = "prose-10-01"
kind = "hidden"
title = "Smooth purity"
order = 425
+++
The functor $f^!$ of Theorem [sk-thm-existence] is a right adjoint
produced by Brown representability, and outside a few cases we know it
only through the adjunction $Rf_!\dashv f^!$. For a smooth morphism we
already know more. If $f:X\to Y$ is smooth of pure relative dimension
$d$ and $U\subset X$ is an open on which $f$ factors as an étale map
$e:U\to\mathbf A^d_Y$ followed by the projection $p_d$, then with finite
coefficients $f^!K|_U\simeq e^*p_d^*K(d)[2d]$
(Proposition [sk-prop-cohsm]). The counit is integration
along $d$ affine lines, and integration along one line comes from the
adjunction for $\mathbf P^1$ (Proposition [sk-prop-geo-p1-adjunction]),
whose trace map sends the class of a point to $1$. Smooth purity says that
these chart descriptions come from one isomorphism on all of $X$, for
every admissible coefficient ring $\Lambda$: there is a canonical
isomorphism

$$
\gamma_f:f^*K(d)[2d]\xrightarrow{\sim}f^!K,
$$

natural in $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$, compatible with base change,
composition and change of coefficients, and normalized by the trace
map of the affine line (Theorem [sk-thm-purity-transport]). For étale $f$ this says $f^!\simeq f^*$, and for the structure map
$a$ of a smooth curve $C$ it says $a^!\Lambda\simeq\Lambda_C(1)[2]$, a
single sheaf placed in degree $-2$.

The topological model explains the shape of the formula. For a
submersion $f:X\to Y$ of topological manifolds with fibres of real
dimension $m$, Verdier's theory gives
$f^!K\simeq f^*K\otimes\mathrm{or}_{X/Y}[m]$, where $\mathrm{or}_{X/Y}$
is the relative orientation sheaf. It is locally constant of rank one,
and it is trivial exactly when $f$ can be oriented. On a chart
$\mathbf R^m$ a linear change of coordinates $g$ acts on
$H^m_c(\mathbf R^m)$ by the sign of $\det g$, and since
$\operatorname{GL}_m(\mathbf R)$ has two components the local
identifications need not glue. For complex manifolds
$\operatorname{GL}_d(\mathbf C)$ is connected, $m=2d$, and the
orientation is canonical. In our setting the same argument applies:
$\operatorname{GL}_d$ has connected geometric fibres, so a linear
change of coordinates acts trivially on the trace map of
$\mathbf A^d$, and every vector bundle has a canonical trace map
(Proposition [sk-prop-an]). What replaces the orientation sheaf
is the Tate twist $\Lambda(d)$. Over an algebraically closed field a
compatible system of roots of unity trivializes $\Lambda(1)$, but no
such choice is canonical, and over $\mathbf F_q$ geometric Frobenius
acts on $\Lambda(1)$ by $q^{-1}$ (Section [sec-frobenius]). This is where the factor $q^d$ in Weil's
Poincaré duality comes from. The analogue in coherent duality is the
formula $f^!K=f^*K\otimes\Omega^d_{X/Y}[d]$, in which $\Omega^d_{X/Y}$
plays the role of the twist and $[d]$ that of $[2d]$.

Connectedness of $\operatorname{GL}_d$ does not settle the
gluing on $X$. Two étale charts $U\to\mathbf A^d_Y$ differ by a map
that is not linear, and the chart identifications of $\omega_f=f^!\Lambda_Y$
with $\Lambda_X(d)[2d]$ have no evident reason to agree on overlaps. We
therefore construct the isomorphism without charts, from the diagonal,
in the way a tubular neighbourhood linearizes a submanifold. By the
projection formula $f^!K\simeq f^*K\otimes^{\mathbf L}\omega_f$
(the map (10.9)), so it is enough to identify $\omega_f$. The diagonal of $X$ over $Y$ is a section
of the smooth projection $p_1:X\times_YX\to X$, and base change gives
$\omega_f\simeq\Delta^*\omega_{p_1}$. The deformation to the normal
bundle is a family over $\mathbf A^1$ that is $(X\times_YX,\Delta)$ at
$t=1$ and the relative tangent bundle with its zero section at $t=0$. Along the deformed section the dualizing complex is, up to the
shift $[2d]$, a locally constant sheaf of rank one over $\mathbf A^1_X$,
and coordinates show that it is pulled back from the base locally. Two
comparisons of such sheaves that agree at $t=1$ agree everywhere,
because the geometric fibres of $\mathbf A^1$ are connected, so the
local comparisons glue. Restricting to $t=0$ we obtain a canonical
isomorphism with the dualizing complex of $T_{X/Y}$ along its zero
section (Lemma [sk-thm-dnc]). There the vector bundle case
applies, and the result is the orientation
$\omega_f\simeq\Lambda_X(d)[2d]$ of Proposition [sk-prop-sp-orientation].
It remains to check that on a chart it is the identification given by
coordinates, which again reduces to vector bundles. This gives smooth
purity with finite coefficients (Proposition [sk-thm-smooth-purity]).

The passage to $\mathcal O_E$ is not a formality. A family of
isomorphisms at the levels $\mathcal O_E/\ell^n$ that are compatible
only up to isomorphism is not a morphism of any category, so it has no
derived limit. We repeat the construction for towers, where the
compatibilities become single morphisms (Section [sec-sp-grp-ladic-summary]), and
then invert $\ell$ and pass to finite extensions (Theorem [sk-thm-sp-qbar]).
In each case we construct an explicit right adjoint of $Rf_!$ and
compare it with $f^!$ by the uniqueness of adjoints
(Proposition [sk-prop-sp-unique-adjoint]). The statement is
Deligne's (SGA4, XVIII), where it is called Poincaré duality.

The uses of smooth purity named in the opening of Part “Duality and the trace formula”
go through Corollary [sk-cor-sp-all-coefficients], which gives
$a^!\Lambda\simeq\Lambda_X(d)[2d]$ for smooth $X$ of pure dimension $d$,
and through the trace map of Definition [sk-def-sp-trace]; they are
Poincaré duality (Theorem [sk-thm-sf-identification]) and the trace
isomorphism in top degree (Theorem [sk-cor-trace]). Smooth purity
on strata also enters the proofs of Lemma [sk-lem-pd-generic-restriction],
used for biduality, and of the Künneth formula for $f^!$
(Proposition [sk-prop-tf-exceptional-external-kunneth]). The compatibility of
$\gamma_f$ and of the trace map with Frobenius is
Proposition [sk-prop-prop-sp-frobenius-purity] in Section [sec-frobenius].
