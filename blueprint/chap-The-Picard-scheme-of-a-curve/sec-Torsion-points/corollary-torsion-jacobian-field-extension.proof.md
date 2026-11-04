+++
kind = "proof"
of = "corollary-torsion-jacobian-field-extension"
order = 1553
uses = ["proposition-multiplication-n", "proposition-integral-tate-module", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian"]
+++
The assertions about $J(C)$ are those of Appendix [chap-Abelian-varieties]
for this abelian variety, and the degree sequence carries them over to
$\operatorname{Pic}(C)$.

By Proposition [proposition-multiplication-n], the kernel $J(C)[n]$
is finite étale of rank $n^{2g}$. A finite étale scheme of rank $r$
over the algebraically closed field $k$ is a disjoint union of $r$
copies of $\operatorname{Spec}k$, a description stable under base
extension. By Theorem [theorem-picard-scheme-jacobian-over-separably]
the formation of the Jacobian and of $[n]$ commutes with base change, so
the natural map $J(C)[n](k)\to J(C_{k'})[n](k')$ is a bijection.

If $\ell^m$ is the exact power of a prime $\ell$ dividing $n$, then
$J(C)[\ell^m](k)\simeq(\mathbf Z/\ell^m)^{2g}$ by
Proposition [proposition-integral-tate-module] applied to $J(C)$. Combining the
parts for the primes dividing $n$, we get the stated
$\mathbf Z/n\mathbf Z$-module structure.

By Proposition [proposition-multiplication-n], the group
$J(C)(k)$ is divisible. In the exact sequence of
Corollary [corollary-degree-jacobian], the group $\mathbf Z$ has no
$n$-torsion and $J(C)(k)/n=0$. This proves the two assertions for
$\operatorname{Pic}(C)$.
