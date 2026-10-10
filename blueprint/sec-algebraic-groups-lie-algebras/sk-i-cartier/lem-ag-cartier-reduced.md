+++
id = "lem-ag-cartier-reduced"
kind = "lemma"
title = "Cartier: group schemes in characteristic zero are smooth and reduced"
order = 2492
uses = ["def-wf-lie-algebra-derivation", "lem-wf-affine-nullstellensatz-vanishing", "lem-wf-affine-product-reduced", "lem-wf-same-lie-closed-subgroup"]
lean = ["AlgebraicGeometry.isReduced_of_grpObj", "AlgebraicGeometry.smooth_of_grpObj_of_charZero", "AlgebraicGeometry.GrpObj.finrank_lie_eq_topologicalKrullDim", "AlgebraicGeometry.GeneralLinearGroup.finrank_lie_eq_ringKrullDim", "AlgebraicGeometry.GrpObj.lieEquivIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.lieAlgebraEquivIdentityComponent", "AlgebraicGeometry.GrpObj.lieEquiv_mul"]
+++
Let $K$ be a field of characteristic zero. Every group scheme locally of
finite type over $K$ is reduced and smooth over $K$. Moreover:

1. If $G$ is a group scheme of finite type over $K$, then
   $\dim_K\operatorname{Lie}(G)=\dim G$. In particular, for a closed
   subgroup scheme $G=V(I)\subseteq\operatorname{GL}_n$ cut out by a Hopf
   ideal $I$, $\dim_K\operatorname{Lie}(G)$ is the Krull dimension of
   $K[x_{ij},\det^{-1}]/I$.
2. If $G$ is a group scheme of finite type over any field $K$, the
   inclusion of the open identity component $G^\circ\subseteq G$ induces
   an isomorphism of Lie algebras
   $\operatorname{Lie}(G^\circ)\cong\operatorname{Lie}(G)$. If $K$ is
   algebraically closed of characteristic zero and $G=V(I)$ is a closed
   subgroup scheme of $\operatorname{GL}_n$, the same holds for the
   *reduced* identity component of [def-wf-lie-algebra-derivation]: the
   inclusion induces $\operatorname{Lie}(G^\circ)\cong\operatorname{Lie}(G)$.
3. For any group scheme $G$, the group law on tangent vectors at the
   identity (the points over the dual numbers reducing to $1$) is the
   addition of $\operatorname{Lie}(G)$; equivalently, the differential at
   $(1,1)$ of the multiplication is $(X,Y)\mapsto X+Y$.

In particular, let $\mathcal G\subseteq\operatorname{GL}(V)$ over
$k=\overline{\mathbf Q}_\ell$ be a closed subscheme of finite type, cut
out by a finitely generated, possibly nonradical, ideal, such that the
multiplication and inversion of $\operatorname{GL}(V)$ restrict to it.
Then $\mathcal G$ is smooth and reduced, so
$\mathcal G=\mathcal G_{\mathrm{red}}$ is a (smooth) closed matrix group. In particular, if a closed subgroup (a
stabilizer, a centralizer, or the kernel of a regular homomorphism) is
given by explicit equations, its Lie algebra in the sense of
[def-wf-lie-algebra-derivation] is the space of $X$ such that
$1+\varepsilon X$ satisfies those equations over
$k[\varepsilon]/\varepsilon^2$; no passage to the reduced structure
changes the tangent space.

## Proof

Let $G$ be a group scheme locally of finite type over $K$, with
characteristic $0$.

