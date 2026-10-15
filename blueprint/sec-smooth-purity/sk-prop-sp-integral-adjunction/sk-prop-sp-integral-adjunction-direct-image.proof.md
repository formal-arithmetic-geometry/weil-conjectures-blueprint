+++
kind = "proof"
of = "det-sp-integral-direct-image-tower"
+++
(1) $\operatorname{red}_XM$ is normalized constructible with the Tor bounds of $M$
([det-sp-normalized-equivalence]). By [det-sp-tower-shriek-levels] and
[det-sp-tower-bound-uniform] its image under $Rf_{!,\bullet}$ is constructible
with bounds widened by $2d$, and its reduction maps are the composites of the
isomorphisms $b$ of [det-sp-reduction-direct-image] with $Rf_!$ of the
(invertible) reduction maps of $\operatorname{red}_XM$, hence isomorphisms.

(2) $R\bar f_*$ and $j_!$ commute with reduction modulo $\ell^n$ (reduction is
the cone of $\ell^n$) and with $R\varprojlim$ ($R\bar f_*$ is a right adjoint;
$j_!$ is exact and commutes with products on the replete site, Stacks, Tag
09BP), and $M\simeq R\varprojlim_nM/\ell^n$ since $M$ is derived complete. Hence
$R\bar f_*j_!M\simeq R\varprojlim_nR\bar f_*j_!(M/\ell^n)=R\varprojlim_nRf_{!,\mathcal O_E/\ell^n}(M/\ell^n)$.
By (1) and the reconstruction lemma, this limit lies in $\Dbc(Y,\mathcal O_E)$ and
reduces to $Rf_{!,\mathcal O_E/\ell^n}(M/\ell^n)$; equivalently
$\operatorname{red}_YRf_{!,\mathcal O_E}M\simeq Rf_{!,\bullet}\operatorname{red}_XM$. Independence of
the compactification holds in the tower category (levelwise, by the finite
statement), hence after $R\varprojlim$.

(3) Pullback is exact on module sheaves and commutes with extension of scalars,
so $(f^*K)/\ell^n=f^*(K/\ell^n)$, and inverse image preserves
$\Dbc(-,\mathcal O_E)$ without completion. Tensor products of objects of
$\Dbc(-,\mathcal O_E)$ stay in this category, with reductions the tensor products
of reductions. The tower projection formula (an isomorphism of towers, being
levelwise the finite projection formula) applied to
$\operatorname{red}_XM$ and $\operatorname{red}_YK$, followed by $R\varprojlim$ and (2), gives the
integral projection formula.
