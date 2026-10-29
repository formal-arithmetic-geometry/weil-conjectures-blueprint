+++
kind = "proof"
of = "prop-pe-continuous-etale-cohomology"
+++
*Degree zero.* $\operatorname{Hom}(\Delta\mathbf Z,(F_{n,\Et}))=\varprojlim_n
\Gamma(X_{\Et},F_{n,\Et})$, and $\Gamma(X_{\Et},F_{n,\Et})=\Gamma(X_{\Proet},F_n)$ by
the bounded-below site comparison ([thm-weil-pbc-site-comparison], with
$\Lambda=\mathbf Z$), which gives $R\Gamma(X_{\Et},G)\simeq R\Gamma(X_{\Proet},\nu_X^*G)$
for every abelian étale sheaf $G$; so
both sides are $\varprojlim_n\Gamma(X_{\Proet},F_n)=\Gamma(X_{\Proet},\varprojlim_nF_n)$,
naturally in the system.

*Injective systems.* Evaluation at $n$ has the exact left adjoint sending a sheaf
$G$ to the system with $G$ in levels $m\leq n$, identity transitions among them, and
$0$ in levels $m>n$; hence an injective system $(I_n)$ has injective levels, and
its transition maps are split epimorphisms. For such a system,
$H^i_{\mathrm{cont}}(X,(I_n))=0$ for $i>0$. On the pro-étale side,
[det-pe-continuous-cohomology-limit] gives
$R\Gamma(X_{\Proet},\varprojlim_n\nu_X^*I_n)\simeq
R\varprojlim_nR\Gamma(X_{\Proet},\nu_X^*I_n)$. Each $\nu_X^*I_n$ is acyclic by the
same comparison, $I_n$ being injective, and the groups $\Gamma(X_{\Proet},\nu_X^*I_n)$ form a
system with surjective transitions, whose derived limit is its limit. So
$\varprojlim_n\nu_X^*I_n$ is acyclic as well.

*Dimension shifting.* Embed $(F_{n,\Et})$ into an injective system $(I_n)$ with
quotient $(Q_n)$; the transitions of $(Q_n)$ are epimorphisms, being quotients of
split epimorphisms. Since $\nu_X^*$ is exact, $0\to F_n\to\nu_X^*I_n\to\nu_X^*Q_n\to0$
is exact for each $n$, and since $(F_n)$ has epimorphic transitions, the limit
sequence $0\to\varprojlim F_n\to\varprojlim\nu_X^*I_n\to\varprojlim\nu_X^*Q_n\to0$ is
exact ([det-pe-continuous-cohomology-limit]). Comparing the two long exact
sequences, whose middle terms vanish in positive degrees, the degree-zero
identification gives
$H^1_{\mathrm{cont}}(X,(F_{n,\Et}))\cong H^1(X_{\Proet},\varprojlim_nF_n)$ as cokernels
of the same map, and
$H^{i+1}_{\mathrm{cont}}(X,(F_{n,\Et}))\cong H^i_{\mathrm{cont}}(X,(Q_n))\cong
H^i(X_{\Proet},\varprojlim_n\nu_X^*Q_n)\cong H^{i+1}(X_{\Proet},\varprojlim_nF_n)$ for
$i\geq1$, by induction on $i$ applied to the system $(Q_n)$.
