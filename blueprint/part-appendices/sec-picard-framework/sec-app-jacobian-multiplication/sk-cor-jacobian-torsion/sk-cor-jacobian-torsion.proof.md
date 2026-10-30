+++
kind = "proof"
of = "sk-cor-jacobian-torsion"
uses = ["sk-prop-av-mult-n-pullback", "sk-def-av", "sk-prop-av-isogeny", "sk-thm-picard-main", "sk-cor-picard-degree"]
+++
By Proposition [sk-prop-av-isogeny], the kernel $J(C)[n]$
is finite étale of rank $n^{2g}$. A finite étale scheme of rank $r$
over the algebraically closed field $k$ is a disjoint union of $r$
copies of $\operatorname{Spec}k$. This description is stable under base
extension, and the formation of the Jacobian and of $[n]$ commutes with
base change (Theorem [sk-thm-picard-main]), so the natural map
$J(C)[n](k)\to J(C_{k'})[n](k')$ is a bijection.

If $\ell^m$ is the exact power of a prime $\ell$ dividing $n$, then
$J(C)[\ell^m](k)\simeq(\mathbf Z/\ell^m)^{2g}$ by
Proposition [sk-prop-av-tate-rank] applied to $J(C)$. Combining the
parts for the primes dividing $n$, we get the stated
$\mathbf Z/n\mathbf Z$-module structure.

By Proposition [sk-prop-av-isogeny], the group
$J(C)(k)$ is divisible. In the exact sequence of
Corollary [sk-cor-picard-degree], the group $\mathbf Z$ has no
$n$-torsion and $J(C)(k)/n=0$. This proves the two assertions for
$\operatorname{Pic}(C)$.
