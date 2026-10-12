+++
id = "sk-def-kernel"
kind = "definition"
title = "The Fourier kernel and integrand"
order = 3030
lean = ["AlgebraicGeometry.Etale.fourierKernel"]
uses = ["sk-def-as", "sk-def-fourier-set"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring in which $p$ is invertible, let
$\pi:V\to S$ and $\pi':V'\to S$ be morphisms of schemes with
$V\times_SV'$ of characteristic $p$, let
$b\in\Gamma(V\times_SV',\mathcal O)$ (the pairing) and let
$\Psi:\Fp\to\Lambda^\times$ be an additive character. The *Fourier
kernel* is the Artin–Schreier sheaf (for $k=\Fp$) of $b$,

$$
\mathcal K_\psi:=\mathcal L_{\Psi,b}=b^*\mathcal L_\Psi
$$

on the small étale site of $V\times_SV'$, $b$ being viewed as a morphism
$V\times_SV'\to\Aone_{\Fp}$; see [sk-def-as]. In the application
$V=V_0\to S=S_0$ is a vector bundle of rank $r$, $V'=V_0^\vee$, and
$b(x,\xi)=\langle x,\xi\rangle$ is the evaluation pairing; on $\Aone$
($r=1$, $S_0=\Spec k_0$) this is $\mathcal K_\psi=\mathcal L_{\psi(x\xi)}$.
