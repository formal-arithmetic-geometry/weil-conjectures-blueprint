+++
id = "def-fd-kernel"
kind = "definition"
title = "The Fourier kernel and integrand"
order = 2691
lean = ["AlgebraicGeometry.Etale.fourierKernel"]
uses = ["def-fd-artin-schreier-sheaf", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions"]
+++
Let $\Lambda$ be a commutative ring in which the prime $p$ is invertible,
let $\pi:V\to S$ and $\pi':V'\to S$ be morphisms of schemes such that
$V\times_SV'$ has characteristic $p$ (that is, $p=0$ in
$\Gamma(V\times_SV',\mathcal O)$), let
$b\in\Gamma(V\times_SV',\mathcal O)$ be a global function (the
*pairing*), and let $\Psi:(\mathbf F_p,+)\to\Lambda^\times$ be an
additive character. The *Fourier kernel* is the Artin–Schreier sheaf of
[def-fd-artin-schreier-sheaf], for $k=\mathbf F_p$, attached to $b$:

$$
\mathcal K_\psi:=\mathcal L_{\Psi,b}=b^*\mathcal L_\Psi ,
$$

a sheaf of $\Lambda$-modules on the small étale site of $V\times_SV'$,
where $b$ is viewed as a morphism $V\times_SV'\to\mathbf A^1_{\mathbf F_p}$.
In the application, $S=S_0$ is a separated scheme of finite type over
$k_0$ (conventions of [def-weil-pbc-scheme-conventions]), $V=V_0\to S_0$
is a vector bundle of rank $r$, $V'=V_0^\vee$ is its dual, and
$b(x,\xi)=\langle x,\xi\rangle$ is the evaluation pairing; on the affine
line over a field this is the sheaf $\mathcal L_{\psi(x\xi)}$.
