+++
kind  = "proof"
of    = "det-lem-constructible-ext-continuity-stratum"
+++
Write $\Phi=L^\vee\otimes u^*i^*(-)$, an exact functor from $\Lambda_X$-modules to
$\Lambda_S$-modules which commutes with all colimits ($u^*$, $i^*$ are inverse images and
$L^\vee$ is flat) and preserves the lower bound $b$. By
[det-lem-formal-closed-support-stratum-hom] and the fiber formula of
[det-lem-formal-closed-support-adjunction] (4),
$$
\Hom(a_!L,K[q])=H^q\bigl(S,\Phi(\fib(K\to Rj_*j^*K))\bigr),
$$
naturally in $K$. The triangle $\Phi(\fib)\to\Phi(K)\to\Phi(Rj_*j^*K)\to$ gives long exact
sequences in $H^*(S,-)$, natural in $K$; by exactness of filtered colimits and the five lemma
it suffices to prove that $H^q(S,\Phi(-))$ commutes with the colimit for the two systems
$K_i$ and $Rj_*j^*K_i$.

*First term.* $(\Phi(K_i))$ is a filtered system of complexes on $S$ vanishing below $b$ with
colimit $\Phi(K)$; $S$ is qcqs (locally closed in the qcqs $X$, via quasi-compact
immersions), so [det-lem-bounded-continuity-sections] (3) applies.

*Second term.* Represent $Rj_*j^*K_i$ by $j_*$ of a K-injective resolution; the cohomology
sheaves are $R^rj_*(j^*K_i)$, which vanish for $r<b$. The hypercohomology spectral sequence
$$
E_2^{p,r}(i)=H^p\bigl(S,\Phi(R^rj_*j^*K_i)\bigr)\Rightarrow H^{p+r}\bigl(S,\Phi(Rj_*j^*K_i)\bigr)
$$
(for bounded below complexes, from the canonical filtration) is natural in $i$, and its
filtered colimit over $i$ is again a convergent spectral sequence, since filtered colimits are
exact. By [det-lem-bounded-continuity-direct-image] (with $j$ qcqs),
$\varinjlim_iR^rj_*(j^*K_i)=R^rj_*(j^*K)$; then by
[det-lem-bounded-continuity-sections] (3) on $S$, applied to sheaves (complexes concentrated
in degree $0$), $\varinjlim_iE_2^{p,r}(i)=E_2^{p,r}$ for $K$. So the comparison map is an
isomorphism on $E_2$ pages. Since $E_2^{p,r}=0$ for $p<0$ or $r<b$, only the finitely many
$(p,r)$ with $0\le p$, $b\le r$, $p+r=n$ contribute to total degree $n$; the induced map on
the finite filtrations of the abutments is an isomorphism on graded pieces, hence on the
abutments.
