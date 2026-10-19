+++
id = "sk-def-kernel"
kind = "definition"
title = "The Fourier kernel and integrand"
order = 3034
uses = ["sk-def-as", "sk-def-fourier-set"]
tags = ["sketch"]
+++
Let $\Lambda$ be a finite commutative ring in which $p$ is invertible, or an
admissible condensed coefficient ring $\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$
of [sk-def-fourier-set]. Let $\pi:V\to S$ and $\pi':V'\to S$ be morphisms of
schemes with $V\times_SV'$ of characteristic $p$, let
$b\in\Gamma(V\times_SV',\mathcal O)$ (the pairing) and let
$\Psi:\Fp\to\Lambda(*)^\times$ be an additive character. The *Fourier
kernel* is the Artin–Schreier sheaf (for $k=\Fp$) of $b$,

$$
\mathcal K_\psi:=\mathcal L_{\Psi,b}=b^*\mathcal L_\Psi ,
$$

$b$ being viewed as a morphism $V\times_SV'\to\Aone_{\Fp}$; see [sk-def-as].
For condensed $\Lambda$ it is a $\Lambda_{V\times_SV'}$-module on the
pro-étale site of $V\times_SV'$, with a finite constant local model of rank
one. For finite $\Lambda$ it may equally be read on the small étale site. In
the application $V=V_0\to S=S_0$ is a vector bundle of rank $r$,
$V'=V_0^\vee$, and $b(x,\xi)=\langle x,\xi\rangle$ is the evaluation
pairing; on $\Aone$ ($r=1$, $S_0=\Spec k_0$) this is
$\mathcal K_\psi=\mathcal L_{\psi(x\xi)}$.
