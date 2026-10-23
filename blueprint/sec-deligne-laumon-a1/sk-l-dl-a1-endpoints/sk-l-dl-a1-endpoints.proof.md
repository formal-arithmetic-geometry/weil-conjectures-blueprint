+++
kind  = "proof"
of    = "sk-l-dl-a1-endpoints"
+++
Since $U$ is connected and the curve is affine, a nonzero section of
$F$ over $U$ cannot have proper support. As $j_*F$ has no punctual
subsheaf ([sk-lem-wft-curve-heart]), this proves $H_c^0(C,j_*F)=0$.
Sheaves with finite support have compact-support cohomology only in
degree zero, and hence localization identifies the group in degree two
with $H_c^2(U,F)$. By smooth global duality ([sk-thm-derived-duality], in the form
of [sk-lem-wrp-hc2]),

$$
 H_c^2(U,F)=H^0(U,F^\vee)^\vee(-1)
                         =V_{\pi_1(U)}(-1).
$$

The coinvariants $V_{\pi_1(U)}$ form the maximal geometrically
constant quotient of $F$. Suppose that $F$ is pure. At a closed point
of degree $d$, the Frobenius of this quotient is the $d$th power of
its constant Frobenius, and its eigenvalues are eigenvalues of a
quotient of the pure stalk. Hence the quotient has weight $w$, and the
twist adds two. For the range of degrees, localization reduces a
constructible sheaf to a lisse sheaf on an open and a sheaf on the
finite boundary; for these, the range follows from smooth duality and
the absence of negative ordinary cohomology.
