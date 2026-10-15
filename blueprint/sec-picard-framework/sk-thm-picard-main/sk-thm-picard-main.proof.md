+++
kind  = "proof"
of    = "sk-thm-picard-main"
uses = ["sk-thm-picard-criterion", "sk-prop-picard-pic-split", "sk-thm-picard-f-representable", "sk-lem-picard-f-open", "sk-thm-picard-twist", "sk-thm-picard-rr", "sk-thm-picard-hilb-curves", "sk-thm-picard-coherence"]
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
