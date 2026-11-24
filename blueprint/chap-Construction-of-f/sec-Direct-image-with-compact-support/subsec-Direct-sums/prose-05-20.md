+++
id = "prose-05-20"
kind = "hidden"
title = "Direct sums (1)"
order = 482
+++
To apply Brown representability, we need $Rf_!$ to preserve arbitrary
direct sums. Since $j_!$ is a left adjoint, it does. The question is
therefore whether $Rp_*$ preserves direct sums for proper $p$.
For complexes with a common lower and upper bound, this would follow from
finiteness of [$\operatorname{cd}_\ell(p)$](@definition-cohomological-dimension). However, the summands of a direct
sum in [$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$](@definition-localizing-subcategory) need not have any common bound. As in the
proof of compactness, we use a uniform bound instead. Let $d$ bound
the fibre dimensions of $p$. We show that $R^qp_*$ vanishes on
[$\IndCons(X,\Lambda)$](@definition-ind-constructible-sheaves) for $q>2d+1$. This means that $\mathcal H^q(Rp_*K)$ depends
only on the cohomology of $K$ in degrees $[q-2d-1,q]$.

We prove the bound on sections over
affine [weakly contractible](@definition-weak-contractibility) objects and then pass to colimits. For this
we use the continuity of pro-étale cohomology,
Corollary [corollary-continuity-cohomology], applied to sheaves, which
are complexes vanishing below degree $0$. It says that for a quasi-compact
and quasi-separated morphism $p$ the functors $R^qp_*$ on sheaves of
modules commute with filtered colimits. Since a direct sum is the
filtered colimit of its finite subsums, they also commute with direct sums.

We also use the following description of $R^qp_*$. If $V\to Y$ is an
affine [weakly contractible](@definition-weak-contractibility) object and $X_V=X\times_YV$, then
$\Gamma(V,-)$ is exact (Corollary [corollary-evaluation-weakly-contractible-objects](1)), and hence

$$
(R^qp_*M)(V)=H^q(\href{@definition-small-pro-etale-site}{(X_V)_{\mathrm{pro}\acute{e}t}},M|_{X_V}).
\tag{5.5}
$$

Since such $V$ form a basis of [$Y_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site), a sheaf on [$Y_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site)
vanishes if its sections over all of them vanish.
