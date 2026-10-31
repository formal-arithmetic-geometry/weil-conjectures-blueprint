+++
id = "sk-ex-ex-gauss-sum"
kind = "remark"
title = "A Gauss sum over $\\mathbf F_3$"
order = 716
tags = ["sketch", "latex:example"]
+++
Take $q=3$, a primitive cube root of unity $\omega\in \overline{\mathbf Q}_\ell$ and
$\psi(x)=\omega^x$ on $\mathbf F_3$. Pull $\mathcal L_\psi$ back along
$h:\mathbf A^1\to\mathbf A^1$, $x\mapsto x^2$. By the lemma, the trace
of Frobenius on the stalk of $h^*\mathcal L_\psi$ at $x\in\mathbf F_3$ is
$\psi(x^2)$, so the trace formula gives

$$
\sum_r(-1)^r\operatorname{Tr}\bigl(F\mid H^r_c(\mathbf A^1_k,h^*\mathcal L_\psi)\bigr)
=\sum_{x\in\mathbf F_3}\omega^{x^2}=1+2\omega=\sqrt{-3} .
$$

The sheaf $h^*\mathcal L_\psi$ is lisse of rank one and geometrically
nontrivial, since the Artin–Schreier cover $u^3-u=x^2$ is connected, so its
geometric coinvariants vanish and $H^0_c=H^2_c=0$
(Lemma [sk-l-dl-a1-endpoints]). The sum is therefore
$-\operatorname{Tr}(F\mid H^1_c)$. The Euler characteristic formula of
Grothendieck–Ogg–Shafarevich, which we do not prove, shows that $H^1_c$ is a
line (the Swan conductor at infinity is $2$, so $\chi_c=1-2=-1$). Frobenius
therefore acts on $H^1_c$ by $-\sqrt{-3}$, of absolute value $3^{1/2}$. The
classical fact $|g|=\sqrt q$ for a quadratic Gauss sum $g$ is thus the
statement that this $H^1_c$ is pure of weight one, which is what
Section [sec-deligne-laumon-a1] proves for every such sheaf.
