+++
kind = "proof"
of = "det-sp-coefficient-towers-abelian"
+++
(1) Inverse systems of sheaves on $T_{\mathrm{proét}}$ form a topos (sheaves on
the product of $T_{\mathrm{proét}}$ with the poset $\mathbf N_{\geq1}$), and
$\mathcal O_{E,T}/\ell^\bullet$ with the reduction maps is a ring object in it.
A module over it is exactly a system $(C_n,t_n)$ as in the definition: $C_n$ is
an $\mathcal O_{E,T}/\ell^n$-module and $t_n$ is semilinear over the reduction
map. Modules over a ring object of a topos form a Grothendieck abelian
category (it has a generator, given by the free modules on the generators of
the topos, and filtered colimits are exact). Limits and colimits of inverse
systems of sheaves are computed objectwise in $\mathbf N_{\geq1}$, i.e. level by
level, and the same holds for modules since the forgetful functor creates
them.

(2) Since kernels and cokernels are computed level by level, evaluation at $n$
preserves them, hence is exact, and so it passes to derived categories without
deriving.

(3) For $m\leq n$ the composite transition $C_n\to C_m$ is linear over
$\mathcal O_{E,T}/\ell^n\to\mathcal O_{E,T}/\ell^m$, hence corresponds by
extension–restriction adjunction to an $\mathcal O_{E,T}/\ell^m$-linear map
$C_n\otimes_{\mathcal O_{E,T}/\ell^n}\mathcal O_{E,T}/\ell^m\to C_m$. On the
derived level, apply this to a K-flat (levelwise K-flat) representative of
$C_\bullet$, which exists in the Grothendieck abelian category of towers; the
resulting map out of the derived tensor product is the reduction map. It is
natural, and compatible with composition because the transitions compose and
the tensor product is associative.
