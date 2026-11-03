+++
kind  = "proof"
of    = "det-prop-sfb-cartesian-coefficients-twists"
+++
*Roots of unity.* $\mu_{\ell^n,Y}$ is represented by the finite étale $Y$-group scheme
$\mu_{\ell^n,Y}=\Spec\cO_Y[t]/(t^{\ell^n}-1)$ ([def-pur-roots-of-unity-sheaf]). For a
representable sheaf $h_V$ on $Y_{\mathrm{proét}}$ one has $f^{-1}h_V=h_{V\times_YX}$ (inverse
image along the continuous, finite-limit preserving base change functor, and
subcanonicity), and $\mu_{\ell^n,Y}\times_YX=\mu_{\ell^n,X}$. The group structure is given by
morphisms of schemes and is preserved. The Kummer maps $u\mapsto u^\ell$ are morphisms of
schemes, hence compatible.

*The integral twist.* $\cO_E(1)_Y=\varprojlim_n(\cO_E/\ell^n)_Y(1)$ and
$(\cO_E/\ell^n)_Y(1)=\mu_{\ell^n,Y}\otimes_{\mathbf Z/\ell^n}(\cO_E/\ell^n)_Y$ is represented
by the finite étale $Y$-scheme of $\cO_E/\ell^n$-linear combinations, i.e. by
$\mu_{\ell^n,Y}^{\,\oplus ef}$ after choosing a $\mathbf Z_\ell$-basis of $\cO_E$ (here $ef=[E:\mathbf Q_\ell]$);
the inverse limit over $n$ is represented by the inverse limit of these schemes, a
pro-étale $Y$-scheme, and its inverse image is represented by its base change to $X$
([Stacks, Tag 09A5](https://stacks.math.columbia.edu/tag/09A5)). Since base change commutes with limits, the base change is the
corresponding limit over $X$, which represents $\cO_E(1)_X$. The module structure over
$\cO_{E,Y}$ is matched with that over $\cO_{E,X}$ via
[det-prop-sfb-qlbar-colimit-x-pullback] (1).

*Finite $A$.* If $\ell^rA=0$, $A_Y(1)=\mu_{\ell^r,Y}\otimes_{\mathbf Z/\ell^r}A_Y$; $f^{-1}$ is
exact and monoidal and $f^{-1}A_Y=A_X$, so $f^{-1}A_Y(1)\cong\mu_{\ell^r,X}\otimes A_X=A_X(1)$.

*Rational and algebraic closure.* $E_Y(1)=\cO_E(1)_Y[1/\ell]$ and
$\Qlb_Y(1)=\varinjlim_EE_Y(1)$; $f^{-1}$ commutes with colimits and with multiplication by
$\ell$, so it carries these to $E_X(1)$ and $\Qlb_X(1)$, compatibly with
[det-prop-sfb-qlbar-colimit-x-pullback] (2), (3).

*Powers and duals.* $f^{-1}$ is strong monoidal on module sheaves (via $\alpha_f$), so it
commutes with tensor powers; and for an invertible module $L$ (locally free of rank one,
[det-def-sp-tate-twist-locally-free]), $f^{-1}\mathcal Hom(L,\Lambda_Y)\to\mathcal Hom(f^{-1}L,\Lambda_X)$
is an isomorphism, as one checks locally where $L$ is free. Finally
$f^*(K\otimes^{\mathbf L}\Lambda_Y(d))\cong f^*K\otimes^{\mathbf L}f^*\Lambda_Y(d)$ since $f^*$
is exact and monoidal.
