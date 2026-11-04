+++
kind = "proof"
of = "theorem-compactness-rational-coefficients"
order = 462
uses = ["lemma-uniform-ext-bound", "proposition-ind-constructible-sheaves", "lemma-reduction-finitely-many-degrees"]
+++
The idea is that, by Lemma [lemma-reduction-finitely-many-degrees], maps out of a
constructible sheaf depend only on the cohomology of the target in $d_C+1$
consecutive degrees, uniformly in the family. For targets with cohomology in a
fixed bounded interval the claim follows from the case of
ind-constructible sheaves by induction on the length.

The first assertion follows from the second, since
$\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$
(Corollary [corollary-ambient-ind-derived]) and direct sums in
$\Loc(\Dbc(X,\Lambda))$ are those of $D(X_{\mathrm{pro}\acute{e}t},\Lambda)$.

First let $C\in\Cons(X,\Lambda)$, and suppose that all $K_\lambda$ have
cohomology in a fixed interval $[a,b]$. We prove the claim, for all
shifts of the $K_\lambda$ at once, by induction on $b-a$. If $a=b$, then
$K_\lambda=B_\lambda[-a]$ with $B_\lambda\in\IndCons(X,\Lambda)$, and the
claim is that $\Ext^q(C,-)$ commutes with direct sums of objects of
$\IndCons(X,\Lambda)$, which is Corollary [corollary-ind-heart-b]. In
general, the triangles
$\tau_{\leq b-1}K_\lambda\to K_\lambda\to H^b(K_\lambda)[-b]\to$ are
compatible with direct sums, because $H^n$ commutes with direct sums. We
apply $\Hom(C,-)$ to these triangles and take the direct sum over
$\lambda$; since direct sums of abelian groups are exact, the result is
again a long exact sequence. It maps to the long exact sequence of the
summed triangle. The outer terms are of the form covered by the
induction hypothesis (cohomology in $[a,b-1]$ and in $[b,b]$), and so
the five lemma gives the claim for cohomology in $[a,b]$.

For arbitrary $K_\lambda$, we apply Lemma [lemma-reduction-finitely-many-degrees] with
$m=0$, which allows us to replace each $K_\lambda$, and
$\bigoplus_\lambda K_\lambda$, by its truncation to degrees $[-d_C,0]$.
Since the interval is the same for the whole family and truncation
commutes with direct sums, the bounded case applies.

From constructible sheaves $C$ we pass to complexes by dévissage.
For fixed $(K_\lambda)$, the objects $C$ for which the map is an
isomorphism are closed under shifts. They are closed under cones by the
five lemma, applied to the long exact sequences of $\Hom(-,K_\lambda)$
summed over $\lambda$ and of $\Hom(-,\bigoplus_\lambda K_\lambda)$. A bounded constructible complex is a
finite extension of shifts of its constructible cohomology sheaves, and
hence it belongs to this class.
