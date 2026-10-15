+++
kind  = "proof"
of    = "sk-thm-picard-main"
uses = ["sk-thm-picard-criterion", "sk-prop-picard-pic-split", "sk-thm-picard-f-representable", "sk-lem-picard-f-open", "sk-thm-picard-twist", "sk-thm-picard-rr", "sk-thm-picard-hilb-curves", "sk-thm-picard-coherence", "sk-def-av-jacobian", "sk-def-picard-f", "sk-lem-picard-zero-dictionary", "det-picard-main-degree", "det-picard-main-jacobian"]
+++
*Representability.* Choose $P\in C(k)$, so that
$\operatorname{Pic}_{C/k}$ is the functor of rigidified invertible
sheaves ([sk-prop-picard-pic-split]). The preceding construction gives a
representable open subfunctor $F\subset\operatorname{Pic}_{C/k}$
([sk-thm-picard-f-representable], [sk-lem-picard-f-open]). For a fixed
class $M\in\operatorname{Pic}_{C/k}(k)$, $M^{-1}F$ is another
representable open subfunctor. Given a class on a test scheme $T$, apply
[sk-thm-picard-twist] to its fibre over each residue field. The open loci
where the corresponding translated class lies in $F$ cover $T$. These
charts therefore cover $\operatorname{Pic}_{C/k}$. Their intersections
are open in either chart, and their transition isomorphisms satisfy the
cocycle condition by functoriality. Gluing constructs a scheme
representing $\operatorname{Pic}_{C/k}$. This is the representability
criterion [sk-thm-picard-criterion] (Stacks Project, Tag 0B9Q); the
resulting curve theorem is Stacks Project, Tag 0B9Z. The group structure
is the tensor product of rigidified sheaves.

*Degree decomposition, smoothness, separatedness.* Fibrewise Euler
characteristic is locally constant for a proper flat family of line
bundles ([sk-thm-picard-coherence]). Riemann–Roch ([sk-thm-picard-rr]) thus makes degree locally
constant and defines the displayed open-and-closed decomposition. The charts in $H_g$ and their
translates show smoothness and dimension $g$. The unit is a closed
immersion for this locally finite type group scheme over a field;
translating the unit shows that its diagonal is closed, so the scheme is
separated.

*Properness and connectedness of the components.* The universal divisor
defines the Abel map

$$
H_g\longrightarrow\operatorname{Pic}^g_{C/k},
\qquad D\longmapsto\cO_C(D).
$$

On every geometric fibre, Riemann–Roch gives $h^0(\cL)\geq1$ for a
degree-$g$ line bundle, so this map is surjective. Its target is
quasi-compact, hence of finite type because the charts are locally of
finite type. A separated finite type target that is the surjective image
of the proper $H_g$ is proper. The image is also geometrically
irreducible ([sk-thm-picard-hilb-curves]). Translation by
$\cO_C((d-g)P)$ identifies this target with every degree component. In
particular the degree-zero component is smooth, proper, connected and
commutative, hence an abelian variety (Stacks Project, Tag 0BA0). Its $k$-points are the rigidified, i.e. all
(since $\operatorname{Pic}(\Spec k)=0$), invertible sheaves of degree
$0$: $J(C)(k)=\operatorname{Pic}^0(C)$.

*Tangent space and base change.* First-order deformations of the
trivial line bundle have transition functions $1+\epsilon a_{ij}$, whose
cocycles modulo coboundaries give $H^1(C,\cO_C)$. Rigidification removes
scalar automorphisms. This gives the tangent-space assertion. Picard sheafification and its
universal functorial description commute with base change, so the
representing scheme does too. Degree and the zero component have the
same compatibility.

*The complement over a separably closed field.* Let now $k$ be separably
closed and $C$ proper, smooth of relative dimension $1$ and geometrically
integral over $k$. Since a scheme which is proper over a field and of
dimension $1$ is projective over it, $C$ is a smooth projective curve, so
the results of this chapter for smooth projective curves apply to it; as $C$
is smooth over the separably closed field $k$, it has a $k$-point $P$.

