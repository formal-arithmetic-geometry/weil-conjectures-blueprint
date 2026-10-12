+++
kind  = "proof"
of    = "lem-sfb-derived-monoidal-closed"
uses = ["lem-sfb-grothendieck-k-injective", "sk-def-sfb-derived-categories"]
+++
*Homotopy level.* For complexes $P,Y$ in $\mathcal C$, let $\underline{\Hom}(P,Y)$ be the
complex with $\underline{\Hom}(P,Y)^n=\prod_p\underline{\Hom}(P^p,Y^{p+n})$, with
differential $df=d_Y\circ f-(-1)^nf\circ d_P$; the products exist because $\mathcal C$ is
Grothendieck abelian. Evaluation and currying give a bijection
$\Hom(P\otimes Z,Y)\cong\Hom(Z,\underline{\Hom}(P,Y))$, natural in $Z$ and $Y$ and
compatible with homotopies. So $P\otimes-\dashv\underline{\Hom}(P,-)$ on $K(\mathcal C)$.

*Fixing one variable.* By [lem-sfb-derived-monoidal], $Q(P)\otimes^{\mathrm L}-$ is the
left derived functor of $P\otimes-$.

*Deriving.* By [lem-sfb-grothendieck-k-injective], $\mathcal C$ has K-injective
resolutions, so $\underline{\Hom}(P,-)$ has a right derived functor. The functor
$P\otimes-$ sends quasi-isomorphisms between K-flat complexes to quasi-isomorphisms: the
cone of such a map is acyclic and K-flat, and its tensor product with $P$ is acyclic, as
one sees by replacing $P$ by a K-flat resolution. So the argument for derived
adjunctions in [sk-def-sfb-derived-categories], applied to the adjunction on
$K(\mathcal C)$, gives $Q(P)\otimes^{\mathrm L}-\dashv R\underline{\Hom}(P,-)$.

*Arbitrary objects.* Every $K\in D(\mathcal C)$ is isomorphic to some $Q(P)$. An
isomorphism $Q(P)\cong K$ induces a natural isomorphism
$Q(P)\otimes^{\mathrm L}-\cong K\otimes^{\mathrm L}-$, along which the adjunction
transports. So $K\otimes^{\mathrm L}-$ has a right adjoint. The bifunctoriality of the
internal hom is then produced by the closed structure.
