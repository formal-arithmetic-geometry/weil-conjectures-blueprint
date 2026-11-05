+++
kind = "proof"
of = "theorem-riemann-roch-coherent-serre-duality--4"
order = 1525004
uses = ["theorem-riemann-roch-coherent-serre-duality--2", "theorem-riemann-roch-coherent-serre-duality--3"]
+++
By [theorem-riemann-roch-coherent-serre-duality--2], taking dimensions
in Serre duality gives
$h^1(C,\mathcal L)=h^0(C,\mathcal L^{-1}\otimes\omega_{C/k})$.
Additivity of degree, the degree of the dual, and
[theorem-riemann-roch-coherent-serre-duality--3] give

$$
\deg(\mathcal L^{-1}\otimes\omega_{C/k})
=-\deg\mathcal L+2g-2<0.
$$

An invertible sheaf of negative degree has no nonzero global section.
Indeed, $H^0(C,\mathcal O_C)=k$ makes $C$ connected, and smoothness
makes it regular, hence integral. A nonzero section would identify the
sheaf with $\mathcal O_C(D)$ for an effective divisor $D$, whose degree
is $\dim_k\Gamma(D,\mathcal O_D)\geq0$. Applying this to
$\mathcal L^{-1}\otimes\omega_{C/k}$ proves the assertion.
