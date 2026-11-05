+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek"
order = 517
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "proposition-proper-base-change-degree-zero", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-nagata-s-compactification-theorem", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
For composition, the only new ingredient is a map that moves an
extension by zero past a proper direct image. It is an isomorphism by
the same argument as for refinements: it restricts to the identity on
an open, and both sides vanish on the closed complement by proper base
change. For base change of $Rf_!$ we combine proper base change with the
elementary fact that extension by zero commutes with pullback.

*The composition isomorphism.* Choose compactifications $f=p\circ j$
and $g=q\circ j_Y$, with $j:X\to\overline X$ and $j_Y:Y\to\overline Y$ open and
$p,q$ proper. In the composite $Rq_*j_{Y!}Rp_*j_!$, the middle factor $j_{Y!}Rp_*$
applies a proper direct image before an extension by zero, and we
want to interchange the two.
To do this, compactify the morphism $j_Y\circ p:\overline X\to\overline Y$ as
$\overline X\xrightarrow{j'}W\xrightarrow{r}\overline Y$, with $j'$ open,
$r$ proper and $\overline X$ dense in $W$. Then $r^{-1}(Y)=\overline X$,
because the open immersion $\overline X\to r^{-1}(Y)$ is a morphism from a proper
$Y$-scheme to a separated $Y$-scheme, hence proper, and its image is
closed, open and dense.

The interchange map is defined as follows. For $M$ in $D(\overline X_{\mathrm{pro}\acute{e}t},\Lambda)$, restriction to the open
$Y\subset\overline Y$ identifies $j_Y^*Rr_*j'_!M$ with $Rp_*M$, because
$r^{-1}(Y)=\overline X$, the restriction of $r$ over $Y$ is $p$, and
$j'_!M$ restricts to $M$ on $\overline X$. By the adjunction $j_{Y!}\dashv j_Y^*$, we obtain a map

$$
\iota_M:j_{Y!}Rp_*M\longrightarrow Rr_*j'_!M,
\tag{5.9}
$$

which is the unique map restricting to the identity of $Rp_*M$ over $Y$.

For $M\in D^b_{\mathrm{ctf}}(\overline X,\Lambda)$, this map is an isomorphism. Indeed, over $Y$ it is the identity, and over $\overline Y\setminus Y$ both sides vanish.
For the right-hand side, the vanishing follows from proper base change on $D^b_{\mathrm{ctf}}$
(Proposition [proposition-proper-base-change-localizing-categories]) for the inclusion
of $\overline Y\setminus Y$ into $\overline Y$, since $j'_!M$ vanishes on
$r^{-1}(\overline Y\setminus Y)=W\setminus\overline X$. Both sides preserve
direct sums on $\Loc(D^b_{\mathrm{ctf}}(\overline X,\Lambda))$
(Proposition [proposition-proper-direct-image-extension-zero]). Hence
Lemma [lemma-checking-isomorphisms-constructible-complexes] shows that
$\iota_M$ is an isomorphism for all
$M\in\Loc(D^b_{\mathrm{ctf}}(\overline X,\Lambda))$. For $M=j_!K$ it gives

$$
Rq_*j_{Y!}Rp_*j_!K\simeq Rq_*Rr_*j'_!j_!K=R(qr)_*(j'j)_!K,
$$

and the right side is $R(gf)_!K$ computed with the compactification
$gf=(qr)\circ(j'j)$.

*Verification of canonicity and associativity.* Every map used is characterized by
its restriction to an open subscheme, since the refinement maps
(5.7) and the maps
$\iota_M$ restrict to identities. For example,
replacing any of the chosen compactifications by a refinement commutes with
$\iota_M$, because both composites restrict to
the same identity and are then equal by adjunction. For associativity, given three composable morphisms, we choose common refinements (by graph closure) of the finitely
many compactifications that occur in the composites of two of them. On these, each of the two bracketings is built from composites of proper direct images,
composites of extensions by zero, and maps of the form
$\iota_M$. The first two kinds of pieces are associative: the isomorphisms $Rq_*Rr_*\simeq R(qr)_*$ are associative because they are the
isomorphisms of derived functors of composites of left exact functors
(equivalently, they are adjoint to the composition isomorphisms of the
inverse images), and composition of extensions by zero is associative by
adjunction. Moreover, interchanging two adjacent open and proper steps in either order gives the same map by the uniqueness of
$\iota_M$. So the two bracketings agree.
Similarly, the unit conditions are the special case where one compactification is the identity.
Finally, transitivity of the refinement maps carries these equalities over to
the originally chosen compactifications.

*Base change.* The base change map for $Rf_!=Rp_*j_!$ is built
from one for each factor, so we treat $j_!$ and $Rp_*$ separately. Since open immersions and proper
morphisms are stable under base change, we may pull back a compactification
$f=p\circ j$ along $v$ to a compactification $f'=p'\circ j'$, where now
$j'$ and $p'$ denote the base changes of $j$ and $p$. For $j_!$, extension by zero commutes with inverse image, as shown before the proposition. Combining this with proper base change
on $\Loc(D^b_{\mathrm{ctf}}(\overline X,\Lambda))$
(Proposition [proposition-proper-base-change-localizing-categories]),
we obtain the isomorphism $v^*Rp_*j_!\simeq Rp'_*v'^*j_!\simeq Rp'_*j'_!u^*$
on $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$. This isomorphism is
compatible with change of compactification because the refinement maps are
characterized by their restriction to the open subscheme.
It is also compatible with composing two cartesian squares, because both factors are. For the first factor, a map between extensions by zero from an
open is determined by its restriction to that open, since
$\Hom(j_!B,j_!B')=\Hom(B,B')$. For the second, a base change map is the adjoint transpose of a counit, and the counit of a composite adjunction
is the composite of the counits. Finally, compatibility with the composition isomorphisms of (1) follows in the same way as canonicity: both composites
are built from refinement maps, maps
$\iota_M$ and proper base change maps, and
they agree because their restrictions to the open part are the same
identity.
