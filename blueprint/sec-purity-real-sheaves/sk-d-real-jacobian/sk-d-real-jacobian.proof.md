+++
kind  = "proof"
of    = "sk-d-real-jacobian"
+++
The inclusion $\mu_{\ell^n}\to\mathbb G_m$ induces a map
$H^1(C,\mu_{\ell^n})\to\operatorname{Pic}(C)$. By the Kummer exact
sequence its image is $\operatorname{Pic}(C)[\ell^n]$, and its kernel
is $k^\times/(k^\times)^{\ell^n}=0$ (see [sk-thm-curveestimate] and
[sk-prop-jacobian-descent]). Torsion line bundles have
degree zero, and the Jacobian represents the Picard functor of degree
zero ([def-sc-jacobian], [sk-prop-jacobian-descent]), which gives the first
identification ([lem-wf-curve-kummer-jacobian-tate-module]). All these maps
are natural under automorphisms of $k/k_0$
([lem-wf-geometric-jacobian-galois-action]). The map
$\mu_{\ell^{n+1}}\to\mu_{\ell^n}$ is $z\mapsto z^\ell$; it induces the
$\ell$th tensor power on line bundles, which is $[\ell]$ on the
Jacobian.

For the dual Tate module we use the Poincaré pairing at finite
level. By [sk-thm-curveestimate], the groups $H^0(C,A_n)$
and $H^2(C,A_n)$ are free of rank one, up to the appropriate twist.
The identification above and [sk-cor-jacobian-torsion]
show that $H^1(C,A_n(1))$ is free of rank $2g$, and hence so is the
untwisted $H^1$. Recall that a bounded complex whose cohomology
modules are projective is isomorphic in the derived category to the
sum of its shifted cohomology modules; to see this, lift the identity
of each cohomology module successively through its cycles. We apply
derived Poincaré duality, [sk-thm-sf-identification], to the
constant sheaf. By this splitting, its adjoint in degree one is an
isomorphism

$$
 H^1(C,A_n)\xrightarrow{\sim}
 \Hom_{A_n}(H^1(C,A_n(1)),A_n)
$$

([lem-wf-curve-finite-level-pd]). This map is the adjoint of cup product
followed by the trace map of the duality theorem. Cup product and trace
commute with reduction of coefficients and with Galois transport, and the
twist on the second factor makes the target $A_n$ invariant.

Since the transition maps $[\ell]$ are surjective, we have
$J[\ell^n](k)=T_\ell J/\ell^nT_\ell J$, and $T_\ell J$ is finite free
([sk-prop-av-tate-rank]). Hence the inverse limit of the
adjoints at finite level is the dual of $T_\ell J$
([lem-wf-curve-h1-dual-tate-module]); indeed, a homomorphism of finite free
$\Zl$-modules is determined by its reductions modulo all $\ell^n$, and every
compatible system of reductions lifts. Finally, geometric Frobenius acts on
the Kummer factor $T_\ell J$ by $B^{-1}$. Since the pairing is invariant, its
matrix on the first factor is $(B^{-1})^{-t}=B^t$.
