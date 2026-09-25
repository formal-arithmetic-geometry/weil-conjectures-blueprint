+++
id = "sk-def-kernel"
kind = "section"
title = "The Fourier kernel and integrand"
order = 2886
uses = ["sk-def-as", "sk-def-fourier-set"]
+++
*Definition (sketch).*

Let $V_0\to S_0$ be a vector bundle of rank $r$ with dual $V_0^\vee$ and
pairing $b:V_0\times_{S_0}V_0^\vee\to S_0$. The *Fourier kernel* is

$$
\mathcal K_\psi:=b^*\mathcal L_{\psi(b(x,\xi))}
$$

on $V_0\times_{S_0}V_0^\vee$; for $K\in\Dbc(V,E)$ the *Fourier
integrand* is
$\mathcal F_\psi(K)=p_{13,*}\bigl(p_{12}^*K\otimes^L\mathcal K_\psi\bigr)$ on
the triple product. On $\Aone$ ($r=1$, $S_0=\Spec k_0$) the pairing is the
product $x\xi$. (Blueprint def:fd-kernel.)

Uses: [sk-def-as], [sk-def-fourier-set]
