+++
kind  = "proof"
of    = "lem-sfb-profinite-to-proetale-finite-limits"
+++
It suffices to treat the terminal object and fibre products.

*Terminal object.* The one-point set goes to $\Spec LC(*,\Z)=\Spec\Z$, which
is terminal in $(\Spec\Z)_{\mathrm{proét}}$.

*Fibre products.* Let $S_1\to S\leftarrow S_2$ be maps of profinite sets.
Every locally constant function on $S_1\times_SS_2$ factors through a finite
quotient. Every finite quotient of $S_1\times_SS_2$ is dominated by one of
the form $A_1\times_CA_2$, where $A_1\to C\leftarrow A_2$ is a compatible
system of finite quotients of $S_1$, $S$, $S_2$. For finite sets,
$\Z^{A_1}\otimes_{\Z^C}\Z^{A_2}=\Z^{A_1\times_CA_2}$. Passing to the filtered
colimit, which commutes with tensor products, gives
$$
LC(S_1\times_SS_2,\Z)\cong LC(S_1,\Z)\otimes_{LC(S,\Z)}LC(S_2,\Z).
$$
Applying $\Spec$, $u(S_1\times_SS_2)=u(S_1)\times_{u(S)}u(S_2)$. Weakly étale
morphisms are stable under base change and composition, so fibre products in
$(\Spec\Z)_{\mathrm{proét}}$ are computed in schemes.
