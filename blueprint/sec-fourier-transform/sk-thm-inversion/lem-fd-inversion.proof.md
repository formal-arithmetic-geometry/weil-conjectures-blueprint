+++
kind  = "proof"
of    = "lem-fd-inversion"
+++
By [lem-fd-kernel-composition] the composite
$\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi$ is the kernel
transform with kernel $\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi$ and shift
$[2r]$, and by [lem-fd-convolution-kernel] that kernel is
$\Delta_*\overline{\mathbf Q}_\ell(-r)[-2r]$. The kernel transform with
kernel $\Delta_*\overline{\mathbf Q}_\ell$ is the identity functor:
$\Delta$ is a closed immersion, so the projection formula of
[prop-functor-package] gives
$s_1^*K\otimes^L\Delta_*\overline{\mathbf Q}_\ell\cong\Delta_*K$, and
$s_{2,!}\Delta_*={(s_2)}_\Delta{}_!=\operatorname{id}_V$ because
$s_2\circ\Delta=\operatorname{id}_V$. Hence

$$
\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)
\cong K(-r)[-2r][2r]=K(-r),
$$

the twist being that of [lem-fd-convolution-kernel] and the two shifts
cancelling. For the second formula the same computation with the
anti-diagonal kernel of [lem-fd-convolution-kernel] identifies
$\operatorname{FT}_\psi\operatorname{FT}_\psi$ with the pullback along
$\iota'$ of the identity transform, whence ${\iota'}^*K(-r)$.
