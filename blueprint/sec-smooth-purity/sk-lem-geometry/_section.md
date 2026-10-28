+++
id = "sk-lem-geometry"
kind = "lemma"
title = "Geometry of the deformation of a section"
order = 3289
uses = ["sk-prop-cohsm", "sk-prop-an", "sk-thm-existence"]
lean = ["AlgebraicGeometry.Scheme.Hom.nonempty_deformationToNormalConeData"]
tags = ["sketch"]
+++
In the conventions of [det-def-purity-conv] let $g:V\to B$ be smooth of pure
relative dimension $d$ with closed section $s$, and let $N_s\to B$ be the
normal bundle of $s$ with zero section $0_N$ and projection $\pi_N$. Then:

1. **(1)** *the fibres.* The fibre of $\widetilde g$ over $1$ is
$(g:V\to B,s)$ and the fibre over $0$ is $(\pi_N:N_s\to B,0_N)$; writing
$i_0,i_1:B\to\Aaf^1_B$ for the two sections, base change gives
$Li_1^{*}\mathcal F\simeq\mathcal C(g,s)$ and
$Li_0^{*}\mathcal F\simeq\mathcal C(\pi_N,0_N)$.
1. **(2)** *coordinates.* Since $s$ is a section of a smooth map, there
are étale-locally coordinates $x_1,\dots,x_d$ on $V$ over $B$ in which $s$
is $x_i=0$; on the deformation chart $u_i=x_i/t$, so $\widetilde g$ is smooth
of pure relative dimension $d$.
1. **(3)** *the punctured trivialization.* Over $\mathbf G_{m,B}$ the
deformation space is canonically $V\times_B\mathbf G_{m,B}$ with
$\widetilde s=s\times1$, so base change gives a canonical
$\kappa^{\circ}:j^{*}\mathcal F\xrightarrow{\ \sim\ }j^{*}a^{*}\mathcal C(g,s)$,
where $a:\Aaf^1_B\to B$.
1. **(4)** *the standard pair.* For $(\Aaf^d_B\to B,0)$ the deformation
space is $\Aaf^d_B\times_B\Aaf^1_B$ with $x_k=tu_k$, the family object is
$a^{*}0^{*}\omega_{\Aaf^d_B/B}$, and $0^{*}\omega_{\Aaf^d_B/B}=\Lambda(d)[2d]$
by the purity isomorphism of [sk-prop-an]
($\omega_{\Aaf^d_B/B}\cong\Lambda(d)[2d]$, pulled back along the zero
section).
1. **(5)** *base change.* All of this commutes with base change in $B$
and with étale localization.
