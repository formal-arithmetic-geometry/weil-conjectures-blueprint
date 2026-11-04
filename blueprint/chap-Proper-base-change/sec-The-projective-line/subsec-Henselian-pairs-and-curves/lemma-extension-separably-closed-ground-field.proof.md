+++
kind = "proof"
of = "lemma-extension-separably-closed-ground-field"
order = 361
uses = ["theorem-cohomology-curves"]
+++
A purely inseparable extension does not change the étale topos. This
allows us to replace $k$ and $k'$ by their algebraic closures and then
apply $(C_7)$.

By the classical
comparison we may compute on the étale site. Choose compatible
algebraic closures $\bar k\subseteq\bar k'$. Since $\bar k/k$ and
$\bar k'/k'$ are purely inseparable, $C_{\bar k}\to C$ and
$C_{\bar k'}\to C_{k'}$ are universal homeomorphisms. Hence they induce
equivalences of small étale topoi [Stacks, [03SI](https://stacks.math.columbia.edu/tag/03SI)]. This reduces the
claim to the pullback from $C_{\bar k}$ to $C_{\bar k'}$, which is an
isomorphism by $(C_7)$ of Theorem [theorem-cohomology-curves]. All these maps are
pullback maps, so the comparison square commutes [Stacks, [0A5E](https://stacks.math.columbia.edu/tag/0A5E)].