**Step 1: reduction to $K$ algebraically closed.** Let $\bar K$ be an
algebraic closure and $G_{\bar K}=G\times_K\bar K$, a group scheme locally
of finite type over $\bar K$. The projection $G_{\bar K}\to G$ is faithfully
flat, so on every affine open $\operatorname{Spec}A\subseteq G$ the map
$A\to A\otimes_K\bar K$ is injective; hence $G$ is reduced if $G_{\bar K}$
is. Smoothness descends along the faithfully flat base change
$\operatorname{Spec}\bar K\to\operatorname{Spec}K$
([Stacks 02VL](https://stacks.math.columbia.edu/tag/02VL)). So we may and
do assume that $K$ is algebraically closed until the end of Step 4.

**Step 2: translations.** Since $G$ is locally of finite type over the
algebraically closed field $K$, its closed points are its $K$-points, and
every nonempty closed subset of $G$ contains one. For $g\in G(K)$, left
translation by $g$ is an automorphism of the scheme $G$ carrying $1$ to
$g$, so all local rings $\mathcal O_{G,g}$ at closed points are isomorphic
to $\mathcal O_{G,1}$. A nonzero nilpotent section over an affine open has
nonempty closed support, which contains a closed point, so $G$ is reduced
as soon as all $\mathcal O_{G,g}$ ($g\in G(K)$) are reduced. Likewise the
non-smooth locus is closed
([Stacks 01V5](https://stacks.math.columbia.edu/tag/01V5)), so $G$ is
smooth as soon as it is smooth at every $K$-point; over the perfect field
$K$ this means that every $\mathcal O_{G,g}$ is regular
([Stacks 00TV](https://stacks.math.columbia.edu/tag/00TV)). By
translation, both follow once $\mathcal O_{G,1}$ is regular, since a
regular local ring is a domain
([Stacks 00NP](https://stacks.math.columbia.edu/tag/00NP)).

**Step 3: the reduction $G_{\mathrm{red}}$ is a smooth group scheme.**
The reduced closed subscheme $G_{\mathrm{red}}$ has the same $K$-points as
$G$. Over the perfect field $K$, the product
$G_{\mathrm{red}}\times_KG_{\mathrm{red}}$ is reduced (the affine case is
[lem-wf-affine-product-reduced]), so multiplication and inversion of $G$
restricted to $G_{\mathrm{red}}$ factor through $G_{\mathrm{red}}$
([lem-wf-affine-nullstellensatz-vanishing] on affine opens). Thus
$G_{\mathrm{red}}$ is a reduced group scheme locally of finite type over
$K$. Its smooth locus is open and dense
([Stacks 056V](https://stacks.math.columbia.edu/tag/056V)), hence contains
a $K$-point $a$, and translation by $ga^{-1}$ carries $a$ to any
$g\in G(K)$. So $G_{\mathrm{red}}$ is smooth at every closed point, hence
smooth by Step 2 (for a matrix group this is (2) of
[lem-wf-same-lie-closed-subgroup]).

**Step 4: Cartier's step.** Let $\mathcal O=\mathcal O_{G,1}$ with maximal
ideal $\mathfrak m$ and nilradical $N$, and let $\hat{\mathcal O}$ be its
completion, a complete Noetherian local $K$-algebra with residue field
$K$. The multiplication and the unit of $G$ give a continuous comultiplication
$\Delta:\hat{\mathcal O}\to\hat{\mathcal O}\hat\otimes_K\hat{\mathcal O}$
(the completed local ring of $G\times_KG$ at $(1,1)$) satisfying the counit
identities. We claim $N\subseteq\mathfrak m^2$. Since
$\mathcal O\to\hat{\mathcal O}$ is faithfully flat,
$\mathfrak m^2\hat{\mathcal O}\cap\mathcal O=\mathfrak m^2$, and nilpotents
of $\mathcal O$ stay nilpotent in $\hat{\mathcal O}$, so it suffices to show
that every nilpotent $b\in\hat{\mathcal O}$ lies in
$\hat{\mathfrak m}^2$. Suppose not, and let $n\ge2$ be the least exponent
with $b^n=0$. The counit identities give
$\Delta(b)=b\otimes1+1\otimes b+w$ with $w$ in the closure of
$\hat{\mathfrak m}\otimes\hat{\mathfrak m}$. Modulo
$\hat{\mathcal O}\hat\otimes\hat{\mathfrak m}^2$, i.e. in
$\hat{\mathcal O}\otimes_K(\hat{\mathcal O}/\hat{\mathfrak m}^2)$, the
element $u=1\otimes b+w$ lies in $\hat{\mathcal O}\otimes\hat{\mathfrak m}$,
so expanding $0=\Delta(b^n)=(b\otimes1+u)^n$ kills every term with two
factors $u$ and leaves
$nb^{n-1}\otimes b+n(b^{n-1}\otimes1)w=0$. Passing further to
$\hat{\mathcal O}/(b^{n-1}\hat{\mathfrak m})$ in the first factor kills
the second term and leaves
$n\,\overline{b^{n-1}}\otimes\overline b=0$ in
$\hat{\mathcal O}/(b^{n-1}\hat{\mathfrak m})\otimes_K
\hat{\mathcal O}/\hat{\mathfrak m}^2$. Here
$\overline{b^{n-1}}\ne0$ by Nakayama (as $b^{n-1}\ne0$) and
$\overline b\ne0$ (as $b\notin\hat{\mathfrak m}^2$), so the tensor product
of the two nonzero vectors is nonzero, and $n\ne0$ in characteristic zero:
a contradiction. Hence $N\subseteq\mathfrak m^2$, and
$\mathfrak m/\mathfrak m^2\simeq(\mathfrak m/N)/(\mathfrak m/N)^2$: $G$ and
$G_{\mathrm{red}}$ have the same cotangent space at $1$. Every prime
contains $N$, so $\dim\mathcal O=\dim\mathcal O/N$. Since
$\mathcal O/N=\mathcal O_{G_{\mathrm{red}},1}$ is regular by Step 3,
$\dim_K\mathfrak m/\mathfrak m^2=\dim\mathcal O$, i.e. $\mathcal O$ is
regular. By Step 2, $G$ is reduced and smooth. With Step 1 this proves the
first assertion over every field of characteristic zero.

**Step 5: the dimension formula (1).** Let $G$ be of finite type over
$K$ of characteristic zero. Both $\dim_K\operatorname{Lie}(G)$ and $\dim G$
are unchanged by the base change to $\bar K$
($\operatorname{Lie}(G_{\bar K})=\operatorname{Lie}(G)\otimes_K\bar K$, and
dimension is invariant under field extension), so let $K$ be algebraically
closed. By Step 4, $G$ is smooth, so
$\dim_K\operatorname{Lie}(G)=\dim_K T_1G=\dim\mathcal O_{G,1}$ by
[def-wf-lie-algebra-derivation]. Translations make all
$\dim\mathcal O_{G,g}$ at closed points equal, and $\dim G$ is their
maximum, so $\dim_K\operatorname{Lie}(G)=\dim G$. For $G=V(I)$ affine,
$\dim G$ is the Krull dimension of $K[x_{ij},\det^{-1}]/I$.

**Step 6: the identity component (2).** For $G$ of finite type over any
field, the identity component $G^\circ$ is open in $G$, so
$\mathcal O_{G^\circ,1}=\mathcal O_{G,1}$; the tangent space at $1$, and the
bracket computed from dual-number points near $1$, are unchanged, so the
open immersion $G^\circ\to G$ induces
$\operatorname{Lie}(G^\circ)\cong\operatorname{Lie}(G)$. If $K$ is
algebraically closed of characteristic zero and $G=V(I)\subseteq
\operatorname{GL}_n$, then $G$ is reduced by Step 4, so the open
subscheme $G^\circ$ is reduced, and therefore it equals the reduced closed
subscheme on the connected component of $1$; the previous sentence applies.

**Step 7: multiplication (3).** Points of $G\times G$ with values in the
dual numbers are pairs of such points. For $G\subseteq\operatorname{GL}(V)$,
$(1+\varepsilon X)(1+\varepsilon Y)=1+\varepsilon(X+Y)$ since
$\varepsilon^2=0$, so the group law on tangent vectors is addition and the
differential of multiplication at $(1,1)$ is $(X,Y)\mapsto X+Y$. For a
general $G$, a tangent vector $v$ is the map
$f\mapsto f(1)+\varepsilon\,v(f)$ on functions near $1$, and the product
$v\cdot w$ is $f\mapsto(v\otimes w)(\Delta f)$ followed by the
multiplication of $K[\varepsilon]/\varepsilon^2$. The counit identities give
$\Delta(f)=f\otimes1+1\otimes f-f(1)\,1\otimes1+\sum_i m_i\otimes m_i'$
with $m_i,m_i'\in\mathfrak m$, and $v(m_i)w(m_i')$ carries the factor
$\varepsilon^2=0$, so $(v\cdot w)(f)=f(1)+\varepsilon\,(v(f)+w(f))$.

**Matrix groups and subgroup schemes.** The final paragraph is the case
$K=k=\overline{\mathbf Q}_\ell$ and $G=\mathcal G$: $\mathcal G$ is reduced, so
$\mathcal G=\mathcal G_{\mathrm{red}}$, which is smooth by Step 3.
Stabilizer, centralizer and kernel loci are closed subgroup schemes, so
the reducedness just proved applies to them verbatim: their defining
equations already compute the tangent space, and no passage to the
reduced structure is involved.

Compare Milne, *Algebraic Groups* (2017), Cartier's Theorem 3.23 and
Proposition 1.37.
