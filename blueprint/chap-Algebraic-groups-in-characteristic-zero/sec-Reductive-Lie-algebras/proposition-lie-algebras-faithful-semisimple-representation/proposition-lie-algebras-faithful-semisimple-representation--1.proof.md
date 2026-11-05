+++
kind = "proof"
of = "proposition-lie-algebras-faithful-semisimple-representation--1"
order = 1740003
uses = ["lemma-lie-s-theorem"]
+++
Put $\mathfrak r=\operatorname{rad}\mathfrak l$. First let $N$ be a
simple $\mathfrak l$-submodule of $M$. The triangularizability
condition passes to $N$ and to the action of $\mathfrak r$. By Lemma
[lemma-lie-s-theorem], there is a nonzero common eigenspace $N_\lambda$
for $\mathfrak r$. The weight-space stability argument
(`LieModule.weightSpaceOfIsLieTower`) makes $N_\lambda$ a
$\mathfrak l$-submodule. Simplicity gives $N_\lambda=N$, so every
$y\in\mathfrak r$ acts on $N$ by the scalar $\lambda(y)$. Thus
$[x,y]$ acts as zero on $N$ for all $x\in\mathfrak l$ and
$y\in\mathfrak r$. This is
`LieModule.toEnd_lie_eq_zero_of_mem_radical`; it does not require $N$
to be faithful.

The complemented lattice of submodules of $M$ is of finite length,
so its atoms, the simple submodules, span $M$. The kernel of the
endomorphism induced by $[x,y]$ contains every such submodule, hence
all of $M$. Faithfulness now gives $[x,y]=0$. Consequently
$\mathfrak r\subseteq Z(\mathfrak l)$, and the reverse inclusion
holds because the center is an abelian ideal.
