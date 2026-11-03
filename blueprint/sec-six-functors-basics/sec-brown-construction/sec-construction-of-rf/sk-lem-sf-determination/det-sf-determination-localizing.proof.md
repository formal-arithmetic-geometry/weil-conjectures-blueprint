+++
kind = "proof"
of = "det-sf-determination-localizing"
uses = ["lem-sf-triangle-two-out-of-three", "lem-sf-generating-class-determination"]
+++
*Shifts.* Since $\eta$ is a natural transformation of exact functors,
$\eta_{K[1]}$ corresponds to $\eta_K[1]$ under the shift isomorphisms
$F_a(K[1])\simeq F_a(K)[1]$, so $K\in\mathcal C_\eta$ if and only if
$K[1]\in\mathcal C_\eta$.

*Cones.* Let $K\to L\to M\to K[1]$ be distinguished with
$K,L\in\mathcal C_\eta$. Applying $F_1$ and $F_2$ gives two distinguished
triangles, and $\eta$ gives a morphism between them (exactness of $\eta$
means the square involving the connecting maps commutes). Two of its three
components are isomorphisms, so the third is, by
[lem-sf-triangle-two-out-of-three] (the five lemma for the long exact
$\operatorname{Hom}(T,-)$-sequences and Yoneda). Hence $M\in\mathcal C_\eta$;
together with shifts, $\mathcal C_\eta$ is a triangulated subcategory.

*Direct sums.* Let $(K_\alpha)$ be a family in $\mathcal C_\eta$ with sum
$K=\bigoplus_\alpha K_\alpha$. Since $F_1$ and $F_2$ preserve direct sums,
the canonical maps $c_a:\bigoplus_\alpha F_a(K_\alpha)\to F_a(K)$ are
isomorphisms, and naturality of $\eta$ with respect to the inclusions
$K_\alpha\to K$ gives $\eta_K\circ c_1=c_2\circ\bigoplus_\alpha\eta_{K_\alpha}$.
The sum of isomorphisms is an isomorphism, so $\eta_K$ is one.

*Summands.* If $K\oplus K'\in\mathcal C_\eta$, then by additivity
$\eta_{K\oplus K'}=\eta_K\oplus\eta_{K'}$, and the inverse composed with the
inclusion and projection of $K$ inverts $\eta_K$
([lem-sf-generating-class-determination]).

*Conclusion.* $\mathcal C_\eta$ is a triangulated subcategory closed under
direct sums containing $\mathcal S$; $\Loc(\mathcal S)$ is the smallest such
subcategory, so $\Loc(\mathcal S)\subset\mathcal C_\eta$. Taking
$\mathcal S=\Dctf(X,\Lambda)$ and $\mathcal T=\Loc(\Dctf(X,\Lambda))$ gives
[sk-lem-sf-determination].
