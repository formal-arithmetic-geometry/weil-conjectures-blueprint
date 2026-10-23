+++
kind = "proof"
of = "sk-prop-pe-finite-local-systems"
uses = ["sk-lem-pe-torsor-comparison"]
+++
Decompose $X$ into the open pieces on which the constant model has a fixed
isomorphism type, and fix a finitely
presented module $M$. By finite presentation, the automorphism sheaf of
$\underline M$ is the constant discrete group $\operatorname{Aut}_\Lambda(M)$,
so $\mathit{Isom}(\underline M,F)$ is a
torsor under this classical group. By [sk-lem-pe-torsor-comparison] it has
sections étale locally; this is the descent argument of Stacks Project, Tag
099Y, and twisting $\underline M$ by the étale torsor gives the étale model. For a finite model one can also descend
its finite set of sections and transition maps to finitely presented stages,
and the fpqc sheaf condition then descends the gluing.
