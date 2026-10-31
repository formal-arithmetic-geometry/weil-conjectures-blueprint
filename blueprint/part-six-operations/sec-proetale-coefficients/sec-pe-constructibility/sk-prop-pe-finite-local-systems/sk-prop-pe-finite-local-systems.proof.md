+++
kind = "proof"
of = "sk-prop-pe-finite-local-systems"
uses = ["sk-lem-pe-torsor-comparison"]
+++
We decompose $X$ into the open pieces on which the constant model has a
fixed isomorphism type, and we fix a finitely presented module $M$. By
finite presentation, the automorphism sheaf of $\underline M$ is the
constant discrete group $\operatorname{Aut}_\Lambda(M)$. Hence
$\mathit{Isom}(\underline M,F)$ is a torsor under this classical
group, and by Lemma [sk-lem-pe-torsor-comparison] it has sections étale
locally. Since $F$ is obtained from this torsor by twisting
$\underline M$, it is the pullback of the corresponding twist of the
constant étale sheaf, and so it is classical. This is the descent
argument of [Stacks, Tag 099Y](https://stacks.math.columbia.edu/tag/099Y).
