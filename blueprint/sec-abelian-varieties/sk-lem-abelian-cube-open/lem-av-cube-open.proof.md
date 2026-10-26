+++
kind  = "proof"
of    = "lem-av-cube-open"
+++
Replace $\mathcal M,\mathcal N$ by $\mathcal L=\mathcal M\otimes\mathcal N^\vee$ and
$\mathcal O$. By [lem-av-seesaw-criterion], triviality on the fibre over $\varphi$
is triviality on the fibre over the residue field $\kappa(t)$ of its image $t$, since
the dimensions of $H^0$ on the fibres do not change under field extension. Now apply
the argument of [sk-lem-abelian-cube-open] at $t$, with $P=X$, $Q=Y$ and
$T$ an affine open neighbourhood of $t$: it produces a section of $\mathcal L$ over
$X\times Y\times U$ that generates $\mathcal L$ there, for an open $U\ni t$. The key
input is that restriction
$H^1(X_t\times Y_t,\mathcal O)\to H^1(X_t,\mathcal O)\oplus H^1(Y_t,\mathcal O)$ to the two
slices is an isomorphism (Künneth, Stacks [0BED](https://stacks.math.columbia.edu/tag/0BED)).
The second statement is the case $F=k$, $\varphi=z$: the fibre over $z$ is the slice
$X\times Y\times z$.
