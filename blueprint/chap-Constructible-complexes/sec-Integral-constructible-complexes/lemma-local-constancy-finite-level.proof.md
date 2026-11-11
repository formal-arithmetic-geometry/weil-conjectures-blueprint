+++
kind = "proof"
of = "lemma-local-constancy-finite-level"
order = 239
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "definition-constructible-sheaves"]
+++
We first show that a model of a stalk spreads out to a neighbourhood, and
then use connectedness to see that the model is the same everywhere.

Every stalk $L_{\bar t}$ has finite Tor amplitude and finite cohomology,
hence is perfect over the local ring $A$, that is, represented by a
bounded complex $M_{\bar t}$ of finite free $A$-modules. An isomorphism
$M_{\bar t}\simeq L_{\bar t}$ is then a section at $\bar t$ of the zeroth
cohomology sheaf of $R\cHom(\underline{M_{\bar t}},L)$; here the stalks of this
sheaf are computed stalkwise, since $\underline{M_{\bar t}}$ is a bounded
complex of finite free modules. We extend the section to an étale
neighbourhood of $\bar t$ and lift it there to a morphism
$\underline{M_{\bar t}}\to L$. Its cone has bounded locally constant finite
cohomology and zero stalk at $\bar t$. Hence its finitely many cohomology
sheaves vanish after shrinking the neighbourhood, and $L$ is isomorphic to
$\underline{M_{\bar t}}$ there. In particular, the stalks of $L$
at all geometric points over the image of this neighbourhood are
isomorphic to $M_{\bar t}$ in $D(A)$.

For each isomorphism class $c$ in $D(A)$, let $S_c\subset S$ be the set of
points at whose geometric points the stalk of $L$ lies in $c$. By the
previous paragraph and openness of étale morphisms, each $S_c$ is open.
Moreover, the sets $S_c$ are disjoint and cover $S$. Since $S$ is connected, $S=S_c$
for the class $c$ of $M$. Thus every point has an étale neighbourhood
on which $L\simeq\underline M$; compare [Stacks, [09BI](https://stacks.math.columbia.edu/tag/09BI)].
