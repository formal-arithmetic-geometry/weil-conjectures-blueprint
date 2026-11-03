+++
kind  = "proof"
of    = "thm-sc-proper-cohomology"
+++
Use $\theta_\zeta$ ([def-sc-mu-trivialization], with the
primitive root of [lem-sc-primitive-root]) to replace
$\mathbf F_n$ by $\mu_n$. By [lem-sc-kummer-les]
(applied to the exact Kummer sequence
[def-sc-kummer-sequence]; the unit group of the proper connected
curve is $k^\times$, $n$-divisible since $k$ is algebraically
closed, so the exact sequence of the lemma degenerates),

$$
H^1(C,\mu_n)=\operatorname{Pic}(C)[n],\quad
H^2(C,\mu_n)=\operatorname{coker}(n:\operatorname{Pic}(C)\to
\operatorname{Pic}(C)),
$$

which by [lem-sc-pic-proper-ntorsion] are
$(\mathbf Z/n\mathbf Z)^{2g}$ and
$\mathbf Z/n\mathbf Z$; $H^0(C,\mu_n)=\mu_n(k)=\mathbf Z/n\mathbf Z$
by [lem-sc-primitive-root]. The vanishing for $q>2$ is
[lem-sc-cohomological-dimension].
