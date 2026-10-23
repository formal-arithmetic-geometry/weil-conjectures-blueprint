+++
kind = "proof"
of = "sk-lem-pbc-curve-field-extension"
uses = ["sk-cor-curve-invariance", "sk-prop-sf-comparison", "sk-thm-pbc-curve-input", "sk-thm-pe-classical-sheaves", "sk-thm-pe-direct-image-comparison"]
+++
This is [sk-cor-curve-invariance]. By the classical comparison we may compute
on the étale site: $F=\nu^*G$ for an étale torsion sheaf $G$
[sk-thm-pe-classical-sheaves], its restriction to $C_{k'}$ is $\nu^*$ of the
restriction of $G$ [sk-thm-pe-direct-image-comparison], and pro-étale
cohomology of $\nu^*G$ is étale cohomology of $G$ [sk-prop-sf-comparison]. Choose compatible
algebraic closures $\bar k\subseteq\bar k'$. Since $\bar k/k$ and
$\bar k'/k'$ are purely inseparable, $C_{\bar k}\to C$ and
$C_{\bar k'}\to C_{k'}$ are universal homeomorphisms, so they induce
equivalences of small étale topoi (Stacks, Tag 03SI). This reduces the claim
to the pullback from $C_{\bar k}$ to $C_{\bar k'}$, which is an isomorphism by
$(C_7)$ of [sk-thm-pbc-curve-input].
