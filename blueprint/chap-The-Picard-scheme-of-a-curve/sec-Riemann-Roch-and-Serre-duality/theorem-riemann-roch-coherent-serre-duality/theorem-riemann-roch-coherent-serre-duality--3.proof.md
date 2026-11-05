+++
kind = "proof"
of = "theorem-riemann-roch-coherent-serre-duality--3"
order = 1525003
uses = ["theorem-riemann-roch-coherent-serre-duality--2"]
+++
Apply [theorem-riemann-roch-coherent-serre-duality--2] to
$\mathcal O_C$ in both degrees. Taking dimensions gives
$h^0(C,\omega_{C/k})=g$ and
$h^1(C,\omega_{C/k})=h^0(C,\mathcal O_C)=1$.
The canonical sheaf is invertible, so cohomology vanishes above degree
one. Thus the definition of degree gives

$$
\deg\omega_{C/k}
=\chi(C,\omega_{C/k})-\chi(C,\mathcal O_C)
=(g-1)-(1-g)=2g-2.
$$
