+++
kind = "proof"
of = "lemma-restriction-normal-subgroup--1"
order = 1121002
uses = []
+++
Finite dimensionality implies that every nonzero $N$-submodule of $V$
contains a simple $N$-submodule: choose a nonzero submodule of least
dimension. Let $T$ be the sum of all simple $N$-submodules of $V$.

For $g\in\Gamma$, normality of $N$ makes $A\mapsto gA$ an order
automorphism of the lattice of $N$-submodules, with inverse
$A\mapsto g^{-1}A$. Indeed, $n(ga)=g((g^{-1}ng)a)$ for $n\in N$.
This automorphism permutes the simple $N$-submodules, so $T$ is
$\Gamma$-stable.

Since $V$ is semisimple as a $\Gamma$-module, $T$ has a
$\Gamma$-stable complement $C$. If $C$ were nonzero, it would contain
a simple $N$-submodule $A$. Then $A\subseteq T$ by the definition of
$T$, contradicting $T\cap C=0$. Hence $C=0$ and $T=V$.

Identify the lattice of $N$-submodules with the lattice of
$k[N]$-submodules of $V$. The sum of its simple submodules is all of
$V$, so the criterion that a module which is a sum of simple submodules
is semisimple gives a complement to every $N$-submodule. Thus the
restriction to $N$ is semisimple.
