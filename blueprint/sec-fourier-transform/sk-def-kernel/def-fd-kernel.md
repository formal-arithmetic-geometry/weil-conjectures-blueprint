+++
id = "def-fd-kernel"
kind = "definition"
title = "The Fourier kernel and integrand"
order = 3035
lean = ["AlgebraicGeometry.Etale.fourierKernel"]
uses = ["def-fd-artin-schreier-sheaf", "def-weil-pbc-scheme-conventions", "sk-def-sf-setting", "sk-def-sfb-module-pushforward-pullback"]
+++
Let $\Lambda$ be a coefficient ring in which the prime $p$ is invertible:
either a finite commutative ring, or an admissible coefficient ring
$\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$ of [sk-def-sf-setting], regarded as a
condensed ring. Let $\pi:V\to S$ and $\pi':V'\to S$ be morphisms of schemes
such that $V\times_SV'$ has characteristic $p$ (that is, $p=0$ in
$\Gamma(V\times_SV',\mathcal O)$), let
$b\in\Gamma(V\times_SV',\mathcal O)$ be a global function (the
*pairing*), and let $\Psi:(\mathbf F_p,+)\to\Lambda(*)^\times$ be an
additive character. The *Fourier kernel* is the Artin–Schreier sheaf of
[def-fd-artin-schreier-sheaf], for $k=\mathbf F_p$, attached to $b$:

$$
\mathcal K_\psi:=\mathcal L_{\Psi,b}=b^*\mathcal L_\Psi ,
$$

where $b$ is viewed as a morphism $V\times_SV'\to\mathbf A^1_{\mathbf F_p}$.

- For an admissible condensed $\Lambda$, $\mathcal K_\psi$ is the
  $\Lambda_{V\times_SV'}$-module on $(V\times_SV')_{\mathrm{proét}}$ obtained
  by pulling back the pro-étale Artin–Schreier sheaf of
  [def-fd-artin-schreier-sheaf] along $b$
  ([sk-def-sfb-module-pushforward-pullback]). It is the pushout of the
  Artin–Schreier $\mathbf F_p$-torsor $b^*\mathrm{AS}_p$ along $\Psi$, and it
  has a finite constant local model of rank one. This is the kernel used for
  $\Lambda=\mathcal O_E,E,\Qlb$.
- For a finite ring $\Lambda$ one may equally regard $\mathcal K_\psi$ as a
  sheaf of $\Lambda$-modules on the small étale site of $V\times_SV'$. For
  finite admissible $\Lambda$ its pullback $\nu^*$ is the pro-étale kernel of
  the first item.

In the application, $S=S_0$ is a separated scheme of finite type over
$k_0$ (conventions of [def-weil-pbc-scheme-conventions]), $V=V_0\to S_0$
is a vector bundle of rank $r$, $V'=V_0^\vee$ is its dual, and
$b(x,\xi)=\langle x,\xi\rangle$ is the evaluation pairing; on the affine
line over a field this is the sheaf $\mathcal L_{\psi(x\xi)}$.
