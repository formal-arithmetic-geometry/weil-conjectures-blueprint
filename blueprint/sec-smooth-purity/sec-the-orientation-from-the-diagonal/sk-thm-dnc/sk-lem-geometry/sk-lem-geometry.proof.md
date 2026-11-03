+++
kind  = "proof"
of    = "sk-lem-geometry"
+++
*Rees description.* The blow-up of [det-def-purity-conv] with the
strict transform of the closed fibre deleted is
$\Spec_V\bigl(\bigoplus_{r\in\Z}\mathcal I_s^{\,r}t^{-r}\bigr)$, with
$\mathcal I_s^{\,r}=\mathcal O_V$ for $r\le0$ and $\widetilde g$ induced by
$t$. Inverting $t$ gives $\mathcal O_V[t,t^{-1}]$, which is (3) and the
fibre $V$ over $1$; setting $t=0$ gives
$\bigoplus_{r\ge0}\mathcal I_s^{\,r}/\mathcal I_s^{\,r+1}$, the normal cone,
a vector bundle because a section of a smooth map is a regular immersion.
This is (1), the comparison of fibres being base change for $\omega$
([sk-prop-cohsm] (G12)).

*Coordinates.* A closed section of a smooth map is étale-locally
$x_i=0$ in relative coordinates $x_1,\dots,x_d$ (the relative local
linearization). On the chart $u_i=x_i/t$ the extended Rees algebra is
$\mathcal O[u_1,\dots,u_d,t]/(tu_i-x_i)$, in which each $x_i$ is eliminated,
so the chart is $\Aaf^d\times\Aaf^1$ over the base and $\widetilde g$ is the
last projection; this is (2), and the remaining charts give the same
computation after substituting a generator of the centre. Item (4) is this
computation for the standard pair together with [sk-prop-an], and (5) is
the base-change behaviour of the Rees algebra, of the punctured
trivialization and of the normal cone.
