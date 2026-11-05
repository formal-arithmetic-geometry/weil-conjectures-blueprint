+++
id = "prose-01-05"
kind = "hidden"
title = "The six operations"
order = 11
+++
Duality has no simple counterpart for functions, and it needs two more
operations: the internal Hom of sheaves and the *exceptional inverse
image* $f^!$, a right adjoint of $Rf_!$. With $f^*$, $Rf_*$, $Rf_!$ and
$\otimes$ these are Grothendieck's *six operations*. Part I
of these notes, roughly their first third, constructs them for all the
coefficient rings we need. To see why $f^!$ is the right tool, consider Poincaré
duality for a smooth variety $X$ of pure dimension $d$ over an
algebraically closed field $k$, with coefficients
$\Lambda=\mathbf Z/\ell^n$. It should say that cup product

$$
H_c^i(X,\Lambda)\times H^{2d-i}(X,\Lambda(d))\longrightarrow
H^{2d}_c(X,\Lambda(d))\longrightarrow\Lambda
$$

is a perfect pairing. Here $\Lambda(d)=\mu_{\ell^n}^{\otimes d}$ is the
*Tate twist* (Definition [definition-tate-twists]). The twist is
needed because Frobenius does not act trivially on top cohomology. For
instance, the map $F:\mathbf P^1\to\mathbf P^1$ has degree $q$. It pulls the
class of a point back to $q$ times itself, so $F$ acts on
$H^2(\mathbf P^1,\Lambda)$ by $q$. With our conventions $F$ acts on
$\Lambda(1)$ by $q^{-1}$ (Section [sec-Coefficient-rings]), and therefore
it acts trivially on $H^2(\mathbf P^1,\Lambda(1))$. In general the twist
$(d)$ removes the factor $q^d$ from the pairing.

For an oriented manifold $V$ of dimension $r$ there is a clean proof, due to
Verdier. Let $a:V\to\mathrm{pt}$ be the map to a point. The functor $Ra_!$,
cohomology with compact supports, has a right adjoint $a^!$, and the
adjunction gives, for every sheaf $G$ on $V$,

$$
R\!\operatorname{Hom}\bigl(R\Gamma_c(V,G),\Lambda\bigr)\simeq R\!\operatorname{Hom}(G,a^!\Lambda).
$$

This isomorphism comes from the adjunction alone and holds for every $V$;
what makes it a duality theorem is a computation of $a^!\Lambda$.
It is a complex of sheaves on $V$, and its restriction to an open subset
$U$ is the corresponding complex for $U$. So it can be computed in a chart
$\mathbf R^r$. There its only cohomology sheaf sits in degree $-r$, with
stalks $\Hom(H^r_c(\mathbf R^r,\Lambda),\Lambda)\simeq\Lambda$. An orientation
identifies these stalks consistently, and this gives
$a^!\Lambda\simeq\Lambda[r]$. For $G=\Lambda$ the displayed isomorphism then
reads $R\!\operatorname{Hom}(R\Gamma_c(V,\Lambda),\Lambda)\simeq R\!\operatorname{Hom}(\Lambda,\Lambda[r])=R\Gamma(V,\Lambda)[r]$.
Taking cohomology in degree $-i$ and using that $\Lambda$ is a field or, for
$\Lambda=\mathbf Z/\ell^n$, a self-injective ring, this says
$\Hom(H^i_c(V,\Lambda),\Lambda)\simeq H^{r-i}(V,\Lambda)$, which is
Poincaré duality for $V$.

We follow the same route. For the structure morphism $a$ of a smooth
variety $X$ of dimension $d$ we show $a^!\Lambda\simeq\Lambda_X(d)[2d]$,
again by a local computation (*smooth purity*). Poincaré duality
follows.

The main theorem of Part I is that $f^!$
exists and carries constructible complexes to constructible complexes
(Theorem [theorem-exceptional-inverse-image]). Existence is a general
fact. Indeed, to give a right adjoint of $Rf_!$ is to find, for each $N$, an object
$f^!N$ with $\Hom(M,f^!N)=\Hom(Rf_!M,N)$, naturally in $M$, and Brown's
representability theorem provides such objects for an exact functor between
triangulated categories that commutes with arbitrary direct sums. It needs
one hypothesis on the source: it must be *compactly generated*, that is,
built by shifts, cones and direct sums from a set of objects $M$ for which
$\Hom(M,-)$ commutes with direct sums. Such objects are called compact; in the
derived category of a ring, for example, the perfect complexes are the
compact objects. Constructible complexes are such objects, but they are not closed
under direct sums. We therefore apply the theorem to the larger category
built from them in this way.

It remains to show that $f^!$ carries constructible complexes to
constructible complexes, and this is geometric. Locally $f$ is a closed
immersion followed by a projection from affine space, and affine space is
open in a product of projective lines, so two cases remain. For the projection
$\mathbf P^1_Y\to Y$, we compute $f^!$ explicitly, whereas for a closed immersion
$i$ with open complement $j$, a distinguished triangle computes $i^!K$ from
$K$ and $Rj_*j^*K$. This case therefore comes down to the theorem of
Deligne that the ordinary direct image $Rj_*$ preserves constructible
complexes.

The six operations must also be available for $\mathbf Z_\ell$- and $\mathbf Q_\ell$-coefficients,
compatibly with reduction modulo $\ell^n$. This is a problem, because inverse limits behave badly on the étale
site: on $\operatorname{Spec}\mathbf F_q$, as we saw in
Section [sec-Weil-cohomology], the constant sheaf $\mathbf Z_\ell$ has $H^1=0$,
although the limit of the groups $H^1(\operatorname{Spec}\mathbf F_q,\mathbf Z/\ell^k)$
is $\mathbf Z_\ell$. For this reason the classical theory works with compatible systems of
sheaves modulo $\ell^n$ and builds the derived categories by
hand [ekedahl90]. We use instead the pro-étale site of Bhatt and Scholze [bhatt-scholze15]. Its
objects over $X$ include, besides the étale maps $U\to X$, inverse limits
$\varprojlim_iU_i\to X$ of affine étale maps, for example the spectrum of an
algebraic closure of $\mathbf F_q$ over $\operatorname{Spec}\mathbf F_q$, and
its coverings are the families that are jointly surjective in a strong sense.
Every étale sheaf defines a sheaf on it, and every bounded below complex of étale
sheaves has the same cohomology on the two sites (Section [chap-The-pro-etale-site]).
The gain is that $\mathbf Z_\ell$, with its topology, becomes a sheaf whose cohomology
is the limit: on the pro-étale site
$H^1(\operatorname{Spec}\mathbf F_q,\mathbf Z_\ell)=\mathbf Z_\ell$
(Example [example-first-cohomology-finite-field]). On it, $\mathbf Z_\ell$ is
a sheaf of rings whose sections are continuous functions to $\mathbf Z_\ell$, so that an
$\ell$-adic sheaf is simply a sheaf of modules over it, and we use the usual
derived category of these modules, with no inverse systems. In this setting all the
geometric arguments are made with coefficients $\mathbf Z/\ell^n$, where the
classical theory applies, and the pro-étale site then carries them over to
$\mathbf Z_\ell$, $\mathbf Q_\ell$ and $\overline{\mathbf Q}_\ell$.
