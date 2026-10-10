+++
kind  = "proof"
of    = "sk-prop-first-formula"
+++
All sheaves here are $E$-sheaves: $\mu_p\subset E$ by [sk-def-fourier-set],
so $\mathcal L_{\psi,f}$ and $\mathcal K_\psi$ are lisse $E$-sheaves of rank
one, and the cohomology computations of [sk-lem-as-properties], stated
there with $\Qlb$-coefficients, hold verbatim at the $E$-stage because
$-\otimes_E\Qlb$ is exact, commutes with $R\Gamma$ and $R\Gamma_c$ on $\Dbc$,
and detects vanishing and dimension. For $K=\underline{E}$, P3 gives the
stalk at a geometric point $\bar\xi:\Spec\Omega\to V^\vee$ as
$H^*_c(V_{\bar\xi},\mathcal L_{\psi(x\xi)})[1]$ with
$V_{\bar\xi}\cong\Aone_\Omega$ (for $\Omega\supsetneq\bar k$ the computation
below is the same over $\Omega$, the cohomology being invariant under
extension of algebraically closed fields). For $\xi=0$ the integrand is
constant and $R\Gamma_c(\Aone,\underline{E})\cong E(-1)[-2]$: the degreewise
duality of [sk-thm-derived-duality] at the field stage $\Lambda=E$ on the
smooth, non-proper curve $\Aone$
makes $H^i_c(\Aone,\underline{E})$ dual to $H^{2-i}(\Aone,E(1))$, which is
$E(1)$ in degree $0$ and zero otherwise ([sk-lem-as-properties], the
$\chi=0$ component), and [sk-thm-frobenius] gives the Frobenius action
$q$ on $H^2_c$; for $\xi\neq0$ the integrand is $\mathcal L_{\psi(x\xi)}$ with
$\xi\neq0$, whose dual $\mathcal L_{\psi(-x\xi)}$ has vanishing cohomology by
[sk-lem-as-properties], hence whose compactly supported cohomology vanishes
by the same duality. So the
transform has a single nonzero stalk, at the origin, one-dimensional in
degree $+1$ (the class of $H^2_c$, shifted by the $[1]$ of the definition)
and twisted by $(-1)$; this is $\delta_0(-1)[-1]$, whose only cohomology
sheaf sits in degree $1$. For $K=\delta_0$ the support of $p_1^*\delta_0$ is
$\{0\}\times V^\vee$, on which $p_2$ is an isomorphism onto $V^\vee$, and the
kernel restricted to it is $\mathcal L_{\psi(0)}$, the $\chi=0$ component of
[sk-lem-as-properties], i.e. the constant sheaf $\underline{E}$; the
compact-support direct
image is therefore $\underline{E}$, and the shift gives $\underline{E}[1]$.
