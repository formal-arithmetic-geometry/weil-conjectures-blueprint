+++
kind = "proof"
of = "det-sf-existence-brown"
uses = ["det-sf-comp-coherence-single", "det-sf-comp-coherence-cocycle", "sk-lem-brown-hypotheses"]
+++
*(1)* Fix $N$. The functor $H_N(M)=\Hom(Rf_!M,N)$ on $\mathcal T_X^{\mathrm{op}}$
is cohomological, because $Rf_!$ is exact ([det-sf-comp-coherence-single]) and
$\Hom(-,N)$ is cohomological; and it carries direct sums to products, because
$Rf_!$ preserves direct sums ([det-sf-comp-coherence-single]) and
$\Hom(\bigoplus_\alpha-,N)=\prod_\alpha\Hom(-,N)$. Brown representability for
the compactly generated triangulated category $\mathcal T_X$ (Stacks, Tag
0A8F) gives an object $f^!N$ and a natural isomorphism
$H_N\simeq\Hom(-,f^!N)$, determined by the element
$\varepsilon_N\in\Hom(Rf_!f^!N,N)$ corresponding to $\mathrm{id}_{f^!N}$. For a
morphism $N\to N'$ the Yoneda lemma gives a unique $f^!N\to f^!N'$ compatible
with the representing isomorphisms; this makes $f^!$ a functor and
$\varepsilon$ a natural transformation, the counit of $Rf_!\dashv f^!$.

*(2)* The right adjoint of an exact functor between triangulated categories
is exact (Stacks, Tag 0A8G): it commutes with shifts via the shift
isomorphisms of $Rf_!$ and adjunction, and for a distinguished triangle
$N_1\to N_2\to N_3\to$ one completes $f^!N_1\to f^!N_2$ to a triangle with
third vertex $C$, constructs a map $C\to f^!N_3$ by adjunction, and checks
that it induces isomorphisms on $\Hom(M,-)$ for all $M$ by the five lemma, so
it is an isomorphism.

*(3)* If $G,G'$ are right adjoints of $Rf_!$, then
$\Hom(M,GN)\simeq\Hom(Rf_!M,N)\simeq\Hom(M,G'N)$ naturally in $M$ and $N$, and
the Yoneda lemma gives a unique natural isomorphism $G\simeq G'$ compatible
with these bijections. Two compactifications give isomorphic functors $Rf_!$
([det-sf-comp-coherence-cocycle]), and composing with that isomorphism
transfers one adjunction to the other; uniqueness of right adjoints then
identifies the two $f^!$, compatibly with the cocycle condition.
