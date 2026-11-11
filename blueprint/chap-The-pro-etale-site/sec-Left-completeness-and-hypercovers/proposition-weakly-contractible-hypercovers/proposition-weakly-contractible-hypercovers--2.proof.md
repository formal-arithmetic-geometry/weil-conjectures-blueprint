+++
kind = "proof"
of = "proposition-weakly-contractible-hypercovers--2"
order = 103004
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--8", "proposition-pro-etale-coverings--2", "definition-w-local-w-strictly-local--4", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1"]
+++
Use the hypercover constructed in clause [proposition-weakly-contractible-hypercovers--1].

For a sheaf $M$, the hypercover spectral sequence has
$E_1^{r,s}=H^s(W_r,M)$, and the rows with $s>0$ vanish by
Corollary [corollary-evaluation-weakly-contractible-objects](1). The remaining row is the
cosimplicial complex of sections. For bounded-below $K^\bullet$, choose
a bounded-below injective resolution $K^\bullet\to I^\bullet$. Since
evaluation on $W_r$ is exact, $K^\bullet(W_r)\to I^\bullet(W_r)$ is a
quasi-isomorphism. After a shift, both double complexes lie in the
first quadrant, so their total complexes are quasi-isomorphic, and
hypercover descent for $I^\bullet$ identifies the second with
$R\Gamma(U,K)$. See [Stacks, [09A2](https://stacks.math.columbia.edu/tag/09A2)].

*Source:* the proof of Proposition [proposition-weakly-contractible-hypercovers].
