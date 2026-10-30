+++
id = "prose-18-02"
kind = "hidden"
title = "The additive character sheaf"
order = 714
+++
The kernel of the transform is a lisse sheaf whose trace function is
the additive character $\psi$, just as $\psi(xy)$ is the kernel of the
discrete transform. It is cut out of the Artin–Schreier cover of the
line as an eigenspace of the translations. The reason this cover is the
right one is that it turns the additive group into a Galois group. If
$u^p-u=x$ with $x\in\mathbf F_{q^n}$, then raising to the powers
$p,p^2,\ldots$ and adding gives $u^{q^n}=u+\operatorname{Tr}(x)$, so
Frobenius acts on the fibre over $x$ by the translation
$\operatorname{Tr}(x)\in\mathbf F_p$, and a character of $\mathbf F_p$
turns this translation into the number $\psi_0(\operatorname{Tr}x)$. The
Kummer cover $u^{q-1}=x$ of $\mathbf G_m$ produces the multiplicative
characters in the same way.

Besides the sheaf itself (Lemma [sk-lem-as-properties]), we need the
sheaf version of $\sum_x\psi(x)=0$, namely the vanishing of
$R\Gamma_c(\mathbf A^r,\lambda^*\mathcal L_\psi)$ for a nonzero linear
form $\lambda$ (Lemma [sk-lem-wft-character-integral]). It is stronger than
its shadow on trace functions: the trace formula only says that the
alternating sum of the traces vanishes over every $\mathbf F_{q^n}$,
whereas Fourier inversion and the stalk computations below need each
cohomology group to vanish. We obtain it from the eigenspace
decomposition of the cover, whose total space is again an affine line.
