+++
kind = "proof"
of = "sk-d-real-jacobian"
uses = ["sk-prop-app-jacobian-equivariant-kummer"]
+++
The Kummer sequence identifies $H^1(C,\mu_{\ell^n})$
with the $\ell^n$-torsion of the Picard group, and Poincaré duality
turns this into a statement about the untwisted $H^1$. We begin at
finite level. The inclusion
$\mu_{\ell^n}\to\mathbf G_m$ induces a map
$H^1(C,\mu_{\ell^n})\to\operatorname{Pic}(C)$. By the Kummer exact
sequence its image is $\operatorname{Pic}(C)[\ell^n]$, and its kernel
is $k^\times/(k^\times)^{\ell^n}=0$ (see
Propositions [sk-thm-curveestimate] and
[sk-prop-app-jacobian-equivariant-kummer]). Since torsion line bundles
have degree zero and the Jacobian represents the Picard functor of
degree zero, we obtain the first identification. All these maps are
natural under automorphisms of $k/k_0$. The map
$\mu_{\ell^{n+1}}\to\mu_{\ell^n}$ is $z\mapsto z^\ell$. It induces the
$\ell$th tensor power on line bundles, which is $[\ell]$ on the
Jacobian.

For the dual Tate module we use the Poincaré pairing at finite
level. By Proposition [sk-thm-curveestimate], we have
$H^0(C,A_n)=A_n$ and $H^2(C,A_n(1))=A_n$.
The identification above and Corollary [sk-cor-jacobian-torsion]
show that $H^1(C,A_n(1))$ is free of rank $2g$, and hence so is the
untwisted $H^1$, since $A_n(1)\simeq A_n$ over the algebraically
closed field $k$. Recall that a bounded complex whose cohomology
modules are projective is isomorphic in the derived category to the
sum of its shifted cohomology modules. We apply
derived Poincaré duality, Theorem [sk-thm-sf-identification], to the
constant sheaf. Because of this splitting, the duality isomorphism
induces in degree one an isomorphism

$$
H^1(C,A_n)\xrightarrow{\sim}
\Hom_{A_n}(H^1(C,A_n(1)),A_n).
$$

This map is the adjoint of cup product followed by the trace map of
the duality theorem. Cup product and trace commute with
reduction of coefficients and with the action of
$\operatorname{Gal}(k/k_0)$. Because of the twist on the second
factor, Frobenius acts trivially on the target $A_n$.

It remains to pass to the limit. Since the transition maps $[\ell]$
are surjective, we have $J[\ell^n](k)=T_\ell J/\ell^nT_\ell J$, and
$T_\ell J$ is finite free (Proposition [sk-prop-av-tate-rank]). Hence
the inverse limit of the adjoints at finite level is the dual of
$T_\ell J$. Indeed, a homomorphism of finite free $\Zl$-modules is
determined by its reductions modulo all $\ell^n$, and every compatible
system of reductions lifts. In the limit we therefore obtain a
perfect pairing

$$
\varprojlim_nH^1(C,A_n)\times T_\ell J\longrightarrow\Zl,
$$

invariant under Frobenius. Geometric Frobenius acts on $T_\ell J$
by $B^{-1}$, so its matrix on $\varprojlim_nH^1(C,A_n)$ in the dual
basis is $(B^{-1})^{-t}=B^t$.
