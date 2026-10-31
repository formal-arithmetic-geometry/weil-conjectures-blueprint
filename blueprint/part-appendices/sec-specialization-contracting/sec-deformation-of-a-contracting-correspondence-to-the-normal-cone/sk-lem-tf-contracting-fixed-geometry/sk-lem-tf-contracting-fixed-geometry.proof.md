+++
kind = "proof"
of = "sk-lem-tf-contracting-fixed-geometry"
uses = ["sk-lem-tf-contracting-cone-geometry"]
+++
Let $I_F=d^{-1}(I)\mathcal O_F$. Since the two legs agree on $F$,
restricting $I_2^n\subset I_1^{n+1}$ to $F$ gives
$I_F^n\subset I_F^{n+1}$, and the reverse inclusion always holds.
Consequently, the coherent ideal $M=I_F^n$ satisfies $M=I_FM$. At a point of
$V(I_F)$, Nakayama's lemma shows that $M=0$ in the local ring, and hence on a
neighbourhood of the point, and at a point outside $V(I_F)$ we have
$M=\mathcal O_F$. Thus $V(I_F)$ is open and closed. It is nonempty by
assumption, and hence $V(I_F)=F$ since $F$ is connected. It follows that
$I_F^n=0$, and this proves the first assertion.

The closed immersion $F\hookrightarrow C$ induces a surjection
of deformation algebras

$$
\mathcal O_{C_T}[I_1/t]\twoheadrightarrow
\mathcal O_{F_T}[I_F/t],
$$

because $I_F^r$ is the image of $I_1^r$ for every $r$. The induced
closed immersion
$\mathcal D_{d^{-1}(Z)}F\hookrightarrow\mathcal D_{Z'}C$
factors through $\widetilde F$, since its two composites to
$\mathcal D_ZX$ are equal. Since $I_F$ is nilpotent, each generator
$h/t$ is nilpotent, and hence the reduction of
$\mathcal D_{d^{-1}(Z)}F$ is $(F_T)_{\mathrm{red}}$.

It remains to show that $\widetilde F$ has no further points. On the
generic fibre, the deformed correspondence is $c$ itself, and hence the
generic fibre of $\widetilde F$ is that of $F_T$. Let $x$ be a
point of the special fibre of $\widetilde F$. By
Lemma [sk-lem-tf-contracting-cone-geometry](2), $\gamma_2(x)$ lies in
the zero section, and hence so does $\gamma_1(x)=\gamma_2(x)$. By
Lemma [sk-lem-tf-contracting-cone-geometry](1) the point $x$ lies on the
zero section $Z'\subset N_{Z'}C$. On $Z'$ the two maps are the restrictions
of $c_1$ and $c_2$, and hence their equalizer is $F\cap Z'$, whose
underlying space is $F$ by the first assertion. Therefore every fixed
point in the special fibre lies in the closed subscheme above, and the
closed immersion of reduced schemes is surjective. Its ideal has zero
radical and is therefore zero, so that the immersion is an isomorphism.
