+++
kind = "proof"
of = "sk-cor-curve-invariance"
uses = ["sk-thm-curve-package", "sk-prop-sf-comparison", "sk-lem-curve-dense-open"]
+++
By the classical
comparison we may compute on the étale site. Choose compatible
algebraic closures $\bar k\subseteq\bar k'$. Since $\bar k/k$ and
$\bar k'/k'$ are purely inseparable, $C_{\bar k}\to C$ and
$C_{\bar k'}\to C_{k'}$ are universal homeomorphisms, so they induce
equivalences of small étale topoi [Stacks, Tag 03SI](https://stacks.math.columbia.edu/tag/03SI). This reduces the
claim to the pullback from $C_{\bar k}$ to $C_{\bar k'}$, which is an
isomorphism by $(C_7)$ of Theorem [sk-thm-curve-package]. All these maps are
pullback maps, so the comparison square commutes [Stacks, Tag 0A5E](https://stacks.math.columbia.edu/tag/0A5E).
