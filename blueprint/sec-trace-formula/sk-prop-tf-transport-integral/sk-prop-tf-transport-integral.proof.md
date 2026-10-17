+++
kind = "proof"
of = "sk-prop-tf-transport-integral"
uses = ["sk-lem-finite", "sk-prop-scalar-six", "sk-thm-tf-coefficient-morphism-formula", "sk-p-trace"]
+++
The point-perfectness of [sk-lem-finite] applies to
$R\Gamma_c(X_{\mathrm{pro\acute et}},K)$ and to geometric stalks.
[sk-prop-scalar-six] gives canonical isomorphisms in
$D(\mathcal O_E/\pi_E^n)$

$$
 \begin{aligned}
 R\Gamma_c(X_{\mathrm{pro\acute et}},K)\dt_{\mathcal O_E}\mathcal O_E/\pi_E^n
   &\simeq R\Gamma_c(X_{\mathrm{pro\acute et}},K_n),\\
 K_{\bar y}\dt_{\mathcal O_E}\mathcal O_E/\pi_E^n&\simeq(K_n)_{\bar y}.
 \end{aligned}
$$

They carry the reductions of the integral operators to the operators
of $\bar\theta_n$, because scalar extension commutes with the
pullbacks, with the units defining the global operators, and with
composition, hence with the iterates $\theta_m$. Since $K_n\in\Dctf(X,\mathcal O_E/\pi_E^n)$,
[sk-thm-tf-coefficient-morphism-formula] applies for every $n$.

To compare the two sides, represent either integral point complex by
a bounded complex $P^\bullet$ of finite projective
$\mathcal O_E$-modules and its endomorphism by a chain map
$v^\bullet$. [sk-p-trace] computes its trace as

$$
 \operatorname{tr}_{\mathcal O_E}(v)
   =\sum_i(-1)^i\operatorname{Tr}(v^i\mid P^i),
$$

and reducing this expression gives the trace on
$P^\bullet\otimes_{\mathcal O_E}\mathcal O_E/\pi_E^n$. Hence the
difference of the two sides of (1), a finite sum
since $X_0(\mathbf F_{q^m})$ is finite, vanishes modulo every
$\pi_E^n$, and it vanishes in $\mathcal O_E$ because
$\mathcal O_E\hookrightarrow\varprojlim_n\mathcal O_E/\pi_E^n$ is
injective. A comparison of scalars suffices here, because all
operators come from the single integral morphism $\theta$, whose
reductions form a morphism of normalized towers realizing the
integral operator.

The same argument for a compatible system of Frobenius coefficient
morphisms on a normalized tower is
[thm-trf-integral-adic-coefficient-morphism-trace-formula].
