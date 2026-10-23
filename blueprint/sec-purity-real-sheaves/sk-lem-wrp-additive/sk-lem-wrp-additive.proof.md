+++
kind  = "proof"
of    = "sk-lem-wrp-additive"
+++
Let $A$ be a finite constant abelian group. Given an $A$-torsor and a
point $p$ in its geometric fibre, the monodromy of the torsor is a
continuous homomorphism $a:P\to A$, defined by $g(p)=p+a(g)$. Since
$A$ is abelian, this homomorphism does not depend on the point.
Conversely, the rule $g\cdot t=t+a(g)$ defines a torsor. Thus
$H^1(U,A)=\Hom_{\mathrm{cont}}(P,A)$ canonically
([cor-galois-abelian-h1], [lem-wf-finite-constant-h1-pi1]). Transport by $s$
replaces $g$ by $s^{-1}gs$, so this identification is compatible with
the Frobenius actions.

Now choose a $\Ql$-basis of $E$, with coordinate maps $t_i$. Since $P$
is compact, each $t_i a(P)$ is bounded, and after multiplying all
coordinates by one power of $\ell$ we may assume that they take values
in $\Zl$. Their reductions modulo $\ell^n$ are compatible classes in
$H^1(U,\mathbf Z/\ell^n)$ fixed by Frobenius
([lem-wf-additive-characters-h1]), and hence they vanish by
[sk-prop-wrp-h1-no-fixed]. Therefore all coordinates of $a$ are zero.
