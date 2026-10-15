+++
kind = "proof"
of = "sk-lem-pbc-curve-field-extension"
uses = ["sk-cor-curve-invariance", "sk-thm-pbc-curve-input"]
+++
This is [sk-cor-curve-invariance]. By the classical comparison one may
compute on the étale site. Choose compatible algebraic closures
$\bar k\subseteq\bar k'$; since $\bar k/k$ and $\bar k'/k'$ are purely
inseparable, $C_{\bar k}\to C$ and $C_{\bar k'}\to C_{k'}$ are universal
homeomorphisms and induce equivalences of small étale topoi (Stacks Project,
Tag 03SI). This reduces the claim to the pullback from $C_{\bar k}$ to
$C_{\bar k'}$, which is an isomorphism by $(C_7)$ of [sk-thm-pbc-curve-input].
