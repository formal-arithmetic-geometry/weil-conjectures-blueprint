+++
kind = "proof"
of = "sk-prop-tf-transport-integral"
uses = ["sk-lem-finite", "sk-prop-scalar-six", "sk-thm-tf-coefficient-morphism-formula", "sk-p-trace"]
+++
Both sides reduce modulo $\pi_E^n$ to the two sides of
the finite formula, and an element of $\mathcal O_E$ that vanishes
modulo every $\pi_E^n$ is zero.
By Lemma [sk-lem-finite], $R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)$ and the
geometric stalks are perfect complexes.
Proposition [sk-prop-scalar-six] provides canonical isomorphisms

$$
\begin{aligned}
R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\pi_E^n
&\simeq R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K_n),\\
K_{\bar y}\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\pi_E^n&\simeq(K_n)_{\bar y}.
\end{aligned}
$$

They carry the reductions of the integral operators to the operators
of $\bar\theta_n$, because extension of scalars commutes with the
pullbacks, with the units defining the endomorphisms $T_{c_m}$, and with
composition, and hence with the iterates $\theta_m$. Since $K_n\in D^b_{\mathrm{ctf}}(X,\mathcal O_E/\pi_E^n)$,
Theorem [sk-thm-tf-coefficient-morphism-formula] applies for every $n$.

To compare the two sides, we represent each of the two integral complexes by
a bounded complex $P^\bullet$ of finite projective
$\mathcal O_E$-modules and its endomorphism by a chain map
$v^\bullet$. Proposition [sk-p-trace] computes its trace as

$$
\operatorname{tr}_{\mathcal O_E}(v)
=\sum_i(-1)^i\operatorname{Tr}(v^i\mid P^i),
$$

and since each $P^i$ is finite projective, the reduction of this
expression modulo $\pi_E^n$ is the trace on
$P^\bullet\otimes_{\mathcal O_E}\mathcal O_E/\pi_E^n$. Thus the
reduction of each side of (13.1) is the corresponding
side of the finite formula for $(K_n,\bar\theta_n)$. Hence the
difference of the two sides of (13.1) lies in
$\pi_E^n\mathcal O_E$ for every $n$. Since the map
$\mathcal O_E\hookrightarrow\varprojlim_n\mathcal O_E/\pi_E^n$ is
injective, the difference is zero.
