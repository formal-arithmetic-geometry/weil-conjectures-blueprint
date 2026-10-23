+++
kind  = "proof"
of    = "sk-lem-wrp-hc2"
+++
The sections of a local system are the invariant vectors of its
fibre ([p-real-sections]). By degreewise Poincaré duality,
[sk-thm-derived-duality], we have

$$
 H_c^2(U,\mathcal F)^\vee
       =H^0(U,\mathcal F^\vee(1))=(V^\vee)^P(1).
$$

Since the dual of $(V^\vee)^P$ is $V_P$, this gives the second
formula, with its twist ([lem-a1-affine-hc2]). The identification is induced
by the canonical duality pairing and is therefore Frobenius equivariant. The
vanishing outside degrees $0,1,2$ follows from the bound on the
cohomological dimension of curves and the comparisons of coefficients
in [sk-thm-curve-package].

Suppose that $U_0$ is affine, and choose a smooth proper completion of
$U$ ([sk-i-real-compactification]). Its boundary is nonempty, because a
connected proper curve has only constant global functions and hence is not
affine. A compactly supported section extends by zero to the completion, so
it vanishes on a neighbourhood of the boundary. Since a section of a lisse
sheaf on a connected curve is determined by its generic value, the section
is zero. Thus $H_c^0(U,\mathcal F)=0$ ([lem-a1-affine-hc0]).

The action of $W(U_0)$ on $V^P$ and $V_P$ factors through the degree
quotient. If $\beta$ is an eigenvalue of the operator of degree one,
then $\beta^{d(x)}$ is an eigenvalue of a subquotient of
$\mathcal F_{\bar x}$, for every closed point $x$. Hence a punctual
bound gives $|\iota(\beta)|\le q^{a/2}$, and purity gives equality.
Finally, the twist $(-1)$ multiplies each global eigenvalue by $q$
([sk-r-real-linear]), which gives the stated weights for $H_c^2$.
