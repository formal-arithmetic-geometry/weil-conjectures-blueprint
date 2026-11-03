+++
kind = "proof"
of = "det-tf-fixed-deformation-points"
uses = ["det-tf-fixed-deformation-immersion", "det-tf-fixed-ideal-nilpotent", "det-tf-cone-zero-sections"]
+++
It suffices to show that the immersion is surjective: a surjective closed immersion of
reduced schemes has an ideal with zero radical, hence zero ideal.

On the generic fibre the deformed correspondence is $c$ itself, so the generic fibre of
$\widetilde F$ is that of $F_T$. Let $x$ be a point of the special fibre of $\widetilde F$,
so $x\in N_EC$ with $\gamma_1(x)=\gamma_2(x)$. By [det-tf-cone-zero-sections] (2),
$\gamma_2(x)$ lies in the zero section $Z\subset N_ZX$; hence so does $\gamma_1(x)$, and
[det-tf-cone-zero-sections] (1) puts $x$ on the zero section $E\subset N_EC$. On $E$ the maps
$\gamma_1,\gamma_2$ are the restrictions of $c_1$ and $c_2$, so their equalizer is $F\cap E$,
whose underlying space is that of $F$ by [det-tf-fixed-ideal-nilpotent]. So every point of
the special fibre of $\widetilde F$ lies in the image of the special fibre of
$\mathcal D_{a^{-1}(Z)}F$, and the immersion is surjective.
