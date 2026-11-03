+++
kind  = "proof"
of    = "lem-ag-lie-centre"
+++
We first show that the kernel of the adjoint representation is the
group centre. If
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
Here the centralizer $C_H(g)$ and the kernel of $\operatorname{Ad}$
are closed subgroup schemes defined by these equations, hence reduced
by [lem-ag-cartier-reduced], so their equations compute their Lie
algebras. Finally $Z(H)^\circ$ is open in $Z(H)$ by
[lem-wf-algebraic-component-cosets], hence has the same tangent space
at the identity, so $\operatorname{Lie}(Z(H)^\circ)=\operatorname{Lie}Z(H)$.
