+++
kind  = "proof"
of    = "lem-wf-finite-constant-h1-pi1"
+++
By [thm-galois-torsor-h1], the left side of (3.1) classifies
torsors under the constant group $M$. By
[thm-galois-lc-etale], their underlying sheaves
are finite etale covers. The finite-etale fibre-functor equivalence of
[thm-galois-fundamental] sends a torsor $P$
to a nonempty finite set $P_{\bar u}$ with commuting actions of
$\pi_1(U,\bar u)$ and $M$,
the latter simply transitive. Choose $p\in P_{\bar u}$. For every
$g\in\pi_1(U,\bar u)$, there is a unique $f_P(g)\in M$ such that

$$
g(p)=p+f_P(g).
$$

The two actions commute, so
$f_P(gh)=f_P(g)+f_P(h)$. The homomorphism is continuous because the
stabilizer of every point in the finite fiber is open. Replacing $p$ by
$p+a$ does not change $f_P$, since $M$ is abelian; the resulting
bijection with the continuous homomorphisms is
[cor-galois-abelian-h1].

Conversely, a continuous homomorphism $f:\pi_1(U,\bar u)\to M$ gives the
finite $\pi_1(U,\bar u)$-set $M$, on which

$$
g\cdot a=f(g)+a.
$$

It commutes with translations by $M$, and the finite-etale
fibre-functor equivalence of [thm-galois-fundamental] therefore gives
an $M$-torsor. The two constructions are inverse, and they are the two
sides of the bijection [cor-galois-abelian-h1]. Each construction is
defined by transporting fibers, so it
commutes with an automorphism of the pointed scheme.

For completeness, consider the descent transport associated with
$s\in W(U_0,\bar u)$. On the fiber functor it replaces the geometric
monodromy element $g$ by $s^{-1}gs$. Therefore a torsor represented by
$f_P$ is pulled back to the torsor represented by

$$
g\longmapsto f_P(s^{-1}gs).
$$

This computation is unaffected by the choice of a point in the torsor
fiber, by the abelian argument above. It proves both (3.1) and the stated
Weil-descent equivariance.
