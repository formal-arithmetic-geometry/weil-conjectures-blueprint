+++
kind = "proof"
of = "sk-thm-constructible-compactness"
uses = ["sk-lem-finite-window", "sk-cor-ambient-ind-derived", "sk-cor-ind-heart-ii"]
+++
The idea is that, by [sk-lem-finite-window], maps out of a constructible sheaf depend only on the
cohomology of the target in $d_C+1$ consecutive degrees, uniformly in the family. For targets with
cohomology in a fixed bounded interval the claim follows from the case of ind-constructible sheaves by
induction on the length.

The first assertion follows from the second, since $\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$
([sk-cor-ambient-ind-derived]) and direct sums in $\Loc(\Dbc(X,\Lambda))$ are those of
$\D(X_{\mathrm{proét}},\Lambda)$.

First let $C\in\Cons(X,\Lambda)$, and suppose that all $K_\lambda$ have cohomology in a fixed interval
$[a,b]$. We prove the claim, for all shifts of the $K_\lambda$ at once, by induction on $b-a$. If $a=b$,
then $K_\lambda=B_\lambda[-a]$ with $B_\lambda\in\IndCons(X,\Lambda)$, and the claim is that $\Ext^q(C,-)$
commutes with direct sums of objects of $\IndCons(X,\Lambda)$, which is [sk-cor-ind-heart-ii]. In
general, the triangles $\tau_{\leq b-1}K_\lambda\to K_\lambda\to H^b(K_\lambda)[-b]\to$ are compatible
with direct sums, because $H^n$ commutes with direct sums. The induction step follows from the long exact
Hom sequences, exactness of direct sums of abelian groups and the five lemma
([det-constructible-compactness-bounded]).

For arbitrary $K_\lambda$, we apply [sk-lem-finite-window] with $m=0$, which allows us to replace each
$K_\lambda$, and $\bigoplus_\lambda K_\lambda$, by its truncation to degrees $[-d_C,0]$. Since the interval
is the same for the whole family and truncation commutes with direct sums, the bounded case applies
([det-constructible-compactness-sheaf]).

Finally, for fixed $(K_\lambda)$, the objects $C$ for which the map is an isomorphism are closed under
shifts and cones (five lemma) and under direct summands
([Stacks, Tag 09QH](https://stacks.math.columbia.edu/tag/09QH)). A bounded constructible complex is a
finite extension of shifts of its constructible cohomology sheaves, and hence it belongs to this class
([det-constructible-compactness-devissage]).