By [det-picard-main-degree] the subfunctor $\Pic^0_{C/k}$ is
represented by the open and closed subgroup scheme
$\underline{\Pic}^0_{C/k}$. A representing object is unique up to unique
isomorphism, so a Jacobian in the sense of [sk-def-av-jacobian] exists
exactly when $\underline{\Pic}^0_{C/k}$ is an abelian variety of dimension
$g$, and then it is $\underline{\Pic}^0_{C/k}$ with its representing
isomorphism. By [det-picard-main-degree],
$\underline{\Pic}^0_{C/k}$ is isomorphic to $\underline{\Pic}^g_{C/k}$
(translation by $\cO_C(gP)$), so it suffices to prove the geometric
properties for $\underline{\Pic}^g_{C/k}$.

*Smooth of dimension $g$.* The subfunctor $F$ of [sk-def-picard-f] is open
([sk-lem-picard-f-open]), represented by an open
$W\subseteq\underline{\Hilb}^g_{C/k}$ ([sk-thm-picard-f-representable]), and
its classes have degree $g$ ([sk-lem-picard-zero-dictionary]); so $W$ is an
open subscheme $U\subseteq\underline{\Pic}^g_{C/k}$, smooth of dimension $g$
because $\underline{\Hilb}^g_{C/k}$ is ([sk-thm-picard-hilb-curves]). The
translates of $U$ by $k$-points cover $\underline{\Pic}^g_{C/k}$: for a point
$t$ with residue field $K$, [sk-thm-picard-twist] gives $\cL_0$ on $C$ with
$\cL_0|_{C_K}\otimes\cL_t\in F(K)$, necessarily of degree $0$, so
$t\in\cL_0^{-1}\cdot U$. Hence $\underline{\Pic}^g_{C/k}$ is smooth of pure
dimension $g$; the tangent space is [det-picard-main-jacobian].

*Proper.* The universal divisor $D_g$ of [sk-thm-picard-hilb-curves],
normalized along $P$, defines
$\alpha:\underline{\Hilb}^g_{C/k}\to\underline{\Pic}^g_{C/k}$,
$D\mapsto\cO_C(D)$. It is surjective: over an algebraically closed field
$K$, a class $\cL$ of degree $g$ has $h^0(\cL)\ge\chi(\cL)=1$ by
[sk-thm-picard-rr], so $\cL\cong\cO_{C_K}(D)$ for the zero divisor $D$ of a
nonzero section, a $K$-point of $\underline{\Hilb}^g_{C/k}$ (complements of
[sk-thm-picard-hilb-curves]). So $\underline{\Pic}^g_{C/k}$ is
quasi-compact, hence of finite type; it is separated, being a group scheme
over a field whose unit section is a closed immersion; and as the surjective
image of the proper $\underline{\Hilb}^g_{C/k}$ it is proper (Stacks, Tag
03GN).

*Connected and commutative.* $\underline{\Hilb}^g_{C/k}$ is an irreducible
variety ([sk-thm-picard-hilb-curves]), so its image
$\underline{\Pic}^g_{C/k}$ under $\alpha$ is irreducible. The group law is
the tensor product of invertible modules (Yoneda), which is commutative.

*Points and base change.* By [sk-prop-picard-pic-split] with $T=\Spec k$ and
$\Pic(\Spec k)=0$, $\underline{\Pic}_{C/k}(k)=\Pic(C)$, and $J(C)(k)$ is its
degree-zero part, the degree being $\chi(\cL)-\chi(\cO_C)$, which equals the
divisor degree by [sk-thm-picard-rr]. The Picard functor, its normalization
along $P$ and the degree commute with base change along $k\to k'$, so
$\underline{\Pic}_{C/k}\times_kk'$ represents $\Pic_{C_{k'}/k'}$ and its
degree-zero part is $J(C_{k'})$. (Classical: Mumford and Milne, *Abelian
Varieties*; Stacks, Tag 0BA0; the detailed blueprint node is
`thm-sc-jacobian-representability`.)
