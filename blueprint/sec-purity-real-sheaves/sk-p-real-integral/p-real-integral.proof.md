+++
kind  = "proof"
of    = "p-real-integral"
+++
By [prop-wf-weil-sheaf-representation-equivalence] the representation admits a model over a finite
$E/\Ql$, whose restriction to the geometric subgroup is continuous by
[lem-wf-weil-fundamental-representation]; a further
finite extension absorbs that choice. Since $\pi_1(U)$ is profinite, hence
compact, $\rho(\pi_1(U))$ is a compact subgroup of $\GL(V)$. The orbit of an
arbitrary $\mathcal O_E$-lattice under a compact subgroup is bounded, so the
$\mathcal O_E$-span $L$ of that orbit is again a lattice; it is stable by
construction and of full rank, whence $L\otimes_{\mathcal O_E}E=V$. Each
$L/\mathfrak m_E^nL$ is a finite set, so the image of $\pi_1(U)$ in its
automorphisms is finite.

*The sheaf $\mathcal L$.* By the finite-coefficient case of
[cor-galois-lisse-representations], the finite continuous $\pi_1(U)$-module
$L/\mathfrak m_E^nL$ is the stalk of a finite locally constant sheaf $\mathcal L_n$ of
$\cO_E/\mathfrak m_E^n$-modules on $U$, with surjective transition maps
$\mathcal L_{n+1}\to\mathcal L_n$. Let $\widetilde U=\varprojlim_iU_i\to U$ be the
pro-finite-étale cover given by the finite étale covers $U_i$ trivializing the
$\mathcal L_n$ (one for each of the finite groups of the statement); it is a
pro-étale cover, and over it
$\mathcal L_n|_{\widetilde U}\simeq(L/\mathfrak m_E^nL)_{\widetilde U}$
compatibly in $n$. Put $\mathcal L=\varprojlim_n\mathcal L_n$ in
$\Sh(U_{\mathrm{proét}})$. Restriction to $\widetilde U$ commutes with limits, so a
choice of basis of $L$ gives
$\mathcal L|_{\widetilde U}\simeq\varprojlim_n(\cO_E/\mathfrak m_E^n)^{\oplus r}_{\widetilde U}
\simeq\cO_{E,\widetilde U}^{\oplus r}$ by the comparison theorem
[sk-prop-sfb-qlbar-colimit-x]. Thus $\mathcal L$ is a lisse $\cO_{E,U}$-module with
stalk $L$ and $\mathcal L/\mathfrak m_E^n\mathcal L\simeq\mathcal L_n$. Its extension of
scalars $\mathcal L\otimes_{\cO_{E,U}}\overline{\mathbf Q}_{\ell,U}$ is a lisse
$\overline{\mathbf Q}_{\ell,U}$-module with geometric representation
$L\otimes_{\cO_E}\Qlb=V$, so it is the sheaf underlying $V|_U$ by
[thm-lisse-qlbar-representations].
