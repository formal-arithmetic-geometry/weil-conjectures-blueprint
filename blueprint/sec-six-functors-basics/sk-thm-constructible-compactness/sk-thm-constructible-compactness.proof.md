+++
kind = "proof"
of = "sk-thm-constructible-compactness"
uses = ["sk-cor-ind-heart-ii", "sk-lem-finite-window", "sk-cor-ambient-ind-derived"]
+++
The first assertion follows from the second, since $\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$
([sk-cor-ambient-ind-derived]) and direct sums in $\Loc(\Dbc(X,\Lambda))$ are those of
$\D(X_{\mathrm{proét}},\Lambda)$.

Let first $C\in\Cons(X,\Lambda)$, and suppose that all $K_\lambda$ have cohomology in a fixed interval
$[a,b]$. We prove the claim, for all shifts of the $K_\lambda$ at once, by induction on $b-a$. If $a=b$,
then $K_\lambda=B_\lambda[-a]$ with $B_\lambda\in\IndCons(X,\Lambda)$, and the claim is that $\Ext^q(C,-)$
commutes with direct sums of objects of $\IndCons(X,\Lambda)$, which is [sk-cor-ind-heart-ii]. In
general, the triangles $\tau_{\leq b-1}K_\lambda\to K_\lambda\to H^b(K_\lambda)[-b]\to$ are compatible
with direct sums, because $H^n$ commutes with direct sums. The long exact Hom sequences, exactness of
direct sums of abelian groups and the five lemma give the induction step
([det-constructible-compactness-bounded]).

For arbitrary $K_\lambda$ apply [sk-lem-finite-window] with $m=0$. It replaces each $K_\lambda$, and
$\bigoplus_\lambda K_\lambda$, by its truncation to degrees $[-d_C,0]$; the interval is the same for the
whole family, and truncation commutes with direct sums. The bounded case therefore applies
([det-constructible-compactness-sheaf]).

Finally, for fixed $(K_\lambda)$ the objects $C$ for which the map is an isomorphism are closed under
shifts and cones (five lemma) and under direct summands (Stacks, Tag 09QH). A bounded constructible
complex is a finite extension of shifts of its constructible cohomology sheaves, so it is among them
([det-constructible-compactness-devissage]).
