+++
id = "lem-ag-connected-group-central-radical"
kind = "lemma"
title = "A connected group with a faithful semisimple module has central Lie radical"
order = 2639
uses = ["def-wf-algebraic-components", "def-wf-algebraic-representations", "def-wf-lie-algebra-derivation", "def-wf-lie-radical-centre", "def-wf-semisimple-module", "def-wf-simple-module", "lem-wf-solvable-common-eigenvector", "lem-wf-solvable-radical-characteristic"]
+++
Let $H\subseteq\operatorname{GL}(V)$ be a connected closed matrix group
over $\overline{\mathbf Q}_\ell$ (connected in the sense of
[def-wf-algebraic-components]) such that $V$ is a semisimple
$H$-module in the sense of [def-wf-semisimple-module] (it is faithful,
since $H\subseteq\operatorname{GL}(V)$). Then the Lie algebra
$\mathfrak h=\operatorname{Lie}(H)$ of [def-wf-lie-algebra-derivation]
has central radical:

$$
\operatorname{rad}(\mathfrak h)=\mathfrak z(\mathfrak h).
$$

## Proof

Put $\mathfrak h=\operatorname{Lie}(H)$ and
$\mathfrak r=\operatorname{rad}(\mathfrak h)$, as in
[def-wf-lie-radical-centre]. The radical is characteristic by
[lem-wf-solvable-radical-characteristic], so
$\operatorname{Ad}(H)$ preserves it. Write
$V=\bigoplus_iM_i$ as in [def-wf-semisimple-module], with each
$M_i$ simple in the sense of [def-wf-simple-module]. For one
$M=M_i$, define explicitly

$$
M_\lambda:=\{v\in M:Xv=\lambda(X)v\text{ for every }X\in\mathfrak r\}.
$$

[lem-wf-solvable-common-eigenvector] gives a nonzero such space.
There are only finitely many possible $\lambda$'s: for a basis
$X_1,\ldots,X_d$ of $\mathfrak r$, each $\lambda(X_i)$ is an
eigenvalue of the fixed matrix $X_i|_M$. For $g\in H$,

$$
gM_\lambda=M_{\lambda\circ\operatorname{Ad}(g^{-1})}.
$$

For fixed nonzero $M_\lambda$ and a possible $\mu$, the condition
$gM_\lambda\subseteq M_\mu$ is a finite collection of linear equations
in the entries of $g$, hence is closed. These finitely many closed
sets are pairwise disjoint and cover $H$; each is therefore also open.
Connectedness of $H$ forces the set containing the identity to be all
of $H$. Thus $M_\lambda$ is $H$-stable, and simplicity gives
$M_\lambda=M$. Consequently $\mathfrak r$ acts by scalars on every
$M_i$. The commutator $[\mathfrak h,\mathfrak r]$ therefore acts as
zero on the faithful space $V$, so it is zero in $\mathfrak h$.
Thus $\mathfrak r\subseteq\mathfrak z(\mathfrak h)$; conversely the
centre is an abelian (hence solvable) ideal, so
$\mathfrak z(\mathfrak h)\subseteq\mathfrak r$.
