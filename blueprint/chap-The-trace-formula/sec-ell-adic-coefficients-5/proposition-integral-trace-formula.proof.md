+++
kind = "proof"
of = "proposition-integral-trace-formula"
order = 1012
+++
We show that both sides reduce modulo $\pi_E^n$ to the two sides of
the finite formula, by identifying the reductions of the complexes, of the
operators and of the traces. This suffices, since an element of
$\mathcal O_E$ that vanishes modulo every $\pi_E^n$ is zero.

*Complexes and operators.* By Lemma [lemma-perfect-complexes-geometric-point],
$R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)$ and the geometric stalks are perfect, and
Proposition [proposition-six-operations-change-coefficients] provides canonical isomorphisms

$$
\begin{aligned}
R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\pi_E^n
&\simeq R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K_n),\\
K_{\bar y}\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\pi_E^n&\simeq(K_n)_{\bar y}.
\end{aligned}
$$

Under these isomorphisms the reductions of the integral operators are the operators
of $\bar\theta_n$, because extension of scalars commutes with the
pullbacks, with the units defining the endomorphisms $T_{c_m}$, and with
composition, and hence with the iterates $\theta_m$. Moreover
Theorem [theorem-trace-formula-frobenius-correspondence] applies for every $n$,
because $K_n\in D^b_{\mathrm{ctf}}(X,\mathcal O_E/\pi_E^n)$.

*Traces.* Represent each of the two integral complexes by
a bounded complex $P^\bullet$ of finite projective
$\mathcal O_E$-modules and its endomorphism by a chain map
$v^\bullet$. By Proposition [proposition-properties-trace] its trace is

$$
\operatorname{tr}_{\mathcal O_E}(v)
=\sum_i(-1)^i\operatorname{Tr}(v^i\mid P^i).
$$

The reduction of this
expression modulo $\pi_E^n$ is the trace on
$P^\bullet\otimes_{\mathcal O_E}\mathcal O_E/\pi_E^n$, as each $P^i$ is finite projective.

*Conclusion.* The
reduction of each side of (12.1) is therefore the corresponding
side of the finite formula for $(K_n,\bar\theta_n)$. Hence the
difference of the two sides lies in
$\pi_E^n\mathcal O_E$ for every $n$. It is zero because
$\mathcal O_E\hookrightarrow\varprojlim_n\mathcal O_E/\pi_E^n$ is
injective.
