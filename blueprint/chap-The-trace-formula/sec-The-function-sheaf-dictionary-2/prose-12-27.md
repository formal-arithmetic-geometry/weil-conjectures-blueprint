+++
id = "prose-12-27"
kind = "hidden"
title = "The function–sheaf dictionary (4)"
order = 1031
+++
The Fourier transform of Section [chap-The-Fourier-transform] is one more entry, and
the proposition shows why it corresponds to the discrete transform. Let
$p_1,p_2$ be the projections of $\mathbf A^1\times\mathbf A^1$, let
$\mu(x,y)=xy$, let $\psi:\mathbf F_q\to E^\times$ be a nontrivial additive
character, and let $\mathcal K_\psi=\mu^*\mathcal L_\psi$, where
$\mathcal L_\psi$ is the Artin–Schreier sheaf of
Lemma [lemma-artin-schreier-character-sheaf] (proved in
Section [chap-The-Fourier-transform] below). Here $\psi$ is a character, not a
Frobenius correspondence. With this kernel the transform is $\operatorname{FT}_\psi K=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[1]$. For
$y\in\mathbf F_{q^m}$ we compute

$$
\begin{aligned}
t_{\operatorname{FT}_\psi K,m}(y)
&=-\,t_{Rp_{2!}(p_1^*K\otimes\mathcal K_\psi),m}(y)
&&\text{(shift)}\\
&=-\sum_{x\in\mathbf F_{q^m}}t_{p_1^*K\otimes\mathcal K_\psi,m}(x,y)
&&\text{by (3)}\\
&=-\sum_{x\in\mathbf F_{q^m}}t_{p_1^*K,m}(x,y)\,t_{\mu^*\mathcal L_\psi,m}(x,y)
&&\text{by (2)}\\
&=-\sum_{x\in\mathbf F_{q^m}}t_{K,m}(x)\,
\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^m}/\mathbf F_q}(xy)\bigr)
&&\text{by (1) and Lemma~16.1.1.}
\end{aligned}
$$

The first equality holds because a shift changes the sign of a trace, by the
chain formula of Proposition [proposition-properties-trace]. Each of the
other three steps is one operation in the formula
$\hat t(y)=\sum_xt(x)\psi(xy)$: pull $t$ back to the plane, multiply by the
kernel, and sum over the fibres of $p_2$.
