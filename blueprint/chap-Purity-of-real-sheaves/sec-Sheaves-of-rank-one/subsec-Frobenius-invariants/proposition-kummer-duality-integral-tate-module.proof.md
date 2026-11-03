+++
kind = "proof"
of = "proposition-kummer-duality-integral-tate-module"
order = 1089
+++
By the Kummer sequence, $H^1(C,\mu_{\ell^n})$ is
the $\ell^n$-torsion of the Picard group. Poincaré duality
turns this into a statement about the untwisted $H^1$.

The first identification is
Proposition [proposition-h-1-curve-tate-module]. That proposition also
gives its Galois equivariance, and it shows that the coefficient map
$z\mapsto z^\ell$ from $\mu_{\ell^{n+1}}$ to $\mu_{\ell^n}$ corresponds to
$[\ell]$ on the Jacobian.

For the dual Tate module, Poincaré duality at finite level pairs the
untwisted $H^1$ with the twisted one that we have just identified with
$J[\ell^n](k)$. Derived duality gives a statement about the single group
$H^1$ because all the groups involved are free $A_n$-modules. We have
$H^0(C,A_n)=A_n$ and $H^2(C,A_n(1))=A_n$ by
Proposition [proposition-smooth-proper-curves-torsion-prime]. The group
$H^1(C,A_n(1))$ is free of rank $2g$ by the identification above and
Corollary [corollary-torsion-jacobian-field-extension]. Since
$A_n(1)\simeq A_n$ over $k$, the untwisted $H^1$ is free of rank $2g$ as well.
Finally, a bounded complex with projective cohomology modules is the sum of its
shifted cohomology modules in the derived category, so $A_n$-duality acts
degree by degree. In this situation derived Poincaré duality,
Theorem [theorem-poincare-duality], applied to the
constant sheaf, induces in degree one an isomorphism

$$
H^1(C,A_n)\xrightarrow{\sim}
\Hom_{A_n}(H^1(C,A_n(1)),A_n).
$$

This map is the adjoint of cup product followed by the trace map of
the duality theorem.  Cup product and trace commute with
reduction of coefficients and with the action of
$\operatorname{Gal}(k/k_0)$.  Because of the twist on the second
factor, Frobenius acts trivially on the target $A_n$.

In the limit, the finite-level dualities combine into a duality with the
Tate module. Since the transition maps $[\ell]$
are surjective, we have $J[\ell^n](k)=T_\ell J/\ell^nT_\ell J$. Moreover
$T_\ell J$ is finite free by Proposition [proposition-integral-tate-module].  A
homomorphism of finite free $\mathbf Z_\ell$-modules is determined by its reductions
modulo all $\ell^n$, and every compatible system of reductions lifts.
Hence the inverse limit of the adjoints at finite level is the dual of
$T_\ell J$. We obtain a perfect pairing

$$
\varprojlim_nH^1(C,A_n)\times T_\ell J\longrightarrow\mathbf Z_\ell,
$$

invariant under Frobenius.  Geometric Frobenius acts on $T_\ell J$
by $B^{-1}$, so its matrix on $\varprojlim_nH^1(C,A_n)$ in the dual
basis is $(B^{-1})^{-t}=B^t$.
