+++
kind = "proof"
of = "det-constructible-compactness-devissage"
+++
*Triangulated.* Closure under shifts is built in. For a triangle $C'\to C\to C''\to C'[1]$ with $C'$,
$C''$ in the subcategory, the contravariant long exact sequences of $\Hom(-,K_\lambda)$, summed over
$\lambda$ (sums of abelian groups are exact), map to that of $\Hom(-,\bigoplus K_\lambda)$; the five
lemma gives the claim for $C$.

*Thick.* If $C=C_1\oplus C_2$, the comparison map for $C$ is the direct sum of those for $C_1$ and $C_2$,
so if it is an isomorphism, so are its summands (Stacks, Tag 09QH).

*Constructible sheaves.* They belong to the subcategory by [det-constructible-compactness-sheaf].

*Bounded constructible complexes.* $C\in\Dbc(X,\Lambda)$ has finitely many nonzero cohomology sheaves,
all constructible; the truncation triangles $\tau_{\leq n-1}C\to\tau_{\leq n}C\to H^n(C)[-n]\to$
exhibit $C$ as a finite extension of shifts of these, so $C$ lies in the subcategory.

*Compactness.* Coproducts in $\Loc(\Dbc(X,\Lambda))$ are those of $\D(X_{\mathrm{proét}},\Lambda)$
([sk-def-localizing-closure]), and $\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$
([sk-cor-ambient-ind-derived]). So for $C\in\Dbc(X,\Lambda)$, $\Hom(C,-)$ commutes with arbitrary
coproducts in $\Loc(\Dbc(X,\Lambda))$, i.e. $C$ is compact there.
