+++
kind  = "proof"
of    = "prop-trf-pairing-local-decomposition"
+++
Apply [lem-trf-integration-component-sum] to $T=E$, the finite
decomposition $E=\coprod_{\beta\in B}\beta$ and
$\tau=\langle u,v\rangle_{\mathrm{LV}}$: it shows that $E$ is proper
over $s$, so that $\int_E$ of [def-trf-integration] is defined, and
that

$$
\int_E\langle u,v\rangle_{\mathrm{LV}}
=\sum_{\beta\in B}\int_\beta\bigl(\langle u,v\rangle_{\mathrm{LV}}|_\beta\bigr)
=\sum_{\beta\in B}\LT_\beta(u,v),
$$

the last equality being the definition of the local terms in
[def-trf-local-term-pair]; for
$E=\emptyset$ the lemma gives $0=0$. When $v=1_K$, so that
$\langle u,1_K\rangle_{\mathrm{LV}}=\Tr_c(u)$ by
[lem-trf-trace-class-diagonal-pairing], the restriction to a component
$\beta\subseteq\Fix(c)$ is the composite used in [def-trf-local-term],
whence $\LT_\beta(u,1_K)=\LT_\beta(u)$, as also recorded in
[def-trf-local-term-pair].

For the point case, $E=s$, $B=\{s\}$, and $j_s$ and the structure map
$a_s$ are identities. Then $\omega_{s,A}=Ra_s^!A=A$ by
[def-trf-dualizing-complex], the restriction to the sole component is
the section itself, and both adjunction maps in [def-trf-integration]
(the unit of $La_s^*\dashv Ra_{s*}$ and the counit of
$Ra_{s!}\dashv Ra_s^!$) are identities, so $\int_s$ is the
identification $\Hom_{D(s,A)}(A,A)=A$. Hence
$\LT_s(w,1_P)=\langle w,1_P\rangle_{\mathrm{LV}}$, which equals
$\tr_A(1_P\circ w\mid P)=\tr_A(w\mid P)$ by the point normalization
[prop-trf-pairing-point-normalization].
