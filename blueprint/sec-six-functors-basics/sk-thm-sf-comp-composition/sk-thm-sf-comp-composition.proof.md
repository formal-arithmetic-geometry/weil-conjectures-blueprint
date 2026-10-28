+++
kind = "proof"
of = "sk-thm-sf-comp-composition"
uses = ["sk-prop-proper-base-change-unbounded", "sk-prop-proper-image-localizing", "sk-lem-sf-determination", "sk-prop-sf-comp-coherence"]
+++
*The composition isomorphism.* Choose compactifications $f=p\circ j$ and
$g=q\circ j_Y$, with $j:X\to\overline X$ and $j_Y:Y\to\overline Y$ open and
$p,q$ proper. In the composite $Rq_*j_{Y!}Rp_*j_!$, the middle factor
$j_{Y!}Rp_*$ applies a proper direct image before an extension by zero, and we
want to interchange the two. Compactify the morphism
$j_Y\circ p:\overline X\to\overline Y$ as
$\overline X\xrightarrow{j'}W\xrightarrow{r}\overline Y$, with $j'$ open, $r$
proper and $\overline X$ dense in $W$. Then $r^{-1}(Y)=\overline X$. Indeed,
the open immersion $\overline X\to r^{-1}(Y)$ is a morphism from a proper
$Y$-scheme to a separated $Y$-scheme, hence proper, so that its image is
closed. Since the image is also open and dense, it is everything.

For $M$ in $D(\overline X_{\mathrm{proét}},\Lambda)$, restriction to the open
$Y\subset\overline Y$ identifies $j_Y^*Rr_*j'_!M$ with $Rp_*M$, because
$r^{-1}(Y)=\overline X$. By the adjunction $j_{Y!}\dashv j_Y^*$, we obtain a
map

$$
j_{Y!}Rp_*M\longrightarrow Rr_*j'_!M,
$$

which is the unique map restricting to the identity of $Rp_*M$ over $Y$. For
$M\in\Dctf(\overline X,\Lambda)$, this map is an isomorphism, because over $Y$
it is the identity, and over $\overline Y\setminus Y$ both sides vanish. For
the right-hand side, this follows from proper base change on $\Dctf$
([sk-prop-proper-base-change-unbounded]) for the inclusion of
$\overline Y\setminus Y$ into $\overline Y$, since $j'_!M$ vanishes on
$r^{-1}(\overline Y\setminus Y)=W\setminus\overline X$. Both sides preserve
direct sums on $\Loc(\Dctf(\overline X,\Lambda))$
([sk-prop-proper-image-localizing]), and hence [sk-lem-sf-determination] shows
that this interchange map is an isomorphism for all
$M\in\Loc(\Dctf(\overline X,\Lambda))$. Taking $M=j_!K$, we obtain

$$
Rq_*j_{Y!}Rp_*j_!K\simeq Rq_*Rr_*j'_!j_!K=R(qr)_*(j'j)_!K,
$$

and the right side is $R(gf)_!K$ computed with the compactification
$gf=(qr)\circ(j'j)$.

*Verification of canonicity and associativity.* Every map used is
characterized by its restriction to an open subscheme, since the refinement
maps $e_{h,K}$ of [sk-prop-sf-comp-coherence] and the interchange maps above
restrict to identities. In particular, replacing any of the chosen
compactifications by a refinement commutes with the interchange map, because
both composites restrict to the same identity and are then equal by
adjunction. Now consider three composable morphisms. We choose common
refinements (by graph closure) of the finitely many compactifications that
occur in the composites of two of them. On these, each of the two bracketings
is built from composites of proper direct images, composites of extensions by
zero, and interchange maps. The isomorphisms $Rq_*Rr_*\simeq R(qr)_*$ are
associative because they are the isomorphisms of derived functors of
composites of left exact functors (equivalently, they are adjoint to the
composition isomorphisms of the inverse images), and composition of extensions
by zero is associative by adjunction. Interchanging two adjacent open and
proper steps in either order gives the same map by the uniqueness of the
interchange map. Hence the two bracketings agree, and the unit conditions are
the case where one compactification is the identity. By transitivity of the
refinement maps, these equalities carry over to the originally chosen
compactifications.

*Base change.* Since open immersions and proper morphisms are stable under
base change, we may pull back a compactification $f=p\circ j$ along $v$ to a
compactification $f'=p'\circ j'$, where now $j'$ and $p'$ denote the base
changes of $j$ and $p$. We first show that extension by zero commutes with
inverse image. Let $v':\overline X'\to\overline X$ be the projection. For
$K\in D(X_{\mathrm{proét}},\Lambda)$, the isomorphism
$j'^*v'^*j_!K\simeq u^*j^*j_!K=u^*K$ corresponds by the adjunction
$j'_!\dashv j'^*$ to a map $j'_!u^*K\to v'^*j_!K$. It is the identity on the
open $X'$, and both sides vanish on its closed complement, since
$v'^{-1}(\overline X\setminus X)=\overline X'\setminus X'$. Hence it is an
isomorphism by [Stacks, Tag 09AH](https://stacks.math.columbia.edu/tag/09AH).
Combining this with proper base change on $\Loc(\Dctf(\overline X,\Lambda))$
([sk-prop-proper-base-change-unbounded]), we obtain the isomorphism
$v^*Rp_*j_!\simeq Rp'_*v'^*j_!\simeq Rp'_*j'_!u^*$ on
$\Loc(\Dctf(X,\Lambda))$. This isomorphism is compatible with change of
compactification because the refinement maps are characterized by their
restriction to the open subscheme. Both factors are compatible with composing
two cartesian squares. For the first, a map between extensions by zero from an
open is determined by its restriction to that open, since
$\Hom(j_!B,j_!B')=\Hom(B,B')$. For the second, a base change map is the
adjoint transpose of a counit, and the counit of a composite adjunction is the
composite of the counits. Hence the base change map for $Rf_!$ is compatible
with composing cartesian squares as well.
