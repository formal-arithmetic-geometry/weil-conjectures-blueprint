+++
kind = "proof"
of = "det-cor-affine-space-rational-induction"
+++
Induction on $d$, the case $d=0$ being trivial. Write
$p=p_{d-1}\circ\pi$ with $\pi:\mathbf A^d_V=\mathbf A^1_{\mathbf A^{d-1}_V}\to\mathbf A^{d-1}_V$
the projection forgetting the last coordinate and
$p_{d-1}:\mathbf A^{d-1}_V\to V$. By compatibility of exceptional inverse
images with composition ([sk-lem-sf-mate]),
$p^!\simeq\pi^!p_{d-1}^!$. By [det-cor-affine-space-rational-line] applied over
the base $\mathbf A^{d-1}_V$, $\pi^!\simeq\pi^*(1)[2]$, and by induction
$p_{d-1}^!\simeq p_{d-1}^*(d-1)[2d-2]$. Since pullback commutes with Tate
twists and shifts,
$p^!\simeq\pi^*p_{d-1}^*(d-1)[2d-2](1)[2]=p^*(d)[2d]$.

For the preservation, let $K\in\Dbc(V,\Lambda)$ with a finite stratification
on whose strata the cohomology sheaves of $K$ are lisse. The preimages of
the strata form a finite stratification of $\mathbf A^d_V$, and since $p^*$ is
exact, $\mathcal H^q(p^*K)=p^*\mathcal H^q(K)$ is lisse on each preimage
stratum. The Tate twist is tensoring with the invertible lisse sheaf
$\Lambda(d)$, which keeps lisse sheaves lisse, and the shift preserves
boundedness. So $p^*K(d)[2d]\in\Dbc(\mathbf A^d_V,\Lambda)$.
