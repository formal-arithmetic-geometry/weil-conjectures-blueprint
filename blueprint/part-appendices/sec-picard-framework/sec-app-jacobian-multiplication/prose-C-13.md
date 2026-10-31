+++
id = "prose-C-13"
kind = "hidden"
title = "Torsion points of the Jacobian"
order = 900
+++
The Kummer sequence on a curve $C$ over an algebraically closed field
identifies $H^1(C,\mu_n)$ with $\operatorname{Pic}(C)[n]$ and
$H^2(C,\mu_n)$ with $\operatorname{Pic}(C)/n$
(Proposition [sk-thm-curveestimate]). To compute these groups, we
combine the exact sequence of Corollary [sk-cor-picard-degree], which
separates the discrete part $\mathbf Z$ of the Picard group from the
Jacobian, with the results of Appendix [sec-abelian-varieties] on
multiplication by $n$ on an abelian variety. Since $\mathbf Z$ is torsion
free and $J(C)(k)$ is divisible, the $n$-torsion of $\operatorname{Pic}(C)$
is $J(C)[n](k)\simeq(\mathbf Z/n)^{2g}$ and the cokernel of $n$ is
$\mathbf Z/n$, given by the degree. For $\mathbf P^1$ the Jacobian is
zero, and for an elliptic curve it is the curve itself, with $n$-torsion
$(\mathbf Z/n)^2$. Proper base change also needs these groups to be
unchanged under extension of the algebraically closed field, and this
holds because $J(C)[n]$ is finite étale
(Corollary [sk-cor-jacobian-torsion]).
