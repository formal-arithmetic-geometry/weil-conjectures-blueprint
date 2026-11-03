+++
kind  = "proof"
of    = "lem-sfb-symmetric-bimod-tensor"
+++
Let $\pi\colon P\otimes Q\to P\otimes_AQ$ be the projection. Since $-\otimes A$ preserves
coequalizers, $\pi\otimes A$ is an epimorphism. So it suffices to compare the right action
of $P\otimes_AQ$ with the braiding followed by its left action after precomposing with
$\pi\otimes A$.

On $(P\otimes Q)\otimes A$ the right action is $\pi\circ(P\otimes\rho_Q)\alpha$. Since $Q$
is symmetric, $\rho_Q=\gamma_Q\beta_{Q,A}$. By the coequalizer relation,
$\pi\circ(P\otimes\gamma_Q)\alpha=\pi\circ(\rho_P\otimes Q)$. Since $P$ is symmetric,
$\rho_P=\gamma_P\beta_{P,A}$. Together:
$$
\pi(P\otimes\rho_Q)\alpha
=\pi(\gamma_P\otimes Q)(\beta_{P,A}\otimes Q)\alpha^{-1}(P\otimes\beta_{Q,A})\alpha .
$$
By the hexagon identity, $(\beta_{P,A}\otimes Q)\alpha^{-1}(P\otimes\beta_{Q,A})\alpha$ is
$\alpha^{-1}\beta_{P\otimes Q,A}$. So the right action is
$\pi(\gamma_P\otimes Q)\alpha^{-1}\beta_{P\otimes Q,A}$. By naturality of $\beta$, this is
the left action of $P\otimes_AQ$ precomposed with $\beta_{P\otimes_AQ,A}(\pi\otimes A)$.
