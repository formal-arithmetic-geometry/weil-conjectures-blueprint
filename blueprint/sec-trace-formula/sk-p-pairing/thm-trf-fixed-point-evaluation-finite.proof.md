+++
kind  = "proof"
of    = "thm-trf-fixed-point-evaluation-finite"
+++
Put $W=Lj^*K$. A local bounded finite-free representative, as in
[def-weil-site-perfect-complex], pulls back to such a representative
of $W$, so $W$ is site-perfect. The fixed-scheme identity $hj=j$
of [def-trf-fixed-scheme] and
[thm-trf-internal-hom-pullback], applied with first variable
$Lh^*K$, give

$$
Lj^*R\mathcal Hom_A(Lh^*K,K)\simeq R\mathcal Hom_A(W,W).
$$

Since $k$ is algebraically closed, a finite etale $k$-scheme is a
finite disjoint union of copies of $\Spec k$; its sheaf category is
the product of their sheaf categories. On each such component set
$W_y^\vee=R\operatorname{Hom}_A(W_y,A)$.
The tensor–Hom adjunction of [def-weil-derived-tensor] identifies
$R\operatorname{Hom}_A(W_y,W_y)$ with
$W_y\otimes_A^LW_y^\vee$. Compose this identification with the
Koszul symmetry and evaluation to obtain a morphism to $A$.
Their finite product defines $\sigma_{h,K}$.

The mate of $u$, after restriction to $y$, is the mate of $u_y$
by the naturality of the internal-Hom comparison. Under the preceding
tensor–Hom identification it is coevaluation followed by
$u_y\otimes1$. The composite with symmetry and evaluation is
exactly the categorical trace of [def-trf-categorical-trace].
More explicitly, on a bounded finite-projective representative $P$
and a chain representative $v$ of $u_y$, it is
$\sum_i(-1)^i\operatorname{tr}_A(v^i\mid P^i)$, by
[lem-trf-chain-supertrace]. This also proves independence of the
representative and the asserted naturality.
