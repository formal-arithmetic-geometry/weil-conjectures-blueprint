+++
id = "prose-C-14"
kind = "hidden"
title = "Torsion points"
order = 1559
+++
The Kummer sequence on a curve $C$ over an algebraically closed field
identifies $H^1(C,\mu_n)$ with $\operatorname{Pic}(C)[n]$ and
$H^2(C,\mu_n)$ with $\operatorname{Pic}(C)/n$
(Proposition [proposition-smooth-proper-curves-torsion-prime]). To compute these groups, we
combine two facts. First, the exact sequence of Corollary [corollary-degree-jacobian]
separates the discrete part $\mathbf Z$ of the Picard group from the
[Jacobian](@theorem-picard-scheme-jacobian-over-separably). Second, Appendix [chap-Abelian-varieties] describes multiplication by
$n$ on an [abelian variety](@definition-abelian-variety) over an algebraically closed field: it is
surjective on points, and for $n$ invertible in $k$ its kernel is
$(\mathbf Z/n)^{2g}$. Now apply the snake lemma to multiplication by $n$
on the [degree sequence](@corollary-degree-jacobian). Since $\mathbf Z$ is torsion free, the
$n$-torsion of $\operatorname{Pic}(C)$ is $\href{@theorem-picard-scheme-jacobian-over-separably}{J(C)}\href{@definition-abelian-variety}{[n]}(k)\simeq(\mathbf Z/n)^{2g}$.
Since [$J(C)(k)$](@theorem-picard-scheme-jacobian-over-separably) is divisible, the cokernel of $n$ on $\operatorname{Pic}(C)$
is $\mathbf Z/n$, given by the degree.

For [proper base change](@theorem-proper-base-change-classical-pro) we also need these groups to be unchanged under
extension of the algebraically closed field. This holds because
[$J(C)[n]$](@definition-abelian-variety) is finite étale
(Corollary [corollary-torsion-jacobian-field-extension]).
