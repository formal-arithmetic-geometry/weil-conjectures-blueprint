+++
id = "prose-18-05"
kind = "hidden"
title = "Fourier inversion"
order = 722
+++
Three choices in the definition below come from what the transform has
to do. We integrate with compact supports, $Rp_{2!}$ rather than
$Rp_{2*}$, because proper base change computes the stalks of $Rp_{2!}$
as compactly supported cohomology of the fibres, which puts
$H^1_c(\mathbf A^1,j_*M)$ at the origin, and because the trace formula
holds for $Rp_{2!}$, which turns the transform into the discrete Fourier
transform of trace functions (18.3). The shift $[r]$ is the one
for which the transform preserves the perverse heart: on the line,
$\operatorname{FT}_\psi(E[1])=\delta_0(-1)$, whereas without the shift the
perverse sheaf $E[1]$ would go to $\delta_0(-1)[-1]$, which is not
perverse. And we work with a vector bundle $V\to S$ rather than
the line alone because the proofs move along the base: the stalk formula
is base change to a point of the dual, and Fourier inversion is a
computation on $V\times_SV^\vee\times_SV$ that reduces, fibre by fibre,
to Lemma [sk-lem-wft-character-integral] on $\mathbf A^r$. The two
properties are recorded in Proposition [sk-thm-inversion], and the
heart is preserved by Proposition [sk-p-dl-a1-perverse].

Let $S$ be a $k_0$-scheme of finite type, let $V\to S$ be a vector
bundle of rank $r$, and let $V^\vee$ be its dual bundle. Write
$p_1,p_2$ for the projections of $V\times_SV^\vee$, and set

$$
\mathcal K_\psi=\langle\ ,\ \rangle^*\mathcal L_\psi,
\qquad
\operatorname{FT}_\psi(K)
=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[r].
\tag{18.1}
$$

The kernel $\mathcal K_\psi$ is lisse of rank one, and since the six
operations preserve constructibility, this defines a triangulated
functor $\operatorname{FT}_\psi:\Dbc(V,E)\to\Dbc(V^\vee,E)$, normalized
by the shift $[r]$.

Two properties of the transform are used repeatedly. Its stalks
compute cohomology with compact support twisted by a character, which
is how $H^1_c$ will appear as a stalk, and it is invertible, so that we
can pass back from the transform to $K$. We also record its value on
the constant sheaf and on the skyscraper at zero.
