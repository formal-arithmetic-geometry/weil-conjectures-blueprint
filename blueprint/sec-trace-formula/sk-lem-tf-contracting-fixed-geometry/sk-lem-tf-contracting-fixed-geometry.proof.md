+++
kind = "proof"
of = "sk-lem-tf-contracting-fixed-geometry"
uses = ["sk-lem-tf-contracting-cone-geometry"]
+++
Let $H=a^\cdot I\,\mathcal O_F$. Since the two legs agree on $F$,
restricting $L^n\subset J^{n+1}$ to $F$ gives
$H^n\subset H^{n+1}$; the reverse inclusion always holds.
Consequently the coherent ideal $M=H^n$ satisfies $M=HM$. At a point of
$V(H)$, Nakayama's lemma gives $M=0$ in the local ring, hence on a
neighbourhood of the point; at a point outside $V(H)$,
$M=\mathcal O_F$. So $V(H)$ is open and closed. It is nonempty by
assumption, so connectedness gives $V(H)=F$, whence $H^n=0$. This
proves the first assertion.

The closed immersion $F\hookrightarrow C$ induces a surjection
of deformation algebras

$$
 \mathcal O_{C_T}[J/t]\twoheadrightarrow
 \mathcal O_{F_T}[H/t],
$$

because $H^r$ is the image of $J^r$ for every $r$. The induced
closed immersion
$\mathcal D_{a^{-1}(Z)}F\hookrightarrow\mathcal D_EC$
lands in $\widetilde F$, since its two composites to
$\mathcal D_ZX$ are equal. As $H$ is nilpotent, each generator
$h/t$ is nilpotent, so the reduction of $\mathcal D_{a^{-1}(Z)}F$ is
$(F_T)_{\mathrm{red}}$.

It remains to show that $\widetilde F$ has no further points. On the
generic fibre the deformed correspondence is $c$ itself, so the
generic fibre of $\widetilde F$ is that of $F_T$. Let $x$ be a
point of the special fibre of $\widetilde F$. By
Lemma [sk-lem-tf-contracting-cone-geometry] (2), $\gamma_2(x)$ lies in
the zero section, hence so does $\gamma_1(x)=\gamma_2(x)$, and
Lemma [sk-lem-tf-contracting-cone-geometry] (1) puts $x$ on the zero
section $E\subset N_EC$. On $E$ the two maps are the restrictions
of $c_1$ and $c_2$, so their equalizer is $F\cap E$, whose underlying
space is $F$ by the first assertion. Every special fixed point
therefore lies in the closed subscheme above, and the closed
immersion of reduced schemes is surjective; its ideal has zero radical, hence is zero, and
the immersion is an isomorphism.
