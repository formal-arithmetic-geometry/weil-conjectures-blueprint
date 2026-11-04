+++
kind = "proof"
of = "corollary-serre-duality-field-extension"
order = 1522
+++
We factor the duality on $C$ through a finite map to $\mathbf P^1_k$,
where the trace is an explicit residue, and check that each step is
compatible with extension of scalars.

A nonconstant rational function on $C$ extends to a finite map
$\phi:C\to\mathbf P^1_k$, which is flat because $\phi_*\mathcal O_C$ is
torsion free over the discrete valuation rings of $\mathbf P^1_k$. We
may construct the duality on $C$ as duality for $\phi$, given by the
dual of the finite locally free module $\phi_*\mathcal L$, followed by
duality on $\mathbf P^1_k$, whose trace $H^1(\mathbf P^1_k,\omega)\to k$
takes the coefficient of $t^{-1}dt$ in a Čech cocycle for the
standard cover. Both steps commute with extension of scalars, hence so
does the resulting pairing. For $\mathcal L=\mathcal O_C$ the duality gives
$\dim_kH^0(C,\omega_{C/k})=\dim_kH^1(C,\mathcal O_C)=g$. Flat base
change shows that $g$ is unchanged by field extension.
