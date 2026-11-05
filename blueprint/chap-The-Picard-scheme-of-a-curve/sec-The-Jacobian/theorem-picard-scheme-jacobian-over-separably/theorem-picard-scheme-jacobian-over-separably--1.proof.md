+++
kind = "proof"
of = "theorem-picard-scheme-jacobian-over-separably--1"
order = 1549006
uses = ["lemma-representability-picard-functor", "lemma-rigidification-along-section", "proposition-divisors-degree-g-open-chart", "theorem-hilbert-schemes-points-smooth-curve", "lemma-twisting-h-0-1-h", "lemma-coherent-base-change-invertible-sheaves"]
+++
Representability, with the tensor-product group law, is
[lemma-representability-picard-functor]. Choose $P_0\in C(k)$ and
use [lemma-rigidification-along-section] to work with normalized
invertible sheaves. The subfunctor where the direct image is
invertible in degree zero is an open subscheme of
$\operatorname{Hilb}^g_{C/k}$ by
[proposition-divisors-degree-g-open-chart]. Its translates cover the
Picard scheme by [lemma-twisting-h-0-1-h]. Since the Hilbert scheme
is smooth of dimension $g$, so is every representing scheme.

The unit section of a group scheme over a field is a closed
immersion. The automorphism $(x,y)\mapsto(x,x^{-1}y)$ of the product
identifies the diagonal with a base change of the unit section.
Thus the Picard scheme is separated.

The fibrewise degree is the difference of the Euler characteristics
of an invertible sheaf and the structure sheaf. These are locally
constant in the proper flat family. The degree descends from
invertible sheaves to the fppf Picard functor, and is compatible
with pullback. In Lean these steps are
`AlgebraicGeometry.isLocallyConstant_picardPresheafDegree`,
`AlgebraicGeometry.picardDegree_map` and
`AlgebraicGeometry.isLocallyConstant_picardDegree`.

Apply this degree function to the universal class on $P$. Its
fibres $P^d=\delta^{-1}(d)$ are open and closed, disjoint, and cover
$P$. A class of fibrewise degree $d$ gives a morphism to $P$ whose
image lies in $P^d$, hence factors uniquely through it. The resulting
map from the degree-$d$ presheaf to the functor represented by $P^d$
is locally bijective for the fppf topology. Sheafification gives the
claimed representation and its compatibility with $P^d\hookrightarrow P$.
