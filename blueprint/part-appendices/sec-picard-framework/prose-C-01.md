+++
id = "prose-C-01"
kind = "hidden"
title = "Picard schemes and Jacobians"
order = 873
+++
For a curve $C$ proper and connected over a separably closed field and
$n$ invertible in that field, the Kummer sequence shows that
$H^1(C,\mu_n)$ is the $n$-torsion of the Picard group of $C$. To count this torsion, and to see
Frobenius act on it, we need the group $\operatorname{Pic}^0(C)$ of
invertible sheaves of degree zero to be the group of points of an
abelian variety; then Appendix [sec-abelian-varieties] applies. Over $\mathbf C$
this is the Abel–Jacobi theorem, $\operatorname{Pic}^0(C)\simeq H^0(C,\Omega^1)^\vee/H_1(C,\mathbf Z)$. Over an arbitrary field the
Jacobian was constructed by Weil, as part of his proof of the Riemann
hypothesis for curves, and later by Grothendieck as a Picard scheme
representing invertible sheaves in families. We follow the second
approach, in the elementary form that is available for curves. Let $C$
be a smooth proper connected curve of genus $g$ over a separably closed
field $k$. We construct the Picard scheme of $C$ and show that its
component of degree zero, the Jacobian $J(C)$, is an abelian variety of
dimension $g$ with $J(C)(k)=\operatorname{Pic}^0(C)$ and tangent space
$H^1(C,\mathcal O_C)$ at the origin (Theorem [sk-thm-picard-main]). This
computes $H^i(C,\mu_n)$ in Appendix [sec-curve-estimates]. Over a finite field
we descend the Jacobian to $J_0$ over $\mathbf F_q$, so that
$\varprojlim_nH^1(C,\mathbf Z/\ell^n(1))\simeq T_\ell J_0$ compatibly with
Frobenius
(Propositions [sk-prop-jacobian-descent]
and [sk-prop-app-jacobian-equivariant-kummer]); this is how the Tate module
controls Frobenius on $H^1$ in Proposition [sk-prop-wrp-h1-no-fixed].

The construction rests on one observation. An invertible sheaf
$\mathcal L$ of degree $g$ with $h^0(\mathcal L)=1$ is determined by the
divisor of zeros of its unique section up to scalars, an effective
divisor of degree $g$. Effective divisors of degree $g$ are the points of
the Hilbert scheme $H_g$, a smooth proper variety of dimension $g$
(Theorem [sk-thm-picard-hilb-curves]). In degree $g$, Riemann–Roch
gives $h^0\geq1$, with equality exactly when $h^1=0$. By semicontinuity
this condition is open in families, and so it defines an open
chart $W\subset H_g$ of the Picard functor
(Proposition [sk-thm-picard-f-representable]). Riemann–Roch shows that every
invertible sheaf can be moved into this chart by a twist defined over $k$
(Lemma [sk-thm-picard-twist]), so the translates of $W$ cover the
Picard functor and glue to the Picard scheme. Note that
$T\mapsto\operatorname{Pic}(C\times T)$ is not a sheaf: if $\mathcal M$
is a nontrivial invertible sheaf on $T$ and $f:C\times T\to T$ is the
projection, then $\mathcal L$ and $\mathcal L\otimes f^*\mathcal M$ are
isomorphic locally on $T$ but not globally. The Picard functor is
therefore a sheafified quotient, and with a rational point we describe it by
invertible sheaves trivialized along that point
(Lemma [sk-prop-picard-pic-split]). Properness of the components
comes from the Abel map $H_g\to\operatorname{Pic}^g$, which is surjective.

The construction uses only coherent cohomology, Riemann–Roch and
descent; see also (Milne JV). Over an arbitrary field the Jacobian is
obtained from the one over a separable closure by descent along a finite
separable extension.
