+++
id = "sk-i-cartier"
kind = "section"
title = "Characteristic-zero group smoothness"
order = 2489
uses = ["sk-d-geometry", "sk-d-tangent", "sk-i-geometry"]
lean = ["AlgebraicGeometry.isReduced_of_grpObj", "AlgebraicGeometry.smooth_of_grpObj_of_charZero", "AlgebraicGeometry.GrpObj.finrank_lie_eq_topologicalKrullDim", "AlgebraicGeometry.GeneralLinearGroup.finrank_lie_eq_ringKrullDim", "AlgebraicGeometry.GrpObj.lieEquivIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.lieAlgebraEquivIdentityComponent", "AlgebraicGeometry.GrpObj.lieEquiv_mul"]
+++
*Proposition (sketch).*

Every group scheme locally of finite type over a field of
characteristic zero is reduced and smooth over that field; in particular
every finite-type matrix group scheme over $k$ is
smooth and reduced. Thus $\dim\Lie(G)=\dim G$ for every group scheme $G$
of finite type over a field of characteristic zero; for a closed subgroup
scheme $G=V(I)\subseteq\GL_n$ this is the Krull dimension of its
coordinate ring. For a group scheme of finite type over a field, the
identity component is open and has the same Lie algebra as the whole
group; for a matrix group scheme over $k$ (algebraically closed of
characteristic zero) this is also the reduced identity component.
Closed subgroup schemes defined by stabilizer and centralizer equations
are included; no passage to the reduced structure changes their tangent
spaces in this characteristic-zero setting.
The group law on tangent vectors at $1$ is addition: differentiating
multiplication at $(1,1)$ gives $(X,Y)\mapsto X+Y$.

## Proof

*Reduction to an algebraically closed field.* For a field $K$ of
characteristic zero with algebraic closure $\bar K$, the projection
$G_{\bar K}\to G$ is faithfully flat, so $G$ is reduced if $G_{\bar K}$ is,
and smoothness descends along $\operatorname{Spec}\bar K\to
\operatorname{Spec}K$ (Stacks 02VL). Dimensions of $G$ and of $\Lie(G)$ are
unchanged by this base change. So let $K$ be algebraically closed. Its
closed points are then $K$-points, every nonempty closed subset contains
one, and translations are automorphisms permuting them transitively; a
nonzero nilpotent and the (closed, Stacks 01V5) non-smooth locus would both
be seen at a closed point. Hence it suffices that the local ring
$\mathcal O_{G,1}$ is regular (a regular local ring is a domain, by the
clause quoted in [sk-i-geometry]).

*Smoothness of the reduction.* The reduction $G_{\mathrm{red}}$ has the
same $K$-points as $G$. Its multiplication is defined on a product of
reduced schemes, reduced over the perfect field $K$ by [sk-i-geometry], so
multiplication and inversion factor through the reduction by the
vanishing principle there; thus $G_{\mathrm{red}}$ is a reduced group
scheme. Such a group is smooth: it has a dense smooth open locus, which
contains a $K$-point $a$, and translation by $ga^{-1}$ carries $a$ to any
$g\in G(K)$, preserving regularity of the local ring.

*Cartier's step.* Write $\mathcal O=\mathcal O_{G,1}$, $N=\sqrt0$ and
$\mathfrak m$ its maximal ideal, and work in the completion
$\hat{\mathcal O}$, which carries the comultiplication
$\Delta:\hat{\mathcal O}\to\hat{\mathcal O}\hat\otimes\hat{\mathcal O}$ with the
counit identities (for affine $G$ one may use $A=k[G]$ and $\Delta$
directly). Then $N\subseteq\mathfrak m^2$. Indeed, let $b$ be nilpotent
with $b\notin\mathfrak m^2$ and least nilpotence exponent $n\ge2$. The
counit identities give $\Delta(b)=b\otimes1+1\otimes b+w$ with $w$ in
(the closure of) $\mathfrak m\otimes\mathfrak m$. Expanding
$0=\Delta(b)^n$ modulo $\hat{\mathcal O}\hat\otimes\mathfrak m^2$ kills every
term with two factors from $1\otimes b+w$ and leaves
$nb^{n-1}\otimes b+n(b^{n-1}\otimes1)w=0$; passing further to
$\hat{\mathcal O}/(b^{n-1}\mathfrak m)$ in the first coordinate leaves
$n\,\overline{b^{n-1}}\otimes\overline b=0$ with both factors nonzero
(the first by Nakayama). Since $n\ne0$ in characteristic zero, this is a
contradiction. Hence
$\mathfrak m/\mathfrak m^2\simeq(\mathfrak m/N)/(\mathfrak m/N)^2$, so
$G$ and its reduction have the same cotangent space at $1$;
primes contain nilpotents, so they also have the same local dimension.
Smoothness of the reduction therefore makes $\mathcal O_{G,1}$ regular,
and $G$ is reduced and smooth.

*The dimension formula.* Smoothness gives $\dim_kT_1G=\dim\mathcal O_{G,1}$,
translations make all local dimensions at $k$-points equal, and the
global dimension is their maximum; since $T_1G=\Lie(G)$ by
[sk-d-tangent], this is $\dim\Lie(G)=\dim G$. For $G=V(I)$ affine,
$\dim G$ is the Krull dimension of its coordinate ring.

*Identity component and subgroup schemes.* The identity component of a
group scheme of finite type over a field is open (there are finitely
many components by [sk-i-geometry], each closed), and restricting to an
open neighborhood of $1$ changes neither the local ring nor its cotangent
space, whence $\Lie(G^\circ)=\Lie(G)$. For a matrix group scheme over $k$
algebraically closed of characteristic zero, $G$ is reduced, so the open
subscheme $G^\circ$ is the reduced closed subscheme on the connected
component of $1$. Stabilizer and centralizer loci are closed subgroup
schemes, so the reducedness just proved applies to them verbatim: their
defining equations already compute the tangent space, and no passage to
the reduced structure is involved.

*Multiplication.* Algebra-valued points of a product are pairs, and
$(1+\varepsilon X)(1+\varepsilon Y)=1+\varepsilon(X+Y)$ in the dual
numbers of [sk-d-tangent], which is the asserted differential; for a
general group scheme the counit identities
$\Delta(f)\in f\otimes1+1\otimes f-f(1)+\mathfrak m\otimes\mathfrak m$ give
the same computation, as $\varepsilon^2=0$.

Compare Milne, [Algebraic
Groups](https://www.jmilne.org/math/Books/iAG2017.pdf) (2017), Cartier's Theorem 3.23 and Proposition 1.37; the
subgroup-scheme clause is what lets the tangent spaces of stabilizers and
centers be read off from their equations. The clauses quoted rather
than proved are all general geometry rather than group theory: density
(0B8X, 056V) and openness (01V5) of the smooth locus over a
perfect field, with the regularity criterion (00TV), faithfully flat
descent of smoothness (02VL), and
the regular-local-domain theorem of [sk-i-geometry]. Cartier's theorem
itself is proved.
