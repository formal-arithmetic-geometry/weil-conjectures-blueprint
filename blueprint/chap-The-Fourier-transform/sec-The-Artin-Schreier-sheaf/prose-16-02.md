+++
id = "prose-16-02"
kind = "hidden"
title = "The Artin–Schreier sheaf (1)"
order = 1216
+++
The kernel of the transform is a lisse sheaf whose trace function is
the additive character $\psi$, just as $\psi(xy)$ is the kernel of the
discrete transform. It is cut out of the Artin–Schreier cover of the
line as an eigenspace of the translations. This cover is Galois with
group the additive group $\mathbf F_p$, acting by $u\mapsto u+a$. Let
$u^p-u=x$ with $x\in\mathbf F_{q^n}$. Raising to the powers
$p,p^2,\ldots$ and adding gives $u^{q^n}=u+\operatorname{Tr}(x)$. In
other words, Frobenius acts on the fibre over $x$ by the translation
$\operatorname{Tr}(x)\in\mathbf F_p$. A character $\psi_0$ of
$\mathbf F_p$ then turns this translation into the number
$\psi_0(\operatorname{Tr}x)$. Similarly, the Kummer cover $u^{q-1}=x$ of $\mathbf G_m$ produces the multiplicative
characters in the same way.

Besides the sheaf itself (Lemma [lemma-artin-schreier-character-sheaf]), we need the
sheaf version of $\sum_x\psi(x)=0$, namely the vanishing of
$R\Gamma_c(\mathbf A^r,\lambda^*\mathcal L_\psi)$ for a nonzero linear
form $\lambda$ (Lemma [lemma-integral-linear-character]). This is stronger than
the statement on trace functions, since the trace formula only says that the
alternating sum of the traces vanishes over every $\mathbf F_{q^n}$.
Fourier inversion and the stalk computations below, however, need each
cohomology group to vanish. This vanishing comes from the eigenspace
decomposition of the cover: the total space of the cover is again an
affine line, and the translations act trivially on the compactly
supported cohomology of a line. Hence the eigenspace of a nontrivial
character is zero.
