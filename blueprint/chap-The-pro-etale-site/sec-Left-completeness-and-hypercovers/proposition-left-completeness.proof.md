+++
kind = "proof"
of = "proposition-left-completeness"
order = 98
uses = ["proposition-etale-implications", "lemma-stability", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-exact-products"]
+++
We compute the cohomology sheaves of the derived limit with the Milnor
sequence and find that they are those of $K$.

Represent $K$ by a complex and form its canonical truncation tower,
with maps $K\to\tau_{\geq-n}K$ and
$\tau_{\geq-(n+1)}K\to\tau_{\geq-n}K$. For fixed $q$, the sheaves
$H^q(\tau_{\geq-n}K)$ and $H^{q-1}(\tau_{\geq-n}K)$ are eventually
constant, with identity transition maps, equal to the corresponding
cohomology sheaves of $K$, so the $R^1$ term in
(2.2) vanishes and the limit term is $H^q(K)$. As the natural
map induces this identification in every degree, it is an
isomorphism; see [Stacks, [0947](https://stacks.math.columbia.edu/tag/0947)](2).
