+++
id = "lem-wf-semisimple-group-lie-algebra"
kind = "lemma"
title = "The Lie algebra of a semisimple matrix group"
order = 4038
uses = ["def-wf-algebraic-representations", "def-wf-lie-radical-centre", "def-wf-semisimple-lie-algebra", "def-wf-semisimple-module", "def-wf-simple-module", "lem-wf-same-lie-closed-subgroup", "lem-wf-solvable-common-eigenvector", "lem-wf-solvable-radical-characteristic"]
+++
If $H\subseteq\operatorname{GL}(V)$ is connected, $Z(H)$ is finite,
and $V$ is a faithful
semisimple $H$-module over
$\overline{\mathbf Q}_\ell$, then $\operatorname{Lie}(H)$ is a
semisimple Lie algebra.

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

For completeness, the adjoint kernel is the group centre. If
$g\in H$ acts trivially on $\mathfrak h$, the closed centralizer
$C_H(g)$ has Lie algebra $\mathfrak h$, so
[lem-wf-same-lie-closed-subgroup] gives $C_H(g)=H$ and
$g\in Z(H)$. The reverse inclusion is immediate; hence
$Z(H)=\ker(\operatorname{Ad}:H\to\operatorname{GL}(\mathfrak h))$.
For a dual-number matrix $1+\epsilon X$,

$$
\operatorname{Ad}(1+\epsilon X)(Y)
=Y+\epsilon[X,Y].
$$

Consequently the tangent equations of this kernel give

$$
\operatorname{Lie}Z(H)
=\ker(d\operatorname{Ad})
=\ker(\operatorname{ad})
=\mathfrak z(\mathfrak h).
$$

A finite linear algebraic group over the characteristic-zero field
$\overline{\mathbf Q}_\ell$ is reduced and zero-dimensional, so its
Lie algebra is zero. Hence $\mathfrak z(\mathfrak h)=0$, and
therefore $\mathfrak r=0$. By
[def-wf-semisimple-lie-algebra], this says precisely that
$\mathfrak h$ is semisimple.
